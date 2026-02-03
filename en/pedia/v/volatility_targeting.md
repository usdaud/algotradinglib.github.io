# Volatility Targeting

Volatility targeting is a portfolio approach that adjusts position size to maintain a target level of volatility. When volatility rises, exposure is reduced. When volatility falls, exposure is increased.

## How it works
- Estimate current or expected volatility.
- Choose a target volatility level.
- Scale position size so expected volatility matches the target.

## Example
A strategy targets 10 percent annualized volatility. If realized volatility rises to 20 percent, exposure is cut in half. If volatility drops to 5 percent, exposure is doubled.

## Benefits and risks
Volatility targeting can smooth risk but can also force selling into declining markets and buying into rising markets. It can amplify trend moves if volatility remains low.

## Practical notes
The choice of volatility measure and lookback window has a large impact on behavior.

## Practical checklist
- Define the time horizon for Volatility Targeting and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Volatility Targeting as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Volatility Targeting, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Volatility Targeting. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Volatility Targeting alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
