# Wilder’s Smoothing Techniques

Wilder’s smoothing techniques refer to the methods of smoothing and filtering financial data developed by J. Welles Wilder, an influential figure in [technical analysis](../t/technical_analysis.md). These techniques are used by algorithmic traders and technical analysts to smooth out price data, reduce the impact of short-term fluctuations, and reveal underlying trends in financial markets.

J. Welles Wilder Jr. introduced several key indicators and methods in his seminal work, "New Concepts in Technical [Trading Systems](../t/trading_systems.md)" (1978). Among his contributions are popular indicators such as the Relative Strength Index (RSI), [Average True Range](../a/average_true_range_(atr).md) (ATR), [Parabolic SAR](../p/parabolic_sar.md) (Stop and Reverse), and the Directional Movement Index (DMI). Let’s dive into the specifics of some of these smoothing techniques and their applications in [algorithmic trading](../a/algorithmic_trading.md).

### Relative Strength Index (RSI)

The RSI is a momentum oscillator that measures the speed and change of price movements. It oscillates between 0 and 100 and is commonly used to identify overbought or oversold conditions in a market.

#### Calculation
The RSI is calculated using the following formula:

\[ RSI = 100 - \frac{100}{1 + RS} \]

where

\[ RS = \frac{\text{Average Gain}}{\text{Average Loss}} \]

The average gain and average loss are typically computed using a 14-period timeframe.

Wilder devised a smoothing technique to calculate these averages using the following steps:

1. **Compute the first average gain and average loss** using simple arithmetic means for the initial 14 periods.
2. **Use the subsequent periods' data** to smooth these values using an exponential moving average approach:

\[ \text{Average Gain}_{\text{New}} = \frac{(\text{Previous Average Gain} \times 13) + \text{Current Gain}}{14} \]

\[ \text{Average Loss}_{\text{New}} = \frac{(\text{Previous Average Loss} \times 13) + \text{Current Loss}}{14} \]

This smoothing method significantly reduces the noise in the price data, making RSI a reliable indicator for identifying trends and potential reversal points.

### Average True Range (ATR)

ATR is a volatility indicator that measures the degree of price variability. It was originally developed for commodities but can be applied to stocks and other financial instruments as well.

#### Calculation
The ATR is calculated as follows:

1. **True Range (TR)** is the greatest of the following:

   - Current High minus Current Low
   - Absolute value of Current High minus Previous Close
   - Absolute value of Current Low minus Previous Close

\[ \text{True Range} = \max(\text{Current High} - \text{Current Low}, |\text{Current High} - \text{Previous Close}|, |\text{Current Low} - \text{Previous Close}|) \]

2. **[Average True Range](../a/average_true_range_(atr).md) (ATR)** is then computed using a 14-period smoothing technique:

\[ \text{ATR}_{\text{New}} = \frac{(\text{Previous ATR} \times 13) + \text{Current TR}}{14} \]

The ATR gives traders an idea of the [historical price volatility](../h/historical_price_volatility.md), which can help in setting stop-loss levels, [position sizing](../p/position_sizing.md), and identifying potential breakout points.

### Parabolic SAR (Stop and Reverse)

The [Parabolic SAR](../p/parabolic_sar.md) is a trend-following indicator that indicates potential reversal points in the market. It plots points on the chart that define the price trend direction.

#### Calculation
The [Parabolic SAR](../p/parabolic_sar.md) is computed as:

1. For an uptrend:

\[ \text{SAR} = \text{Previous SAR} + \alpha (\text{EP} - \text{Previous SAR}) \]

2. For a downtrend:

\[ \text{SAR} = \text{Previous SAR} - \alpha (\text{Previous SAR} - \text{EP}) \]

where EP (Extreme Point) is the highest high or lowest low of the current trend, and \(\alpha\) (acceleration factor) starts at 0.02 and increases by 0.02 up to a maximum of 0.20 every time a new EP is reached.

The resulting SAR values create a parabola that moves closer to the price under trending conditions, offering a dynamic system for setting trailing stops.

### Directional Movement Index (DMI) and Average Directional Index (ADX)

The DMI is used to identify the presence and strength of a trend. It consists of three components:

1. **+DI (Positive Directional Indicator)** - measures the strength of upward movement
2. **-DI (Negative Directional Indicator)** - measures the strength of downward movement
3. **ADX ([Average Directional Index](../a/average_directional_index_(adx).md))** - measures the overall strength of the trend without regard to direction

#### Calculation
1. **Calculate Directional Movement (+DM and -DM)**:

   - +DM = Current High - Previous High (if positive and greater than -DM, else 0)
   - -DM = Previous Low - Current Low (if positive and greater than +DM, else 0)

2. **Calculate Smoothed +DM and -DM** using a 14-period smoothing:

\[ +DM_{\text{S}} = (+DM_{\text{Prior}} - \frac{+DM_{\text{Prior}}}{14}) + +DM_{\text{Current}} \]

\[ -DM_{\text{S}} = (-DM_{\text{Prior}} - \frac{-DM_{\text{Prior}}}{14}) + -DM_{\text{Current}} \]

3. **Calculate the Directional Indicator values**:

\[ +DI = 100 \times \frac{+DM_{\text{S}}}{ATR} \]

\[ -DI = 100 \times \frac{-DM_{\text{S}}}{ATR} \]

4. **Calculate the ADX** to measure the trend strength:

\[ DX = 100 \times \frac{| +DI - -DI |}{ +DI + -DI } \]

\[ ADX = \left( \text{Prior ADX} \times 13 + \text{Current DX} \right) / 14 \]

The ADX line helps distinguish trending from non-trending conditions, while the +DI and -DI lines indicate the trend's direction and strength.

### Applications in Algorithmic Trading

Algorithmic traders utilize Wilder's smoothing techniques in various strategies, including:

1. **[Mean Reversion](../m/mean_reversion.md) Strategies**: Using RSI to identify overbought or oversold conditions for triggering buy or sell signals.
2. **[Trend Following](../t/trend_following.md) Strategies**: Implementing [Parabolic SAR](../p/parabolic_sar.md) and ADX to determine entry and exit points in line with prevailing trends.
3. **Volatility-Based Strategies**: Leveraging ATR to dynamically set stop-loss levels and adjust [position sizing](../p/position_sizing.md) according to market volatility.

These techniques provide a robust framework for [systematic trading](../s/systematic_trading.md) due to their ability to filter out noise and focus on significant price movements and trends.

For more information about their applications in modern [trading systems](../t/trading_systems.md), consider reviewing resources provided by financial market education services or professional trading firms that specialize in [algorithmic trading](../a/algorithmic_trading.md).

- [Investopedia: Relative Strength Index (RSI)](https://www.investopedia.com/terms/r/rsi.asp)
- [Investopedia: Average True Range (ATR)](https://www.investopedia.com/terms/a/atr.asp)
- [Investopedia: Parabolic SAR](https://www.investopedia.com/terms/p/parabolicindicator.asp)
- [Investopedia: Directional Movement Index (DMI)](https://www.investopedia.com/terms/d/dmi.asp)