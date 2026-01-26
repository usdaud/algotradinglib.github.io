# Williams Percent Range

[Перевод с английского языка]

Williams Percent Range, also known as Williams %R, is a momentum-based technical indicator that measures overbought and oversold levels. Developed by Larry Williams in the 1970s, the indicator is used primarily in the realm of stock and forex trading to help traders identify potential reversal points in market prices. Williams %R is designed for range-bound markets where prices oscillate between highs and lows, and it’s particularly useful in determining market entry and exit points.

### Calculation of Williams %R
Williams %R is calculated over a specific lookback period, typically 14 days, although this can be adjusted depending on the trading strategy. The formula for Williams %R is:

```
%R = (Highest High - Close) / (Highest High - Lowest Low) * -100
```

Where:
- `Highest High` is the highest price over the lookback period.
- `Lowest Low` is the lowest price over the lookback period.
- `Close` is the closing price of the current period.

This formula yields a value ranging from -100 to 0. A value of -100 indicates that the closing price is equal to the lowest low over the lookback period, while a value of 0 indicates that the closing price is equal to the highest high over the lookback period.

### Interpretation of Williams %R
The Williams %R indicator helps traders identify overbought and oversold conditions:
- **Overbought Condition**: When Williams %R is above -20.
- **Oversold Condition**: When Williams %R is below -80.

Overbought conditions suggest that prices are getting unsustainably high and may be due for a pullback. Conversely, oversold conditions suggest that prices are getting unsustainably low and may be due for a rebound.

### Trading Strategies Using Williams %R
There are several trading strategies that incorporate Williams %R:

#### 1. Overbought/Oversold Strategy
This simple strategy involves selling when the Williams %R indicator suggests overbought conditions (values above -20) and buying when it suggests oversold conditions (values below -80).

#### 2. Trend Reversal
Traders can also use Williams %R to identify potential trend reversals. For instance, a move from overbought territory to below -20 can signal the beginning of a downtrend. Similarly, a move from oversold territory to above -80 can signal the beginning of an uptrend.

#### 3. Confirming Signals
Williams %R is often used in conjunction with other indicators to confirm signals. For example, traders may look for alignment between Williams %R and other technical indicators like Moving Averages, RSI (Relative Strength Index), or MACD (Moving Average Convergence Divergence) to confirm trade signals.

### Advantages of Williams %R
- **Speed**: Williams %R is responsive and captures short-term price movements effectively.
- **Simplicity**: The indicator is straightforward to calculate and easy to interpret.
- **Versatility**: It can be used across different markets and time frames.

### Limitations of Williams %R
- **False Signals**: Like most technical indicators, Williams %R can produce false signals, particularly in trending markets where it may remain in overbought or oversold conditions for extended periods.
- **Lag**: It is a lagging indicator, meaning it reflects past price movements, which may not always reliably predict future price movements.

### Practical Examples of Williams %R
Let’s look at some practical examples to deepen our understanding.

#### Example 1: Stock Trading
Suppose a trader is examining the stock of a tech company, and the Williams %R indicator for the stock has moved above -20, indicating overbought conditions. The trader might decide to sell the stock or hold off on buying more, anticipating a potential price drop.

#### Example 2: Forex Market
In the forex market, if the EUR/USD currency pair shows a Williams %R value below -80, this suggests that the pair is in oversold territory. A trader observing this may consider entering a long position, expecting a price rebound.

### Implementing Williams %R in Algorithmic Trading
Algorithmic trading involves the use of automated systems to execute trades based on predefined criteria. Williams %R can be a valuable tool in an algorithmic trading system for identifying trade opportunities and making data-driven decisions.

#### Example Algorithm Strategy
Consider an algorithm that:
1. Buys a security when Williams %R moves below -80.
2. Sells the security when Williams %R moves above -20.

### Advanced Techniques
#### 1. Combining with Moving Averages
Traders can enhance the effectiveness of Williams %R by combining it with moving averages. For example, a trader might use a 50-period moving average to determine the overall trend and then use Williams %R to identify entry points within that trend.

#### 2. Integrating with Relative Strength Index (RSI)
Williams %R can be used alongside RSI to confirm signals. For instance, when both indicators show oversold conditions, it could be a stronger signal to buy.

#### 3. Adaptive Williams %R
Some advanced traders may use an adaptive Williams %R, where the lookback period adjusts based on market volatility. This approach aims to make the indicator more responsive during volatile periods and less responsive during stable periods.

### Implementing Williams %R in Software
#### Python Example
Below is a basic example of how to implement Williams %R in Python using the pandas library:

```python
import pandas as pd

def williams_r(data, lookback_period=14):
    highest_high = data['High'].rolling(window=lookback_period).max()
    lowest_low = data['Low'].rolling(window=lookback_period).min()
    williams_r = (highest_high - data['Close']) / (highest_high - lowest_low) * -100
    return williams_r

# Sample data
data = {
    'High': [10, 12, 13, 15, 14, 17, 18],
    'Low': [5, 6, 7, 7, 9, 10, 11],
    'Close': [9, 11, 10, 13, 12, 14, 15]
}
df = pd.DataFrame(data)

# Calculate Williams %R
df'[Williams %R'] = williams_r(df)
print(df)
```

### Conclusion
Williams Percent Range is a robust technical indicator that helps traders identify potential overbought and oversold conditions, providing valuable insights for making informed trading decisions. Whether used in isolation or combined with other indicators, Williams %R is a versatile tool that can enhance both discretionary and algorithmic trading strategies. Given its responsiveness and simplicity, it remains a popular choice among traders across various markets.
