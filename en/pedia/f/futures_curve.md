# Futures Curve

The futures curve, also called the term structure, is the set of futures prices across different expirations for the same underlying. It shows how the market prices delivery at various points in time.

## Shapes
- Contango: later contracts are higher than near contracts.
- Backwardation: later contracts are lower than near contracts.

## Drivers
Storage costs, interest rates, convenience yield, and expectations about future supply and demand all influence the curve. In financial futures, the curve often reflects interest rate differentials and dividend expectations.

## Why it matters
- It determines roll yield for strategies that hold futures over time.
- It can signal market stress or tight supply.
- It informs hedging and inventory decisions.

## Example
In crude oil, a steep backwardation curve suggests tight near term supply. Traders may prefer holding near contracts to capture the positive roll yield.

## Practical note
Curve analysis is usually done by comparing spreads between consecutive months and monitoring how those spreads change over time.

## Practical checklist
- Define the time horizon for Futures Curve and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Futures Curve as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Futures Curve, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Futures Curve. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Futures Curve alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
