import yfinance as ticker
from crewai_tools import tool
import logging

logger = logging.getLogger(__name__)

@tool("fetch_stock_financials")
def fetch_stock_financials(stock_symbol: str) -> str:
    """
    Fetches fundamental financial data for a given stock symbol using Yahoo Finance.
    Includes Balance Sheet, Income Statement, and Cash Flow summaries.
    """
    try:
        stock = ticker.Ticker(stock_symbol)
        info = stock.info
        
        financials = {
            "Market Cap": info.get("marketCap"),
            "Forward P/E": info.get("forwardPE"),
            "Price to Book": info.get("priceToBook"),
            "Dividend Yield": info.get("dividendYield"),
            "Free Cash Flow": info.get("freeCashflow"),
            "Total Revenue": info.get("totalRevenue"),
            "Net Income to Common": info.get("netIncomeToCommon")
        }
        
        return f"Financials for {stock_symbol}:\n{financials}"
    except Exception as e:
        logger.error(f"Error fetching financials for {stock_symbol}: {e}")
        return f"Failed to fetch financials: {str(e)}"

@tool("fetch_stock_history")
def fetch_stock_history(stock_symbol: str, period: str = "1y") -> str:
    """
    Fetches historical price data for technical analysis.
    Period options: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max.
    """
    try:
        stock = ticker.Ticker(stock_symbol)
        history = stock.history(period=period)
        
        # Return summary of the history for technical agents
        last_closes = history['Close'].tail(30).to_dict()
        return f"Last 30 days of Closing Prices for {stock_symbol}:\n{last_closes}"
    except Exception as e:
        logger.error(f"Error fetching history for {stock_symbol}: {e}")
        return f"Failed to fetch history: {str(e)}"
