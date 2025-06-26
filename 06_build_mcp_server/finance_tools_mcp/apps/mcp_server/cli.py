import logging

# Import the application factory
from apps.mcp_server.main import create_mcp_application

# Import the sse_server run function from its new location


logger = logging.getLogger(__name__) # Use the logger from main.py or define a new one

def main():


    mcp_app = create_mcp_application()


    mcp_app.run(transport="streamable-http")

if __name__ == "__main__":
    main()