import requests
import yfinance as yf
from google.adk.agents import Agent
import os

# Tool to get stock ticker info and current price using yfinance
def get_ticker(query:str)->dict:
    """ Retrieves required company ticker """
    try:
        stock=yf.Ticker(query)
        price = stock.info.get("currentPrice", None)

        return {
            "ticker":query,
            "price":price
        }
    except Exception as e:
        return {
            "status":"error",
            "error_message":str(e),
        }

# Sub-agent to identify ticker based on user query
indentify_ticker = Agent(
    name="indentify_ticker",
    model="gemini-2.0-flash",
    description="Fetches company ticker",
    instruction="""
    Use the tool to retrieve the company ticker.
    Tools - 
    get_ticker
    """,
    tools=[get_ticker]
)
