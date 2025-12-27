# IV Rank

IV rank measures where current implied volatility sits between the highest and lowest IV over a lookback period. It expresses current IV as a position within the range, not the distribution.

## Formula
IV Rank = (Current IV - IV Low) / (IV High - IV Low) * 100

## Interpretation
- A value near 100 means IV is near its high for the period.
- A value near 0 means IV is near its low for the period.

## Example
If IV high is 60, IV low is 20, and current IV is 35, then IV rank is (35 - 20) / (60 - 20) * 100 = 37.5.

## Practical use
IV rank helps compare current option pricing to recent extremes and is often used with IV percentile for context.

## Practical checklist
- Define the time horizon for IV Rank and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating IV Rank as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For IV Rank, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying IV Rank. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use IV Rank alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.

## Practical checklist
- Define the time horizon for IV Rank and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating IV Rank as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For IV Rank, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying IV Rank. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use IV Rank alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.

## Practical checklist
- Define the time horizon for IV Rank and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating IV Rank as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For IV Rank, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying IV Rank. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use IV Rank alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
