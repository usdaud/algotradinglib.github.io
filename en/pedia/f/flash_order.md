# Flash Order

A flash order is a short term order display mechanism in which an order is shown to select market participants for a brief time before being routed to the broader market. The goal was to find a matching counterparty quickly, often within milliseconds.

## How it worked
When an order arrived at a venue, it could be flashed to a subset of participants. If someone filled the order quickly, the trade executed without routing elsewhere. If not, the order continued to the wider market.

## Controversy
Critics argued that flash orders created information advantages for certain participants and reduced fairness. The practice drew regulatory scrutiny and many venues removed flash functionality.

## Example
A buy order is received by an exchange and flashed to a select group of liquidity providers for a short time. One provider fills the order, so it never reaches the public order book.

## Current status
Flash orders are far less common today due to changes in market rules and industry preferences.

## Practical checklist
- Define the time horizon for Flash Order and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Flash Order as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Flash Order, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Flash Order. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Flash Order alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
