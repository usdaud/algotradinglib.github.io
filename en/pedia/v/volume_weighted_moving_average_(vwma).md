# Volume Weighted Moving Average (VWMA)

The volume weighted moving average is a moving average that weights prices by volume. It gives more influence to periods with higher volume, reflecting stronger participation.

## Formula
VWMA = Sum(Price * Volume) / Sum(Volume) over the lookback period

## Interpretation
- If price is above VWMA, momentum may be bullish.
- If price is below VWMA, momentum may be bearish.

## Example
A trader uses a 20 period VWMA to confirm trend strength. Price holding above VWMA with rising volume suggests sustained demand.

## Practical notes
VWMA is often compared to a simple moving average to gauge the effect of volume weighting.

## Practical checklist
- Define the time horizon for Volume Weighted Moving Average (VWMA) and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Volume Weighted Moving Average (VWMA) as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Volume Weighted Moving Average (VWMA), confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Volume Weighted Moving Average (VWMA). Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Volume Weighted Moving Average (VWMA) alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
