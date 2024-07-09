# 2-Week Moving Average

The 2-Week Moving Average (2WMA) is a form of the moving average primarily used in financial markets to analyze and smooth out the price data over a two-week period. This specific short-term moving average helps traders and analysts to detect trends, make predictions, and execute trades based on the recent market momentum. Here's a deep dive into what the 2-Week Moving Average entails and how it is utilized in [algorithmic trading](../a/algorithmic_trading.md).

## Concept and Calculation

### Definition
The 2-Week Moving Average is the arithmetic mean of the closing prices for a security over the past two weeks.

### Formula
\[
2WMA = \frac{P_1 + P_2 + ... + P_{14}}{14}
\]
where \(P\) represents the closing price of the security.

### Example Calculation
If the closing prices for the last 14 days are:
\[ 100, 102, 101, 103, 104, 106, 107, 108, 110, 112, 113, 115, 117, 118 \]
Then the 2WMA is calculated as:
\[
2WMA = \frac{100 + 102 + 101 + 103 + 104 + 106 + 107 + 108 + 110 + 112 + 113 + 115 + 117 + 118}{14} = \frac{1426}{14} = 101.86
\]

## Application in Trading

### Trend Analysis
The primary use of the 2-Week Moving Average is to identify short-term trends in the market. By averaging out the price data, it smooths out day-to-day volatility and allows a clearer view of the underlying trend.

### Signal Generation
In [algorithmic trading](../a/algorithmic_trading.md), the 2WMA can be used to generate buy or sell signals. Traditional signals include:
- **Buy Signal**: Occurs when the price crosses above the 2WMA, indicating a potential upward trend.
- **Sell Signal**: Occurs when the price crosses below the 2WMA, indicating a potential downward trend.

### Comparison with Longer-Term Moving Averages
The 2WMA is often compared with longer-term moving averages like the 50-day or 200-day moving averages to confirm trends. For instance:
- **[Golden Cross](../g/golden_cross.md)**: A bullish signal generated when the short-term 2WMA crosses above a longer-term moving average.
- **Death Cross**: A bearish signal generated when the 2WMA crosses below a longer-term moving average.

## Algorithm and Technical Implementation

### Basic Algorithm

Here is a simple Python algorithm to compute the 2-Week Moving Average:

```python
import pandas as pd

def calculate_2wma(data):
    return data['Close'].rolling(window=14).mean()

# Example usage
# Assuming `data` is a pandas DataFrame with a 'Close' column
data['2WMA'] = calculate_2wma(data)
```

### Incorporating into Trading Strategy
To incorporate the 2WMA into an [algorithmic trading](../a/algorithmic_trading.md) strategy, one needs to backtest the strategy to ensure its efficacy. Here's a simple example using [backtesting](../b/backtesting.md) with a strategy based on 2WMA:

```python
import pandas as pd
import numpy as np

# Example DataFrame 'data' with 'Close' prices
data['2WMA'] = data['Close'].rolling(window=14).mean()

# Generating signals based on crossover
data['Signal'] = 0
data['Signal'][14:] = np.where(data['Close'][14:] > data['2WMA'][14:], 1, -1)

# Calculating returns based on signal
data['Return'] = data['Close'].pct_change()
data['Strategy_Return'] = data['Return'] * data['Signal'].shift(1)

# Plotting the results
data[['Close', '2WMA', 'Signal']].plot()
```

## Advantages and Disadvantages

### Advantages
1. **Simplicity**: Easy to understand and implement.
2. **Smooths Data**: Reduces the noise of daily price fluctuations.
3. **Short-Term Trend Identification**: Effective for detecting short-term trend reversals.

### Disadvantages
1. **Lag**: Being a lagging indicator, it may not respond quickly to sudden market changes.
2. **Whipsaws**: Prone to generating [false signals](../f/false_signals_in_trading.md) in choppy markets.
3. **Limited Scope**: May not be effective for long-term [trend analysis](../t/trend_analysis.md).

## Practical Use Cases

### Day Trading
Day traders often use short-term moving averages like the 2WMA to make quick decisions. They rely on these moving averages to identify entry and exit points throughout the trading day.

### Swing Trading
Swing traders use the 2WMA to catch short- to medium-term price movements. The 2WMA helps in detecting the onset of a trend which can last from a few days to a couple of weeks.

### Pair Trading
In pair trading, which involves taking opposing positions in two highly correlated stocks, the 2WMA can be used to detect divergences and convergences in the price movements of the two stocks.

## Companies and Platforms

### Alpha Trading Labs (https://alphatradinglabs.com)
Alpha Trading Labs provides a platform for developing and deploying [algorithmic trading](../a/algorithmic_trading.md) strategies, including those based on moving averages.

### QuantConnect (https://www.quantconnect.com)
[QuantConnect](../q/quantconnect.md) is an [algorithmic trading](../a/algorithmic_trading.md) platform that offers [backtesting](../b/backtesting.md) and live-trading services. Their platform supports numerous [technical indicators](../t/technical_indicators.md), including moving averages, and allows traders to build strategies using Python and C#.

### Alpaca (https://alpaca.markets)
[Alpaca](../a/alpaca.md) provides commission-free trading APIs that allow users to automate their [trading algorithms](../t/trading_algorithms.md) with ease. They offer extensive documentation and support for integrating moving average-based strategies.

## Conclusion

The 2-Week Moving Average is a fundamental tool used in [algorithmic trading](../a/algorithmic_trading.md) to analyze short-term price trends and generate [trading signals](../t/trading_signals.md). Its simplicity and relevance make it a go-to for traders looking to capitalize on short-term market movements. By combining the 2WMA with other [technical indicators](../t/technical_indicators.md) and [backtesting](../b/backtesting.md) the strategy, traders can create robust [trading systems](../t/trading_systems.md) to improve their profitability.