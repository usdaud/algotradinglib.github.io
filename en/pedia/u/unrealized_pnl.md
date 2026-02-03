# Unrealized PnL

Unrealized PnL is the profit or loss on open positions based on current market prices. It represents the current mark to market value of the portfolio.

## Calculation
Unrealized PnL is calculated by comparing the current price of each position to its entry price and multiplying by position size. For derivatives, contract size and currency conversion may apply. Accurate pricing feeds are essential.

## Why It Matters
Unrealized PnL provides a real time view of risk and exposure. It informs margin usage, risk limits, and stress testing. Sudden changes in unrealized PnL can signal market regime shifts or data issues.

## Risks and Pitfalls
Illiquid instruments can produce misleading marks. Pricing errors or stale quotes can distort PnL. Rapid market moves can cause large swings that require immediate risk actions.

## Conclusion
Unrealized PnL is a critical operational metric. It should be monitored continuously and reconciled with realized results over time.

## Practical checklist
- Define the time horizon for Unrealized PnL and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Unrealized PnL as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Unrealized PnL, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Unrealized PnL. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Unrealized PnL alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
