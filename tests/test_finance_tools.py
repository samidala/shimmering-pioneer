from src.tools.finance_tools import fetch_stock_financials
import pytest

def test_fetch_stock_financials_valid():
    # Test with a known valid ticker
    result = fetch_stock_financials("AAPL")
    assert "Financials for AAPL" in result
    assert "Market Cap" in result

def test_fetch_stock_financials_invalid():
    # Test with an invalid ticker
    result = fetch_stock_financials("INVALID_TICKER_123")
    assert "Failed to fetch financials" in result
