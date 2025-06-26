import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient


async def call_tool_directly():
    # Initialize the MultiServerMCPClient with your server configuration
    client = MultiServerMCPClient(
        {
            "fred_database": {
                "url": "https://stock-data-mcp.1x378ktkz0ug.us-east.codeengine.appdomain.cloud/sse",
                "transport": "sse",
            }
        }
    )

    # Use async with to access the session
    # async with client.session("fred_database") as session:
    #     # Call the tool directly using the session
    #     response = await session.call_tool(
    #         "get_price_history", {"ticker": "TSLA", "period": "3mo"}
    #     )

    #     print("Response:", response)
    # general ticker data
    async with client.session("fred_database") as session:
        response = await session.call_tool("get_ticker_data", {"ticker": "TSLA"})
        print("Response:", response)
    print("-------------------------------------------------------\n")

    # gives a good overview of overall state of company
    async with client.session("fred_database") as session:
        response = await session.call_tool(
            "get_financial_statements",
            {"ticker": "GOOGL", "statement_type": "income", "frequency": "quarterly"},
        )
        print("Response:", response)

    print("-------------------------------------------------------\n")

    # not interesting
    async with client.session("fred_database") as session:
        response = await session.call_tool("get_earnings_history", {"ticker": "MSFT"})
        print("Response:", response)

    # not interesting
    print("-------------------------------------------------------\n")
    async with client.session("fred_database") as session:
        response = await session.call_tool("get_insider_trades", {"ticker": "NVDA"})
        print("Response:", response)
    print("-------------------------------------------------------\n")

    # good for news agent?
    async with client.session("fred_database") as session:
        response = await session.call_tool("get_ticker_news_tool", {"ticker": "AMZN"})
        print("Response:", response)
    print("-------------------------------------------------------\n")

    # too deep?
    async with client.session("fred_database") as session:
        response = await session.call_tool("super_option_tool", {"ticker": "NFLX"})
        print("Response:", response)
    print("-------------------------------------------------------\n")
    # not implemented as tool
    async with client.session("fred_database") as session:
        response = await session.call_tool("get_holdings_summary", {"ticker": "META"})
        print("Response:", response)

    print("-------------------------------------------------------\n")

    # interesting
    async with client.session("fred_database") as session:
        response = await session.call_tool("get_overall_sentiment_tool", {})
        print("Response:", response)

    print("-------------------------------------------------------\n")

    # interesting (historical fear& greed)
    async with client.session("fred_database") as session:
        response = await session.call_tool("get_historical_fng_tool", {"days": 30})
        print("Response:", response)

    print("-------------------------------------------------------\n")
    # also good for fear & greed
    async with client.session("fred_database") as session:
        response = await session.call_tool("analyze_fng_trend", {"days": 14})
        print("Response:", response)
    print("-------------------------------------------------------\n")

    # why use a calculator tool?
    async with client.session("fred_database") as session:
        response = await session.call_tool(
            "calculate", {"expression": "sqrt(64) + np.log(100)"}
        )
        print("Response:", response)
    print("-------------------------------------------------------\n")

    # good for both to get time context
    async with client.session("fred_database") as session:
        response = await session.call_tool("get_current_time", {})
        print("Response:", response)

    print("-------------------------------------------------------\n")

    # no
    async with client.session("fred_database") as session:
        response = await session.call_tool("get_fred_series", {"series_id": "GDP"})
        print("Response:", response)
    print("-------------------------------------------------------\n")
    #  no
    async with client.session("fred_database") as session:
        response = await session.call_tool("search_fred_series", {"query": "inflation"})
        print("Response:", response)

    print("-------------------------------------------------------\n")
    # good for cnbc news
    async with client.session("fred_database") as session:
        response = await session.call_tool("cnbc_news_feed", {})
        print("Response:", response)

    print("-------------------------------------------------------\n")
    async with client.session("fred_database") as session:
        response = await session.call_tool("social_media_feed", {})
        print("Response:", response)


# Run the asynchronous function
asyncio.run(call_tool_directly())
