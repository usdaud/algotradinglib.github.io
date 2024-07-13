# Chande Momentum Oscillator (CMO)

The Chande [Momentum](../m/momentum.md) [Oscillator](../o/oscillator.md) (CMO) is a [technical analysis](../t/technical_analysis.md) tool developed by Tushar Chande. This [indicator](../i/indicator.md) is derived from the [Relative Strength](../r/relative_strength.md) [Index](../i/index.md) (RSI) and is used to identify the [momentum](../m/momentum.md) of a [financial asset](../f/financial_asset.md) by comparing the sum of all recent gains to the sum of all recent losses over a specified period. It oscillates between -100 and +100 and provides valuable insights into whether an [asset](../a/asset.md) is [overbought](../o/overbought.md) or [oversold](../o/oversold.md), thus enabling traders to make informed decisions.

## Origins and Development

The Chande [Momentum](../m/momentum.md) [Oscillator](../o/oscillator.md) was introduced by Tushar Chande in his 1997 book "The New Technical [Trader](../t/trader.md)," co-authored with Stanley Kroll. Chande developed this [indicator](../i/indicator.md) to address some limitations in existing [momentum indicators](../m/momentum_indicators.md). Dr. Chande is known for his contributions to [technical analysis](../t/technical_analysis.md) and [quantitative trading](../q/quantitative_trading.md) strategies. His work is prominently featured in professional trading communities, although he does not maintain a personal website.

## Calculation

The calculation of the CMO involves several steps, which can be broken down into the following components:
1. **Select the period (n):** Common periods used for the CMO are 9, 14, or 20 days.
2. **Calculate Up and Down Days:**
   - **Up Days:** Sum of all gains over the selected period.
   - **Down Days:** Sum of all losses over the selected period.
3. **CMO Formula:**
   \[
   CMO = 100 \times \frac{(Sum\ of\ Gains\ -\ Sum\ of\ Losses)}{(Sum\ of\ Gains + Sum\ of\ Losses)}
   \]

The resulting [value](../v/value.md) oscillates between -100 and +100. Values above +50 indicate an [overbought](../o/overbought.md) condition, while values below -50 indicate an [oversold](../o/oversold.md) condition.

## Interpretation

### Overbought and Oversold Levels

When the CMO crosses above the +50 mark, it signals that the [asset](../a/asset.md) may be [overbought](../o/overbought.md), indicating a potential [reversal](../r/reversal.md) or [pullback](../p/pullback.md). Conversely, when the [value](../v/value.md) falls below -50, it suggests that the [asset](../a/asset.md) may be [oversold](../o/oversold.md), signaling a possible upward [reversal](../r/reversal.md). 

### Divergence

[Divergence](../d/divergence.md) between the CMO and the price of an [asset](../a/asset.md) can provide critical signals. For instance, if prices are rising but the CMO is falling, it indicates a potential bearish [reversal](../r/reversal.md). Similarly, if prices are falling and the CMO is rising, a bullish [reversal](../r/reversal.md) might be imminent.

### Trend Confirmation

The CMO can also be used to confirm the strength of a [trend](../t/trend.md). If the [oscillator](../o/oscillator.md) is moving in the same direction as the [trend](../t/trend.md) and remains in the [overbought](../o/overbought.md) or [oversold](../o/oversold.md) zone for an extended period, it reinforces the strength of the [trend](../t/trend.md).

## Advantages

1. **Sensitivity:** The CMO is more sensitive to price changes compared to some other [momentum indicators](../m/momentum_indicators.md), providing earlier signals.
2. **[Range](../r/range.md)-Bound:** Provides a clear indication when an [asset](../a/asset.md) is [overbought](../o/overbought.md) or [oversold](../o/oversold.md).
3. **Versatility:** Can be used across various time frames and [asset](../a/asset.md) classes.

## Limitations

1. **[Whipsaw Effect](../w/whipsaw_effect.md):** Higher sensitivity can also lead to [false signals](../f/false_signals_in_trading.md) during sideways markets.
2. **[Lagging Indicator](../l/lagging_indicator.md):** As with any [momentum](../m/momentum.md) [indicator](../i/indicator.md), the CMO lags behind price movements and may not predict reversals accurately.

## Practical Applications

### Integration with Other Indicators

To minimize the [risk](../r/risk.md) of [false signals](../f/false_signals_in_trading.md), traders often use the CMO in conjunction with other indicators such as Moving Averages, [Bollinger Bands](../b/bollinger_bands.md), or the [Relative Strength](../r/relative_strength.md) [Index](../i/index.md) (RSI).

### Buy and Sell Signals

- **Buy Signal:** When the CMO crosses above the -50 level.
- **Sell Signal:** When the CMO crosses below the +50 level.

### Algorithmic Trading

The CMO can be integrated into [algorithmic trading](../a/algorithmic_trading.md) strategies to automate buy and sell decisions. For instance, algorithms can be programmed to execute trades when the CMO crosses certain thresholds, thereby eliminating emotional biases.

## Example

Consider a stock with the following price changes over a 14-day period:

- Up days: 0.5, 1.2, 0.7, 1.8, 0.3
- Down days: -0.6, -1.0, -0.9, -1.1, -0.4

Sum of gains = 0.5 + 1.2 + 0.7 + 1.8 + 0.3 = 4.5
Sum of losses = 0.6 + 1.0 + 0.9 + 1.1 + 0.4 = 4.0

CMO = 100 * ((4.5 - 4.0) / (4.5 + 4.0)) 
    = 100 * (0.5 / 8.5)
    = 100 * 0.0588 
    = 5.88

In this example, the CMO is 5.88, which implies a [neutral](../n/neutral.md) zone where neither [overbought](../o/overbought.md) nor [oversold](../o/oversold.md) conditions prevail.

## Software Implementation

Traders and analysts can calculate the CMO using various [software tools](../s/software_tools_for_trading.md) and platforms. Popular trading software such as MetaTrader, [TradingView](../t/tradingview.md), and [NinjaTrader](../n/ninjatrader.md) [offer](../o/offer.md) built-in functions for the Chande [Momentum](../m/momentum.md) [Oscillator](../o/oscillator.md). 

### TradingView Example

To calculate the CMO in [TradingView](../t/tradingview.md), you can use the following script:

```pine
//@version=4
study("Chande [Momentum](../m/momentum.md) [Oscillator](../o/oscillator.md)", shorttitle="CMO", [overlay](../o/overlay.md)=false)
length = input(14, minval=1, title="Length")
src = close
up = change(src) > 0 ? change(src) : 0
down = change(src) < 0 ? -change(src) : 0
sumUp = sum(up, length)
sumDown = sum(down, length)
CMO = 100 * (sumUp - sumDown) / (sumUp + sumDown)
plot(CMO, color=color.blue, title="CMO")
hline(50, "[Overbought](../o/overbought.md)", color=color.red)
hline(-50, "[Oversold](../o/oversold.md)", color=color.green)
```

## Real-World Application

### Use by Professional Traders

Professional trading firms such as Renaissance Technologies, D.E. Shaw Group, and Two Sigma have been known to incorporate various [momentum oscillators](../m/momentum_oscillators.md), including the CMO, into their [trading algorithms](../t/trading_algorithms.md). These firms use a combination of [quantitative analysis](../q/quantitative_analysis.md) and algorithmic strategies to exploit [market](../m/market.md) inefficiencies.

### Case Study

A notable example of the application of [momentum oscillators](../m/momentum_oscillators.md) in trading comes from Renaissance Technologies, renowned for its Medallion [Fund](../f/fund.md). Although specific details about their algorithms are proprietary, the integration of indicators like the CMO helps in their [market](../m/market.md)-timing strategies. Renaissance Technologies has consistently delivered impressive returns by blending [mathematical models](../m/mathematical_models_in_trading.md) with real-world trading scenarios, showcasing the effectiveness of tools like the Chande [Momentum](../m/momentum.md) [Oscillator](../o/oscillator.md).

For more information about Renaissance Technologies, visit their [official website](https://www.rentec.com/).

## Conclusion

The Chande [Momentum](../m/momentum.md) [Oscillator](../o/oscillator.md) is a [robust](../r/robust.md) tool for identifying the [momentum](../m/momentum.md) of financial assets. Its sensitivity to price changes and ability to oscillate within a bounded [range](../r/range.md) make it a valuable addition to any [trader](../t/trader.md)'s toolkit. While it has its limitations, when used in conjunction with other indicators and within a comprehensive [trading strategy](../t/trading_strategy.md), the CMO can provide significant insights and aid in making more informed trading decisions.