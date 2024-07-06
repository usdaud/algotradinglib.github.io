# Average True Range

Average True Range (ATR) is a [technical analysis](../t/technical_analysis.md) indicator designed to measure market volatility. J. Welles Wilder, the founder of ATR, introduced it in his 1978 book "New Concepts in Technical [Trading Systems](../t/trading_systems.md)." ATR does not provide an indication of price direction like many other indicators, but rather the degree of price movement, making it a useful tool for traders to gauge market volatility and potential price fluctuation.

### How ATR is Calculated

The ATR is based on a series of true range values, which are computed from the following three components:

1. Current high less the current low
2. Absolute value of the current high less the previous close
3. Absolute value of the current low less the previous close

The true range (TR) is the greatest of these three values. The formula for calculating true range is:

\[ TR = \max\left(High - Low, \left|High - Previous\ Close\right|, \left|Low - Previous\ Close\right|\right) \]

The Average True Range (ATR) is then derived as an exponential moving average (EMA) of these true range values over a designated period, typically 14 days as per Wilder's original recommendation. The ATR formula is given by:

\[ ATR = EMA_{n}(TR) \]

Where \( n \) is the period for the moving average.

### Interpretation of ATR

#### Volatility Measurement

The primary utility of ATR is to serve as a volatility gauge:
- **High ATR values** indicate higher volatility, suggesting that prices are undergoing larger movements.
- **Low ATR values** indicate lower volatility, suggesting that prices are relatively stable.

#### Use in Trading Strategies

- **Stop-Loss Setting:** Traders often use ATR to set stop-loss levels, ensuring that the stop-loss is proportional to the asset's volatility. For instance, a stop-loss might be set at 1.5 times the ATR below a long position entry point.
- **Entry and Exit Signals:** ATR can also signal when to enter or exit trades. In trend-following strategies, a rising ATR during upward price movement may reinforce the buying decision, indicating strong market momentum.
- **[Position Sizing](../p/position_sizing.md):** By adjusting position sizes according to ATR, traders manage their risk exposure more effectively. Larger positions are justified during low volatility, while smaller positions are prudent during high volatility.

#### Risk Management

In [risk management](../r/risk_management.md), ATR is used to evaluate market noise and determine appropriate levels for emergency asset liquidation or risk exposure. For example, if the market shifts sharply within a day and crosses the ATR threshold, this could trigger automatic responses to minimize losses.

### Practical Applications

Several platforms and trading tools integrate ATR to assist traders in market analysis:

- **[TradingView](../t/tradingview.md):** Provides interactive ATR charts customizable for various asset classes.
- **MetaTrader 4 and 5 (MT4/MT5):** Offers built-in ATR indicators available for forex, futures, and stock markets.
- **[Thinkorswim](../t/thinkorswim.md) by TD [Ameritrade](../a/ameritrade.md):** Includes ATR in its suite of volatility indicators and trading tools.

### Advantages of ATR

1. **Simplicity and Clarity:** ATR is straightforward to compute and interpret, offering immediacy for decision-making.
2. **Adaptability:** Suitable for all market types (stocks, forex, commodities).
3. **Non-Directional Nature:** Focuses purely on price volatility, avoiding directional bias.

### Limitations of ATR

1. **Historical Data Dependence:** Relies solely on past price data, which may not always predict future behavior accurately.
2. **Ignores Market Context:** ATR does not consider broader market trends, [economic indicators](../e/economic_indicators.md), or fundamental data.
3. **Fixed Period Selection:** Constant period settings may not capture varying market dynamics or external influences effectively.

### Conclusion

Average True Range (ATR) remains an invaluable tool for traders focused on [volatility analysis](../v/volatility_analysis.md) and [risk management](../r/risk_management.md). Its incorporation into [trading systems](../t/trading_systems.md) helps in setting strategic entry, exit, and stop-loss points while providing a deeper understanding of market behavior. By coupling ATR with other [technical indicators](../t/technical_indicators.md) and [fundamental analysis](../f/fundamental_analysis.md), traders can enhance their operational strategies and achieve more stable returns.

For further information on ATR tools and platforms, here are links to relevant sites:

- **[TradingView](../t/tradingview.md):** [https://www.tradingview.com/](https://www.tradingview.com/)
- **MetaTrader:** [https://www.metatrader4.com/](https://www.metatrader4.com/)
- **[Thinkorswim](../t/thinkorswim.md):** [https://www.thinkorswim.com/](https://www.thinkorswim.com/)
