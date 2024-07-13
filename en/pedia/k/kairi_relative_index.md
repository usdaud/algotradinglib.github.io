# Kairi Relative Index

The Kairi Relative [Index](../i/index.md) (KRI), also known as the Kairi [Index](../i/index.md), is a [technical analysis](../t/technical_analysis.md) [indicator](../i/indicator.md) used primarily in the world of financial trading. This [index](../i/index.md) is utilized to measure the distance between an [asset](../a/asset.md)'s price and its simple moving average (SMA) in percentage terms. The KRI provides traders with insights into the [market](../m/market.md)'s condition, helping them identify [overbought](../o/overbought.md) or [oversold](../o/oversold.md) situations.

## Calculation

The formula to calculate the Kairi Relative [Index](../i/index.md) is straightforward:

\[ \text{KRI} = \left( \frac{\text{Current Price} - \text{SMA}}{\text{SMA}} \right) \times 100 \]

Where:
- **Current Price** is the current [market price](../m/market_price.md) of the [asset](../a/asset.md).
- **SMA** is the Simple Moving Average of the [asset](../a/asset.md)'s price, calculated over a specified period.

The KRI values fluctuate around 0. When the current price is above the SMA, the KRI [will](../w/will.md) be positive, signaling that the [asset](../a/asset.md) might be [overbought](../o/overbought.md). Conversely, when the current price is below the SMA, the KRI [will](../w/will.md) be negative, indicating the [asset](../a/asset.md) might be [oversold](../o/oversold.md).

## Interpretation

### Overbought and Oversold Conditions

- **[Overbought](../o/overbought.md)**: If the KRI shows a high positive [value](../v/value.md), it suggests that the [asset](../a/asset.md) is trading significantly above its moving average, which could indicate that it is [overbought](../o/overbought.md). Traders might interpret this as a signal to sell or short the [asset](../a/asset.md) since the price could be due for a [correction](../c/correction.md).
- **[Oversold](../o/oversold.md)**: Conversely, a high negative KRI [value](../v/value.md) indicates that the [asset](../a/asset.md) is trading well below its moving average, suggesting it is [oversold](../o/oversold.md). This situation might present a buying opportunity for traders as the price could be poised for a rebound.

### Confirmation of Trends

- **[Trend Following](../t/trend_following.md)**: The KRI can be used as a [trend](../t/trend.md)-following [indicator](../i/indicator.md). If the KRI is consistently positive, it might confirm an [uptrend](../u/uptrend.md). If it remains negative over an extended period, it could confirm a [downtrend](../d/downtrend.md).
- **[Signal Filtering](../s/signal_filtering.md)**: By setting thresholds for positive and negative values, traders can filter out [noise](../n/noise.md) and focus on significant price deviations, improving the accuracy of their [trading strategies](../t/trading_strategies.md).

### Divergences

Identifying divergences between the KRI and the [underlying](../u/underlying.md) price can also provide valuable [trading signals](../t/trading_signals.md):
- **[Bullish Divergence](../b/bullish_divergence.md)**: When the price makes a new low but the KRI does not, it could signal a potential upward [reversal](../r/reversal.md).
- **[Bearish Divergence](../b/bearish_divergence.md)**: When the price makes a new high but the KRI does not, it could indicate an impending downward [reversal](../r/reversal.md).

## Advantages

1. **Simplicity**: The Kairi Relative [Index](../i/index.md) is easy to understand and calculate, making it accessible for traders of all experience levels.
2. **Versatility**: It can be applied to various [asset](../a/asset.md) classes, including [stocks](../s/stock.md), commodities, forex, and cryptocurrencies.
3. **Early Signal Identification**: By highlighting significant deviations from the moving average, the KRI helps traders identify potential [reversal](../r/reversal.md) points early.

## Limitations

1. **Lagging Nature**: Since the KRI relies on moving averages, it inherently lags behind the current [price action](../p/price_action.md), which might result in delayed signals.
2. **[False Signals](../f/false_signals_in_trading.md)**: In volatile markets, short-term fluctuations could produce false [overbought](../o/overbought.md) or [oversold](../o/oversold.md) signals, leading to potential losses.
3. **Dependence on SMA Period** The effectiveness of the KRI is highly dependent on the selected period for the simple moving average. Different periods can produce varying signals, so traders need to optimize this parameter based on their [trading strategy](../t/trading_strategy.md).

## Practical Applications

### Example 1: Stock Trading

Consider a [trader](../t/trader.md) analyzing the stock of a technology company. The [trader](../t/trader.md) applies the KRI to a 20-day SMA to assess the stock's condition. If the KRI reaches +10% or higher, the [trader](../t/trader.md) might consider selling the stock or taking short positions, anticipating a price [correction](../c/correction.md). Conversely, if the KRI drops to -10% or lower, the [trader](../t/trader.md) might see it as a buying opportunity, expecting the stock to rebound.

### Example 2: Forex Trading

A forex [trader](../t/trader.md) uses the KRI on the EUR/USD [currency](../c/currency.md) pair with a 50-day SMA. The KRI rising above +5% could signal that the [euro](../e/euro.md) is [overbought](../o/overbought.md) against the dollar, prompting the [trader](../t/trader.md) to sell euros. If the KRI falls below -5%, it suggests that the [euro](../e/euro.md) is [oversold](../o/oversold.md), and the [trader](../t/trader.md) might buy euros.

### Example 3: Cryptocurrency Trading

In the highly volatile cryptocurrency [market](../m/market.md), a [trader](../t/trader.md) uses the KRI with a shorter period, such as a [10-day SMA](../1/10-day_sma.md), for quicker reactions. When the KRI exceeds +15%, it could indicate that the cryptocurrency is [overbought](../o/overbought.md). Conversely, a KRI below -15% might signal an [oversold](../o/oversold.md) condition, suggesting potential entry points.

## Implementation in Trading Platforms

### MetaTrader

In MetaTrader, traders can implement the KRI by coding it as a custom [indicator](../i/indicator.md) in MQL4 or MQL5. The [indicator](../i/indicator.md) can be added to the chart, and traders can customize the SMA period to fit their strategy.

### TradingView

In [TradingView](../t/tradingview.md), traders can script the KRI using Pine Script. The interactive nature of [TradingView](../t/tradingview.md) allows traders to backtest the KRI across [multiple](../m/multiple.md) assets and timeframes to refine their strategies.

### Example Pine Script Code

```pinescript
// Kairi Relative [Index](../i/index.md) (KRI) in Pine Script
//@version=4
study("Kairi Relative [Index](../i/index.md)", shorttitle="KRI", [overlay](../o/overlay.md)=true)
length = input(20, title="SMA Length")
sma = sma(close, length)
kri = ((close - sma) / sma) * 100
plot(kri, color=color.blue, title="KRI")
hline(10, color=color.red, linestyle=hline.style_dashed)
hline(-10, color=color.green, linestyle=hline.style_dashed)
```

## Conclusion

The Kairi Relative [Index](../i/index.md) is a valuable tool in a [trader](../t/trader.md)'s arsenal. By quantifying the deviation of an [asset](../a/asset.md)'s price from its moving average, the KRI helps traders make informed decisions about [market](../m/market.md) conditions. Despite its simplicity, the KRI provides meaningful insights into potential [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions, [trend](../t/trend.md) confirmations, and divergences. However, like any technical [indicator](../i/indicator.md), it should be used in conjunction with other tools and analysis methods to enhance its effectiveness and reduce the [risk](../r/risk.md) of [false signals](../f/false_signals_in_trading.md).