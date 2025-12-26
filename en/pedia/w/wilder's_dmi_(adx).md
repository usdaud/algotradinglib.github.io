# Wilder's DMI (ADX)

Wilder's Directional Movement [Index](../i/index_instrument.md) (DMI), often known simply as ADX ([Average Directional Index](../a/average_directional_index_(adx).md)), is a [technical analysis](../t/technical_analysis.md) [indicator](../i/indicator.md) designed by J. Welles Wilder. It is primarily used to quantify the strength of a [trend](../t/trend.md) in a financial [market](../m/market.md), be it an upward (bullish) or downward (bearish) [trend](../t/trend.md). Traders and analysts use ADX extensively because of its ability to reflect the dynamism or stability of trading patterns in diverse financial instruments, including [stocks](../s/stock.md), commodities, forex, and more.

The ADX forms part of a comprehensive set of indicators introduced by Wilder in his seminal book, "New Concepts in Technical [Trading Systems](../t/trading_systems.md)," published in 1978. Besides ADX, Wilder also introduced the [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI), [Parabolic SAR](../p/parabolic_sar.md), and more, which have become indispensable tools in modern [technical analysis](../t/technical_analysis.md).

## Components of the DMI

The Directional Movement [Index](../i/index_instrument.md) is comprised of three lines:

1. **Plus Directional [Indicator](../i/indicator.md) (+DI)** - Represents positive directional movement.
2. **Minus Directional [Indicator](../i/indicator.md) (-DI)** - Represents negative directional movement.
3. **[Average Directional Index](../a/average_directional_index_(adx).md) (ADX)** - Represents the strength of the [trend](../t/trend.md), regardless of the direction.

### Calculating the DI Lines

The calculations for the +DI and -DI lines are relatively straightforward and consist of several steps:

1. **True [Range](../r/range.md) (TR)**: The true [range](../r/range.md) is the greatest of the following:
 - Current high minus current low
 - Absolute [value](../v/value.md) of the current high minus the previous close
 - Absolute [value](../v/value.md) of the current low minus the previous close

 \[
 TR = \max[(\text{current high} - \text{current low}), \|(\text{current high} - \text{previous close})\|, \|(\text{current low} - \text{previous close})\|]
 \]

2. **Directional Movement (DM)**:
 - Positive Directional Movement (+DM): If the current high minus the previous high is greater than the previous low minus the current low, and greater than zero, then +DM is the current high minus the previous high. Otherwise, +DM is zero.
 - Negative Directional Movement (-DM): If the previous low minus the current low is greater than the current high minus the previous high, and greater than zero, then -DM is the previous low minus the current low. Otherwise, -DM is zero.

 \[
 +DM = (\text{current high} - \text{previous high}) \, \text{(if \, it too \, is \, greater \, than \, the \, other)}
 \]

 \[
 -DM = (\text{previous low} - \text{current low}) \, \text{(if \, it \, is \, greater \, than \, the \, other)}
 \]

3. **Smoothen the DI**: Calculate the smooth average of the Directional Movement over a set period (usually 14 days):

 \[
 +DI = 100 \times (\operatorname{Smoothed +DM}/\operatorname{ATR})
 \]

 \[
 -DI = 100 \times (\operatorname{Smoothed -DM}/\operatorname{ATR})
 \]

 Where ATR ([Average True Range](../a/average_true_range_(atr).md)) is the smoothened True [Range](../r/range.md) over the same period.

### Calculating the ADX

After obtaining +DI and -DI, the ADX itself can be calculated through the following steps:

1. **Directional Movement (DX)**: This computes the absolute difference between the +DI and -DI lines, divided by the sum of the +DI and -DI lines, then multiplied by 100:

 \[
 DX = \frac{\left|(+DI) - (-DI)\right|}{(+DI) + (-DI)} \times 100
 \]

2. **Average DX (ADX)**:
 Smooth the DX values over a set period ([default](../d/default.md) is usually 14 days). The ADX values indicate the strength of the [trend](../t/trend.md):

 \[
 ADX = \operatorname{Smooth\ Average\ of\ } DX
 \]

## Interpreting ADX Values

The ADX values generally [range](../r/range.md) from 0 to 100 but rarely exceed 60. These values provide insight into the strength of a [trend](../t/trend.md):

- **0-20**: A weak or non-existent [trend](../t/trend.md).
- **20-40**: An emerging or moderate [trend](../t/trend.md).
- **40-60**: A strong [trend](../t/trend.md).
- **60-100**: An extremely strong [trend](../t/trend.md).

Importantly, ADX does not indicate the direction of the [trend](../t/trend.md), only its strength. For instance, an ADX above 40 could indicate either a strong upward or downward [trend](../t/trend.md).

## Practical Applications of ADX

### Identifying Trends

One of the primary uses of ADX is to determine whether a [market](../m/market.md) is trending or ranging. When ADX is above 20, it suggests that the [market](../m/market.md) is trending, and thus, [trend](../t/trend.md)-following strategies might be effective. Conversely, an ADX below 20 implies a ranging [market](../m/market.md) where mean-reversion strategies may be more suitable.

### Momentum Confirmation

Traders often use ADX to confirm [momentum](../m/momentum.md). For example, if a stock breaks out of a [consolidation](../c/consolidation.md) phase with ADX rising above 20, it suggests that the [breakout](../b/breakout.md) is backed by strong [momentum](../m/momentum.md), increasing the probability of a sustained move.

### Divergence Analysis

Although less common, ADX can also be used in conjunction with +DI and -DI lines for [divergence](../d/divergence.md) analysis. For instance, if prices reach new highs while ADX is declining, it may indicate that the upward [trend](../t/trend.md) is losing strength.

## Real-World Example

Let's consider a real-world application of ADX in stock trading:

Suppose a [trader](../t/trader.md) is monitoring the stock of Tesla, Inc.. The [trader](../t/trader.md) can add the ADX [indicator](../i/indicator.md) to their [technical analysis](../t/technical_analysis.md) chart. If the ADX line crosses above 20 while the +DI line is above the -DI line, the [trader](../t/trader.md) may interpret this as a signal to go long, expecting the stock's [uptrend](../u/uptrend.md) to continue.

Similarly, if the ADX crosses below 20, it could signal a weakening [trend](../t/trend.md), prompting the [trader](../t/trader.md) to exit their position or implement [risk management](../r/risk_management.md) strategies.

## Integration with Algorithmic Trading

In the realm of [algorithmic trading](../a/algorithmic_trading.md), ADX can be utilized in developing automated [trading strategies](../t/trading_strategies.md). Here's how:

### Coded Strategies

By integrating ADX within [trading algorithms](../t/trading_algorithms.md), traders can automate entries and exits based on predetermined ADX thresholds. For instance, an algorithm could be programmed to initiate buy orders when the ADX rises above 20 and the +DI is greater than the -DI, and sell orders when the ADX declines below 20.

### Backtesting

Algorithms can backtest strategies that incorporate ADX to gauge their historical performance. This helps in refining the parameters and improving the strategy's robustness before deploying it in live trading.

### Optimization

Algorithmic traders often use optimized ADX parameters tailored to specific financial instruments or [market](../m/market.md) conditions. [Machine learning](../m/machine_learning.md) techniques can further enhance the adaptive nature of these strategies, allowing them to dynamically adjust to changing [market](../m/market.md) environments.

## Conclusion

Wilder's DMI (ADX) remains a cornerstone in the toolkit of technical analysts and traders worldwide. Its ability to quantitatively depict [trend](../t/trend.md) strength makes it invaluable for making informed trading decisions. Whether used in manual trading or as part of sophisticated algorithmic strategies, ADX serves as a reliable gauge of [market dynamics](../m/market_dynamics.md), contributing to more effective and profitable trading outcomes.