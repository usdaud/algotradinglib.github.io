# Directional Movement Index (DMI)

The Directional Movement [Index](../i/index.md) (DMI) is a technical [indicator](../i/indicator.md) developed by J. Welles Wilder as part of his book "New Concepts in Technical [Trading Systems](../t/trading_systems.md)," published in 1978. The DMI assesses the strength of a price [trend](../t/trend.md) and helps traders distinguish between trending and non-trending conditions. It serves as a tool for both [trend](../t/trend.md)-following and filtering out [market](../m/market.md) [noise](../n/noise.md), thus aiding in more informed decision-making in [financial markets](../f/financial_market.md).

### Components of DMI

The DMI consists of three main components:  
1. **Plus Directional [Indicator](../i/indicator.md) (+DI):** This [indicator](../i/indicator.md) measures upward movement or the strength of positive price changes. It captures the largest part of daily high movements over a specified period.  
2. **Minus Directional [Indicator](../i/indicator.md) (-DI):** This element captures downward price movements and shows the strength of negative price changes, considering the largest part of daily low movements over a specified period.  
3. **[Average Directional Index](../a/average_directional_index_(adx).md) (ADX):** This component specifies the overall strength of the [trend](../t/trend.md), regardless of its direction. The ADX is derived from the smoothed averages of the difference between +DI and -DI.

### Calculating DMI

To understand the DMI components, we must first calculate the True [Range](../r/range.md) (TR), Plus Directional Movement (+DM), and Minus Directional Movement (-DM).

1. **True [Range](../r/range.md) (TR):** The maximum [range](../r/range.md) of price movement for a given period, which is derived as follows:
   - \( TR = \max[(Hight - Lowt), |Hight - Closet-1|, |Lowt - Closet-1|] \)

2. **Plus Directional Movement (+DM):** Only the positive part of price movement between the current and previous periods:
   - If \( Hight - High_{t-1} > Low_{t-1} - Lowt \) and \( Hight - High_{t-1} > 0 \), then \( +DM = Hight - High_{t-1} \); otherwise, \( +DM = 0 \)

3. **Minus Directional Movement (-DM):** The negative part of price movement between the current and previous periods:
   - If \( Low_{t-1} - Lowt > Hight - High_{t-1} \) and \( Low_{t-1} - Lowt > 0 \), then \( -DM = Low_{t-1} - Lowt \); otherwise, \( -DM = 0 \)

The smoothed averages of +DM and -DM over a specified period (commonly 14 days) are then calculated to get the Plus and Minus Directional Indicators:
   - \( +DI = \left( \frac{SMMA(+DM)}{TR} \right) \times 100 \)
   - \( -DI = \left( \frac{SMMA(-DM)}{TR} \right) \times 100 \)

Where SMMA refers to the smoothed moving average. The ADX is then computed as the smoothed average of the Directional Movement [Index](../i/index.md) (DX):
   - \( DX = \left( \frac{| +DI - -DI |}{+DI + -DI } \right) \times 100 \)
   - \( ADX = SMMA(DX) \)

### Interpreting DMI

#### Trend Strength

The ADX [value](../v/value.md) represents the overall [trend](../t/trend.md) strength on a scale from 0 to 100:
- **0-20:** Weak [trend](../t/trend.md) or [market](../m/market.md) is likely moving sideways.
- **20-40:** Building or moderately strong [trend](../t/trend.md).
- **40-60:** Strong [trend](../t/trend.md).
- **60-100:** Very strong [trend](../t/trend.md).

#### Directional Indicators

- When **+DI is above -DI**, it indicates an upward [trend](../t/trend.md).
- When **-DI is above +DI**, it suggests a downward [trend](../t/trend.md).

#### Crossovers

Crossover points between +DI and -DI are particularly significant:
- A **bullish crossover** occurs when +DI crosses above -DI, suggesting a potential buying signal.
- A **bearish crossover** occurs when -DI crosses above +DI, signaling a potential selling opportunity.

### DMI in Algorithmic Trading

[Algorithmic trading](../a/algorithmic_trading.md) systems often incorporate DMI as part of complex [trading algorithms](../t/trading_algorithms.md). DMI offers clear quantitative criteria, enabling [trading systems](../t/trading_systems.md) to automatically generate buy or sell signals. By integrating DMI with other indicators like Moving Average Convergence [Divergence](../d/divergence.md) (MACD), [Relative Strength](../r/relative_strength.md) [Index](../i/index.md) (RSI), or [Bollinger Bands](../b/bollinger_bands.md), algorithms can enhance decision-making accuracy and potentially improve profitability.

Here are a couple of use cases of the Directional Movement [Index](../i/index.md) in [algorithmic trading](../a/algorithmic_trading.md):

#### Use Case 1: Trend Following Systems

A [trend](../t/trend.md)-following algo might use ADX to confirm the existence of a [trend](../t/trend.md). The system might:
- Enter long positions when ADX exceeds a threshold (e.g., 25) and +DI is above -DI.
- Enter short positions when ADX exceeds the threshold, but -DI is above +DI.
- Exit positions when the ADX falls below a certain [value](../v/value.md) (indicating weakening [trend](../t/trend.md) strength).

#### Use Case 2: Range-Bound Market Filtering

Another use case is a [range](../r/range.md)-bound or sideways [market](../m/market.md) filtering:
- If ADX drops below a certain threshold (e.g., 20), the algo may avoid opening new directional trades as this indicates less likelihood of [trend](../t/trend.md) formation.
- This filter can also be applied to [trend](../t/trend.md)-following strategies to avoid losses during non-trending periods.

### Popular Algorithmic Trading Providers

Several [algorithmic trading](../a/algorithmic_trading.md) platforms and providers incorporate DMI in their strategies. Some notable ones include:

- **[QuantConnect](../q/quantconnect.md)**: A cloud-based [algorithmic trading](../a/algorithmic_trading.md) platform [QuantConnect](https://www.quantconnect.com/)
- **[AlgoTrader](../a/algotrader.md)**: An institutional multi-[asset](../a/asset.md) [algorithmic trading](../a/algorithmic_trading.md) software [AlgoTrader](https://www.algotrader.com/)
- **Quantopian**: Another platform providing tools for [algorithmic trading](../a/algorithmic_trading.md) (although it ceased operations, it was popular for educational purposes)

### Conclusion

The Directional Movement [Index](../i/index.md) (DMI) is a powerful tool in the arsenal of both manual and algorithmic traders. Its ability to quantify [trend](../t/trend.md) strength and deliver clear buy and sell signals makes it invaluable for crafting sophisticated [trading strategies](../t/trading_strategies.md). When used in conjunction with other [technical indicators](../t/technical_indicators.md), DMI offers enriched insights and [robust](../r/robust.md) trading opportunities, further emphasizing its enduring significance in the world of [financial markets](../f/financial_market.md).
