# Statistical Arbitrage

Statistical arbitrage uses statistical models to exploit temporary mispricings across many instruments. It relies on diversification across a large number of small bets rather than a few concentrated positions.

## Core Techniques
Common methods include mean reversion in spreads, factor residual trading, and market neutral portfolios. Signals are often derived from historical relationships and normalized by volatility or liquidity.

## Portfolio Construction
Stat arb strategies typically control exposure to market, sector, and factor risks. Position sizing is scaled to target a stable risk profile. Turnover and transaction costs are critical because profits per trade are often small.

## Risks
Model breakdowns can occur during regime shifts. Liquidity stress can cause rapid drawdowns when many participants exit at once. Operational risk is significant because portfolios are complex and highly automated.

## Conclusion
Statistical arbitrage can produce steady returns when models are robust and costs are controlled. It demands disciplined risk management and continuous monitoring.

## Practical checklist
- Define the time horizon for Statistical Arbitrage and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Statistical Arbitrage as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Statistical Arbitrage, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Statistical Arbitrage. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Statistical Arbitrage alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
