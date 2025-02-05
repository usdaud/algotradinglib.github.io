# Swing High and Low

Swing high and low are critical concepts in [technical analysis](../t/technical_analysis.md) and [algorithmic trading](../a/algorithmic_trading.md). They are used to identify potential turning points in the [market](../m/market.md) and to pinpoint entry and exit points for trades.

## Swing High

A swing high is a peak reached by an [asset](../a/asset.md)'s price before a decline. More technically, a swing high is a high point in a series of price movements that is immediately preceded and followed by two lower highs. Swing highs are often used as indicators of resistance levels.

Swing highs can help traders identify potential reversals in price trends. They are used in various [technical analysis](../t/technical_analysis.md) tools, such as [Fibonacci retracement](../f/fibonacci_retracement.md), to determine how far the price may move against its current [trend](../t/trend.md).

### Identifying Swing Highs

Swing highs can be identified using different [charting techniques](../c/charting_techniques.md):

1. **[Candlestick Patterns](../c/candlestick_patterns.md)**: Swing highs can frequently be recognized by specific [candlestick](../c/candlestick.md) formations like bearish engulfing, [evening star](../e/evening_star.md), or [shooting star](../s/shooting_star.md). These patterns often signal a potential high point before a [reversal](../r/reversal.md).
2. **Moving Averages**: Traders use moving averages, such as the 50-day or [200-day moving average](../1/200-day_moving_average.md), to smooth out price movements and identify swing highs.
3. **Trendlines and Channels**: Drawing trendlines along the peaks of price movements can help pinpoint swing highs.
4. **[Technical Indicators](../t/technical_indicators.md)**: Indicators such as [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI) or Stochastic can be used to identify [overbought](../o/overbought.md) conditions, which might precede a swing high.

## Swing Low

A swing low is a [trough](../t/trough.md) reached by an [asset](../a/asset.md)'s price before it begins to rise. More technically, a swing low is a low point in a series of price movements that is immediately preceded and followed by two higher lows. Swing lows are often seen as [support levels](../s/support_levels.md).

Swing lows can help traders identify potential reversals in price trends and can be used to set stop-loss points for trades.

### Identifying Swing Lows

Similar to swing highs, swing lows can be identified using various methods:

1. **[Candlestick Patterns](../c/candlestick_patterns.md)**: Swing lows often manifest through specific [candlestick](../c/candlestick.md) formations like bullish engulfing, [morning star](../m/morning_star.md), or hammer patterns. These can indicate a potential low point before a [reversal](../r/reversal.md).
2. **Moving Averages**: Longer-term moving averages are helpful in identifying swing lows, as they help smooth out price movements.
3. **Trendlines and Channels**: Drawing trendlines along the troughs of price movements can help identify swing lows.
4. **[Technical Indicators](../t/technical_indicators.md)**: Indicators like RSI or Stochastic, when indicating [oversold](../o/oversold.md) conditions, might signal a potential swing low.

## Practical Application in Algorithmic Trading

### Designing an Algorithm

[Algorithmic trading](../a/algorithmic_trading.md) strategies that incorporate swing highs and lows can be designed to [capitalize](../c/capitalize.md) on [market](../m/market.md) reversals. Here is an outline of how such an algorithm might work:

1. **Data Collection**: Collect historical price data for the [asset](../a/asset.md).
2. **Identify Swing Points**: Use [technical analysis](../t/technical_analysis.md) tools to identify swing highs and lows.
3. **Set Rules for Entry and Exit**:
    - **Entry Point**: The algorithm could be programmed to enter a buy [trade](../t/trade.md) near identified swing lows when other indicators (like RSI below 30) confirm that the [asset](../a/asset.md) is [oversold](../o/oversold.md).
    - **Exit Point**: Exit the [trade](../t/trade.md) at a swing high or when other indicators (like RSI above 70) show the [asset](../a/asset.md) being [overbought](../o/overbought.md).
4. **[Risk Management](../r/risk_management.md)**: Set [stop-loss orders](../s/stop-loss_orders.md) at recent swing lows to minimize [risk](../r/risk.md).

### Example Algorithm

```python
[import](../i/import.md) pandas as pd
[import](../i/import.md) numpy as np

# Sample DataFrame with historical price data
data = pd.read_csv('historical_price_data.csv')

# Function to identify swing highs and lows
def identify_swing_points(data, window=5):
    data['Swing_High'] = data['High'][(data['High'].shift(1) < data['High']) & 
                                      (data['High'].shift(-1) < data['High'])].rolling(window=window).max()
    data['Swing_Low'] = data['Low'][(data['Low'].shift(1) > data['Low']) & 
                                    (data['Low'].shift(-1) > data['Low'])].rolling(window=window).min()
    [return](../r/return.md) data

# Applying the function
data = identify_swing_points(data)

# Define entry and exit criteria
def backtest_strategy(data, rsi_period=14, [overbought](../o/overbought.md)=70, [oversold](../o/oversold.md)=30):
    data['RSI'] = compute_rsi(data['Close'], rsi_period)
    buy_signals = (data['Low'] == data['Swing_Low']) & (data['RSI'] < [oversold](../o/oversold.md))
    sell_signals = (data['High'] == data['Swing_High']) & (data['RSI'] > [overbought](../o/overbought.md))
    
    data['Signal'] = 0  # 0: no signal, 1: buy, -1: sell
    data.loc[buy_signals, 'Signal'] = 1
    data.loc[sell_signals, 'Signal'] = -1
    
    [return](../r/return.md) data

# Applying the strategy
data = backtest_strategy(data)

# Function to compute RSI
def compute_rsi(series, period):
    [delta](../d/delta.md) = series.diff()
    [gain](../g/gain.md) = ([delta](../d/delta.md).where([delta](../d/delta.md) > 0, 0)).fillna(0)
    loss = (-[delta](../d/delta.md).where([delta](../d/delta.md) < 0, 0)).fillna(0)
    
    avg_gain = [gain](../g/gain.md).rolling(window=period, min_periods=1).mean()
    avg_loss = loss.rolling(window=period, min_periods=1).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    [return](../r/return.md) rsi

# Execute and visualize results
[import](../i/import.md) matplotlib.pyplot as plt

plt.figure(figsize=(14,7))
plt.plot(data['Close'], label='Price')
buy_signals = data[data['Signal'] == 1]
sell_signals = data[data['Signal'] == -1]
plt.scatter(buy_signals.[index](../i/index_instrument.md), buy_signals['Close'], marker='^', color='green', label='Buy Signal', [alpha](../a/alpha.md)=1)
plt.scatter(sell_signals.[index](../i/index_instrument.md), sell_signals['Close'], marker='v', color='red', label='Sell Signal', [alpha](../a/alpha.md)=1)
plt.legend()
plt.show()
```

### Risk and Limitations

1. **[False Signals](../f/false_signals_in_trading.md)**: Swing highs and lows might produce [false signals](../f/false_signals_in_trading.md), especially in volatile or thinly traded markets.
2. **[Lagging Indicator](../l/lagging_indicator.md)**: Swing highs and lows are often [lagging indicators](../l/lagging_indicators.md), meaning they are identified only after the [market](../m/market.md) has moved.
3. **[Market](../m/market.md) Conditions**: The [efficiency](../e/efficiency.md) of this strategy can vary with different [market](../m/market.md) conditions. It works well in trending markets but can be less effective in ranging markets.

## Case Study: Real-World Application

Some trading firms specialize in algorithmic strategies based on swing highs and lows. One notable company is [Two Sigma](https://www.twosigma.com/), a [firm](../f/firm.md) that applies [machine learning](../m/machine_learning.md) and [artificial intelligence in trading](../a/artificial_intelligence_in_trading.md) strategies. While specifics are proprietary, firms like Two Sigma use swing points as a component of larger, more complex [trading algorithms](../t/trading_algorithms.md).

## Conclusion

Swing highs and lows are invaluable tools in the arsenal of many algorithmic traders. These markers help define potential [reversal](../r/reversal.md) points and establish [market](../m/market.md) [entry and exit strategies](../e/entry_and_exit_strategies.md). While they have limitations and risks, combining them with other [technical indicators](../t/technical_indicators.md) and sound [risk management](../r/risk_management.md) principles can lead to the development of [robust](../r/robust.md) [trading algorithms](../t/trading_algorithms.md). Leveraging these techniques can thus provide considerable advantages in the competitive sphere of [algorithmic trading](../a/algorithmic_trading.md).
