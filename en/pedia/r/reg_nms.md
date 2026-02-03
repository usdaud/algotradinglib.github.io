# Reg NMS

Reg NMS is a set of US rules that govern equity market structure and order handling. It aims to promote fair access, price transparency, and competition among trading venues.

## Key Rules
The Order Protection Rule prevents trade throughs by requiring execution at the best displayed price. The Access Rule addresses fair access to quotes and caps certain fees. The Sub Penny Rule limits quoting in extremely small price increments.

## Impact on Trading
Reg NMS influences routing decisions, order types, and venue selection. Execution systems must consider best prices across venues and maintain audit trails for routing logic. Compliance requirements often shape algorithm design.

## Operational Considerations
Firms need monitoring to ensure compliance with trade through requirements. Changes in market structure or venue behavior can alter routing performance. Regulatory updates should be incorporated into execution logic promptly.

## Conclusion
Understanding Reg NMS is essential for trading US equities. It defines the rules that shape execution quality and venue competition.

## Practical checklist
- Define the time horizon for Reg NMS and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Reg NMS as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Reg NMS, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Reg NMS. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Reg NMS alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
