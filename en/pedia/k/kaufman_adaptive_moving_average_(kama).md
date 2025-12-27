# Kaufman Adaptive Moving Average (KAMA)

The Kaufman Adaptive Moving Average is a moving average that adapts its speed based on market noise. It responds quickly during trends and slows down during sideways markets to reduce whipsaws.

## Core components
- Efficiency Ratio (ER): measures trend strength relative to volatility.
- Smoothing Constant (SC): adapts based on ER.

## Common formula
ER = Change over n periods / Sum of absolute daily changes over n periods
SC = (ER * (FastSC - SlowSC) + SlowSC) ^ 2
KAMA = Prior KAMA + SC * (Price - Prior KAMA)

FastSC is typically 2 / (fast period + 1) and SlowSC is 2 / (slow period + 1).

## Interpretation
When ER is high, KAMA moves closer to price and captures trends. When ER is low, KAMA smooths more and avoids noise.

## Example
A trader uses a 10 period ER with fast 2 and slow 30. During a trend, KAMA hugs price and provides timely signals. During a range, it flattens and reduces false signals.

## Practical notes
KAMA works well as a trend filter when combined with breakouts or momentum signals.

## Practical checklist
- Define the time horizon for Kaufman Adaptive Moving Average (KAMA) and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Kaufman Adaptive Moving Average (KAMA) as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Kaufman Adaptive Moving Average (KAMA), confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Kaufman Adaptive Moving Average (KAMA). Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Kaufman Adaptive Moving Average (KAMA) alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.

## Practical checklist
- Define the time horizon for Kaufman Adaptive Moving Average (KAMA) and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Kaufman Adaptive Moving Average (KAMA) as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Kaufman Adaptive Moving Average (KAMA), confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Kaufman Adaptive Moving Average (KAMA). Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Kaufman Adaptive Moving Average (KAMA) alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.

## Practical checklist
- Define the time horizon for Kaufman Adaptive Moving Average (KAMA) and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Kaufman Adaptive Moving Average (KAMA) as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.
