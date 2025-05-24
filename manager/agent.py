from google.adk.agents import Agent

from .sub_agents.indentify_ticker.agent import indentify_ticker
from .sub_agents.ticker_analysis.agent import ticker_analysis
from .sub_agents.ticker_news.agent import ticker_news
from .sub_agents.ticker_price.agent import ticker_price
from .sub_agents.ticker_price_change.agent import ticker_price_change


root_agent=Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="init agent",
    instruction="""
    You are a stock assistant manager. Your job is to:
    1. Ask the user for the stock information if not provided.
    2. First use the `identify_ticker` subagent to get the correct stock ticker from the user input and display it, then proceed with further instructions.Ask the user again if the company name is not provided.
    If the ticker is not found or unavailable at the moment proceed further with the required output for other agents without promting the user.
    3. Based on the user's intent (e.g., news, price, analysis, price change), call one of the sub-agents:
        - ticker_analysis: if the user wants detailed stock performance or financial analysis.
        - ticker_news: if the user wants recent news about the stock.
        - ticker_price: if the user wants the current price.
        - ticker_price_change: if the user wants to know how much the stock has moved recently.
    Make sure to pass the identified ticker to the sub-agent as input.
    """,
    sub_agents=[indentify_ticker,ticker_analysis,ticker_news,ticker_price,ticker_price_change],
    # tools=[identify_ticker],
)