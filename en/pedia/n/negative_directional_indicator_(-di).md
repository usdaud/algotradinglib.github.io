# Negative Directional Indicator (-DI)

The Negative Directional [Indicator](../i/indicator.md) (-DI) is a component of the Directional Movement [Index](../i/index_instrument.md) (DMI), developed by J. Welles Wilder. The -DI line is used in [technical analysis](../t/technical_analysis.md) to help traders identify the strength and direction of a [market](../m/market.md) [trend](../t/trend.md). It specifically measures movements to the downside, helping to determine bearish pressure in the [market](../m/market.md). By comparing +DI (Positive Directional [Indicator](../i/indicator.md)) with -DI, traders can [gain](../g/gain.md) insights into the [momentum](../m/momentum.md) and make informed trading decisions. To fully understand -DI and its applications, we need to explore its calculation, usage, interpretation, and limitations.

## Calculation of Negative Directional Indicator (-DI)

The -DI calculation involves several steps, starting with the determination of daily price movements and then applying Wilder's smoothing techniques. Here's a breakdown of the process:

1. **Calculate True [Range](../r/range.md) (TR):**
   True [Range](../r/range.md) is the greatest of the following:
   - Current High - Current Low
   - Absolute [Value](../v/value.md) of the Current High - Previous Close
   - Absolute [Value](../v/value.md) of the Current Low - Previous Close

2. **Calculate Negative Directional Movement (-DM):**
   If the previous low minus the current low is greater than the current high minus the previous high, and greater than zero:
   - Negative Directional Movement (-DM) = Previous Low - Current Low
   Otherwise:
   - Negative Directional Movement (-DM) = 0

3. **Smooth -DM and TR:**
   Apply Wilder's smoothing method, which is akin to a moving average but with certain adjustments. The commonly used period is 14.
   - Smoothed -DM = Previous -DM - (Previous -DM/Period) + Current -DM
   - Smoothed TR = Previous TR - (Previous TR/Period) + Current TR

4. **Calculate the -DI:**
   -DI is calculated as:
   - -DI = (Smoothed -DM / Smoothed TR) * 100

The final [value](../v/value.md) is plotted on an [oscillator](../o/oscillator.md) that traders can use to analyze [market](../m/market.md) conditions.

## Usage of -DI in Trading

The -DI line is predominantly used in conjunction with the Positive Directional [Indicator](../i/indicator.md) (+DI) to form the DMI that represents the overall directional movement in the marketplace. Here are some common uses:

1. **Identifying [Trend](../t/trend.md) Direction:**
   - When -DI is above +DI, it indicates that the [market](../m/market.md) [trend](../t/trend.md) is predominantly bearish.
   - Conversely, when +DI is above -DI, it suggests a bullish [trend](../t/trend.md).

2. **Generating [Trade](../t/trade.md) Signals:**
   - A common [trading strategy](../t/trading_strategy.md) is the crossover method. If +DI crosses above -DI, it can be considered a buy signal. If -DI crosses above +DI, it can be interpreted as a sell signal.

3. **Assessing [Trend](../t/trend.md) Strength:**
   - The distance between +DI and -DI can indicate the strength of a [trend](../t/trend.md). A wider gap suggests stronger trends, while a narrower gap suggests weaker trends.

## Interpretation and Analysis

Understanding how to interpret the -DI in various [market](../m/market.md) conditions is crucial:

1. **Bullish and Bearish Crossovers:**
   - A bullish crossover occurs when +DI crosses above -DI, signaling upward [momentum](../m/momentum.md).
   - A bearish crossover happens when -DI crosses above +DI, indicating downward [momentum](../m/momentum.md).

2. **Wilder's ADX:**
   - The [Average Directional Index](../a/average_directional_index_(adx).md) (ADX), another component of Wilder’s DMI system, is often used in conjunction with +DI and -DI. ADX measures the strength of a [trend](../t/trend.md) without considering its direction.

3. **Divergences:**
   - Comparing price movements against -DI can help spot divergences. If prices are rising while -DI shows increasing values, it may be a sign of [underlying](../u/underlying.md) weakness.

## Example of -DI Application

Let’s consider an example to demonstrate how -DI can be applied in a real trading scenario:

1. **Stock XYZ Analysis:**
   - Calculate the True [Range](../r/range.md) (TR) for each day.
   - Determine Negative Directional Movement (-DM) using price lows.
   - Smooth the values of -DM and TR over a 14-day period.
   - Compute -DI using the smoothed values.
   - Plot -DI and +DI on the chart.

2. **[Trading Signals](../t/trading_signals.md):**
   - If -DI crosses above +DI, XYZ shows bearish [momentum](../m/momentum.md), leading to a possible short position.
   - If +DI crosses above -DI, bullish [momentum](../m/momentum.md) takes over, suggesting a possible long position.

## Limitations of the -DI

1. **[Lagging Indicator](../l/lagging_indicator.md):**
   - Like most [trend](../t/trend.md)-following indicators, -DI tends to lag, meaning it may not capture the very beginning or end of a [trend](../t/trend.md). This could result in delayed entry or exit points.

2. **Sideways Markets:**
   - In ranging or sideways markets, -DI crossover signals may generate whipsaws, leading to [false signals](../f/false_signals_in_trading.md) and potential losses.

3. **Dependency on Period Settings:**
   - The choice of period for smoothing can significantly impact the [indicator](../i/indicator.md)'s sensitivity. Longer periods may overlook short-term movements, while shorter periods could result in excessive [noise](../n/noise.md).

## Enhancing -DI with Other Indicators

To mitigate some of the limitations, traders often use -DI in combination with other [technical analysis tools](../t/technical_analysis_tools.md):

1. **Combining with ADX:**
   - Using ADX alongside -DI and +DI helps to filter out weak trends, ensuring trades are only taken in strong trending environments.

2. **Moving Averages:**
   - Implementing moving averages can help smooth out [price action](../p/price_action.md) and validate trends identified by -DI crossovers.

3. **Oscillators:**
   - [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI) or Moving Average Convergence [Divergence](../d/divergence.md) (MACD) can be used to confirm the signals generated by -DI.

## Conclusion

The Negative Directional [Indicator](../i/indicator.md) (-DI) is a versatile tool in [technical analysis](../t/technical_analysis.md), facilitating the identification of bearish trends and aiding in the generation of [trade](../t/trade.md) signals. When effectively combined with other indicators and proper [risk management](../r/risk_management.md) strategies, -DI can substantially augment a [trader](../t/trader.md)'s analytical capabilities. However, it's essential to be aware of its limitations and continuously validate its signals with comprehensive [market](../m/market.md) analysis. For those interested in a deeper dive, consider exploring specialized trading platforms and resources like the [official J. Welles Wilder website](https://welleswilder.com/) for more advanced insights and educational materials.