# 3-Period RSI

In [algorithmic trading](../a/algorithmic_trading.md), one of the most widely used [technical indicators](../t/technical_indicators.md) for quantifying the [momentum](../m/momentum.md) of [asset](../a/asset.md) prices is the [Relative Strength](../r/relative_strength.md) [Index](../i/index.md) (RSI). The RSI was introduced by J. Welles Wilder in his 1978 book "New Concepts in Technical [Trading Systems](../t/trading_systems.md)." The RSI is a [momentum](../m/momentum.md) [oscillator](../o/oscillator.md) that measures the speed and change of price movements. It oscillates between 0 and 100 and is typically used to identify [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions in a [market](../m/market.md). While the standard RSI calculation uses a 14-period timeframe, shorter period RSIs, such as the 3-period RSI, are also commonly employed, particularly in [short-term trading](../s/short-term_trading.md) strategies.

## Calculation of the 3-Period RSI

### Standard RSI Formula

To understand the 3-period RSI, it is crucial first to grasp the standard calculation of the RSI. The RSI is calculated using the following formula:

\[ RSI = 100 - \left( \frac{100}{1 + RS} \right) \]

where RS ([Relative Strength](../r/relative_strength.md)) is the average of 'N' days' up closes divided by the average of 'N' days' down closes:

\[ RS = \frac{\text{Average [Gain](../g/gain.md) over } N \text{ periods}}{\text{Average Loss over } N \text{ periods}} \]

### Calculation Steps for the 3-Period RSI

1. **Determine the Up and Down Days**:
   - Calculate the daily price changes for the [asset](../a/asset.md) over the past 3 periods.
   - A day is considered an "up day" if the closing price is higher than the previous day's close. Conversely, it is a "down day" if the closing price is lower.

2. **Calculate the Average [Gain](../g/gain.md) and Average Loss**:
   - The average [gain](../g/gain.md) over the last 3 periods is the sum of all up day changes divided by 3.
   - The average loss over the last 3 periods is the sum of all down day changes divided by 3.

3. **Compute the [Relative Strength](../r/relative_strength.md) (RS)**:
   - RS is calculated as the ratio of the average [gain](../g/gain.md) to the average loss over the 3 periods.

4. **Calculate the RSI**:
   - Plug the RS [value](../v/value.md) into the RSI formula to compute the 3-period RSI.

### Example Calculation

Suppose we have the following closing prices for an [asset](../a/asset.md) over four days: $50, $52, $51, and $53.

1. Calculate the daily price changes:
   - Day 1 to Day 2: $52 - $50 = +2 (Up Day)
   - Day 2 to Day 3: $51 - $52 = -1 (Down Day)
   - Day 3 to Day 4: $53 - $51 = +2 (Up Day)

2. Calculate the average [gain](../g/gain.md) and average loss:
   - Average [Gain](../g/gain.md) = (2 + 2) / 3 = 1.33
   - Average Loss = 1 / 3 = 0.33

3. Compute the [Relative Strength](../r/relative_strength.md) (RS):
   - RS = 1.33 / 0.33 ≈ 4.03

4. Calculate the RSI:
   - RSI = 100 - (100 / (1 + 4.03)) ≈ 80.1

Thus, the 3-period RSI in this example is approximately 80.1.

## Application in Algorithmic Trading

### Trading Signals

The 3-period RSI can be used to generate [trading signals](../t/trading_signals.md) in a variety of ways:

1. **[Overbought](../o/overbought.md)/[Oversold](../o/oversold.md) Conditions**:
   - An RSI above 70 is typically considered "[overbought](../o/overbought.md)," suggesting that the [asset](../a/asset.md) might be [overvalued](../o/overvalued.md) and due for a [pullback](../p/pullback.md).
   - An RSI below 30 is considered "[oversold](../o/oversold.md)," indicating that the [asset](../a/asset.md) might be [undervalued](../u/undervalued.md) and ripe for a potential [rally](../r/rally.md).

2. **[Divergence](../d/divergence.md)**:
   - [Bullish Divergence](../b/bullish_divergence.md): Occurs when the price makes a new low, but the RSI makes a higher low. This [divergence](../d/divergence.md) may indicate a potential upward [reversal](../r/reversal.md).
   - [Bearish Divergence](../b/bearish_divergence.md): Occurs when the price makes a new high, but the RSI makes a lower high. This [divergence](../d/divergence.md) could signal a potential downward [reversal](../r/reversal.md).

3. **Swing Rejections**:
   - Bullish Rejection: RSI falls below 30 ([oversold](../o/oversold.md)), rises above 30, falls again but stays above 30, and then rises above its previous high.
   - Bearish Rejection: RSI rises above 70 ([overbought](../o/overbought.md)), falls below 70, rises again but stays below 70, and then falls below its previous low.

### Algorithmic Implementation

#### Pseudocode for 3-Period RSI Calculation

Below is a pseudocode example for integrating the 3-period RSI into an [algorithmic trading](../a/algorithmic_trading.md) system:

```pseudo
function calculate3PeriodRSI(prices):
    N = 3
    gains = []
    losses = []

    for i from 1 to N:
        change = prices[i] - prices[i-1]
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))

    averageGain = sum(gains) / N
    averageLoss = sum(losses) / N

    if averageLoss == 0:
        [return](../r/return.md) 100  # Prevent division by zero and resulting in undefined RSI

    RS = averageGain / averageLoss
    RSI = 100 - (100 / (1 + RS))
  
    [return](../r/return.md) RSI
```

This pseudocode calculates the 3-period RSI of a given series of prices. In a real [algorithmic trading](../a/algorithmic_trading.md) system, this function would be incorporated into a broader strategy, where buy and sell signals could be generated and acted upon.

#### Example in Python

```python
[import](../i/import.md) numpy as np

def calculate_3_period_rsi(prices):
    n = 3
    changes = np.diff(prices)
    gains = np.maximum(changes, 0)
    losses = -np.minimum(changes, 0)

    average_gain = np.sum(gains[:n]) / n
    average_loss = np.sum(losses[:n]) / n

    if average_loss == 0:
        [return](../r/return.md) 100  # To [handle](../h/handle.md) the division by zero edge case
    
    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))

    [return](../r/return.md) rsi

# Example usage
prices = [50, 52, 51, 53]
rsi = calculate_3_period_rsi(prices)
print(f"3-Period RSI: {rsi}")
```

In this Python example, the `calculate_3_period_rsi` function calculates the 3-period RSI for a given series of prices. The example usage demonstrates how to call the function and print the resulting RSI.

## Benefits and Limitations

### Benefits

1. **Speed and Sensitivity**:
   - The 3-period RSI responds more quickly to price changes compared to the standard 14-period RSI. This quick responsiveness is beneficial for short-term traders who need timely signals.

2. **Detecting Short-Term Price Extremes**:
   - Due to its high sensitivity, the 3-period RSI is adept at detecting short-term [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions, which can lead to profitable contrarian trades.

3. **Versatility**:
   - The [indicator](../i/indicator.md) can be used across different [asset](../a/asset.md) classes, including [stocks](../s/stock.md), forex, and commodities. Its versatility makes it a valuable tool for various [trading strategies](../t/trading_strategies.md).

### Limitations

1. **[False Signals](../f/false_signals_in_trading.md)**:
   - The increased sensitivity of the 3-period RSI can also be a double-edged sword, leading to more [false signals](../f/false_signals_in_trading.md). Short-term [noise](../n/noise.md) and [market](../m/market.md) [volatility](../v/volatility.md) can trigger premature buy or sell signals.

2. **Dependency on [Market](../m/market.md) Conditions**:
   - In trending markets, the 3-period RSI may give numerous [overbought](../o/overbought.md) or [oversold](../o/oversold.md) signals without a resulting price [reversal](../r/reversal.md). This can lead to losses for traders relying solely on RSI signals.

3. **Need for Confirmation**:
   - To mitigate the [risk](../r/risk.md) of [false signals](../f/false_signals_in_trading.md), traders often combine the 3-period RSI with other [technical indicators](../t/technical_indicators.md) or analysis methods to confirm [trading signals](../t/trading_signals.md).

## Practical Use Cases and Strategies

### Mean Reversion Strategy

In a [mean reversion](../m/mean_reversion.md) strategy, the 3-period RSI can be used to identify when an [asset](../a/asset.md) is [overbought](../o/overbought.md) or [oversold](../o/oversold.md). The idea is to buy when the RSI is below 30 and sell when the RSI is above 70.

#### Simple Mean Reversion Algorithm

1. Calculate the 3-period RSI for the [asset](../a/asset.md).
2. Enter a long position when the RSI falls below 30.
3. Enter a short position when the RSI rises above 70.
4. Exit long positions when the RSI crosses above 50.
5. Exit short positions when the RSI crosses below 50.

### Trend Following with RSI Confirmation

RSI can also be used in [trend](../t/trend.md)-following strategies, providing a confirmation signal for [trend](../t/trend.md) direction.

#### Simple Trend Following Algorithm

1. Calculate a longer-term moving average (e.g., 50-period) to determine the [trend](../t/trend.md) direction.
2. Calculate the 3-period RSI for the [asset](../a/asset.md).
3. Enter a long position if the moving average indicates an [uptrend](../u/uptrend.md) and the RSI rises above 50 from below.
4. Enter a short position if the moving average indicates a [downtrend](../d/downtrend.md) and the RSI falls below 50 from above.
5. Exit positions based on opposite signals or predefined [profit](../p/profit.md)/loss targets.

### Combining with Other Indicators

To increase the robustness of [trading strategies](../t/trading_strategies.md), traders often combine the 3-period RSI with other [technical indicators](../t/technical_indicators.md) such as Moving Averages, MACD, or [Bollinger Bands](../b/bollinger_bands.md).

#### Example Strategy

1. Calculate the 3-period RSI and Moving Average Convergence [Divergence](../d/divergence.md) (MACD).
2. Enter a long position when:
   - The 3-period RSI is below 30, indicating [oversold](../o/oversold.md) conditions.
   - The MACD line crosses above the signal line, indicating bullish [momentum](../m/momentum.md).
3. Enter a short position when:
   - The 3-period RSI is above 70, indicating [overbought](../o/overbought.md) conditions.
   - The MACD line crosses below the signal line, indicating bearish [momentum](../m/momentum.md).
4. Exit positions based on opposite signals or predefined [profit](../p/profit.md)/loss targets.

## Conclusion

The 3-period RSI is a powerful tool in the arsenal of algorithmic traders. Its ability to provide timely insights into short-term [market](../m/market.md) conditions makes it particularly useful for high-frequency trading and intraday strategies. However, like all [technical indicators](../t/technical_indicators.md), it is not infallible and should be used in combination with other indicators and analysis techniques to improve accuracy and reduce the [risk](../r/risk.md) of [false signals](../f/false_signals_in_trading.md). By understanding its calculation, applications, and limitations, traders can effectively incorporate the 3-period RSI into their [trading strategies](../t/trading_strategies.md) to enhance their decision-making process and potentially increase profitability.