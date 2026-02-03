# Good Till Canceled (GTC)

A good till canceled order remains active until it is filled or explicitly canceled by the trader. It can stay open for days or weeks, depending on broker policy.

## Key characteristics
- Stays active across sessions.
- Can be used for longer term entry or exit targets.
- May have maximum life limits set by the broker.

## Example
A trader places a GTC sell order at 60 for a stock currently trading at 55. The order remains open until price reaches 60 or the trader cancels it.

## Risks
A long lived order can be triggered by unexpected news or during low liquidity. Traders should review open GTC orders regularly to avoid stale instructions.

## Practical checklist
- Define the time horizon for Good Till Canceled (GTC) and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Good Till Canceled (GTC) as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Good Till Canceled (GTC), confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Good Till Canceled (GTC). Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Good Till Canceled (GTC) alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
