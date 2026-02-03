# Post-Only Order

A post-only order is designed to add liquidity to the order book. If the order would execute immediately, it is canceled or rejected instead of taking liquidity.

## Behavior
Post-only orders rest on the book at the specified price. They ensure the trader receives maker pricing and avoids paying taker fees. The order may be canceled if the market moves through the price level.

## Use Cases
Post-only orders are common in market making and passive execution. They help control costs by avoiding taker fees and reducing immediate market impact. They can also improve queue position in stable markets.

## Risks and Limitations
Because post-only orders never cross the spread, they can miss fills in fast markets. Adverse selection is possible when prices move through the order. Some venues have specific rules about how post-only orders are handled.

## Conclusion
Post-only orders are useful for passive trading but require careful placement and monitoring to avoid missed opportunities.

## Practical checklist
- Define the time horizon for Post-Only Order and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Post-Only Order as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Post-Only Order, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Post-Only Order. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Post-Only Order alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
