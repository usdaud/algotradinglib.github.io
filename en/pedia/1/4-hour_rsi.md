# 4-Hour RSI

The 4-hour [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI) is a [momentum](../m/momentum.md) [oscillator](../o/oscillator.md) used in [technical analysis](../t/technical_analysis.md) to measure the speed and change of price movements over a specified period. RSI ranges from 0 to 100, with levels above 70 indicating [overbought](../o/overbought.md) conditions and levels below 30 indicating [oversold](../o/oversold.md) conditions. The 4-hour RSI is a variant that analyzes price data in 4-hour intervals, providing a mid-term perspective on [market](../m/market.md) [momentum](../m/momentum.md). This tool is particularly useful for traders who engage in short to mid-term [trading strategies](../t/trading_strategies.md), including [algorithmic trading](../a/algorithmic_trading.md).

## Overview
[Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI) is one of the most popular [technical indicators](../t/technical_indicators.md) used by traders. Developed by J. Welles Wilder, it was first introduced in his 1978 book "New Concepts in Technical [Trading Systems](../t/trading_systems.md)." RSI measures the magnitude of recent price changes to evaluate [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions in the price of a stock or other [asset](../a/asset.md).

The formula for calculating RSI is:
\[ 
RSI = 100 - \frac{100}{1 + RS}
\]
where \( RS \) ([Relative Strength](../r/relative_strength.md)) is the average of \( n \) days' up closes divided by the average of \( n \) days' down closes.

When applied to a [4-hour chart](../1/4-hour_chart.md), RSI uses the price data from each 4-hour interval to compute this ratio. This offers a unique blend of short-term and mid-term [technical analysis](../t/technical_analysis.md) and is favored for its ability to catch prevailing trends and potential [reversal](../r/reversal.md) points.

## Calculation
For a 4-hour RSI, RS ([Relative Strength](../r/relative_strength.md)) is usually calculated using 14 periods by [default](../d/default.md), though this can be adjusted based on the [trader](../t/trader.md)’s preference.

### Step-by-Step Calculation
1. **Collect 4-Hour Price Data:** Gather the closing prices for each 4-hour interval over a chosen look-back period (e.g., 14 periods).
2. **Compute Gains and Losses:** Determine the gains and losses for each interval.
3. **Calculate Average Gains and Losses:** Compute the average [gain](../g/gain.md) and average loss over the look-back period.
4. **Determine [Relative Strength](../r/relative_strength.md) (RS):** Divide the average [gain](../g/gain.md) by the average loss to get the RS.
5. **Compute RSI:** Apply the RSI formula to convert RS to an [index](../i/index_instrument.md) that ranges from 0 to 100.

### Example
1. **Collect 4-Hour Price Data:** Assume closing prices for the past 14 four-hour intervals are [45, 47, 48, 50, 49, 51, 52, 51, 53, 54, 56, 57, 58, 59].
2. **Calculate Gains and Losses:**
   - Gains (positive changes): [2, 1, 2, 3, 2, 1, 2, 3, 2, 1]
   - Losses (negative changes, treated as 0 since there are no losses in this example): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
3. **Average Gains and Losses:**
   - Average [Gain](../g/gain.md): \((2 + 1 + 2 + 3 + 2 + 1 + 2 + 3 + 2 + 1) / 14 = 1.42\)
   - Average Loss: \((0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0) / 14 = 0\)
4. **Calculate RS:**
   - \( RS = \frac{Average [Gain](../g/gain.md)}{Average Loss} = \frac{1.42}{0} \,(\text{undefined, but practically infinite}) \)
5. **Compute RSI:**
   - \( RSI = 100 - \frac{100}{1 + \infty} = 100 \) (Strong bullish signal)

## Application in Algorithmic Trading
The 4-hour RSI plays a crucial role in [algorithmic trading](../a/algorithmic_trading.md), which involves automated, pre-programmed trading instructions to execute orders. These algorithms can utilize 4-hour RSI values to make real-time trading decisions, ensuring quick reaction times to fluctuating [market](../m/market.md) conditions.

### Trading Strategies Using 4-Hour RSI
1. **[Overbought](../o/overbought.md)/[Oversold](../o/oversold.md) Levels:** When the RSI crosses below 30, it could indicate that the [asset](../a/asset.md) is [oversold](../o/oversold.md), providing a buying opportunity. Conversely, when the RSI crosses above 70, it indicates the [asset](../a/asset.md) might be [overbought](../o/overbought.md) and could be a signal to sell.
2. **[Divergence](../d/divergence.md):** RSI [divergence](../d/divergence.md) occurs when the price moves in the opposite direction of the RSI. For instance, if the price is rising but the RSI is falling, it could signify a potential [reversal](../r/reversal.md). This can be leveraged by algos for [trend reversal](../t/trend_reversal.md) strategies.
3. **Midpoint (50 level):** A move above 50 generally indicates an upward [trend](../t/trend.md), while a move below 50 can denote a downward [trend](../t/trend.md). Algorithms can use this to confirm [trend](../t/trend.md) direction before executing trades.
4. **RSI Crossovers:** A crossover strategy involves buying when the RSI crosses above a certain threshold (e.g., 50) and selling when it crosses below another threshold (e.g., 30).

### Implementation in Algorithmic Systems
In a typical [algorithmic trading](../a/algorithmic_trading.md) system, the 4-hour RSI might be one of several [technical indicators](../t/technical_indicators.md) used. The trading algorithm could be written in a programming language like Python or C++, using libraries such as TA-Lib ([Technical Analysis](../t/technical_analysis.md) Library) to calculate RSI.

#### Sample Python Code Using TA-Lib
```python
[import](../i/import.md) talib
[import](../i/import.md) numpy as np

# Sample closing prices for the past 14 four-hour intervals
closing_prices = np.array([45, 47, 48, 50, 49, 51, 52, 51, 53, 54, 56, 57, 58, 59])

# Calculate 4-hour RSI
rsi_values = talib.RSI(closing_prices, timeperiod=14)

print(rsi_values)
```

## Real-World Examples and Use Cases
Many trading firms and individual traders use the 4-hour RSI within their [trading strategies](../t/trading_strategies.md). Leading financial institutions and [hedge](../h/hedge.md) funds often integrate [momentum indicators](../m/momentum_indicators.md) like RSI into their [high-frequency trading algorithms](../h/high-frequency_trading_algorithms.md).

### Trading Firms Specializing in Algorithmic Trading
1. **Two Sigma:** A quantitative [investment management](../i/investment_management.md) company that utilizes [machine learning](../m/machine_learning.md), [artificial intelligence](../a/artificial_intelligence_in_trading.md), and advanced algorithms in its [trading strategies](../t/trading_strategies.md). Though specific details on their use of 4-hour RSI are proprietary, companies like Two Sigma often employ a blend of [technical indicators](../t/technical_indicators.md) for their [trading models](../t/trading_models.md). (Website: [Two Sigma](https://www.twosigma.com/))
2. **AQR [Capital](../c/capital.md) Management:** Known for its [systematic trading](../s/systematic_trading.md) approaches, AQR incorporates various technical and fundamental indicators, possibly including RSI, into its [quantitative models](../q/quantitative_models.md). (Website: [AQR Capital Management](https://www.aqr.com/))

## Advantages and Limitations
### Advantages
1. **Timely Insights:** The 4-hour RSI provides quicker insights compared to daily RSI, enabling traders to make timely decisions.
2. **Versatility:** Suitable for a [range](../r/range.md) of assets including [stocks](../s/stock.md), forex, commodities, and cryptocurrencies.
3. **Clear Signals:** Easily interpretable signals ([overbought](../o/overbought.md)/[oversold](../o/oversold.md)) for entry and exit points, even for novice traders.

### Limitations
1. **[False Signals](../f/false_signals_in_trading.md):** Like all [technical indicators](../t/technical_indicators.md), RSI is prone to [false signals](../f/false_signals_in_trading.md), especially in volatile markets.
2. **Limited [Scope](../s/scope.md):** It's a [momentum](../m/momentum.md) [indicator](../i/indicator.md) and doesn’t consider [underlying](../u/underlying.md) [market](../m/market.md) fundamentals.
3. **Over-Reliance:** Over-relying on RSI without corroborating with other indicators or analysis methods can lead to potential losses.

## Conclusion
The 4-hour RSI is a powerful tool for traders seeking to balance between short-term and mid-term [trading strategies](../t/trading_strategies.md). Its ability to provide timely and clear signals makes it valuable for both manual and [algorithmic trading](../a/algorithmic_trading.md). By understanding its calculations, applications, and limitations, traders can effectively incorporate the 4-hour RSI into their [technical analysis](../t/technical_analysis.md) toolkit. Whether used in high-frequency trading by firms like Two Sigma or by individual traders, the 4-hour RSI remains a staple [indicator](../i/indicator.md) in the ever-evolving landscape of [algorithmic trading](../a/algorithmic_trading.md).