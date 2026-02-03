# Underperformance

Underperformance occurs when a portfolio or strategy returns less than a benchmark or target. It can be temporary or structural depending on the cause.

## Measurement
Underperformance is measured by comparing total return or risk adjusted return to a benchmark. Tracking error and relative drawdown can provide additional context. The time horizon matters because short term underperformance can be normal for some strategies.

## Common Causes
Causes include exposure mismatch, market regime changes, rising transaction costs, and model drift. Operational issues such as execution problems or data errors can also contribute. Identifying the cause is essential before making changes.

## Response Framework
A structured review should examine signal quality, risk exposures, and execution costs. If the strategy logic is sound but the regime has changed, position sizing or timing adjustments may help. If the underperformance is structural, the strategy should be redesigned or retired.

## Conclusion
Underperformance is a normal part of trading, but persistent underperformance requires disciplined investigation and action.

## Practical checklist
- Define the time horizon for Underperformance and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Underperformance as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Underperformance, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Underperformance. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Underperformance alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
