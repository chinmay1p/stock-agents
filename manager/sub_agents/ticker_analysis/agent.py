import requests
from google.adk.agents import Agent
import os

API_KEY ="zXO2lbc7OInWU6GdVOslqqKMmvj3n6me4pceutA6"

# Tool to fetch recent news for a stock ticker with extra context for analysis
def get_analysis_with_news(ticker: str) -> dict:
    """Fetches top 5 news articles and prepares them for analysis."""
    try:
        url = "https://api.marketaux.com/v1/news/all"
        params = {
            "api_token": API_KEY,
            "symbols": ticker,
            "filter_entities": "true",
            "language": "en",
            "limit": 5
            # Limit to top 5 articles
        }

        response = requests.get(url, params=params)
        data = response.json()

        if "data" not in data:
            return {"status": "error", "error_message": "Unable to fetch news for analysis."}

        # Extract title, summary, and URL from each news item
        news_items = data["data"]
        headlines = [
            {
                "title": item.get("title"),
                "summary": item.get("description", ""),
                "url": item.get("url")
            }
            for item in news_items
        ]

        return {
            "status": "success",
            "news": headlines,
            "ticker": ticker,
            "instruction": "Based on the following news headlines and summaries, analyze and explain the likely reasons behind recent movements in the stock or investor sentiment shifts."
        }

    except Exception as e:
        return {"status": "error", "error_message": str(e)}

ticker_analysis = Agent(
    name="ticker_analysis",
    model="gemini-2.0-flash",
    description="Performs an analysis of stock based on recent news.",
    instruction="""
    Use the tool to fetch the top 5 most recent news items about a stock ticker.
    
    Analyze the content of the news (title + summary) to:
    - Identify key drivers or causes of recent price movement,
    - Detect sentiment trends (positive/negative/neutral),
    - Mention significant events (e.g. earnings reports, legal issues, market upgrades/downgrades).

    Output a concise analysis paragraph that explains the most probable reasons behind recent stock performance or shifts in investor sentiment.
    
    Tools -
    get_analysis_with_news
    """,
    tools=[get_analysis_with_news]
)
