# XIRR

XIRR is the internal rate of return for irregular cash flows. It solves for the discount rate that makes the net present value of all cash flows equal to zero.

## How It Works
XIRR uses the timing and size of each cash flow to estimate a single annualized return. It requires an iterative solver because there is no closed form solution. The result is sensitive to the timing of large deposits or withdrawals.

## Use Cases
XIRR is useful for portfolios with deposits, withdrawals, or uneven cash flow timing. It provides a more realistic performance measure than simple holding period return when cash flows are irregular.

## Limitations
XIRR can be misleading if cash flows are large and frequent or if the underlying asset values are volatile. Different cash flow assumptions can produce different results. It should be considered alongside time weighted metrics.

## Conclusion
XIRR is a practical tool for real world performance measurement. It is most informative when interpreted with awareness of cash flow timing effects.

## Practical checklist
- Define the time horizon for XIRR and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating XIRR as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For XIRR, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying XIRR. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use XIRR alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.

## Practical checklist
- Define the time horizon for XIRR and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating XIRR as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For XIRR, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying XIRR. Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use XIRR alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.

## Practical checklist
- Define the time horizon for XIRR and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating XIRR as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For XIRR, confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.
