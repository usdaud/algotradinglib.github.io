# Average True Range

Average True [Range](../r/range.md) (ATR) is a [technical analysis](../t/technical_analysis.md) [indicator](../i/indicator.md) designed to measure [market](../m/market.md) [volatility](../v/volatility.md). J. Welles Wilder, the founder of ATR, introduced it in his 1978 book "New Concepts in Technical [Trading Systems](../t/trading_systems.md)." ATR does not provide an indication of price direction like many other indicators, but rather the degree of price movement, making it a useful tool for traders to gauge [market](../m/market.md) [volatility](../v/volatility.md) and potential price fluctuation.

### How ATR is Calculated

The ATR is based on a series of true [range](../r/range.md) values, which are computed from the following three components:

1. Current high less the current low
2. Absolute [value](../v/value.md) of the current high less the previous close
3. Absolute [value](../v/value.md) of the current low less the previous close

The true [range](../r/range.md) (TR) is the greatest of these three values. The formula for calculating true [range](../r/range.md) is:

\[ TR = \max\left(High - Low, \left|High - Previous\ Close\right|, \left|Low - Previous\ Close\right|\right) \]

The Average True [Range](../r/range.md) (ATR) is then derived as an exponential moving average (EMA) of these true [range](../r/range.md) values over a designated period, typically 14 days as per Wilder's original recommendation. The ATR formula is given by:

\[ ATR = EMA_{n}(TR) \]

Where \( n \) is the period for the moving average.

### Interpretation of ATR

#### Volatility Measurement

The primary [utility](../u/utility.md) of ATR is to serve as a [volatility](../v/volatility.md) gauge:
- **High ATR values** indicate higher [volatility](../v/volatility.md), suggesting that prices are undergoing larger movements.
- **Low ATR values** indicate lower [volatility](../v/volatility.md), suggesting that prices are relatively stable.

#### Use in Trading Strategies

- **Stop-Loss Setting:** Traders often use ATR to set stop-loss levels, ensuring that the stop-loss is proportional to the [asset](../a/asset.md)'s [volatility](../v/volatility.md). For instance, a stop-loss might be set at 1.5 times the ATR below a long position entry point.
- **Entry and Exit Signals:** ATR can also signal when to enter or exit trades. In [trend](../t/trend.md)-following strategies, a rising ATR during upward price movement may reinforce the buying decision, indicating strong [market](../m/market.md) [momentum](../m/momentum.md).
- **[Position Sizing](../p/position_sizing.md):** By adjusting position sizes according to ATR, traders manage their [risk](../r/risk.md) exposure more effectively. Larger positions are justified during low [volatility](../v/volatility.md), while smaller positions are prudent during high [volatility](../v/volatility.md).

#### Risk Management

In [risk management](../r/risk_management.md), ATR is used to evaluate [market](../m/market.md) [noise](../n/noise.md) and determine appropriate levels for emergency [asset](../a/asset.md) [liquidation](../l/liquidation.md) or [risk](../r/risk.md) exposure. For example, if the [market](../m/market.md) shifts sharply within a day and crosses the ATR threshold, this could trigger automatic responses to minimize losses.

### Practical Applications

Several platforms and trading tools integrate ATR to assist traders in [market](../m/market.md) analysis:

- **[TradingView](../t/tradingview.md):** Provides interactive ATR charts customizable for various [asset](../a/asset.md) classes.
- **MetaTrader 4 and 5 (MT4/MT5):** Offers built-in ATR indicators available for forex, [futures](../f/futures.md), and stock markets.
- **[Thinkorswim](../t/thinkorswim.md) by TD [Ameritrade](../a/ameritrade.md):** Includes ATR in its suite of [volatility](../v/volatility.md) indicators and trading tools.

### Advantages of ATR

1. **Simplicity and Clarity:** ATR is straightforward to compute and interpret, [offering](../o/offering.md) immediacy for decision-making.
2. **Adaptability:** Suitable for all [market](../m/market.md) types ([stocks](../s/stock.md), forex, commodities).
3. **Non-Directional Nature:** Focuses purely on price [volatility](../v/volatility.md), avoiding directional bias.

### Limitations of ATR

1. **Historical Data Dependence:** Relies solely on past price data, which may not always predict future behavior accurately.
2. **Ignores [Market](../m/market.md) Context:** ATR does not consider broader [market](../m/market.md) trends, [economic indicators](../e/economic_indicators.md), or fundamental data.
3. **Fixed Period Selection:** Constant period settings may not capture varying [market dynamics](../m/market_dynamics.md) or external influences effectively.

### Conclusion

Average True [Range](../r/range.md) (ATR) remains an invaluable tool for traders focused on [volatility analysis](../v/volatility_analysis.md) and [risk management](../r/risk_management.md). Its [incorporation](../i/incorporation.md) into [trading systems](../t/trading_systems.md) helps in setting strategic entry, exit, and stop-loss points while providing a deeper understanding of [market](../m/market.md) behavior. By coupling ATR with other [technical indicators](../t/technical_indicators.md) and [fundamental analysis](../f/fundamental_analysis.md), traders can enhance their operational strategies and achieve more stable returns.

For further information on ATR tools and platforms, here are links to relevant sites:

- **[TradingView](../t/tradingview.md):** - **MetaTrader:** - **[Thinkorswim](../t/thinkorswim.md):**
