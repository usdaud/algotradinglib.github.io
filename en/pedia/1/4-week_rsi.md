# 4-Week RSI

The 4-Week [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI) is a [momentum](../m/momentum.md) [oscillator](../o/oscillator.md) that measures the speed and change of price movements over a specified period, in this case, four weeks. The RSI was originally introduced by J. Welles Wilder Jr. in his 1978 book, "New Concepts in Technical [Trading Systems](../t/trading_systems.md)". Traditionally, the RSI is calculated using a 14-day period; however, adapting it to a 4-week (roughly equivalent to a 20-day) timeframe can provide a different perspective, particularly useful for medium-term [trading strategies](../t/trading_strategies.md). This technical [indicator](../i/indicator.md) is widely used in algotrading for identifying [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions in a [security](../s/security.md)'s price, as well as for signaling potential reversals.

## Calculation of 4-Week RSI

The RSI calculation consists of two main components: RS, the [Relative Strength](../r/relative_strength.md), which is the average of X days' up closes divided by the average of X days' down closes, and RS, which is then used to form the RSI. Here is a step-by-step guide:

1. Calculate the daily gains and losses:
 - **[Gain](../g/gain.md)** is the closing price increase compared to the previous day.
 - **Loss** is the closing price decrease compared to the previous day.

2. Calculate the average gains and losses over the 4-week period.
 - **Average [Gain](../g/gain.md)** = Sum of all gains over the past 4 weeks / 20
 - **Average Loss** = Sum of all losses over the past 4 weeks / 20

3. Calculate the [Relative Strength](../r/relative_strength.md) (RS):
 - RS = Average [Gain](../g/gain.md) / Average Loss

4. Calculate the RSI using the following formula:
 - RSI = 100 - (100 / (1 + RS))

The RSI [will](../w/will.md) move between 0 and 100, with high values (typically above 70) indicating that the [asset](../a/asset.md) may be [overbought](../o/overbought.md), and low values (typically below 30) indicating that the [asset](../a/asset.md) may be [oversold](../o/oversold.md).

## Interpretation of 4-Week RSI

### Overbought and Oversold Conditions

- **[Overbought](../o/overbought.md)**: When RSI values are above 70, it suggests that the [asset](../a/asset.md) may be experiencing a buying excess and could be poised for a price [pullback](../p/pullback.md) or [reversal](../r/reversal.md).

- **[Oversold](../o/oversold.md)**: When RSI values are below 30, it indicates that the [asset](../a/asset.md) might be experiencing selling excess and could be due for an upward [correction](../c/correction.md).

### Divergence

- **[Bullish Divergence](../b/bullish_divergence.md)**: Occurs when the price of an [asset](../a/asset.md) makes a new low while the RSI fails to make a new low. This suggests potential weakening of the downward [trend](../t/trend.md).

- **[Bearish Divergence](../b/bearish_divergence.md)**: Occurs when the price of an [asset](../a/asset.md) makes a new high while RSI fails to make a new high. This indicates potential weakening of the upward [trend](../t/trend.md).

### RSI as a Complementary Tool

The 4-week RSI should not be used in isolation but rather in conjunction with other indicators and analysis methods, such as moving averages, MACD, and support/resistance levels, to improve the reliability of [trading signals](../t/trading_signals.md).

## Applications in Algotrading

### Algorithm Development

Developers of [algorithmic trading](../a/algorithmic_trading.md) systems can integrate the 4-week RSI into their models to automate the detection of [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions. The RSI can be programmed to trigger buy or sell signals when certain thresholds are crossed, enhancing the ability to [capitalize](../c/capitalize.md) on [momentum](../m/momentum.md) shifts.

### Backtesting

Before deploying a trading algorithm based on the 4-week RSI, it's crucial to perform thorough [backtesting](../b/backtesting.md). This process involves running the algorithm on historical data to evaluate its performance and fine-tune the parameters to minimize risks and maximize returns.

### Risk Management

Incorporating the 4-week RSI can also aid in [risk management](../r/risk_management.md) by providing exit signals when an [asset](../a/asset.md) is becoming [overbought](../o/overbought.md) or [oversold](../o/oversold.md), thus helping to avoid potential losses due to abrupt [trend](../t/trend.md) reversals.

## Practical Example

### Trading Strategy

Consider a simple [trading strategy](../t/trading_strategy.md) using the 4-week RSI:

- **Entry Rule**: Buy when the RSI crosses above 30 from below (indicating the [asset](../a/asset.md) is exiting an [oversold](../o/oversold.md) condition).
- **Exit Rule**: Sell when the RSI crosses below 70 from above (indicating the [asset](../a/asset.md) is exiting an [overbought](../o/overbought.md) condition).

### Python Implementation

Below is a basic outline of how one might implement a 4-week RSI-based strategy in Python:

```python
[import](../i/import.md) pandas as pd

def calculate_rsi(data, window_length):
    close = data['Close']
    [delta](../d/delta.md) = close.diff()
    [gain](../g/gain.md) = ([delta](../d/delta.md).where([delta](../d/delta.md) > 0, 0)).fillna(0)
    loss = (-[delta](../d/delta.md).where([delta](../d/delta.md) < 0, 0)).fillna(0)
    
    avg_gain = [gain](../g/gain.md).rolling(window=window_length, min_periods=1).mean()
    avg_loss = loss.rolling(window=window_length, min_periods=1).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    [return](../r/return.md) rsi

# Example usage with a hypothetical data frame 'df' containing price data
df['RSI_4W'] = calculate_rsi(df, window_length=20)

# Define trading signals
df['Buy_Signal'] = (df['RSI_4W'] < 30)
df['Sell_Signal'] = (df['RSI_4W'] > 70)
```

This code snippet calculates the 4-week RSI and flags buy and sell signals based on the defined strategy rules.

## Real-World Example

One of the real-world applications of RSI in [trading algorithms](../t/trading_algorithms.md) can be observed through various trading platforms and institutional investors.

### QuantConnect

QuantConnect is an [open](../o/open.md)-source [algorithmic trading](../a/algorithmic_trading.md) platform that offers a comprehensive environment for [backtesting](../b/backtesting.md) and deploying [trading strategies](../t/trading_strategies.md). Traders using [QuantConnect](../q/quantconnect.md) can [leverage](../l/leverage.md) the RSI among numerous other indicators to build [robust](../r/robust.md) [trading algorithms](../t/trading_algorithms.md).

## Conclusion

The 4-week RSI is a powerful tool in the arsenal of [technical indicators](../t/technical_indicators.md) available to traders and algo developers. By focusing on a medium-term timeframe, it allows for improved detection of [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions that can significantly enhance the effectiveness of [trading strategies](../t/trading_strategies.md). Proper implementation, [backtesting](../b/backtesting.md), and [risk](../r/risk.md) assessment are essential to [capitalize](../c/capitalize.md) on the signals provided by the 4-week RSI and to achieve consistent and reliable trading results.