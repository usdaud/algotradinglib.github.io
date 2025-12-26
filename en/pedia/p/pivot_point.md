# Pivot Point

[Pivot Points](../p/pivot_points.md) are a popular [technical analysis](../t/technical_analysis.md) [indicator](../i/indicator.md) used by traders in various [financial markets](../f/financial_market.md), including [stocks](../s/stock.md), commodities, and forex. The concept of [pivot points](../p/pivot_points.md) stems from the idea that the [market](../m/market.md) tends to have recurring patterns, and using these patterns can help traders identify critical [support and resistance](../s/support_and_resistance.md) levels. These levels can be pivotal in determining entry and exit points for trades, thus aiding in the decision-making process.

## Definition and Calculation
[Pivot Points](../p/pivot_points.md) are calculated using the high, low, and closing prices from the previous period (day, week, etc.). The pivot point itself is considered a significant [price level](../p/price_level.md) that serves as a [basis](../b/basis.md) for the [indicator](../i/indicator.md). From this central pivot point, additional levels are calculated to establish potential [support and resistance](../s/support_and_resistance.md) levels.

### Formula
The primary pivot point (P) is calculated as follows:
```plaintext
Pivot Point (P) = (High + Low + Close) / 3
```

Based on this pivot point, the following support (S) and resistance (R) levels can be calculated:
```plaintext
First Resistance (R1) = (2 * P) - Low
First Support (S1) = (2 * P) - High

Second Resistance (R2) = P + (High - Low)
Second Support (S2) = P - (High - Low)

Third Resistance (R3) = High + 2 * (P - Low)
Third Support (S3) = Low - 2 * (High - P)
```

## Types of Pivot Points
### Standard Pivot Points
The standard method of calculating [pivot points](../p/pivot_points.md) relies on the straightforward formulas mentioned above. This type of pivot point is widely used in various markets for its simplicity and effectiveness.

### Fibonacci Pivot Points
Fibonacci numbers are applied to [pivot points](../p/pivot_points.md) to predict potential [support and resistance](../s/support_and_resistance.md) levels. In this context, traders often use [Fibonacci retracement](../f/fibonacci_retracement.md) levels (such as 38.2%, 50%, and 61.8%) to establish potential price targets.

### Camarilla Pivot Points
Developed by Nick Stott in the late 1980s, Camarilla [pivot points](../p/pivot_points.md) [offer](../o/offer.md) a unique perspective. The calculation involves [multiple](../m/multiple.md) intraday levels, creating eight potential levels (four resistance and four support). The formula for R3 and S3 is similar to the standard [pivot points](../p/pivot_points.md) method.
```plaintext
R1 = Close + ((High - Low) * 1.0833)
S1 = Close - ((High - Low) * 1.0833)
R2 = Close + ((High - Low) * 1.1666)
S2 = Close - ((High - Low) * 1.1666)
```

### Woodie's Pivot Points
Woodie's [pivot points](../p/pivot_points.md) use more weight on the closing price and are calculated as follows:
```plaintext
Pivot Point (P) = (High + Low + 2 * Close) / 4
```

### Demark Pivot Points
Demark's method is slightly more complex and adjusts the [pivot points](../p/pivot_points.md) based on the relationship between the [open](../o/open.md) and close prices.
```plaintext
If Close < [Open](../o/open.md):
Pivot Point (X) = High + 2 * Low + Close

If Close > [Open](../o/open.md):
Pivot Point (X) = 2 * High + Low + Close

If Close == [Open](../o/open.md):
Pivot Point (X) = High + Low + 2 * Close

Pivot Point (P) = X / 4

Resistance (R1) = X / 2 - Low

Support (S1) = X / 2 - High
```

## Application in Trading
[Pivot points](../p/pivot_points.md) serve as a predictive [indicator](../i/indicator.md) and help traders in different ways:
- **[Trend](../t/trend.md) Identification**: When the price is above the pivot point, it generally indicates a bullish [trend](../t/trend.md), while a price below the pivot point indicates a bearish [trend](../t/trend.md).
- **Entry and Exit Points**: [Pivot points](../p/pivot_points.md) can provide traders with specific levels to enter or exit trades. Breakouts above resistance levels or breakdowns below [support levels](../s/support_levels.md) can signal entry points.
- **[Risk Management](../r/risk_management.md)**: By identifying potential [support and resistance](../s/support_and_resistance.md) levels, [pivot points](../p/pivot_points.md) allow traders to set stop losses and take profits more effectively.

### Day Trading
Day traders often rely on [pivot points](../p/pivot_points.md) since they condense price data into clear and actionable levels. Given that [day trading](../d/day_trading.md) involves rapid decision making, having predefined levels for [support and resistance](../s/support_and_resistance.md) simplifies the trading process.

### Swing Trading
For swing traders who [hold](../h/hold.md) positions for several days or weeks, weekly or monthly [pivot points](../p/pivot_points.md) are more useful. These provide higher-level economic insights and help in understanding broader [market](../m/market.md) trends.

## Pros and Cons
### Pros
- **Simplicity**: [Pivot points](../p/pivot_points.md) are straightforward and easy to calculate.
- **Versatility**: They can be used across all [market](../m/market.md) types and timeframes.
- **Effective Levels**: Provide clear [support and resistance](../s/support_and_resistance.md) levels, aiding in trading decisions.
- **Predictive Abilities**: Help in [forecasting](../f/forecasting.md) [market](../m/market.md) movements.

### Cons
- **[Lagging Indicator](../l/lagging_indicator.md)**: As they are based on historical prices, they may lag current [market](../m/market.md) conditions.
- **[False Signals](../f/false_signals_in_trading.md)**: In volatile markets, [pivot points](../p/pivot_points.md) can sometimes give [false signals](../f/false_signals_in_trading.md).
- **Subjectivity**: Different types of [pivot points](../p/pivot_points.md) can [yield](../y/yield.md) different [support and resistance](../s/support_and_resistance.md) levels.

## Automation and Algo Trading
With the rise of [algorithmic trading](../a/algorithmic_trading.md), [pivot points](../p/pivot_points.md) can be integrated into [trading algorithms](../t/trading_algorithms.md) for automated decision making. By programming pivot point calculations and associated [trading rules](../t/trading_rules.md), traders can design algorithms that automatically place trades when certain levels are reached. These algorithms can include:
- **[Breakout](../b/breakout.md) Strategies**: Algorithms can be programmed to buy when the price crosses above resistance levels or sell when it crosses below [support levels](../s/support_levels.md).
- **[Mean Reversion](../m/mean_reversion.md)**: Algorithms can execute trades when the price is expected to revert to the pivot point.
- **[Risk Management](../r/risk_management.md)**: Automated systems can set stop-loss and take-[profit](../p/profit.md) levels based on [pivot points](../p/pivot_points.md), ensuring disciplined trading.

## Conclusion
[Pivot points](../p/pivot_points.md) are a [robust](../r/robust.md) tool in the [trader](../t/trader.md)'s arsenal. Whether used alone or in conjunction with other [technical indicators](../t/technical_indicator.md), they [offer](../o/offer.md) insightful levels that help traders make informed decisions. Their simplicity, combined with predictive abilities, makes them valuable for traders across all markets and timeframes. Although not without their drawbacks, the strategic application of [pivot points](../p/pivot_points.md) can lead to more effective [trading strategies](../t/trading_strategies.md) and improved [risk management](../r/risk_management.md).