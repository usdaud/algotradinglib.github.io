# 4-Period RSI

The 4-Period [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI) is a [momentum](../m/momentum.md) [oscillator](../o/oscillator.md) that measures the speed and change of price movements over a specified period, in this case, four periods. The RSI oscillates between zero and 100 and is typically used to identify [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions in a [market](../m/market.md) for a given [security](../s/security.md).

## Calculation of RSI
The RSI is calculated using the following formula:

\[ RSI = 100 - \left( \frac{100}{1 + RS} \right) \]

where RS ([Relative Strength](../r/relative_strength.md)) is the average of 'N' days' up closes divided by the average of 'N' days' down closes, with 'N' being the period specified, which is four days in the context of a 4-period RSI.

\[ RS = \frac{\text{Average [Gain](../g/gain.md)}}{\text{Average Loss}} \]

### Steps to Calculate RSI
1. Determine the average [gain](../g/gain.md) and average loss over the specified period.
 - Gains are the difference between the closing prices on up days.
 - Losses are the differences between closing prices on down days.
2. Divide the sum of gains by the number of periods to get the average [gain](../g/gain.md).
3. Divide the sum of losses by the number of periods to get the average loss.
4. Compute the [relative strength](../r/relative_strength.md) (RS).
5. Plug RS into the RSI formula to get the current RSI.

### Example Calculation
Assume the following closing prices over a 4-day period:
- Day 1: 150
- Day 2: 155
- Day 3: 153
- Day 4: 160

**Step-by-Step Calculation:**

1. Calculate the daily changes:
 - Day 2: 155 - 150 = +5 ([gain](../g/gain.md))
 - Day 3: 153 - 155 = -2 (loss)
 - Day 4: 160 - 153 = +7 ([gain](../g/gain.md))

2. Calculate average [gain](../g/gain.md) and loss:
 - Average [Gain](../g/gain.md) = (5 + 7) / 4 = 3 (using only days with gains)
 - Average Loss = 2 / 4 = 0.5 (using only days with losses)

3. Calculate RS:
 - RS = 3 / 0.5 = 6

4. Calculate RSI:
 - RSI = 100 - (100 / (1 + 6))
 - RSI = 100 - (100 / 7)
 - RSI = 100 - 14.29 ≈ 85.71

The RSI for these 4 periods is approximately 85.71, which indicates that the stock might be [overbought](../o/overbought.md).

## Interpretation of RSI
Generally, an RSI above 70 indicates that a [security](../s/security.md) is becoming [overbought](../o/overbought.md) or [overvalued](../o/overvalued.md), which may signal a [trend reversal](../t/trend_reversal.md) or corrective [pullback](../p/pullback.md) in price. Conversely, an RSI below 30 suggests that a [security](../s/security.md) may be [oversold](../o/oversold.md) or [undervalued](../u/undervalued.md), which may signal a [trend reversal](../t/trend_reversal.md) or corrective [rally](../r/rally.md).

### Overbought and Oversold Conditions
- **[Overbought](../o/overbought.md) (RSI > 70):** When the RSI crosses above 70, the [security](../s/security.md) is considered [overbought](../o/overbought.md). This situation can indicate that the [asset](../a/asset.md) may be due for a [pullback](../p/pullback.md) or [correction](../c/correction.md).

- **[Oversold](../o/oversold.md) (RSI < 30):** When the RSI crosses below 30, the [security](../s/security.md) is considered [oversold](../o/oversold.md). This situation can indicate that the [asset](../a/asset.md) may be due for a [rally](../r/rally.md) or rebound.

## Advantages of 4-Period RSI
- **Sensitivity:** The 4-period RSI is more sensitive to price changes compared to longer periods like the 14-period RSI. This can make it more useful for [short-term trading](../s/short-term_trading.md) strategies.
- **[Quick Response](../q/quick_response_in_trading.md):** The shorter calculation period allows the RSI to respond more quickly to recent price changes, making it ideal for catching short-term [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions.

## Disadvantages of 4-Period RSI
- **Higher [Volatility](../v/volatility.md):** Due to its sensitivity, the RSI can produce more [false signals](../f/false_signals_in_trading.md), which might lead to premature entries or exits.
- **Less Smoothing:** The shorter time frame offers less smoothing, which may increase the likelihood of misleading signals.

## Comparison with Other RSI Periods
- **14-Period RSI:** The traditional RSI [indicator](../i/indicator.md) is calculated over 14 periods and is widely used. While it is less sensitive than the 4-period RSI, it produces fewer [false signals](../f/false_signals_in_trading.md) and offers better long-term [trend](../t/trend.md) detection.

- **6 or [10-Period RSI](../1/10-period_rsi.md):** Medium-term RSI periods, such as 6 or 10 periods, provide a balance between sensitivity and smoothing. These are less prone to [volatility](../v/volatility.md) compared to the 4-period RSI but more responsive than the 14-period RSI.

## Practical Uses
### Short-Term Trading
The 4-period RSI is particularly useful in [short-term trading](../s/short-term_trading.md) strategies, including [day trading](../d/day_trading.md) and [swing trading](../s/swing_trading.md). Traders can [leverage](../l/leverage.md) the rapid responsiveness of the 4-period RSI to [capitalize](../c/capitalize.md) on short-term price movements.

### Divergence Detection
Traders often use the RSI to detect divergent price movements. [Divergence](../d/divergence.md) occurs when the price moves in one direction while the RSI moves in the opposite direction. This can indicate potential reversals:
- **[Bullish Divergence](../b/bullish_divergence.md):** Occurs when price makes a new low while the RSI forms a higher low.
- **[Bearish Divergence](../b/bearish_divergence.md):** Occurs when price makes a new high while the RSI forms a lower high.

## Implementing 4-Period RSI in Trading Algorithms
Many [algorithmic trading](../a/algorithmic_trading.md) platforms allow traders to backtest strategies using indicators like the 4-period RSI. Platforms such as QuantConnect and AlgoTrader provide sophisticated environments for developing and testing [algorithmic trading](../a/algorithmic_trading.md) strategies.

### Sample Algorithm
Here's a simple example of how you might implement a trading algorithm using the 4-period RSI in Python with the `pandas` and `numpy` libraries:

```python
[import](../i/import.md) pandas as pd
[import](../i/import.md) numpy as np

# Fetch price data (this is assumed to be a DataFrame with a 'Close' column)
data = pd.DataFrame{
    'Close': [150, 155, 153, 160, 162, 158, 159]
})

# Calculate the price changes
data['Change'] = data['Close'].diff()

# Separate gains and losses
data['[Gain](../g/gain.md)'] = np.where(data['Change'] > 0, data['Change'], 0)
data['Loss'] = np.where(data['Change'] < 0, -data['Change'], 0)

# Calculate the average gain and average loss
data['Avg_Gain'] = data['[Gain](../g/gain.md)'].rolling(window=4).mean()
data['Avg_Loss'] = data['Loss'].rolling(window=4).mean()

# Calculate the RS and RSI
data['RS'] = data['Avg_Gain'] / data['Avg_Loss']
data['RSI'] = 100 - (100 / (1 + data['RS']))

# Define trading rules
buy_signal = []
sell_signal = []

for rsi in data['RSI']:
    if rsi < 30:
        buy_signal.append(True)
        sell_signal.append(False)
    elif rsi > 70:
        buy_signal.append(False)
        sell_signal.append(True)
    else:
        buy_signal.append(False)
        sell_signal.append(False)

data['Buy_Signal'] = buy_signal
data['Sell_Signal'] = sell_signal

print(data)
```

This script calculates the 4-period RSI for a given set of closing prices and generates buy and sell signals based on RSI thresholds (below 30 for buying and above 70 for selling).

## Conclusion
The 4-period RSI is a powerful tool in the arsenal of technical analysts and algorithmic traders. Its sensitivity to price movements makes it particularly useful for identifying short-term [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions. However, its increased [volatility](../v/volatility.md) can sometimes produce [false signals](../f/false_signals_in_trading.md), so it's often best used in conjunction with other indicators and analysis methods. Whether used in manual trading or algorithmic strategies, understanding and effectively utilizing the 4-period RSI can be a significant advantage in navigating the complex world of [financial markets](../f/financial_market.md).
