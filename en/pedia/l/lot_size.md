# Lot Size

Lot size is the standardized quantity of an asset used for trading. It defines the minimum or standard contract size in a given market.

## Examples
- Equities often trade in lots of 100 shares.
- Standard FX lots are commonly 100,000 units of the base currency.
- Futures contracts have fixed contract sizes defined by the exchange.

## Why it matters
Lot size affects position sizing, margin requirements, and transaction costs. It also determines the minimum price movement value for derivatives.

## Example
A trader buys one futures contract with a lot size of 50 units. A 1 point move equals 50 in profit or loss.

## Practical notes
Some markets allow mini or micro lots that reduce minimum exposure and margin.

## Practical checklist
- Define the time horizon for Lot Size and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Lot Size as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Lot Size, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Lot Size. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Lot Size alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
