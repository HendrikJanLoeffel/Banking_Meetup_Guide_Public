import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_ibm import ChatWatsonx
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent


async def main():
    load_dotenv()

    # Set up MCP client
    client = MultiServerMCPClient(
        {
            "fred_database": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    # Get tools
    tools = await client.get_tools()

    # Set up LLM
    # model = ChatOpenAI(model="gpt-4")

    watsonx_llm = ChatWatsonx(
        model_id=os.getenv("WX_MODEL_ID"),
        url=os.getenv("WX_URL"),
        project_id=os.getenv("WX_PROJECT_ID"),
        apikey=os.getenv("WX_API_KEY"),
    )
    # Create LangGraph agent
    agent = create_react_agent(watsonx_llm, tools=tools)

    # Stream the reasoning and final output
    print("Streaming thoughts...\n")
    async for step in agent.astream(
        {
            "messages": [
                HumanMessage(
                    content="What happened to the TSLA stock in the last 3 months?"
                )
            ]
        },
    ):
        print("Next Step: ")
        if "agent" in step:
            for msg in step["agent"]["messages"]:
                if isinstance(msg, AIMessage):
                    # Tool call reasoning
                    if msg.tool_calls:
                        for call in msg.tool_calls:
                            print(
                                f"[Tool Call] {call['name']} with args {call['args']}"
                            )
                    else:
                        # Final or intermediate reasoning
                        print(f"[AI] {msg.content}")
        elif "tools" in step:
            for msg in step["tools"]["messages"]:
                if isinstance(msg, ToolMessage):
                    print(f"[Tool Response] {msg.name}: {msg.content}")
        elif "final" in step:
            print("\n✅ Final Answer:")
            for msg in step["final"]:
                print(msg.content)


if __name__ == "__main__":
    asyncio.run(main())
