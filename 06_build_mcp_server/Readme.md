# README.md

This document serves as a guide to setting up and running the mcp server, as well as exploring its available tools for the project. Follow the steps below to get started.

---

## Setting Up the Virtual Environment

To create and activate a virtual environment, and install the required dependencies, run the following commands:

```bash
python3.11 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## Available Tools

A detailed description of all the available tools can be found in the following files:

- `mcp_client/tools.json`  
- `mcp_client/tool_description.md`

These files outline the functionality and use cases of each tool provided in this project.

---

## Running the MCP Server

To start the MCP server, navigate to the appropriate directory and run the server script as follows:

```bash
cd finance_tools_mcp

python3 apps/mcp_server/cli.py
```

The definition of all the tools used by the MCP server is located in the following file:

```
finance_tools_mcp/apps/mcp_server/main.py
```

---

## Trying Out the Tools

If you'd like to experiment with the tools, follow these steps:

1. Navigate to the `mcp_client` directory:

   ```bash
   cd mcp_client
   ```

2. Create a `.env` file in the same directory with the following entries. Replace the placeholders with your actual values:

   ```plaintext
   WX_MODEL_ID=
   WX_API_KEY=
   WX_URL=
   WX_PROJECT_ID=
   ```

3. Once the `.env` file is set up, you can run the client script using:

   ```bash
   python3 mcp_client.py
   ```

### Sample Tool Calls

Sample tool calls are provided in the following file for reference:

```
mcp_client/tool_test.py
```

You can use these examples to understand how to interact with the tools and test their functionality.

---

This concludes the setup instructions. For further details or troubleshooting, please refer to the additional documentation included in the project files.