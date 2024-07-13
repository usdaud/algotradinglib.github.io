# Williams Percent Range

Williams Percent [Range](../r/range.md), also known as [Williams %R](../w/williams_%r.md), is a [momentum](../m/momentum.md)-based technical [indicator](../i/indicator.md) that measures [overbought](../o/overbought.md) and [oversold](../o/oversold.md) levels. Developed by Larry Williams in the 1970s, the [indicator](../i/indicator.md) is used primarily in the realm of stock and forex trading to help traders identify potential [reversal](../r/reversal.md) points in [market](../m/market.md) prices. [Williams %R](../w/williams_%r.md) is designed for [range](../r/range.md)-bound markets where prices oscillate between highs and lows, and it’s particularly useful in determining [market](../m/market.md) entry and exit points.

### Calculation of Williams %R
[Williams %R](../w/williams_%r.md) is calculated over a specific lookback period, typically 14 days, although this can be adjusted depending on the [trading strategy](../t/trading_strategy.md). The formula for [Williams %R](../w/williams_%r.md) is:

```
%R = (Highest High - Close) / (Highest High - Lowest Low) * -100
```

Where:
- `Highest High` is the highest price over the lookback period.
- `Lowest Low` is the lowest price over the lookback period.
- `Close` is the closing price of the current period.

This formula yields a [value](../v/value.md) ranging from -100 to 0. A [value](../v/value.md) of -100 indicates that the closing price is equal to the lowest low over the lookback period, while a [value](../v/value.md) of 0 indicates that the closing price is equal to the highest high over the lookback period.

### Interpretation of Williams %R
The [Williams %R](../w/williams_%r.md) [indicator](../i/indicator.md) helps traders identify [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions:
- **[Overbought](../o/overbought.md) Condition**: When [Williams %R](../w/williams_%r.md) is above -20.
- **[Oversold](../o/oversold.md) Condition**: When [Williams %R](../w/williams_%r.md) is below -80.

[Overbought](../o/overbought.md) conditions suggest that prices are getting unsustainably high and may be due for a [pullback](../p/pullback.md). Conversely, [oversold](../o/oversold.md) conditions suggest that prices are getting unsustainably low and may be due for a rebound.

### Trading Strategies Using Williams %R
There are several [trading strategies](../t/trading_strategies.md) that incorporate [Williams %R](../w/williams_%r.md):

#### 1. Overbought/Oversold Strategy
This simple strategy involves selling when the [Williams %R](../w/williams_%r.md) [indicator](../i/indicator.md) suggests [overbought](../o/overbought.md) conditions (values above -20) and buying when it suggests [oversold](../o/oversold.md) conditions (values below -80).

#### 2. Trend Reversal
Traders can also use [Williams %R](../w/williams_%r.md) to identify potential [trend](../t/trend.md) reversals. For instance, a move from [overbought](../o/overbought.md) territory to below -20 can signal the beginning of a [downtrend](../d/downtrend.md). Similarly, a move from [oversold](../o/oversold.md) territory to above -80 can signal the beginning of an [uptrend](../u/uptrend.md).

#### 3. Confirming Signals
[Williams %R](../w/williams_%r.md) is often used in conjunction with other indicators to confirm signals. For example, traders may look for alignment between [Williams %R](../w/williams_%r.md) and other [technical indicators](../t/technical_indicators.md) like Moving Averages, RSI ([Relative Strength](../r/relative_strength.md) [Index](../i/index.md)), or MACD (Moving Average Convergence [Divergence](../d/divergence.md)) to confirm [trade](../t/trade.md) signals.

### Advantages of Williams %R
- **Speed**: [Williams %R](../w/williams_%r.md) is responsive and captures short-term price movements effectively.
- **Simplicity**: The [indicator](../i/indicator.md) is straightforward to calculate and easy to interpret.
- **Versatility**: It can be used across different markets and time frames.

### Limitations of Williams %R
- **[False Signals](../f/false_signals_in_trading.md)**: Like most [technical indicators](../t/technical_indicators.md), [Williams %R](../w/williams_%r.md) can produce [false signals](../f/false_signals_in_trading.md), particularly in trending markets where it may remain in [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions for extended periods.
- **Lag**: It is a [lagging indicator](../l/lagging_indicator.md), meaning it reflects past price movements, which may not always reliably predict future price movements.

### Practical Examples of Williams %R
Let’s look at some practical examples to deepen our understanding.

#### Example 1: Stock Trading
Suppose a [trader](../t/trader.md) is examining the stock of a tech company, and the [Williams %R](../w/williams_%r.md) [indicator](../i/indicator.md) for the stock has moved above -20, indicating [overbought](../o/overbought.md) conditions. The [trader](../t/trader.md) might decide to sell the stock or [hold](../h/hold.md) off on buying more, anticipating a potential price drop.

#### Example 2: Forex Market
In the forex [market](../m/market.md), if the EUR/USD [currency](../c/currency.md) pair shows a [Williams %R](../w/williams_%r.md) [value](../v/value.md) below -80, this suggests that the pair is in [oversold](../o/oversold.md) territory. A [trader](../t/trader.md) observing this may consider entering a long position, expecting a price rebound.

### Implementing Williams %R in Algorithmic Trading
[Algorithmic trading](../a/algorithmic_trading.md) involves the use of automated systems to execute trades based on predefined criteria. [Williams %R](../w/williams_%r.md) can be a valuable tool in an [algorithmic trading](../a/algorithmic_trading.md) system for identifying [trade](../t/trade.md) opportunities and making data-driven decisions.

#### Example Algorithm Strategy
Consider an algorithm that:
1. Buys a [security](../s/security.md) when [Williams %R](../w/williams_%r.md) moves below -80.
2. Sells the [security](../s/security.md) when [Williams %R](../w/williams_%r.md) moves above -20.

### Advanced Techniques
#### 1. Combining with Moving Averages
Traders can enhance the effectiveness of [Williams %R](../w/williams_%r.md) by combining it with moving averages. For example, a [trader](../t/trader.md) might use a [50-period moving average](../1/50-period_moving_average.md) to determine the overall [trend](../t/trend.md) and then use [Williams %R](../w/williams_%r.md) to identify entry points within that [trend](../t/trend.md).

#### 2. Integrating with Relative Strength Index (RSI)
[Williams %R](../w/williams_%r.md) can be used alongside RSI to confirm signals. For instance, when both indicators show [oversold](../o/oversold.md) conditions, it could be a stronger signal to buy.

#### 3. Adaptive Williams %R
Some advanced traders may use an adaptive [Williams %R](../w/williams_%r.md), where the lookback period adjusts based on [market](../m/market.md) [volatility](../v/volatility.md). This approach aims to make the [indicator](../i/indicator.md) more responsive during volatile periods and less responsive during stable periods.

### Implementing Williams %R in Software
#### Python Example
Below is a basic example of how to implement [Williams %R](../w/williams_%r.md) in Python using the pandas library:

```python
[import](../i/import.md) pandas as pd

def williams_r(data, lookback_period=14):
    highest_high = data['High'].rolling(window=lookback_period).max()
    lowest_low = data['Low'].rolling(window=lookback_period).min()
    williams_r = (highest_high - data['Close']) / (highest_high - lowest_low) * -100
    [return](../r/return.md) williams_r

# Sample data
data = {
    'High': [10, 12, 13, 15, 14, 17, 18],
    'Low': [5, 6, 7, 7, 9, 10, 11],
    'Close': [9, 11, 10, 13, 12, 14, 15]
}
df = pd.DataFrame(data)

# Calculate Williams %R
df['[Williams %R](../w/williams_%r.md)'] = williams_r(df)
print(df)
```

### Conclusion
Williams Percent [Range](../r/range.md) is a [robust](../r/robust.md) technical [indicator](../i/indicator.md) that helps traders identify potential [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions, providing valuable insights for making informed trading decisions. Whether used in isolation or combined with other indicators, [Williams %R](../w/williams_%r.md) is a versatile tool that can enhance both discretionary and [algorithmic trading](../a/algorithmic_trading.md) strategies. Given its responsiveness and simplicity, it remains a popular choice among traders across various markets.
