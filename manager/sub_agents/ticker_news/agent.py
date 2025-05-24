import requests
from google.adk.agents import Agent
import os

API_KEY = "zXO2lbc7OInWU6GdVOslqqKMmvj3n6me4pceutA6"


def get_ticker_news(ticker: str) -> dict:
    """Fetches the top 5 news headlines for a stock ticker using Marketaux."""
    try:
        url = "https://api.marketaux.com/v1/news/all"
        params = {
            "api_token": API_KEY,
            "symbols": ticker,
            "filter_entities": "true",
            "language": "en"
        }

        response = requests.get(url, params=params)
        data = response.json()

        if "data" not in data:
            return {"status": "error", "error_message": "No news found or bad response format."}

        news_items = data["data"][:5]
        headlines = [{"title": item["title"], "url": item["url"]} for item in news_items]

        return {
            "status": "success",
            "news": headlines,
            "ticker": ticker
        }

    except Exception as e:
        return {"status": "error", "error_message": str(e)}


ticker_news = Agent(
    name="ticker_news",
    model="gemini-2.0-flash",
    description="Fetches recent news for a stock ticker.",
    instruction="""
    Use the tool to retrieve the latest 5 news items for a ticker.
    Tools - 
    get_ticker_news
    """,
    tools=[get_ticker_news]
)
