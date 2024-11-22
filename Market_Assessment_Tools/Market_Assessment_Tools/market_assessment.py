# market_assessment.py
# Author: Yi Ma
# Description: This script provides tools for market trend analysis and competitor evaluation.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_market_trends(data):
    """
    Analyze market trends over time using a time series approach.

    Args:
        data (pandas.DataFrame): Data containing columns 'Date' and 'Sales'.
    
    Returns:
        None: Displays a trend plot.
    """
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values('Date')
    data.set_index('Date', inplace=True)
    
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Sales'], label="Market Sales", marker="o")
    plt.title("Market Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    plt.show()

def evaluate_competitors(data):
    """
    Evaluate competitors by analyzing their market shares.

    Args:
        data (pandas.DataFrame): Data containing columns 'Competitor' and 'Market Share'.
    
    Returns:
        None: Displays a bar chart.
    """
    data = data.groupby('Competitor')['Market Share'].mean().reset_index()
    
    plt.figure(figsize=(10, 5))
    plt.bar(data['Competitor'], data['Market Share'], color='skyblue')
    plt.title("Competitor Market Shares")
    plt.xlabel("Competitor")
    plt.ylabel("Market Share (%)")
    plt.xticks(rotation=45)
    plt.show()

# Sample Usage
if __name__ == "__main__":
    # Example market data
    market_data = pd.DataFrame({
        "Date": ["2023-01-01", "2023-02-01", "2023-03-01"],
        "Sales": [100, 120, 140]
    })
    competitor_data = pd.DataFrame({
        "Competitor": ["A", "B", "C", "A", "B", "C"],
        "Market Share": [30, 50, 20, 35, 45, 25]
    })
    
    # Analyze market trends
    analyze_market_trends(market_data)
    
    # Evaluate competitors
    evaluate_competitors(competitor_data)
