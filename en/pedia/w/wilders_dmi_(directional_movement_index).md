# Wilder's Directional Movement Index (DMI)

The Directional Movement [Index](../i/index_instrument.md) (DMI), developed by J. Welles Wilder, is a technical [indicator](../i/indicator.md) that estimates the strength and direction of a [trend](../t/trend.md). It aids in identifying whether a [security](../s/security.md) is trending and how strong that [trend](../t/trend.md) is. Traders often use DMI to make trading decisions and to develop [trading strategies](../t/trading_strategies.md).

## Components of DMI

The DMI consists of three lines:
1. **+DI (Positive Directional [Indicator](../i/indicator.md))**: Measures the strength of the upward movement.
2. **-DI (Negative Directional [Indicator](../i/indicator.md))**: Measures the strength of the downward movement.
3. **ADX ([Average Directional Index](../a/average_directional_index_(adx).md))**: Calculates the absolute strength of the [trend](../t/trend.md), regardless of direction.

### +DI and -DI Calculation

To calculate +DI and -DI, you must first determine the Directional Movement (DM) for each period:

1. **Calculate UpMove and DownMove**:
 - **UpMove** = Current High - Previous High
 - **DownMove** = Previous Low - Current Low

2. **Determine Positive and Negative Directional Movement**:
 - If UpMove > DownMove and UpMove > 0: +DM = UpMove
 - If DownMove > UpMove and DownMove > 0: -DM = DownMove
 - If neither condition is met, +DM = 0 and -DM = 0

3. **Calculate the True [Range](../r/range.md) (TR)**:
 - TR is the greatest of the following:
 - Current High - Current Low
 - Absolute [Value](../v/value.md) of Current High - Previous Close
 - Absolute [Value](../v/value.md) of Current Low - Previous Close

4. **Smoothed +DM, -DM, and TR**:
 - Use a smoothing technique (commonly a 14-period average).

5. **+DI and -DI**:
 - +DI = (Smoothed +DM / Smoothed TR) * 100
 - -DI = (Smoothed -DM / Smoothed TR) * 100

### ADX Calculation

1. **Calculate the Directional Movement [Index](../i/index_instrument.md) (DX)**:
 - DX = (| +DI - -DI | / (+DI + -DI)) * 100

2. **Calculate ADX**:
 - The ADX is the smoothed average of DX values over a specified period (commonly 14 periods).

## Interpreting DMI

### Crossovers

The +DI and -DI lines can be used in crossover strategies:
- **Bullish Signal**: When +DI crosses above -DI, it indicates a potentially bullish [trend](../t/trend.md).
- **Bearish Signal**: When -DI crosses above +DI, it indicates a potentially bearish [trend](../t/trend.md).

### ADX Trend Strength

- **ADX below 20**: Weak or non-existent [trend](../t/trend.md).
- **ADX above 20**: Indicates the presence of a [trend](../t/trend.md).
- **ADX above 40**: Indicates a strong [trend](../t/trend.md).

## Applications in Trading Strategies

### Trend Following

When ADX is above 20, traders often use the DMI for [trend](../t/trend.md)-following strategies:
- Enter long positions when +DI crosses above -DI if ADX is rising.
- Enter short positions when -DI crosses above +DI if ADX is rising.

### Range Bound Strategies

When ADX is below 20, it may be an indication of a [range](../r/range.md)-bound [market](../m/market.md). Strategies such as oscillators or mean-reversion techniques are more suitable.

## Limitations of DMI

1. **[Lagging Indicator](../l/lagging_indicator.md)**: The DMI relies on historical data, so it may not respond quickly to sudden price changes.
2. **[False Signals](../f/false_signals_in_trading.md)**: In highly volatile markets, DMI can produce [false signals](../f/false_signals_in_trading.md).
3. **Complexity**: The calculation of DMI involves [multiple](../m/multiple.md) steps, making it somewhat complex for beginners.

## Conclusion

The Directional Movement [Index](../i/index_instrument.md) is a powerful and versatile tool for assessing [trend](../t/trend.md) strength and direction. While it has its limitations, when combined with other indicators and sound trading principles, it can significantly enhance trading decisions.

For more detailed information on [technical indicators](../t/technical_indicators.md) and [trading strategies](../t/trading_strategies.md), you can explore resources from financial institutions and trading platforms such as:
- Investopedia
- TradingView
- StockCharts

## Practical checklist
- Define the time horizon for Wilder's Directional Movement Index (DMI) and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Wilder's Directional Movement Index (DMI) as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Wilder's Directional Movement Index (DMI), confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.
