# Stock-Agents
This project is a multi-agent system built using the google-adk framework that answers stock-related queries in natural language. 
It is designed to parse user questions, fetch real-time financial data, and generate a concise analysis using multiple specialized agents.

## 🧠 Key Components (Agents)
> identify_ticker
Detects the stock ticker symbol from a user query (e.g., "Tesla" → TSLA) using yfinance library.

> ticker_news
Retrieves the latest news about the identified company or ticker using the *** marketaux API ***.

> ticker_price
Fetches the current stock price using the *** Alphavantage API ***.

> ticker_price_change
Calculates price movement (amount and percentage) over a short timeframe.

> ticker_analysis
Summarizes the reason behind price changes by analysing recent news.

---

## 🚀 Features
- 🌐 **Natural Language Input**  
  Understands user queries like:
  - "Why did Tesla stock drop today?"
  - "What’s happening with Palantir recently?"
  - "How has Nvidia stock changed in the last 7 days?"

- 🧠 **Modular Agent Design**  
  Each function (ticker lookup, news fetch, price analysis) is handled by an independent agent using the `google-adk` framework.

- 🔄 **Real-Time Stock Data**  
  Integrates with the [Alpha Vantage API](https://www.alphavantage.co/) to fetch current prices and historical data.

---

## Set-Up
1. Clone the repository
   ``` bash
       git clone https://github.com/yourusername/stock-agents.git
   ```
2. Open the terminal
3. Start a python virtual environment using -
   ``` python -m venv .venv ```
4. Run -
   ``` .venv\Scripts\activate.ps1 ```
5.Install dependencies -
   ``` pip install -r req.txt ```
6. Redirect to -
   ``` cd manager ```
7. Enter -
   ``` adk web ```
8. Open your browser and enter the following URL -
   http://127.0.0.1:8000

## Working 

