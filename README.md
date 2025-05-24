# Stock-Agents
This project is a multi-agent system built using the google-adk framework that answers stock-related queries in natural language. 
It is designed to parse user questions, fetch real-time financial data, and generate a concise analysis using multiple specialized agents.

## 🧠 Key Components (Agents)

- **identify_ticker**

Detects the stock ticker symbol from a user query (e.g., "Tesla" → TSLA) using yfinance library.

- **ticker_news**

Retrieves the latest news about the identified company or ticker using the ***marketaux API***.

- **ticker_price**

Fetches the current stock price using the ***Alphavantage API***.

- **ticker_price_change**

Calculates price movement (amount and percentage) over a short timeframe.

- **ticker_analysis**

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
   ```
   python -m venv .venv
   ```
5. Run -
   ```
   .venv\Scripts\activate.ps1
   ```
5.Install dependencies -
   ``` 
   pip install -r req.txt
   ```
7. Redirect to -
   ```
   cd manager
   ```
9. Enter -
   ```
   adk web
   ```
11. Open your browser and enter the following URL -
   ```
    http://127.0.0.1:8000
   ```

## Working 

![image](https://github.com/user-attachments/assets/75580a0e-6d4d-4e04-b7da-57a66fb5cb0a)

![image](https://github.com/user-attachments/assets/79288de4-3da4-4382-ac4c-457634444d60)

![image](https://github.com/user-attachments/assets/f9610cf1-651d-4e06-bd45-445823a5dcd8)

![image](https://github.com/user-attachments/assets/08afd4eb-b54b-498b-9d8b-5e3743261edb)


