# Trend Following Indicators

[Trend following](../t/trend_following.md) is a widely respected methodology in the world of [algorithmic trading](../a/algorithmic_trading.md) that focuses on identifying the general direction of [market](../m/market.md) prices. [Trend](../t/trend.md)-following strategies aim to [profit](../p/profit.md) by riding the wave of the [market](../m/market.md)’s [momentum](../m/momentum.md). This section dives deep into the various [trend](../t/trend.md)-following indicators that traders utilize to make data-driven decisions. These indicators are potent tools that help traders to confirm existing trends and make predictions about future price movements.

## Moving Averages (MA)

Moving Averages are perhaps the most commonly used [trend](../t/trend.md)-following indicators. They smooth out price data to help identify the direction of the [trend](../t/trend.md) over a specific period. There are several types of moving averages used in trading, including:

1. **Simple Moving Average (SMA):** It calculates the average of a selected [range](../r/range.md) of prices, typically closing prices, by the number of periods in that [range](../r/range.md). 
2. **Exponential Moving Average (EMA):** This type of moving average places more weight on recent prices, which makes it more responsive to new information.
3. **[Weighted](../w/weighted.md) Moving Average (WMA):** Similar to the EMA, but the weighting of each price decreases linearly.

### Application in Trading

Traders use crossovers of MAs to generate buy/sell signals. For instance, a common strategy is the [Golden Cross](../g/golden_cross.md), where the 50-day SMA crosses above the 200-day SMA, signaling a potential [uptrend](../u/uptrend.md). Conversely, a [Death Cross](../d/death_cross.md) occurs when the 50-day SMA crosses below the 200-day SMA, suggesting a potential [downtrend](../d/downtrend.md).

## Moving Average Convergence Divergence (MACD)

The MACD is a [trend](../t/trend.md)-following [momentum](../m/momentum.md) [indicator](../i/indicator.md) that captures the relationship between two moving averages of a [security](../s/security.md)’s price. It is calculated by subtracting the 26-period EMA from the 12-period EMA. A nine-day EMA of the MACD, called the "signal line," is then plotted on top of the MACD line, which can function as a trigger for buy and sell signals.

### Components and Signals

1. **MACD Line**: The difference between the 12-day EMA and the 26-day EMA.
2. **Signal Line**: The 9-day EMA of the MACD Line.
3. **[Histogram](../h/histogram.md)**: Represents the difference between the MACD Line and the Signal Line.

MACD signals bullish trends when the MACD line crosses above the signal line and bearish trends when it crosses below.

## Average Directional Index (ADX)

The ADX is a [trend](../t/trend.md) strength [indicator](../i/indicator.md), not a [trend](../t/trend.md) direction [indicator](../i/indicator.md). It consists of three lines: the ADX line, the +DI line, and the –DI line. The ADX itself only shows the strength of the [trend](../t/trend.md), whereas the +DI and –DI lines show the direction.

### How to Use ADX

- **ADX above 25**: Indicates a strong [trend](../t/trend.md).
- **ADX below 20**: Suggests a weak [trend](../t/trend.md).
- **+DI above –DI**: Identifies an [uptrend](../u/uptrend.md).
- **+DI below –DI**: Identifies a [downtrend](../d/downtrend.md).

## Bollinger Bands

[Bollinger Bands](../b/bollinger_bands.md) consist of a middle band being an N-period SMA (simple moving average), an upper band at K times an N-period [standard deviation](../s/standard_deviation.md) above the middle band, and a lower band at K times an N-period [standard deviation](../s/standard_deviation.md) below the middle band.

### Utilization in Strategies

- **[Trend](../t/trend.md) Identification**: Prices moving along the upper band can indicate a strong [uptrend](../u/uptrend.md), while prices moving along the lower band may indicate a [downtrend](../d/downtrend.md).
- **[Volatility](../v/volatility.md) Measurement**: When the bands expand, it indicates increasing [volatility](../v/volatility.md); when they contract, it suggests decreasing [volatility](../v/volatility.md).

## Ichimoku Cloud

Also called the Ichimoku Kinko Hyo, this tool is often used for identifying future areas of [support and resistance](../s/support_and_resistance.md). It is composed of five main components:

1. **Tenkan-sen (Conversion Line)**: The average of the highest high and the lowest low over the last 9 periods.
2. **Kijun-sen (Base Line)**: The average of the highest high and the lowest low over the last 26 periods.
3. **Senkou Span A (Leading Span A)**: The average of the Tenkan-sen and Kijun-sen plotted 26 periods ahead.
4. **Senkou Span B (Leading Span B)**: The average of the highest high and lowest low over the last 52 periods, plotted 26 periods ahead.
5. **Chikou Span (Lagging Span)**: Current closing price plotted 26 periods back.

### Significance for Traders

- **Bullish Signal**: When the price is above the cloud.
- **Bearish Signal**: When the price is below the cloud.
- **[Consolidation](../c/consolidation.md)**: When the price is within the cloud.

## Parabolic SAR

The Parabolic Stop and Reverse (SAR) is a [trend](../t/trend.md)-following [indicator](../i/indicator.md) that is used to identify potential [reversal](../r/reversal.md) points. It is denoted by dots that are placed above or below the price on a chart, depending on the direction of the [trend](../t/trend.md).

### Trading with Parabolic SAR

- **Buy Signal**: When the [indicator](../i/indicator.md) dots move below the price, it suggests upward [momentum](../m/momentum.md).
- **Sell Signal**: When the [indicator](../i/indicator.md) dots move above the price, it indicates downward [momentum](../m/momentum.md).

## Supertrend Indicator

The Supertrend [indicator](../i/indicator.md) is a [trend](../t/trend.md)-following [overlay](../o/overlay.md) on the chart. Compared to other indicators, it is easier to use due to its simpler approach. The [indicator](../i/indicator.md) changes its color depending on the direction of the [trend](../t/trend.md).

### Application

- **Green Line**: Indicates a buy signal.
- **Red Line**: Indicates a sell signal.

## Donchian Channels

[Donchian Channels](../d/donchian_channels.md) were developed by Richard Donchian and consist of three lines: an upper, a lower, and a middle band. The upper band shows the highest price over a certain period while the lower band shows the lowest price. The middle band is the average of these two values.

### Usage in Trading

- **Breakouts**: When the price breaks above the upper band, it may indicate a buy signal. Conversely, when the price breaks below the lower band, it could be a sell signal.

## Turtle Trading Strategy

Developed by Richard Dennis and William Eckhardt, this system employs [breakout](../b/breakout.md) strategies to determine entry and exit points. This strategy heavily depends on [Donchian Channels](../d/donchian_channels.md) for [trade](../t/trade.md) signals and has specific rules for [position sizing](../p/position_sizing.md) and [risk management](../r/risk_management.md).

### Rules

- Entry signals are generated when the price exceeds the high or low of a specific period (20-day or 55-day [breakout](../b/breakout.md) periods are commonly used).
- Stop-loss levels are set using the [Average True Range](../a/average_true_range_(atr).md) (ATR) [indicator](../i/indicator.md).

## ADX + DI Strategy

This strategy utilizes the [Average Directional Index](../a/average_directional_index_(adx).md) in combination with the Directional Movement [Index](../i/index.md) (DMI) to identify and [trade](../t/trade.md) based on the [trend](../t/trend.md)'s strength and direction.

### Trading Signals

- **Buy Signal**: When +DI crosses above –DI and the ADX is above 25.
- **Sell Signal**: When -DI crosses above +DI and the ADX is above 25.

## Coppock Curve

Developed by Edwin Coppock, this [indicator](../i/indicator.md) was initially designed for identifying long-term buying opportunities. The curve consists of a 10-month [weighted](../w/weighted.md) moving average of the sum of a 14-month rate of change and an 11-month rate of change.

### Application

- **Buy Signal**: When the curve turns up after being below zero.
- **Sell Signal**: Not traditionally used for selling signals, making it less useful for those looking to short-sell.

## Conclusion

[Trend](../t/trend.md)-following indicators are indispensable tools for algorithmic traders aiming to [capitalize](../c/capitalize.md) on consistent [market](../m/market.md) movements. Each [indicator](../i/indicator.md) has its unique properties and is suited to different types of [market](../m/market.md) conditions. Employing a combination of these indicators can help in creating a [robust](../r/robust.md) [trading strategy](../t/trading_strategy.md) that minimizes [risk](../r/risk.md) and maximizes [return](../r/return.md). By understanding the functions and applications of each, traders can optimize their approaches and make more informed trading decisions.