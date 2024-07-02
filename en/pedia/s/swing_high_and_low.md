# Swing High and Low

Swing high and low are critical concepts in [technical analysis](../t/technical_analysis.md) and [algorithmic trading](../a/algorithmic_trading.md). They are used to identify potential turning points in the market and to pinpoint entry and exit points for trades.

## Swing High

A swing high is a peak reached by an asset's price before a decline. More technically, a swing high is a high point in a series of price movements that is immediately preceded and followed by two lower highs. Swing highs are often used as indicators of resistance levels.

Swing highs can help traders identify potential reversals in price trends. They are used in various [technical analysis](../t/technical_analysis.md) tools, such as Fibonacci retracement, to determine how far the price may move against its current trend.

### Identifying Swing Highs

Swing highs can be identified using different [charting techniques](../c/charting_techniques.md):

1. **[Candlestick Patterns](../c/candlestick_patterns.md)**: Swing highs can frequently be recognized by specific candlestick formations like bearish engulfing, evening star, or shooting star. These patterns often signal a potential high point before a reversal.
2. **Moving Averages**: Traders use moving averages, such as the 50-day or [200-day moving average](../1/200-day_moving_average.md), to smooth out price movements and identify swing highs.
3. **Trendlines and Channels**: Drawing trendlines along the peaks of price movements can help pinpoint swing highs.
4. **[Technical Indicators](../t/technical_indicators.md)**: Indicators such as Relative Strength Index (RSI) or Stochastic can be used to identify overbought conditions, which might precede a swing high.

## Swing Low

A swing low is a trough reached by an asset's price before it begins to rise. More technically, a swing low is a low point in a series of price movements that is immediately preceded and followed by two higher lows. Swing lows are often seen as [support levels](../s/support_levels.md).

Swing lows can help traders identify potential reversals in price trends and can be used to set stop-loss points for trades.

### Identifying Swing Lows

Similar to swing highs, swing lows can be identified using various methods:

1. **[Candlestick Patterns](../c/candlestick_patterns.md)**: Swing lows often manifest through specific candlestick formations like bullish engulfing, morning star, or hammer patterns. These can indicate a potential low point before a reversal.
2. **Moving Averages**: Longer-term moving averages are helpful in identifying swing lows, as they help smooth out price movements.
3. **Trendlines and Channels**: Drawing trendlines along the troughs of price movements can help identify swing lows.
4. **[Technical Indicators](../t/technical_indicators.md)**: Indicators like RSI or Stochastic, when indicating oversold conditions, might signal a potential swing low.

## Practical Application in Algorithmic Trading

### Designing an Algorithm

[Algorithmic trading](../a/algorithmic_trading.md) strategies that incorporate swing highs and lows can be designed to capitalize on market reversals. Here is an outline of how such an algorithm might work:

1. **Data Collection**: Collect historical price data for the asset.
2. **Identify Swing Points**: Use [technical analysis](../t/technical_analysis.md) tools to identify swing highs and lows.
3. **Set Rules for Entry and Exit**:
    - **Entry Point**: The algorithm could be programmed to enter a buy trade near identified swing lows when other indicators (like RSI below 30) confirm that the asset is oversold.
    - **Exit Point**: Exit the trade at a swing high or when other indicators (like RSI above 70) show the asset being overbought.
4. **[Risk Management](../r/risk_management.md)**: Set [stop-loss orders](../s/stop-loss_orders.md) at recent swing lows to minimize risk.

### Example Algorithm

```python
import pandas as pd
import numpy as np

# Sample DataFrame with historical price data
data = pd.read_csv('historical_price_data.csv')

# Function to identify swing highs and lows
def identify_swing_points(data, window=5):
    data['Swing_High'] = data['High'][(data['High'].shift(1) < data['High']) & 
                                      (data['High'].shift(-1) < data['High'])].rolling(window=window).max()
    data['Swing_Low'] = data['Low'][(data['Low'].shift(1) > data['Low']) & 
                                    (data['Low'].shift(-1) > data['Low'])].rolling(window=window).min()
    return data

# Applying the function
data = identify_swing_points(data)

# Define entry and exit criteria
def backtest_strategy(data, rsi_period=14, overbought=70, oversold=30):
    data['RSI'] = compute_rsi(data['Close'], rsi_period)
    buy_signals = (data['Low'] == data['Swing_Low']) & (data['RSI'] < oversold)
    sell_signals = (data['High'] == data['Swing_High']) & (data['RSI'] > overbought)
    
    data['Signal'] = 0  # 0: no signal, 1: buy, -1: sell
    data.loc[buy_signals, 'Signal'] = 1
    data.loc[sell_signals, 'Signal'] = -1
    
    return data

# Applying the strategy
data = backtest_strategy(data)

# Function to compute RSI
def compute_rsi(series, period):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)
    
    avg_gain = gain.rolling(window=period, min_periods=1).mean()
    avg_loss = loss.rolling(window=period, min_periods=1).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

# Execute and visualize results
import matplotlib.pyplot as plt

plt.figure(figsize=(14,7))
plt.plot(data['Close'], label='Price')
buy_signals = data[data['Signal'] == 1]
sell_signals = data[data['Signal'] == -1]
plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='green', label='Buy Signal', alpha=1)
plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='red', label='Sell Signal', alpha=1)
plt.legend()
plt.show()
```

### Risk and Limitations

1. **False Signals**: Swing highs and lows might produce false signals, especially in volatile or thinly traded markets.
2. **Lagging Indicator**: Swing highs and lows are often [lagging indicators](../l/lagging_indicators.md), meaning they are identified only after the market has moved.
3. **Market Conditions**: The efficiency of this strategy can vary with different market conditions. It works well in trending markets but can be less effective in ranging markets.

## Case Study: Real-World Application

Some trading firms specialize in algorithmic strategies based on swing highs and lows. One notable company is [Two Sigma](https://www.twosigma.com/), a firm that applies machine learning and [artificial intelligence in trading](../a/artificial_intelligence_in_trading.md) strategies. While specifics are proprietary, firms like Two Sigma use swing points as a component of larger, more complex [trading algorithms](../t/trading_algorithms.md).

## Conclusion

Swing highs and lows are invaluable tools in the arsenal of many algorithmic traders. These markers help define potential reversal points and establish market [entry and exit strategies](../e/entry_and_exit_strategies.md). While they have limitations and risks, combining them with other [technical indicators](../t/technical_indicators.md) and sound [risk management](../r/risk_management.md) principles can lead to the development of robust [trading algorithms](../t/trading_algorithms.md). Leveraging these techniques can thus provide considerable advantages in the competitive sphere of [algorithmic trading](../a/algorithmic_trading.md).
