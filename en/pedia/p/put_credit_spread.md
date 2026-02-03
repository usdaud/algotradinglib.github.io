# Put Credit Spread

A put credit spread is an options strategy that sells a put option and buys another put at a lower strike, both with the same expiration. The position collects a net credit and profits if the underlying stays above the short strike.

## Structure
- Sell a higher strike put.
- Buy a lower strike put.
- Net credit received up front.

## Profit and loss
- Maximum profit is the credit received.
- Maximum loss is the strike difference minus the credit.
- Breakeven is short strike minus credit.

## Example
A stock trades at 100. A trader sells the 95 put and buys the 90 put. If the stock stays above 95 at expiration, the credit is kept.

## Risks
Losses occur if the stock drops below the short strike. Risk is limited but can still be significant relative to the credit.

## Practical checklist
- Define the time horizon for Put Credit Spread and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Put Credit Spread as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Put Credit Spread, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Put Credit Spread. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Put Credit Spread alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
