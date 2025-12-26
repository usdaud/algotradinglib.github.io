# Vortex Indicator (VI)

The Vortex [Indicator](../i/indicator.md) (VI) is a [technical analysis](../t/technical_analysis.md) tool used in [financial markets](../f/financial_market.md), particularly in trading, to identify the start of new trends and to confirm the direction of existing trends. It was developed by Etienne Botes and Douglas Siepman and introduced in a 2010 edition of the *[Technical Analysis](../t/technical_analysis.md) of [Stocks](../s/stock.md) & Commodities* magazine. This [indicator](../i/indicator.md) is based on the concept of vortex motion, as seen in water and other natural phenomena, applied to price movements in the [market](../m/market.md). The Vortex [Indicator](../i/indicator.md) is made up of two lines: the positive vortex line (VI+) and the negative vortex line (VI-). These lines oscillate around a centerline, helping traders to spot [trend](../t/trend.md) formations and potential [reversal](../r/reversal.md) points.

## Key Components

### Positive Vortex Line (VI+)

The positive vortex line (VI+) captures upward price movement by identifying significant upward price differences over a given period. It is calculated using the current high and the previous low prices. When VI+ crosses above VI-, it signals a potential bullish [trend](../t/trend.md).

### Negative Vortex Line (VI-)

The negative vortex line (VI-) measures downward price movement, capturing significant downward price differences over a specified period. This is calculated using the current low and the previous high prices. When VI- crosses above VI+, it indicates a potential bearish [trend](../t/trend.md).

## Calculation of the Vortex Indicator

The Vortex [Indicator](../i/indicator.md) is calculated using the following steps:

1. **Compute the True [Range](../r/range.md) (TR):**
 The True [Range](../r/range.md) is the greatest of the following:

 - Current high minus the current low
 - Absolute [value](../v/value.md) of the current high minus the previous close
 - Absolute [value](../v/value.md) of the current low minus the previous close

 \[
 TR_t = \max [(High_t - Low_t), |High_t - Close_{t-1}|, |Low_t - Close_{t-1}|]
 \]

2. **Compute Upward Movement (VM+):**
 The upward movement for the period is the absolute [value](../v/value.md) of the current high minus the previous low.

 \[
 VM^+_t = |High_t - Low_{t-1}|
 \]

3. **Compute Downward Movement (VM-):**
 The downward movement for the period is the absolute [value](../v/value.md) of the current low minus the previous high.

 \[
 VM^-_t = |Low_t - High_{t-1}|
 \]

4. **Sum these values over a specific period (n):**
 Sum the True [Range](../r/range.md), the Upward Movement, and the Downward Movement over 'n' periods.

 \[
 TR_n = \sum_{i=1}^n TR_i
 \]
 \[
 VM^+_n = \sum_{i=1}^n VM^+_i
 \]
 \[
 VM^-_n = \sum_{i=1}^n VM^-_i
 \]

5. **Calculate VI+ and VI-:**
 Divide the summed values of VM+ and VM- by the sum of the True [Range](../r/range.md) over the chosen period.

 \[
 VI^+_n = \frac{VM^+_n}{TR_n}
 \]
 \[
 VI^-_n = \frac{VM^-_n}{TR_n}
 \]

## Interpretation and Use in Trading

### Bullish and Bearish Signals

- **Bullish Signal:** When VI+ crosses above VI-, it indicates that upward price movement is stronger than downward movement, signaling a potential bullish [trend](../t/trend.md).
- **Bearish Signal:** When VI- crosses above VI+, it implies that downward price movement is stronger, suggesting a potential bearish [trend](../t/trend.md).

### Trend Confirmation

The Vortex [Indicator](../i/indicator.md) is particularly useful in confirming the direction of a [trend](../t/trend.md). For instance, if VI+ continues rising above VI-, it reaffirms the strength of the bullish [trend](../t/trend.md). Conversely, if VI- stays above VI+, it validates the strength of the bearish [trend](../t/trend.md).

### Divergence Analysis

Traders can also use the Vortex [Indicator](../i/indicator.md) to identify [divergence](../d/divergence.md). [Divergence](../d/divergence.md) occurs when the price moves in one direction and the [indicator](../i/indicator.md) moves in the opposite direction, signaling a potential [trend reversal](../t/trend_reversal.md). For example:
- **[Bullish Divergence](../b/bullish_divergence.md):** If the price is making lower lows while VI+ is making higher lows.
- **[Bearish Divergence](../b/bearish_divergence.md):** If the price is making higher highs while VI- is making lower highs.

## Limitations

Despite its effectiveness, the Vortex [Indicator](../i/indicator.md) has some limitations:

- **Lag:** The Vortex [Indicator](../i/indicator.md), like many [trend](../t/trend.md)-following indicators, can lag due to its reliance on past price data.
- **[False Signals](../f/false_signals_in_trading.md):** In sideways or choppy markets, the Vortex [Indicator](../i/indicator.md) may generate [false signals](../f/false_signals_in_trading.md) as VI+ and VI- frequently cross each other without establishing a clear [trend](../t/trend.md).
- **Parameter Sensitivity:** The choice of period (n) can significantly impact the [indicator](../i/indicator.md)’s performance. Shorter periods make the [indicator](../i/indicator.md) more sensitive to price changes but may increase [false signals](../f/false_signals_in_trading.md), while longer periods smooth out price movements but reduce sensitivity.

## Practical Application

### Stock Markets

The Vortex [Indicator](../i/indicator.md) is frequently used in stock trading to identify potential entry and exit points. For example, a [trader](../t/trader.md) might enter a long position when VI+ crosses above VI- and exit when VI- crosses above VI+.

### Forex and Commodities

In Forex and [commodity](../c/commodity.md) markets, the Vortex [Indicator](../i/indicator.md) can be particularly effective in identifying [trend](../t/trend.md) reversals and confirming the strength of ongoing trends. It's often used in conjunction with other [technical indicators](../t/technical_indicator.md) to filter out [false signals](../f/false_signals_in_trading.md) and improve the accuracy of trading decisions.

### Algorithmic Trading

The Vortex [Indicator](../i/indicator.md) can be integrated into [algorithmic trading](../a/algorithmic_trading.md) systems due to its clear formula and straightforward logic. Algorithms can be programmed to automatically execute trades based on the crossing points of VI+ and VI-, thereby eliminating emotional decision-making from trading.

### Customization and Integration

Traders can customize the Vortex [Indicator](../i/indicator.md) by adjusting the period (n) for different trading styles and [market](../m/market.md) conditions. It is also compatible with numerous trading platforms and software, including MetaTrader, [TradingView](../t/tradingview.md), and others, allowing for seamless integration into various [trading strategies](../t/trading_strategies.md).

## Comparing Vortex Indicator with Other Indicators

### Vortex Indicator vs. Moving Average Convergence Divergence (MACD)

Both VI and MACD are used to identify trends and potential reversals, but they do so in different ways:
- **VI** focuses on up and down movements relative to each other.
- **MACD** considers the relationship between two moving averages of prices.

### Vortex Indicator vs. Relative Strength Index (RSI)

While RSI measures the speed and change of price movements to identify [overbought](../o/overbought.md)/[oversold](../o/oversold.md) conditions, VI simply tracks potential [trend](../t/trend.md) direction and strength without delving into [market](../m/market.md) conditions of extremes.

### Vortex Indicator vs. ADX (Average Directional Index)

The ADX measures [trend](../t/trend.md) strength without indicating direction, while the VI provides both [trend](../t/trend.md) direction and strength. Traders may use the VI to determine [trend](../t/trend.md) direction and the ADX to confirm [trend](../t/trend.md) strength.

## Conclusion

The Vortex [Indicator](../i/indicator.md) (VI) is a valuable tool in a [trader](../t/trader.md)’s arsenal for identifying and confirming trends in various [financial markets](../f/financial_market.md). Despite its limitations, when used in conjunction with other indicators and analysis techniques, it can significantly enhance [trading strategies](../t/trading_strategies.md) by providing clear and actionable signals. A deep understanding of this [indicator](../i/indicator.md)'s mechanics and careful period selection can help traders optimize its use and improve their trading outcomes.

For more information, traders can refer to resources and publications that originally introduced and discussed the Vortex [Indicator](../i/indicator.md): Vortex Indicator Official.