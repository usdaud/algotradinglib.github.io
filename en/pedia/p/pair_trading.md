# Pair Trading

Pair trading is a market neutral strategy that trades two related instruments based on their price relationship. The strategy aims to profit when the spread between the two instruments reverts to its historical mean.

## Selection and Modeling
Pairs are selected based on economic similarity or statistical tests. Traders often use correlation and cointegration to identify stable relationships. A spread or ratio is defined as the primary signal.

## Trading Logic
When the spread widens beyond a threshold, the strategy goes long the undervalued asset and short the overvalued one. Positions are closed when the spread reverts or if the relationship breaks down. Hedge ratios are used to balance exposure.

## Risk Management
Relationships can change due to structural shifts or corporate events. Liquidity differences between the legs can cause execution risk. Stop rules and maximum holding periods help manage tail risk.

## Conclusion
Pair trading reduces market direction exposure but depends on the stability of the relationship. Ongoing monitoring is required to keep the strategy viable.

## Practical checklist
- Define the time horizon for Pair Trading and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Pair Trading as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Pair Trading, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Pair Trading. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Pair Trading alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.
