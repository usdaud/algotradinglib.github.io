# Relative Volume

Relative volume compares current trading volume to a historical average for the same time period. It helps determine whether activity is higher or lower than normal.

## Calculation
Relative Volume = Current volume / Average volume

The average can be based on the same time of day over a lookback window or on full day averages.

## Interpretation
- Values above 1 indicate higher than normal activity.
- Values below 1 indicate lower than normal activity.

## Example
By 10:30 AM a stock has traded 2 million shares, while the average by that time is 1 million. The relative volume is 2.0, indicating elevated activity.

## Practical notes
Relative volume is useful for validating breakouts, news reactions, and unusual activity. It is less informative in very low liquidity markets.

## Practical checklist
- Define the time horizon for Relative Volume and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Relative Volume as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Relative Volume, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Relative Volume. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Relative Volume alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
