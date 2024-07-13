# Volume Momentum Indicators

[Volume](../v/volume.md) [momentum indicators](../m/momentum_indicators.md) are tools used in [technical analysis](../t/technical_analysis.md) to gauge the strength or weakness of price movements based on [volume](../v/volume.md). These indicators combine [price momentum](../p/price_momentum.md) with [volume](../v/volume.md) to provide insights into the current state and potential future movements of an [asset](../a/asset.md). They help traders and investors identify trends, determine the strength of price movements, and spot trading opportunities. Various [volume](../v/volume.md) [momentum indicators](../m/momentum_indicators.md) are employed in [trading strategies](../t/trading_strategies.md), each [offering](../o/offering.md) unique advantages and interpretations.

## Types of Volume Momentum Indicators

### 1. On-Balance Volume (OBV)

On-Balance [Volume](../v/volume.md) (OBV) is a simple cumulative [volume](../v/volume.md)-based [indicator](../i/indicator.md) that adds [volume](../v/volume.md) on up days and subtracts [volume](../v/volume.md) on down days. OBV provides insights into whether [volume](../v/volume.md) is following or leading price movements.

##### Calculation:
- If the closing price is higher than the previous close, today's [volume](../v/volume.md) is added to the previous OBV.
- If the closing price is lower than the previous close, today's [volume](../v/volume.md) is subtracted from the previous OBV.

OBV can indicate the strength of a price move. A rising OBV suggests that buying [volume](../v/volume.md) is stronger, often preceding price increases, while a falling OBV indicates stronger selling [volume](../v/volume.md), often preceding price declines.

### 2. Volume Price Trend (VPT)

The [Volume](../v/volume.md) Price [Trend](../t/trend.md) (VPT) [indicator](../i/indicator.md) combines price and [volume](../v/volume.md) to provide insights into the strength of a price [trend](../t/trend.md). It accumulates a [percentage change](../p/percentage_change.md) in price and [volume](../v/volume.md) over time.

##### Calculation:
\[ \text{VPT}(i) = \text{VPT}(i-1) + \left( \frac{\text{Close}(i) - \text{Close}(i-1)}{\text{Close}(i-1)} \right) \times \text{[Volume](../v/volume.md)}(i) \]

VPT helps determine the balance between [demand](../d/demand.md) and [supply](../s/supply.md) and can indicate whether a [trend](../t/trend.md) is likely to continue or reverse.

### 3. Chaikin Money Flow (CMF)

The Chaikin [Money Flow](../m/money_flow.md) (CMF) [indicator](../i/indicator.md) uses both price and [volume](../v/volume.md) to measure the buying and selling pressure over a specific period. It ranges from -1 to +1.

##### Calculation:
\[ \text{CMF} = \frac{ \sum_{i=n}^{m} \text{ADL}_{i} \times \text{[Volume](../v/volume.md)}_{i} }{ \sum_{i=n}^{m} \text{[Volume](../v/volume.md)}_{i} } \]

where ADL (Accumulation/[Distribution](../d/distribution.md) Line) is calculated as:
\[ \text{ADL} = \frac{ (\text{Close} - \text{Low}) - (\text{High} - \text{Close}) }{ \text{High} - \text{Low} } \]

A positive CMF [value](../v/value.md) indicates buying pressure, while a negative CMF [value](../v/value.md) indicates selling pressure.

### 4. Money Flow Index (MFI)

The [Money Flow](../m/money_flow.md) [Index](../i/index_instrument.md) (MFI) is a [volume](../v/volume.md)-[weighted](../w/weighted.md) version of the [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI). It ranges from 0 to 100 and is used to identify [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions in the [market](../m/market.md).

##### Calculation:
\[ \text{MFI} = 100 - \left( \frac{100}{1 + \text{[Money Flow](../m/money_flow.md) Ratio}} \right) \]

The [Money Flow](../m/money_flow.md) Ratio is the ratio of positive [money flow](../m/money_flow.md) to negative [money flow](../m/money_flow.md) over a specified period. Positive [money flow](../m/money_flow.md) is calculated when the typical price is higher than the previous typical price, and negative [money flow](../m/money_flow.md) is calculated when the typical price is lower.

### 5. Volume Oscillator

The [Volume Oscillator](../v/volume_oscillator.md) measures the difference between two moving averages of [volume](../v/volume.md), providing insights into changes in [volume](../v/volume.md) trends.

##### Calculation:
\[ \text{[Volume Oscillator](../v/volume_oscillator.md)} = \frac{ \text{Short-term MA of [Volume](../v/volume.md)} - \text{Long-term MA of [Volume](../v/volume.md)} }{ \text{Long-term MA of [Volume](../v/volume.md)} } \times 100 \]

A positive [value](../v/value.md) indicates increasing [volume](../v/volume.md), while a negative [value](../v/value.md) suggests decreasing [volume](../v/volume.md).

### 6. Force Index (FI)

The Force [Index](../i/index_instrument.md) (FI) is an [indicator](../i/indicator.md) that uses price and [volume](../v/volume.md) to assess the power behind a price movement.

##### Calculation:
\[ \text{Force Index} = \text{[Volume](../v/volume.md)} \times (\text{Close} - \text{Previous Close}) \]

A positive Force [Index](../i/index_instrument.md) suggests buying pressure, while a negative Force [Index](../i/index_instrument.md) indicates selling pressure.

### 7. Negative Volume Index (NVI) and Positive Volume Index (PVI)

The Negative [Volume](../v/volume.md) [Index](../i/index_instrument.md) (NVI) and Positive [Volume](../v/volume.md) [Index](../i/index_instrument.md) (PVI) are indicators that focus on [volume](../v/volume.md) changes. NVI increases when [volume](../v/volume.md) decreases, while PVI increases when [volume](../v/volume.md) increases.

#### NVI Calculation:
- If today's [volume](../v/volume.md) is less than the previous day's [volume](../v/volume.md):
\[ \text{NVI}(i) = \text{NVI}(i-1) + \left( \frac{\text{Close}(i) - \text{Close}(i-1)}{\text{Close}(i-1)} \right) \times \text{NVI}(i-1) \]

#### PVI Calculation:
- If today's [volume](../v/volume.md) is greater than the previous day's [volume](../v/volume.md):
\[ \text{PVI}(i) = \text{PVI}(i-1) + \left( \frac{\text{Close}(i) - \text{Close}(i-1)}{\text{Close}(i-1)} \right) \times \text{PVI}(i-1) \]

These indicators help identify trends and reversals based on [volume](../v/volume.md) activity.

### 8. Ease of Movement (EMV)

The Ease of Movement (EMV) [indicator](../i/indicator.md) combines [volume](../v/volume.md) with price [range](../r/range.md) to quantify the ease of price movement. It ranges from negative to positive values.

##### Calculation:
\[ \text{EMV} = \frac{ \frac{(\text{High} + \text{Low})}{2} - \frac{(\text{Previous High} + \text{Previous Low})}{2} }{\text{[Volume](../v/volume.md)}} \]

Higher EMV values indicate that the price is moving easily with relatively low [volume](../v/volume.md), while lower EMV values indicate that it is harder for the price to move.

### 9. Volume Weighted Average Price (VWAP)

The [Volume](../v/volume.md) [Weighted Average](../w/weighted_average.md) Price (VWAP) is a trading [benchmark](../b/benchmark.md) that calculates the average price a [security](../s/security.md) has traded at throughout the day, based on both [volume](../v/volume.md) and price.

##### Calculation:
\[ \text{VWAP} = \frac{\sum{ \text{Typical Price} \times \text{[Volume](../v/volume.md)} }}{\sum{ \text{[Volume](../v/volume.md)} }} \]

where Typical Price is:
\[ \text{Typical Price} = \frac{\text{High} + \text{Low} + \text{Close}}{3} \]

VWAP helps traders discern the direction of the [market](../m/market.md) [trend](../t/trend.md) and decide entry and exit points.

### 10. Coppock Curve Volume Indicator

The Coppock Curve is a [momentum](../m/momentum.md) [indicator](../i/indicator.md) originally created for stock markets but can be adapted for [volume analysis](../v/volume_analysis.md). It is used to identify long-term buying opportunities.

##### Calculation:
- Apply a 10-month [weighted](../w/weighted.md) moving average (WMA) to the [volume](../v/volume.md) series.
- Compute a 14-period Rate of Change (ROC) on this WMA.
- Compute an 11-period Rate of Change on the result from the previous step.

### Applications and Strategies

[Volume](../v/volume.md) [momentum indicators](../m/momentum_indicators.md) are versatile tools that can be used in various [trading strategies](../t/trading_strategies.md):

- **[Trend Following](../t/trend_following.md)**: By confirming the strength of a [trend](../t/trend.md) with [volume indicators](../v/volume_indicators.md), traders can identify the best entry and exit points.
- **[Reversal](../r/reversal.md) Trading**: [Volume](../v/volume.md) [momentum indicators](../m/momentum_indicators.md) can signal potential reversals when there are divergences between price and the [indicator](../i/indicator.md).
- **[Breakout Trading](../b/breakout_trading.md)**: High [volume](../v/volume.md) typically accompanies breakouts, and [volume](../v/volume.md) [momentum indicators](../m/momentum_indicators.md) can help confirm the validity of the [breakout](../b/breakout.md).
- **[Volume](../v/volume.md) Clusters**: Identifying areas of high [volume](../v/volume.md) can help understand significant [support and resistance](../s/support_and_resistance.md) levels.

### Limitations

While [volume](../v/volume.md) [momentum indicators](../m/momentum_indicators.md) provide valuable insights, traders should be aware of certain limitations:

- **Lagging Nature**: Some indicators may lag price, potentially causing delays in trading decisions.
- **[False Signals](../f/false_signals_in_trading.md)**: During low [volume](../v/volume.md) periods, indicators may generate [false signals](../f/false_signals_in_trading.md).
- **Complexity**: Combining various indicators can be complex and requires an understanding of each one's mechanics.

### Conclusion

[Volume](../v/volume.md) [momentum indicators](../m/momentum_indicators.md) are essential tools in the arsenal of technical analysts and traders. They provide a deeper understanding of [market dynamics](../m/market_dynamics.md) by combining [price momentum](../p/price_momentum.md) with [volume](../v/volume.md), helping to confirm trends, identify potential reversals, and make informed trading decisions. As with any trading tool, it is crucial to integrate these indicators with other analysis methods and remain mindful of their limitations to achieve optimal results.