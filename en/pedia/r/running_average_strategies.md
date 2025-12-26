# Running Average Strategies

Running average strategies, often referred to as [moving average strategies](../m/moving_average_strategies.md), are a cornerstone of [algorithmic trading](../a/algorithmic_trading.md). These strategies incorporate moving averages into their design to help forecast future price movements based on historical data and statistical analyses. There are various forms of moving averages, each with its unique application and significance. This in-depth exploration [will](../w/will.md) cover the different types of moving averages, their role in [trading strategies](../t/trading_strategies.md), programming aspects, and [industry](../i/industry.md) applications.

## Types of Moving Averages

### Simple Moving Average (SMA)

The Simple Moving Average (SMA) is one of the most straightforward forms of moving averages. It is calculated by summing up the prices over a certain period and then dividing by that period.

**Formula**:
\[ \text{SMA}_n = \frac{P_1 + P_2 +... + P_n}{n} \]

Where \( P \) represents the price at a given time point, and \( n \) is the time period.

### Exponential Moving Average (EMA)

The Exponential Moving Average (EMA) is a type of moving average that gives more weight to recent prices. This makes it more responsive to new information compared to the SMA.

**Formula**:
\[ \text{EMA}_t = P_t \cdot \[alpha](../a/alpha.md) + \text{EMA}_{t-1} \cdot (1 - \[alpha](../a/alpha.md)) \]

Where \( \[alpha](../a/alpha.md) \) is the smoothing [factor](../f/factor.md) calculated as:
\[ \[alpha](../a/alpha.md) = \frac{2}{n+1} \]

### Weighted Moving Average (WMA)

The [Weighted](../w/weighted.md) Moving Average (WMA) assigns a different weight to each price point within the period. The most recent price gets the highest weight, and weights decrease in a linear fashion.

**Formula**:
\[ \text{WMA} = \frac{n \cdot P_1 + (n-1) \cdot P_2 +... + 1 \cdot P_n}{\sum_{i=1}^n i} \]

### Moving Average Convergence Divergence (MACD)

Although MACD is not a moving average per se, it is derived from the difference between the 26-period EMA and 12-period EMA. The MACD line is then contrasted with a 9-period EMA of itself to generate buy and sell signals.

**Formula**:
\[ \text{MACD} = \text{EMA}_{12} - \text{EMA}_{26} \]
\[ \text{Signal Line} = \text{EMA}_{9}(\text{MACD}) \]

## Application in Trading Strategies

### Crossover Strategy

The crossover strategy employs two moving averages: a short-term and a long-term average. A buy signal is generated when the short-term average crosses above the long-term average, and a sell signal is triggered when it crosses below.

### Moving Average Ribbon

This strategy uses [multiple](../m/multiple.md) SMAs or EMAs to create a ribbon of moving averages. The strategy looks for points where all the moving averages begin to converge or diverge, signaling potential buy or sell opportunities.

### Moving Average Envelopes

Moving Average Envelopes place a certain percentage above and below the moving average line. Buy and sell signals are triggered when the price crosses outside these envelopes.

### Adaptive Moving Average (AMA)

Unlike traditional moving averages, the AMA adapts based on [volatility](../v/volatility.md) and [market](../m/market.md) trends. This makes it more dynamic and responsive to changing [market](../m/market.md) conditions.

## Programming Moving Averages

### Python Implementation

Python is a popular language for implementing [algorithmic trading](../a/algorithmic_trading.md) strategies due to its [robust](../r/robust.md) libraries like pandas, NumPy, and TA-Lib.

```python
[import](../i/import.md) pandas as pd
[import](../i/import.md) numpy as np

def calculate_sma(data, period):
    [return](../r/return.md) data.rolling(window=period).mean()

def calculate_ema(data, period):
    [return](../r/return.md) data.ewm(span=period, adjust=False).mean()

def calculate_wma(data, period):
    weights = np.arange(1, period+1)
    [return](../r/return.md) data.rolling(period).apply([lambda](../l/lambda.md) prices: np.dot(prices, weights)/weights.sum(), raw=True)

# Example Usage
data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sma = calculate_sma(data, 3)
ema = calculate_ema(data, 3)
wma = calculate_wma(data, 3)
```

### Backtesting

[Backtesting](../b/backtesting.md) is crucial for assessing the [efficiency](../e/efficiency.md) of [moving average strategies](../m/moving_average_strategies.md). Libraries like [Backtrader](../b/backtrader.md) and Zipline [offer](../o/offer.md) [robust](../r/robust.md) frameworks for [backtesting](../b/backtesting.md):

```python
[import](../i/import.md) [backtrader](../b/backtrader.md) as bt

class MovingAverageStrategy(bt.SignalStrategy):
    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=15)
        self.ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=30)
        self.cross = bt.indicators.CrossOver(self.sma, self.ema)

    def next(self):
        if self.cross > 0:  # a buy signal
            self.buy()
        elif self.cross < 0:  # a sell signal
            self.sell()

# Load data and run backtest
data = bt.feeds.YahooFinanceData(dataname='AAPL', fromdate=dt.datetime(2018, 1, 1),
                                  todate=dt.datetime(2020, 12, 31))
cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(MovingAverageStrategy)
cerebro.run()
cerebro.plot()
```

## Industry Application

### StockSharp

[StockSharp](../s/stocksharp.md) provides a [algorithmic trading](../a/algorithmic_trading.md) platform adhering to institutional standards. The platform supports diverse financial instruments and C#.


### Bloomberg Terminal

[Bloomberg](../b/bloomberg.md) Terminal offers [robust](../r/robust.md) analytics tools facilitating the implementation of [moving average strategies](../m/moving_average_strategies.md). The terminal is widely used in the [finance](../f/finance.md) [industry](../i/industry.md) for [real-time data analysis](../r/real-time_data_analysis.md) and trading operations.


### AlgoTrader

[AlgoTrader](../a/algotrader.md) is a comprehensive [algorithmic trading](../a/algorithmic_trading.md) platform supporting [multiple](../m/multiple.md) [trading strategies](../t/trading_strategies.md), including moving averages. The platform offers extensive [backtesting](../b/backtesting.md) capabilities and connectivity to various [liquidity](../l/liquidity.md) providers.


### TradingView

[TradingView](../t/tradingview.md) is an online platform that provides charting tools and moving average indicators for traders. It supports scripting in Pine Script for custom strategy development and [backtesting](../b/backtesting.md).


## Conclusion

Running average strategies serve as a foundational element in [algorithmic trading](../a/algorithmic_trading.md), [offering](../o/offering.md) numerous applications, from simple crossover techniques to advanced analytics like adaptive moving averages. Their versatility and ease of integration make them indispensable tools for traders seeking to [leverage](../l/leverage.md) historical data for predictive insights. Whether utilizing platforms like [QuantConnect](../q/quantconnect.md) or employing custom Python scripts, these strategies continue to play a pivotal role in modern trading environments.