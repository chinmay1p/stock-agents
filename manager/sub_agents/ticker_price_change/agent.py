import requests
from google.adk.agents import Agent
import os

API_KEY ="PBG610RYUPML0I5F"

# Tool to fetch recent price change percentage for a given ticker
def get_price_change(ticker: str) -> dict:
    """Fetches the recent price change percentage for the given ticker."""
    try:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"
        response = requests.get(url).json()

        if "Global Quote" not in response:
            return {"status": "error", "error_message": "Unable to fetch price change."}

        # Extract change percentage
        change_percent = response["Global Quote"]["10. change percent"]

        return {
            "status": "success",
            "change_percent": change_percent,
            "ticker": ticker
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}


ticker_price_change = Agent(
    name="ticker_price_change",
    model="gemini-2.0-flash",
    description="Provides the recent price movement for a stock.",
    instruction="Use the tool to get the price change percentage for the ticker and give it to the user.",
    tools=[get_price_change]
)
