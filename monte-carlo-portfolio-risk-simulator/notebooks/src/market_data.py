"""
================================================================================
Market Data Module
================================================================================

This module provides utilities for downloading and preparing historical
financial market data.

The objective is to retrieve real stock market information that will be used
throughout the Monte Carlo Portfolio Risk Simulator project.

The data source is Yahoo Finance through the yfinance library.

This module focuses only on data acquisition and preparation.

Financial calculations such as returns, volatility, portfolio metrics, and
Monte Carlo simulation are implemented in separate modules.

Author:
    José Reyes

Project:
    Monte Carlo Portfolio Risk Simulator

================================================================================
"""


# =============================================================================
# Imports
# =============================================================================

import pandas as pd
import yfinance as yf


# =============================================================================
# Market Configuration
# =============================================================================

# 5 years
DEFAULT_START_DATE = "2020-01-01"
DEFAULT_END_DATE = "2025-01-01" 


# Defining a function to download stock data based on public vars for a single stock
def download_stock_data(
    ticker: str,
    start_date: str,
    end_date: str
    ) -> pd.DataFrame:
    """
    Downloads historical market data for a single stock.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol.

    start_date : str
        Beginning date of historical data.

    end_date : str
        Ending date of historical data.

    Returns
    -------
    pandas.DataFrame
        Historical stock price data.
    """

    data = yf.download(
        ticker,
        start=start_date,
        end=end_date
    )

    data["Ticker"] = ticker
    
    return data


# Defining a function to download the portfolio data based on public vars for multiple stocks
def download_portfolio_data(
    tickers: list[str],
    start_date: str,
    end_date: str
    ) -> pd.DataFrame:
    """
    Downloads historical data for multiple stocks.

    Parameters
    ----------
    tickers : list
        List of stock tickers.

    start_date : str
        Beginning date.

    end_date : str
        Ending date.

    Returns
    -------
    pandas.DataFrame
        Combined historical market dataset.
    """

    portfolio_data = []

    for ticker in tickers:
        stock_data = download_stock_data(ticker, start_date, end_date)
        portfolio_data.append(stock_data)

    return pd.concat(portfolio_data)


# Defining a function to prepare and clean stock/market data
def prepare_market_data(
    data: pd.DataFrame
    ) -> pd.DataFrame:
    """
    Cleans and prepares market data.

    Parameters
    ----------
    data : pandas.DataFrame
        Raw market dataset.

    Returns
    -------
    pandas.DataFrame
        Clean financial dataset.
    """

    cleaned_data = (data.reset_index().copy())
    cleaned_data = cleaned_data[["Date", "Ticker", "Close"]]

    return cleaned_data


# Defining a main function
def get_market_dataset(
    tickers_list: list[str],
    start_date: str,
    end_date: str
    ) -> pd.DataFrame:
    """
    Returns a prepared market dataset using default portfolio assets.

    Returns
    -------
    pandas.DataFrame
        Prepared stock price dataset.
    """

    raw_data = download_portfolio_data(tickers_list, start_date, end_date)

    return prepare_market_data(raw_data)
