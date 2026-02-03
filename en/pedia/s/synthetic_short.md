# Synthetic Short

A synthetic short is an options position that replicates the payoff of a short stock position. It is created by selling a call and buying a put at the same strike and expiration.

## Structure
- Short call at strike X.
- Long put at strike X.
- Same expiration date.

## Payoff
The combined position gains when the stock falls and loses when the stock rises, similar to shorting the stock.

## Example
A trader sells a 100 call and buys a 100 put. If the stock declines, the put gains while the call expires, creating a profit similar to a short position.

## Practical notes
Synthetic shorts can avoid the need to borrow shares, but they still have risk and margin requirements. Early assignment on the short call can occur.

## Practical checklist
- Define the time horizon for Synthetic Short and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Synthetic Short as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Synthetic Short, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Synthetic Short. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Synthetic Short alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
