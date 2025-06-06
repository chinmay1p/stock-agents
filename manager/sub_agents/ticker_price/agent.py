import requests
from google.adk.agents import Agent
import os

API_KEY ="PBG610RYUPML0I5F"

# Tool to get the current stock price using Alpha Vantage
def get_current_price(ticker: str) -> dict:
    """Fetches the current stock price for the given ticker."""
    try:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"
        response = requests.get(url).json()

        if "Global Quote" not in response:
            return {"status": "error", "error_message": "Unable to fetch current price."}

        # Extract price from the response
        price = response["Global Quote"]["05. price"]

        return {
            "status": "success",
            "price": price,
            "ticker": ticker
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

ticker_price = Agent(
    name="ticker_price",
    model="gemini-2.0-flash",
    description="Provides the current price of a stock.",
    instruction="Use the tool to get the current stock price for the given ticker.",
    tools=[get_current_price]
)
