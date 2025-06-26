import json
import logging
import os
import time
import uuid

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_ibm import ChatWatsonx
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel

# Load environment variables from .env
load_dotenv(dotenv_path=".env")

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI()


# Input schema
class ChatRequest(BaseModel):
    model: str = None
    messages: list
    stream: bool = False
    extra_body: dict = None


# Globals
tools = None
agent = None


@app.on_event("startup")
async def startup_event():
    global tools, agent

    # Initialize MCP client
    client = MultiServerMCPClient(
        {
            "fred_database": {
                "url": os.getenv("MCP_SERVER_URL") + "/mcp",
                "transport": "streamable_http",
            }
        }
    )
    tools = await client.get_tools()

    # Initialize Watsonx LLM
    watsonx_llm = ChatWatsonx(
        model_id=os.getenv("WX_MODEL_ID"),
        url=os.getenv("WX_URL"),
        project_id=os.getenv("WX_PROJECT_ID"),
        apikey=os.getenv("WX_API_KEY"),
    )

    agent = create_react_agent(watsonx_llm, tools=tools)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chat/completions")
async def chat_completions(req: ChatRequest, request: Request):
    try:
        user_message = req.messages[-1]["content"]
        logger.info(f"📩 User Query: {user_message}")

        if req.stream:

            async def event_stream():
                async for step in agent.astream(
                    {"messages": [HumanMessage(content=user_message)]}
                ):
                    if "agent" in step:
                        for msg in step["agent"]["messages"]:
                            if isinstance(msg, AIMessage) and msg.content:
                                chunk = {
                                    "choices": [{"delta": {"content": msg.content}}],
                                    "object": "chat.completion.chunk",
                                }
                                yield f"data: {json.dumps(chunk)}\n\n"
                    if "tools" in step:
                        for msg in step["tools"]["messages"]:
                            if isinstance(msg, ToolMessage):
                                chunk = {
                                    "choices": [
                                        {
                                            "delta": {
                                                "content": f"[Tool Response] {msg.name}: {msg.content}"
                                            }
                                        }
                                    ],
                                    "object": "chat.completion.chunk",
                                }
                                yield f"data: {json.dumps(chunk)}\n\n"
                    if "final" in step:
                        for msg in step["final"]:
                            if msg.content:
                                chunk = {
                                    "choices": [{"delta": {"content": msg.content}}],
                                    "object": "chat.completion.chunk",
                                }
                                yield f"data: {json.dumps(chunk)}\n\n"
                yield "data: [DONE]\n\n"

            return StreamingResponse(event_stream(), media_type="text/event-stream")

        else:
            final_output = ""
            tool_outputs = []

            async for step in agent.astream(
                {"messages": [HumanMessage(content=user_message)]}
            ):
                if "agent" in step:
                    for msg in step["agent"]["messages"]:
                        if isinstance(msg, AIMessage):
                            if msg.tool_calls:
                                for call in msg.tool_calls:
                                    logger.info(
                                        f"🛠️ Tool Call: {call['name']} with args {call['args']}"
                                    )
                            elif msg.content:
                                logger.info(f"💭 AI: {msg.content}")
                                final_output += msg.content + "\n"

                elif "tools" in step:
                    for msg in step["tools"]["messages"]:
                        if isinstance(msg, ToolMessage):
                            logger.info(f"📦 Tool Response: {msg.name}: {msg.content}")
                            tool_outputs.append(f"{msg.name}: {msg.content}")

                elif "final" in step:
                    logger.info("✅ Final Answer:")
                    for msg in step["final"]:
                        if msg.content:
                            logger.info(msg.content)
                            final_output += msg.content
                        else:
                            logger.warning("⚠️ Final message content was empty")

            else:
                logger.info(f"💭 AI: {msg.content}")
            if not final_output and tool_outputs:
                final_output = "\n".join(tool_outputs)
            elif not final_output:
                final_output = "No meaningful output generated."

            logger.info("📤 Final output sent to user:\n" + final_output)

            response = {
                "id": str(uuid.uuid4()),
                "object": "chat.completion",
                "created": int(time.time()),
                "model": req.model or os.getenv("WX_MODEL_ID"),
                "choices": [
                    {
                        "index": 0,
                        "message": {"role": "assistant", "content": final_output},
                        "finish_reason": "stop",
                    }
                ],
            }

            return JSONResponse(content=response)

    except Exception as e:
        logger.error("❌ Exception occurred: %s", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})
