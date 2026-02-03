# Liquidity Provider

A liquidity provider is a market participant that supplies buy and sell quotes to facilitate trading. Liquidity providers earn the spread or rebates and help keep markets efficient.

## Role in markets
- Post bids and offers to create continuous markets.
- Absorb order flow and manage inventory risk.
- Provide depth that reduces price impact for other traders.

## Example
A market maker posts a bid at 25.10 and an ask at 25.12, earning the spread when trades occur on both sides.

## Risks
Liquidity providers face adverse selection when trading against informed participants. They also manage risk during fast markets when spreads widen.

## Practical checklist
- Define the time horizon for Liquidity Provider and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Liquidity Provider as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Liquidity Provider, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Liquidity Provider. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Liquidity Provider alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
