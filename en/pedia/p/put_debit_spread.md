# Put Debit Spread

A put debit spread is an options strategy that buys a put option and sells another put at a lower strike, both with the same expiration. The position pays a net debit and profits from a decline in the underlying.

## Structure
- Buy a higher strike put.
- Sell a lower strike put.
- Net debit paid up front.

## Profit and loss
- Maximum profit is the strike difference minus the debit.
- Maximum loss is the debit paid.
- Breakeven is long strike minus debit.

## Example
A stock trades at 100. A trader buys the 100 put and sells the 95 put. If the stock falls below 95 at expiration, the spread reaches max profit.

## Risks
The position loses if the stock stays above the long strike. It is a defined risk bearish strategy.

## Practical checklist
- Define the time horizon for Put Debit Spread and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Put Debit Spread as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Put Debit Spread, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Put Debit Spread. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Put Debit Spread alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
