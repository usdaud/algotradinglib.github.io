# Negative Volume Index (NVI)

The Negative [Volume](../v/volume.md) [Index](../i/index_instrument.md) (NVI) is a [technical analysis](../t/technical_analysis.md) tool used by traders to identify and evaluate price trends and changes within [financial markets](../f/financial_market.md). It was developed by Paul L. Dysart in the 1930s and later popularized by Norman Fosback in his 1976 book, "[Stock Market](../s/stock_market.md) Logic."

## Understanding NVI

NVI is based on the idea that the most significant price movements occur on days when the trading [volume](../v/volume.md) decreases compared to the previous day's trading [volume](../v/volume.md). This concept operates under the assumption that the "[smart money](../s/smart_money.md)" (institutional investors and knowledgeable traders) primarily operates when the [volume](../v/volume.md) is low, accumulating or distributing positions discreetly without drawing too much attention from the broader [market](../m/market.md).

In contrast, days with high trading volumes are believed to be dominated by the general public and less-informed investors. The NVI helps to filter out the [noise](../n/noise.md) those higher [volume](../v/volume.md) days may cause and focuses on more subtle, potentially more meaningful price movements corresponding to lower [volume](../v/volume.md) days.

## Calculation of NVI

The calculation of the NVI is relatively straightforward. It starts with an initial [value](../v/value.md), generally set to 1,000, and adjusts based on the daily [percentage change](../p/percentage_change.md) in the [asset](../a/asset.md)'s price when the [volume](../v/volume.md) decreases compared to the previous day’s [volume](../v/volume.md). If the day's [volume](../v/volume.md) is higher than the previous day’s [volume](../v/volume.md), the NVI [value](../v/value.md) remains [unchanged](../u/unchanged.md).

The formula for NVI when there is a decrease in [volume](../v/volume.md) is as follows:

\[ \text{NVI}_t = \text{NVI}_{t-1} + \left( \frac{\text{Close}_t - \text{Close}_{t-1}}{\text{Close}_{t-1}} \times \text{NVI}_{t-1} \right) \]

Where:
- \( \text{NVI}_t \) is the NVI [value](../v/value.md) at time t,
- \( \text{NVI}_{t-1} \) is the NVI [value](../v/value.md) for the previous period,
- \( \text{Close}_t \) is the closing price of the current period,
- \( \text{Close}_{t-1} \) is the closing price of the previous period.

If the trading [volume](../v/volume.md) for the current period is greater than the trading [volume](../v/volume.md) for the previous period, then:

\[ \text{NVI}_t = \text{NVI}_{t-1} \]

## Interpreting NVI

The NVI is typically used in conjunction with price charts and moving averages to help identify changes in trends. When interpreting the NVI, several key points should be considered:

### Trend Confirmation

- **Bullish Signal**: When the NVI is above its moving average (typically a 255-day moving average), it can indicate a longer-term bullish [trend](../t/trend.md). This signifies that the price is more likely to rise on days of decreasing [volume](../v/volume.md), suggesting accumulation by knowledgeable investors.
- **Bearish Signal**: When the NVI is below its moving average, it can indicate a longer-term bearish [trend](../t/trend.md). This suggests that the price is more likely to fall on days of decreasing [volume](../v/volume.md), indicating [distribution](../d/distribution.md) by knowledgeable investors.

### Divergences

Traders also look for divergences between the NVI and price. A [divergence](../d/divergence.md) occurs when the NVI and price move in opposite directions:

- **[Bullish Divergence](../b/bullish_divergence.md)**: Price is making lower lows while the NVI is making higher lows. This can be a sign that the [downtrend](../d/downtrend.md) is weakening and a [reversal](../r/reversal.md) to the [upside](../u/upside.md) may be forthcoming.
- **[Bearish Divergence](../b/bearish_divergence.md)**: Price is making higher highs while the NVI is making lower highs. This can indicate that the [uptrend](../u/uptrend.md) is weakening and a [reversal](../r/reversal.md) to the downside may be imminent.

## Practical Application in Trading

### Historical Testing

NVI can be applied historically to test its effectiveness in predicting significant [market](../m/market.md) moves. Traders can backtest NVI strategies on historical data to evaluate how well the [indicator](../i/indicator.md) has performed in various [market](../m/market.md) conditions. This helps in understanding its strengths and limitations and in refining the strategy for better performance.

### Integration with Other Indicators

NVI is often used in conjunction with other [technical indicators](../t/technical_indicator.md) to improve trading decisions. Commonly paired indicators include On-Balance [Volume](../v/volume.md) (OBV), Moving Averages, and the Positive [Volume](../v/volume.md) [Index](../i/index_instrument.md) (PVI), which focuses on days of increasing [volume](../v/volume.md). Combining NVI with other indicators can provide a more comprehensive analysis and reinforce signals.

### Example: Trading Strategy

A straightforward [trading strategy](../t/trading_strategy.md) using the NVI involves following these steps:

1. Plot the NVI and its 255-day moving average.
2. Identify crossovers:
   - Buy signal: When NVI crosses above its 255-day moving average.
   - Sell signal: When NVI crosses below its 255-day moving average.
3. Confirm signals with additional indicators (e.g., Moving Average Convergence [Divergence](../d/divergence.md) (MACD), [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI)) to reduce [false signals](../f/false_signals_in_trading.md).

### Risk Management

Like any [trading strategy](../t/trading_strategy.md), using the NVI requires sound [risk management](../r/risk_management.md) practices. Traders should set [stop-loss orders](../s/stop-loss_orders.md) based on their [risk tolerance](../r/risk_tolerance.md) and [market](../m/market.md) conditions to protect against significant losses. Additionally, proper [position sizing](../p/position_sizing.md) and [diversification](../d/diversification.md) should be employed to manage [risk](../r/risk.md) effectively.

## Advantages and Limitations

### Advantages

- **Focus on [Smart Money](../s/smart_money.md)**: NVI filters out the [noise](../n/noise.md) generated by high-[volume](../v/volume.md) days, focusing on the movements of presumed more informed investors.
- **[Trend](../t/trend.md) Identification**: Helps in identifying longer-term trends and potential reversals, providing valuable insights for traders.
- **Simplicity**: The calculation and interpretation of NVI are straightforward, making it accessible to traders of all experience levels.

### Limitations

- **[Lagging Indicator](../l/lagging_indicator.md)**: Like many [trend](../t/trend.md)-following indicators, the NVI may lag behind the actual price movements, leading to delayed signals.
- **[Volume](../v/volume.md) Requirements**: The effectiveness of NVI relies heavily on the quality and accuracy of [volume](../v/volume.md) data, which may not always be reliable.
- **Sole Reliance Risks**: Relying solely on NVI for trading decisions can be risky. It is best used in conjunction with other [technical analysis tools](../t/technical_analysis_tools.md) to confirm signals and reduce the [risk](../r/risk.md) of false positives.

## Conclusion

The Negative [Volume](../v/volume.md) [Index](../i/index_instrument.md) is a valuable tool for traders and investors looking to identify and analyze price movements driven by lower trading volumes. By focusing on these quieter days, the NVI aims to capture the activities of more informed [market](../m/market.md) participants, potentially providing early indications of significant price trends and reversals.

While it offers several advantages, including its simplicity and focus on "[smart money](../s/smart_money.md)," it is essential to be aware of its limitations. NVI should not be used in isolation but rather as part of a comprehensive [trading strategy](../t/trading_strategy.md) that incorporates [multiple](../m/multiple.md) indicators and sound [risk management](../r/risk_management.md) practices.

For those interested in exploring the NVI further, historical analysis, [backtesting](../b/backtesting.md), and integrating it with other [technical indicators](../t/technical_indicator.md) can provide a deeper understanding and more [robust](../r/robust.md) trading approach. By doing so, traders can enhance their decision-making process and increase their chances of success in the dynamic world of [financial markets](../f/financial_market.md).

To learn more about trading tools and strategies, consider visiting educational resources provided by prominent trading platforms and institutions, such as [Investopedia](https://www.investopedia.com) or [TradingView](https://www.tradingview.com).