# Partial Fill

A partial fill occurs when only part of an order is executed. The remaining quantity stays open unless canceled or replaced.

## Common Causes
Partial fills happen when available liquidity at the order price is limited or when order size exceeds visible depth. They are common in fast markets and in less liquid instruments. Hidden liquidity and order priority rules can also affect fill outcomes.

## Handling Partial Fills
Trading systems must track filled and remaining quantities accurately. Strategies may need to adjust exposure, update hedge ratios, or place follow up orders. Some systems automatically replace the remaining portion to improve fill probability.

## Risks
Partial fills can create unintended exposure, especially in multi leg trades. They can also increase execution costs if the remainder fills at worse prices. Proper monitoring and contingency logic are essential.

## Conclusion
Partial fills are a normal part of trading. Systems should handle them explicitly to avoid execution errors and risk drift.

## Practical checklist
- Define the time horizon for Partial Fill and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Partial Fill as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Partial Fill, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Partial Fill. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Partial Fill alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
