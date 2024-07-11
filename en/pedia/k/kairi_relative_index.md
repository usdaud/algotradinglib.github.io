# Kairi Relative Index

The Kairi Relative Index (KRI), also known as the Kairi Index, is a technical analysis indicator used primarily in the world of financial trading. This index is utilized to measure the distance between an asset's price and its simple moving average (SMA) in percentage terms. The KRI provides traders with insights into the market's condition, helping them identify overbought or oversold situations.

## Calculation

The formula to calculate the Kairi Relative Index is straightforward:

\[ \text{KRI} = \left( \frac{\text{Current Price} - \text{SMA}}{\text{SMA}} \right) \times 100 \]

Where:
- **Current Price** is the current market price of the asset.
- **SMA** is the Simple Moving Average of the asset's price, calculated over a specified period.

The KRI values fluctuate around 0. When the current price is above the SMA, the KRI will be positive, signaling that the asset might be overbought. Conversely, when the current price is below the SMA, the KRI will be negative, indicating the asset might be oversold.

## Interpretation

### Overbought and Oversold Conditions

- **Overbought**: If the KRI shows a high positive value, it suggests that the asset is trading significantly above its moving average, which could indicate that it is overbought. Traders might interpret this as a signal to sell or short the asset since the price could be due for a correction.
- **Oversold**: Conversely, a high negative KRI value indicates that the asset is trading well below its moving average, suggesting it is oversold. This situation might present a buying opportunity for traders as the price could be poised for a rebound.

### Confirmation of Trends

- **Trend Following**: The KRI can be used as a trend-following indicator. If the KRI is consistently positive, it might confirm an uptrend. If it remains negative over an extended period, it could confirm a downtrend.
- **Signal Filtering**: By setting thresholds for positive and negative values, traders can filter out noise and focus on significant price deviations, improving the accuracy of their trading strategies.

### Divergences

Identifying divergences between the KRI and the underlying price can also provide valuable trading signals:
- **Bullish Divergence**: When the price makes a new low but the KRI does not, it could signal a potential upward reversal.
- **Bearish Divergence**: When the price makes a new high but the KRI does not, it could indicate an impending downward reversal.

## Advantages

1. **Simplicity**: The Kairi Relative Index is easy to understand and calculate, making it accessible for traders of all experience levels.
2. **Versatility**: It can be applied to various asset classes, including stocks, commodities, forex, and cryptocurrencies.
3. **Early Signal Identification**: By highlighting significant deviations from the moving average, the KRI helps traders identify potential reversal points early.

## Limitations

1. **Lagging Nature**: Since the KRI relies on moving averages, it inherently lags behind the current price action, which might result in delayed signals.
2. **False Signals**: In volatile markets, short-term fluctuations could produce false overbought or oversold signals, leading to potential losses.
3. **Dependence on SMA Period** The effectiveness of the KRI is highly dependent on the selected period for the simple moving average. Different periods can produce varying signals, so traders need to optimize this parameter based on their trading strategy.

## Practical Applications

### Example 1: Stock Trading

Consider a trader analyzing the stock of a technology company. The trader applies the KRI to a 20-day SMA to assess the stock's condition. If the KRI reaches +10% or higher, the trader might consider selling the stock or taking short positions, anticipating a price correction. Conversely, if the KRI drops to -10% or lower, the trader might see it as a buying opportunity, expecting the stock to rebound.

### Example 2: Forex Trading

A forex trader uses the KRI on the EUR/USD currency pair with a 50-day SMA. The KRI rising above +5% could signal that the euro is overbought against the dollar, prompting the trader to sell euros. If the KRI falls below -5%, it suggests that the euro is oversold, and the trader might buy euros.

### Example 3: Cryptocurrency Trading

In the highly volatile cryptocurrency market, a trader uses the KRI with a shorter period, such as a 10-day SMA, for quicker reactions. When the KRI exceeds +15%, it could indicate that the cryptocurrency is overbought. Conversely, a KRI below -15% might signal an oversold condition, suggesting potential entry points.

## Implementation in Trading Platforms

### MetaTrader

In MetaTrader, traders can implement the KRI by coding it as a custom indicator in MQL4 or MQL5. The indicator can be added to the chart, and traders can customize the SMA period to fit their strategy.

### TradingView

In TradingView, traders can script the KRI using Pine Script. The interactive nature of TradingView allows traders to backtest the KRI across multiple assets and timeframes to refine their strategies.

### Example Pine Script Code

```pinescript
// Kairi Relative Index (KRI) in Pine Script
//@version=4
study("Kairi Relative Index", shorttitle="KRI", overlay=true)
length = input(20, title="SMA Length")
sma = sma(close, length)
kri = ((close - sma) / sma) * 100
plot(kri, color=color.blue, title="KRI")
hline(10, color=color.red, linestyle=hline.style_dashed)
hline(-10, color=color.green, linestyle=hline.style_dashed)
```

## Conclusion

The Kairi Relative Index is a valuable tool in a trader's arsenal. By quantifying the deviation of an asset's price from its moving average, the KRI helps traders make informed decisions about market conditions. Despite its simplicity, the KRI provides meaningful insights into potential overbought or oversold conditions, trend confirmations, and divergences. However, like any technical indicator, it should be used in conjunction with other tools and analysis methods to enhance its effectiveness and reduce the risk of false signals.