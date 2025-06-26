FROM python:3.11-slim AS base

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential python3-venv curl git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Create virtual environment and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV="/app/.venv"

# Use PORT env for cloud compatibility (Code Engine injects PORT)
ENV PORT=8000
EXPOSE 8000

# Run the MCP server
CMD ["python", "finance_tools_mcp/apps/mcp_server/cli.py"]
