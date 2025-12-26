# Ultimate Oscillator

The Ultimate [Oscillator](../o/oscillator.md) is a [technical analysis](../t/technical_analysis.md) tool used to measure [momentum](../m/momentum.md) across three different timeframes. Developed by Larry Williams in 1976, the Ultimate [Oscillator](../o/oscillator.md) aims to capture the advantages of various timeframes and minimize the drawbacks inherent to single time period oscillators. This tool combines short, intermediate, and long-term periods to create a single [value](../v/value.md) that attempts to be more accurate and less susceptible to [false signals](../f/false_signals_in_trading.md) than other [momentum indicators](../m/momentum_indicators.md).

## Components of the Ultimate Oscillator

The Ultimate [Oscillator](../o/oscillator.md) is designed to blend short, medium, and long-term timeframes into a single [oscillator](../o/oscillator.md) [value](../v/value.md). The three time periods typically used are 7, 14, and 28 periods. The formula calculates a [weighted average](../w/weighted_average.md) of each of these periods to create a unified measure of [market](../m/market.md) [momentum](../m/momentum.md).

### Calculation of the Ultimate Oscillator

The calculation of the Ultimate [Oscillator](../o/oscillator.md) involves several steps, which includes the True [Range](../r/range.md), Buying Pressure, and average Buying Pressure across three different timeframes. Below are the steps broken down:

1. **True [Range](../r/range.md) (TR)**:
 The True [Range](../r/range.md) is the highest [value](../v/value.md) of the following:
 - The current High minus the current Low.
 - The absolute [value](../v/value.md) of the current High minus the previous Close.
 - The absolute [value](../v/value.md) of the current Low minus the previous Close.

 \[
 TR = \max\left(\text{Current High} - \text{Current Low}, |\text{Current High} - \text{Previous Close}|, |\text{Current Low} - \text{Previous Close}|\right)
 \]

2. **Buying Pressure (BP)**:
 The Buying Pressure is the difference between the Current Close and the Lesser of the Current Low or the Previous Close.

 \[
 BP = \text{Current Close} - \min(\text{Current Low}, \text{Previous Close})
 \]

3. **Average Buying Pressure (AvgBP)**:
 For each of the three different periods (typically 7, 14, and 28), calculate the Sum of Buying Pressures and the Sum of True Ranges:
 \[
 \text{AvgBP}_{7} = \sum_{i=1}^{7} BP_i, \quad \text{AvgTR}_{7} = \sum_{i=1}^{7} TR_i
 \]
 \[
 \text{AvgBP}_{14} = \sum_{i=1}^{14} BP_i, \quad \text{AvgTR}_{14} = \sum_{i=1}^{14} TR_i
 \]
 \[
 \text{AvgBP}_{28} = \sum_{i=1}^{28} BP_i, \quad \text{AvgTR}_{28} = \sum_{i=1}^{28} TR_i
 \]

4. **[Weighted Averages](../w/weighted_averages_in_trading.md)**:
 Calculate the [weighted average](../w/weighted_average.md) of these Buying Pressure averages and True [Range](../r/range.md) averages:
 \[
 BP_w = \frac{(4 \cdot \text{AvgBP}_{7} + 2 \cdot \text{AvgBP}_{14} + \text{AvgBP}_{28})}{(4 + 2 + 1)}
 \]
 \[
 TR_w = \frac{(4 \cdot \text{AvgTR}_{7} + 2 \cdot \text{AvgTR}_{14} + \text{AvgTR}_{28})}{(4 + 2 + 1)}
 \]

5. **Ultimate [Oscillator](../o/oscillator.md) (UO)**:
 Finally, the Ultimate [Oscillator](../o/oscillator.md) [value](../v/value.md) is calculated as:
 \[
 UO = 100 \times \left(\frac{BP_w}{TR_w}\right)
 \]

### Interpretation of the Ultimate Oscillator

The Ultimate [Oscillator](../o/oscillator.md) ranges between 0 and 100, similar to other oscillators like the RSI ([Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md)). It helps traders identify buying or selling pressure in a [security](../s/security.md).

- **[Overbought](../o/overbought.md) and [Oversold](../o/oversold.md) Conditions**: Generally, a [value](../v/value.md) above 70 is considered [overbought](../o/overbought.md), and a [value](../v/value.md) below 30 is considered [oversold](../o/oversold.md). These conditions usually indicate a potential [reversal](../r/reversal.md) in the price [trend](../t/trend.md).
- **Bullish and Bearish Divengences**: [Divergence](../d/divergence.md) occurs when the price of an [asset](../a/asset.md) moves in the opposite direction of the Ultimate [Oscillator](../o/oscillator.md).
 - **[Bullish Divergence](../b/bullish_divergence.md)**: This happens when prices are making new lows but the Ultimate [Oscillator](../o/oscillator.md) is making higher lows. This is an indication that the selling pressure is declining and a [reversal](../r/reversal.md) to the [upside](../u/upside.md) might happen soon.
 - **[Bearish Divergence](../b/bearish_divergence.md)**: This is when prices are making new highs, but the Ultimate [Oscillator](../o/oscillator.md) is making lower highs. This suggests that buying pressure is waning and a [reversal](../r/reversal.md) to the downside might be imminent.

## Practical Use of the Ultimate Oscillator

The Ultimate [Oscillator](../o/oscillator.md) is employed similarly to other [momentum oscillators](../m/momentum_oscillators.md) but is renowned for its multi-dimensional approach to timeframes, reducing the chances of [false signals](../f/false_signals_in_trading.md). Below are a few strategies:

### Overbought/Oversold Strategy

This is the most basic strategy and uses the 70/30 rule mentioned earlier.

- **Buy Signal**: When the Ultimate [Oscillator](../o/oscillator.md) falls below 30 ([oversold](../o/oversold.md)) and then rises above it.
- **Sell Signal**: When the Ultimate [Oscillator](../o/oscillator.md) rises above 70 ([overbought](../o/overbought.md)) and then falls below it.

### Divergence Strategy

Using divergences to identify potential reversals is a popular strategy:

- **[Bullish Divergence](../b/bullish_divergence.md)**: If the price chart shows lower lows but the Ultimate [Oscillator](../o/oscillator.md) shows higher lows, it suggests a potential upward [reversal](../r/reversal.md).
- **[Bearish Divergence](../b/bearish_divergence.md)**: If the price chart shows higher highs but the Ultimate [Oscillator](../o/oscillator.md) shows lower highs, it suggests a potential downward [reversal](../r/reversal.md).

### Confirmation Strategy

Traders often use the Ultimate [Oscillator](../o/oscillator.md) in conjunction with other [technical indicators](../t/technical_indicator.md) such as Moving Averages, RSI, or MACD to confirm signals:

- **Buy Confirmation**: When the Ultimate [Oscillator](../o/oscillator.md) rises above a certain threshold (e.g., 50), with a simultaneous crossover in a complementary [indicator](../i/indicator.md), it confirms a buying opportunity.
- **Sell Confirmation**: When the Ultimate [Oscillator](../o/oscillator.md) drops below a certain threshold (e.g., 50), with a simultaneous crossover in a complementary [indicator](../i/indicator.md), it confirms a selling opportunity.

## Advantages and Disadvantages

### Advantages
1. **Multi-Timeframe Analysis**: By incorporating [multiple](../m/multiple.md) timeframes (short, medium, long), the Ultimate [Oscillator](../o/oscillator.md) aims to capture more comprehensive [market sentiment](../m/market_sentiment.md).
2. **Low [Risk](../r/risk.md) of [False Signals](../f/false_signals_in_trading.md)**: The use of [multiple](../m/multiple.md) [weighted averages](../w/weighted_averages_in_trading.md) helps to filter out [false signals](../f/false_signals_in_trading.md) that are common in single-period oscillators.
3. **Versatility**: The Ultimate [Oscillator](../o/oscillator.md) can be used in various markets including [stocks](../s/stock.md), commodities, and forex.

### Disadvantages
1. **Complexity**: The [multiple](../m/multiple.md) steps involved in calculating the Ultimate [Oscillator](../o/oscillator.md) make it more complex compared to simpler indicators like RSI or Moving Averages.
2. **[Lagging Indicator](../l/lagging_indicator.md)**: Like other oscillators, the Ultimate [Oscillator](../o/oscillator.md) can lag behind real-time price movements, potentially [offering](../o/offering.md) signals after a [trend](../t/trend.md) has already started.
3. **Parameter Sensitivity**: The choice of time periods (7, 14, 28) may not be optimal for all assets or trading conditions, requiring manual adjustment and testing.

## Conclusion

The Ultimate [Oscillator](../o/oscillator.md), by melding together varying time periods, seeks to [offer](../o/offer.md) a balanced and less noisy perspective on [market](../m/market.md) [momentum](../m/momentum.md). While its complexity might deter some traders, the nuanced signals it provides can be invaluable in making informed trading decisions. Whether used alone or in conjunction with other [technical indicators](../t/technical_indicator.md), the Ultimate [Oscillator](../o/oscillator.md) can be a potent tool in a [trader](../t/trader.md)'s arsenal when applied correctly.

For more information on Larry Williams and his other contributions to [technical analysis](../t/technical_analysis.md),