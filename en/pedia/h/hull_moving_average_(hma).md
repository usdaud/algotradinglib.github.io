# Hull Moving Average (HMA)

The hull moving average is a fast and smooth moving average designed to reduce lag. It uses weighted moving averages and a square root period to respond quickly while keeping the line smooth.

## Formula
HMA = WMA(2 * WMA(n/2) - WMA(n), sqrt(n))

Where WMA is a weighted moving average and n is the period length.

## Interpretation
- The HMA changes direction quickly, which helps spot trend shifts.
- A rising HMA suggests upward momentum, while a falling HMA suggests downward momentum.
- Crosses of price and HMA can be used as simple signals.

## Example
A trader uses a 55 period HMA on a daily chart. When the HMA turns up after a pullback, the trader interprets it as a trend resumption signal.

## Practical notes
The HMA can be sensitive in choppy markets. Many traders pair it with higher timeframe trend context.

## Practical checklist
- Define the time horizon for Hull Moving Average (HMA) and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Hull Moving Average (HMA) as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Hull Moving Average (HMA), confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Hull Moving Average (HMA). Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Hull Moving Average (HMA) alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.

## Practical checklist
- Define the time horizon for Hull Moving Average (HMA) and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Hull Moving Average (HMA) as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Hull Moving Average (HMA), confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Hull Moving Average (HMA). Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Hull Moving Average (HMA) alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.

## Practical checklist
- Define the time horizon for Hull Moving Average (HMA) and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Hull Moving Average (HMA) as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Hull Moving Average (HMA), confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.
