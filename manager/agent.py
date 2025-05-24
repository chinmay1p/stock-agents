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
    2. Based on the user's intent (e.g., news, price, analysis, price change), call one of the sub-agents:
        - identify_ticker: if user wants the ticker name for the given company
        - ticker_analysis: if the user wants detailed stock performance or financial analysis.
        - ticker_news: if the user wants recent news about the stock.
        - ticker_price: if the user wants the current price.
        - ticker_price_change: if the user wants to know how much the stock has moved recently.
    """,
    sub_agents=[indentify_ticker,ticker_analysis,ticker_news,ticker_price,ticker_price_change],
)