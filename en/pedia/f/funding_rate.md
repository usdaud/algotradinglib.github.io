# Funding Rate

The funding rate is a periodic payment exchanged between long and short positions in perpetual futures or swaps. It is used to keep the contract price close to the underlying spot price.

## How it works
When the perpetual price trades above spot, the funding rate is often positive and longs pay shorts. When the perpetual price trades below spot, the rate can turn negative and shorts pay longs. The payment is based on position size and the current rate.

## Simple formula
Funding Payment = Position Notional * Funding Rate

The exact rate is determined by the venue and can include an interest rate component and a premium or discount component.

## Trading implications
- Persistent positive funding can signal crowded long positioning.
- Traders may use funding to estimate carry costs.
- Some strategies capture funding by hedging spot and perpetual positions.

## Risks
Funding rates can be volatile during sharp market moves. Large rates can eat into returns or force position changes.

## Practical checklist
- Define the time horizon for Funding Rate and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Funding Rate as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Funding Rate, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Funding Rate. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Funding Rate alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
