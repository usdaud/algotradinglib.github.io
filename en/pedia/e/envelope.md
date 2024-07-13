# Envelope

An envelope, in the context of trading and [technical analysis](../t/technical_analysis.md), refers to a technical [indicator](../i/indicator.md) that is primarily used to identify the [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions in a [security](../s/security.md)'s price. Envelopes are created by plotting two lines above and below a simple moving average (SMA) or an exponential moving average (EMA) of a [security](../s/security.md)’s price data. These lines are generally set at a predetermined percentage distance from the moving average, which envelops the price with a [range](../r/range.md). The envelope provides traders with a clear picture of the [range](../r/range.md) within which the [security](../s/security.md)'s price typically moves. This [range](../r/range.md) can then be used to predict potential [trading signals](../t/trading_signals.md) based on price movements.

## Components of an Envelope

1. **Moving Average**: The central line or base around which the envelope is plotted. It can be a simple moving average (SMA) or an exponential moving average (EMA). The selection of the type and period of the moving average depends on the [trader](../t/trader.md)'s strategy and the [volatility](../v/volatility.md) of the [security](../s/security.md) being traded.
   
2. **Envelope Bands**: These are the lines that are plotted at a certain percentage above and below the moving average. They create a “channel” or “envelope” around the price. The percentage can be adjusted according to the [trader](../t/trader.md)'s preference for capturing the normal price movement.

## Calculation of Envelope

1. Compute the moving average:
   If SMA is used, the formula is:
   \[
   SMA = \frac{\sum{Price_i}}{n}
   \]
   where \( n \) is the number of periods and \( Price_i \) is the price at period \( i \).

   If EMA is used, the formula is a bit more complex:
   \[
   EMA_t = Price_t \times K + EMA_{t-1} \times (1-K)
   \]
   where \( K = \frac{2}{n+1} \).

2. Calculate the upper and lower bands:
   \[
   Upper Band = SMA \times (1 + \%\text{Envelope})
   \]
   \[
   Lower Band = SMA \times (1 - \%\text{Envelope})
   \]

## Usage of Envelopes in Trading

Envelopes are used by traders to identify possible trading opportunities. Here are some common strategies:

1. **[Trend](../t/trend.md) Identification**: When prices consistently stay above the moving average and near the upper envelope band, it indicates an [uptrend](../u/uptrend.md). Conversely, when prices stay below the moving average and near the lower envelope band, it indicates a [downtrend](../d/downtrend.md).

2. **[Overbought](../o/overbought.md) and [Oversold](../o/oversold.md) Conditions**: Prices moving close to the upper band may suggest an [overbought](../o/overbought.md) condition, potentially signaling a sell opportunity. Prices moving close to the lower band may suggest an [oversold](../o/oversold.md) condition, potentially signaling a buy opportunity.

3. **Breakouts**: When prices break out from the envelope bands — either above the upper band or below the lower band — it could indicate a significant change in [trend](../t/trend.md) or increased [volatility](../v/volatility.md), which might signal an entry or exit point for traders.

## Practical Examples and Insights

### Example 1: Forex Trading

In forex trading, envelopes can be used to set optimal entry and exit points. A 20-period SMA might be used with an envelope set at 2.5% above and below the average. If the EUR/USD pair is hovering near the upper envelope, a [trader](../t/trader.md) might anticipate a [reversal](../r/reversal.md) and prepare to sell. Conversely, if the pair is near the lower envelope, it could suggest a buying opportunity.

### Example 2: Stock Trading

For a stock like Apple Inc. (AAPL), a [trader](../t/trader.md) might use an EMA of 50 periods with a 3% envelope. When the stock price approaches the upper band, it might indicate that the stock is becoming [overbought](../o/overbought.md), suggesting to sell or short. If the price approaches the lower band, this might indicate that the stock is [oversold](../o/oversold.md), suggesting to buy or go long.

## Visualization

Visualization of envelopes on a chart is pretty straightforward. Most charting tools like [TradingView](../t/tradingview.md), MetaTrader, and others provide built-in functionalities to plot envelopes. Here’s a step-by-step guide to plot and interpret envelopes on [TradingView](../t/tradingview.md):

1. [Open](../o/open.md) the [TradingView](../t/tradingview.md) platform: [TradingView](https://www.tradingview.com/).
2. Select a [security](../s/security.md) (e.g., Apple Inc. - AAPL).
3. Choose the desired chart time frame (e.g., daily, weekly).
4. Go to the "Indicators" section and search for "Envelope".
5. Adjust settings (e.g., moving average type, period, and percentage).
6. Apply the [indicator](../i/indicator.md) to the chart.

Traders can then observe how the price interacts with the envelope bands and make informed trading decisions accordingly.

## Advanced Considerations

1. **[Volatility](../v/volatility.md) Adjustment**: During periods of high [market](../m/market.md) [volatility](../v/volatility.md), traders might need to adjust the envelope percentage to prevent frequent [false signals](../f/false_signals_in_trading.md).
2. **Confirmation with Other Indicators**: To enhance the accuracy of [trading signals](../t/trading_signals.md), envelopes can be used in conjunction with other [technical indicators](../t/technical_indicator.md) such as the [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI), Moving Average Convergence [Divergence](../d/divergence.md) (MACD), and [Bollinger Bands](../b/bollinger_band.md).
3. **[Algorithmic Trading](../a/accountability.md) Applications**: Algorithmic traders often implement envelopes in their [trading algorithms](../t/trading_algorithms.md) to automate [trade](../t/trade.md) decisions based on predefined criteria.
4. **[Backtesting](../b/backtesting.md)**: Before using envelopes in live trading, it’s crucial to backtest the strategy on historical data to evaluate the performance and reliability of the signals generated.

## Conclusion

Envelopes provide a versatile and effective method for traders to identify potential [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions, track [market](../m/market.md) trends, and spot significant breakouts. By understanding the components and calculation of envelopes, traders can tailor their strategies to align with [market](../m/market.md) conditions, ultimately enhancing their [trading performance](../t/trading_performance.md). As with any [technical analysis](../t/technical_analysis.md) tool, envelopes should be used in conjunction with other analysis techniques and [risk management](../r/risk_management.md) practices to maximize their effectiveness.