# Futures Calendar Spread

A futures calendar spread is a position that is long one futures contract month and short another month on the same underlying. It isolates the change in the term structure rather than the outright price direction.

## Structure
- Buy a near month and sell a far month, or the reverse.
- The spread price is the difference between the two contract prices.
- The spread reflects storage costs, interest rates, and supply or demand expectations.

## Uses
- Trading contango or backwardation shifts.
- Rolling hedges with lower directional exposure.
- Speculating on seasonal effects in commodities.

## Example
A trader buys the September contract and sells the December contract. If the curve moves from contango toward backwardation, the spread can widen in the traders favor.

## Risks
Spreads can be less volatile than outright futures but still move sharply when supply shocks occur. Liquidity can vary by month, so execution matters.

## Practical checklist
- Define the time horizon for Futures Calendar Spread and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Futures Calendar Spread as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Futures Calendar Spread, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Futures Calendar Spread. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Futures Calendar Spread alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
