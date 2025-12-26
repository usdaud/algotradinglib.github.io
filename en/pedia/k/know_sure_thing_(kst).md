# Know Sure Thing (KST)

The **Know Sure Thing (KST)** is a [momentum](../m/momentum.md) [oscillator](../o/oscillator.md) developed by Martin Pring. It's specifically designed for identifying price cycles and potential turning points in a [market](../m/market.md). This [technical analysis](../t/technical_analysis.md) tool aims to help traders and investors determine the strength and direction of a [security](../s/security.md)'s [momentum](../m/momentum.md).

## Overview of KST

KST is based on the smoothed rate-of-change for four different time periods. It is calculated by combining the [weighted averages](../w/weighted_averages_in_trading.md) of these different time periods. The formula essentially gives more significance to longer-term [momentum](../m/momentum.md), which helps in identifying the major [trend](../t/trend.md).

### How It Works

The KST [indicator](../i/indicator.md) takes [multiple](../m/multiple.md) rates of change (ROC) at different time frames and smooths them with moving averages. These smoothed values are then [weighted](../w/weighted.md) and summed up to generate a single [oscillator](../o/oscillator.md). This allows it to capture both the short-term and long-term cycles of [momentum](../m/momentum.md).

### KST Formula

The KST can be computed using the following steps:

1. **Calculate the Rate of Change (ROC) for [multiple](../m/multiple.md) time periods**.

 - ROC1 = (Current Price / Price N1 periods ago) - 1
 - ROC2 = (Current Price / Price N2 periods ago) - 1
 - ROC3 = (Current Price / Price N3 periods ago) - 1
 - ROC4 = (Current Price / Price N4 periods ago) - 1

2. **Smooth each ROC with a moving average (usually a simple moving average (SMA)).**

 - SMA1 = SMA(ROC1, Period1)
 - SMA2 = SMA(ROC2, Period2)
 - SMA3 = SMA(ROC3, Period3)
 - SMA4 = SMA(ROC4, Period4)

3. **Assign weights to each smoothed ROC.**

 - [Weighted](../w/weighted.md) ROC1 = Weight1 * SMA1
 - [Weighted](../w/weighted.md) ROC2 = Weight2 * SMA2
 - [Weighted](../w/weighted.md) ROC3 = Weight3 * SMA3
 - [Weighted](../w/weighted.md) ROC4 = Weight4 * SMA4

4. **Combine the [weighted](../w/weighted.md) SMAs** to generate the KST [value](../v/value.md).

 - KST = [Weighted](../w/weighted.md) ROC1 + [Weighted](../w/weighted.md) ROC2 + [Weighted](../w/weighted.md) ROC3 + [Weighted](../w/weighted.md) ROC4

By summing these [weighted](../w/weighted.md) and smoothed rates of change, the [indicator](../i/indicator.md) becomes more [robust](../r/robust.md) and less susceptible to [market](../m/market.md) [noise](../n/noise.md).

### Interpretation

Interpreting the KST is similar to other [momentum oscillators](../m/momentum_oscillators.md). It swings above and below a centerline (usually zero), providing insight into the strength and direction of [momentum](../m/momentum.md).

- **Above Zero**: [Positive momentum](../p/positive_momentum.md), consider long positions.
- **Below Zero**: Negative [momentum](../m/momentum.md), consider short positions.
- **Crossovers**: Crosses above zero signify potential buy signals. Crosses below zero indicate potential sell signals.
- **Divergences**: If the price moves higher while KST moves lower (or vice versa), it may signify a potential [reversal](../r/reversal.md).

### Advantages and Disadvantages

#### Advantages

- **Multi-timeframe Analysis**: Incorporates [multiple](../m/multiple.md) rates of change which offers a more comprehensive view of [market](../m/market.md) [momentum](../m/momentum.md).
- **Less [Noise](../n/noise.md)**: Smoothing and weighting reduce the impact of short-term [market](../m/market.md) fluctuations.
- **Easy to Interpret**: Simple crossovers and divergences make it user-friendly.

#### Disadvantages

- **Lag**: Like many [technical indicators](../t/technical_indicator.md), KST can lag [price action](../p/price_action.md) due to its smoothing components.
- **Complexity**: The calculation involves [multiple](../m/multiple.md) steps and parameters, making it more complicated than simpler oscillators.

## Real-world Applications

KST can be applied in various scenarios of trading and [investing](../i/investing.md):

1. **Stock Trading**: Particularly useful for long-term stock traders to identify multi-month uptrends or downtrends.
2. **Forex Trading**: Helps in identifying longer-term [currency](../c/currency.md) trends without getting caught in short-term [noise](../n/noise.md).
3. **[Commodity](../c/commodity.md) Trading**: Useful in [commodity](../c/commodity.md) markets, which can have cyclical price movements.

## Tools and Platforms Supporting KST

Several trading platforms and [software tools](../s/software_tools_for_trading.md) support the KST [indicator](../i/indicator.md). Some of the most notable include:

- **[TradingView](../t/tradingview.md)**: A popular web-based charting tool used by traders globally, supporting a wide array of indicators including KST.
- **MetaTrader 4 and 5 (MT4/MT5)**: Widely used in forex trading, these platforms also support custom indicators like the KST.
- **ThinkorSwim**: Offered by TD [Ameritrade](../a/ameritrade.md), this platform provides advanced charting tools that include the KST.

## Notable Traders Using KST

Though specific traders who exclusively use KST may not have widespread recognition, Martin Pring, its developer, has a well-established reputation in the financial community. His work on [market cycles](../m/market_cycles.md) and [technical analysis](../t/technical_analysis.md) has influenced many traders.

## Practical Example

Imagine you're analyzing the stock of **Apple Inc. (AAPL)**. You've decided to use the 10-day, 15-day, 20-day, and 30-day ROC values. Calculate the SMAs for these ROCs and assign weights as follows:

- Weight1 = 1
- Weight2 = 2
- Weight3 = 3
- Weight4 = 4

You would then sum the [weighted](../w/weighted.md) SMAs to generate the KST. If the KST crosses above zero, it would be a potential buy signal. Conversely, a cross below zero would indicate a possible sell signal.

## Resources for Further Study

For those interested in deeper learning, Martin Pring has several resources available:

- **Books**: "[Technical Analysis](../t/technical_analysis.md) Explained" by Martin Pring

## Conclusion

The Know Sure Thing (KST) is a versatile [momentum](../m/momentum.md) [oscillator](../o/oscillator.md) that can help traders identify the strength and direction of [price momentum](../p/price_momentum.md). By incorporating [multiple](../m/multiple.md) timeframes and smoothing factors, it provides a comprehensive view that minimizes short-term [market](../m/market.md) [noise](../n/noise.md). While it has its complexities and limitations, when used correctly, it can be a valuable tool in a [trader](../t/trader.md)'s arsenal.