# Fail To Deliver (FTD)

A fail to deliver occurs when a seller does not deliver securities to the buyer by the settlement date. It is a settlement failure that can arise from short sales without a borrow, operational errors, or temporary shortages of shares.

## How it happens
Equity trades typically settle on a fixed cycle, such as T+2. If the seller cannot provide the shares by that date, the trade is marked as a fail. The clearing system records the fail and it remains open until shares are delivered or the position is closed out.

## Common causes
- Short sales executed without a locate or borrow.
- Administrative or processing issues at brokers or custodians.
- Corporate actions, stock lending delays, or transfer restrictions.
- Illiquid securities with scarce borrow supply.

## Regulatory context
In the United States, Regulation SHO sets rules for close outs of fails and defines threshold securities lists. If fails persist, brokers may be required to buy in shares to close the position within a set time frame.

## Monitoring and metrics
Public data often reports aggregate FTD counts. Traders may compute ratios such as FTDs divided by average daily volume or shares outstanding to understand scale.

## Example
A trader sells short 50,000 shares in a thin stock without a proper borrow. On settlement day the shares are unavailable, creating a fail. The broker must locate or buy shares to close the fail, which can raise borrowing costs and price pressure.

## Interpretation risks
FTD data can be noisy and delayed. Fails can reflect operational frictions rather than intent, so it is risky to infer manipulation from a single data point.

## Practical checklist
- Define the time horizon for Fail To Deliver (FTD) and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Fail To Deliver (FTD) as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Fail To Deliver (FTD), confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Fail To Deliver (FTD). Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Fail To Deliver (FTD) alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.

## Practical checklist
- Define the time horizon for Fail To Deliver (FTD) and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.

## Common pitfalls
- Treating Fail To Deliver (FTD) as a standalone signal instead of context.
- Ignoring liquidity, spreads, and execution friction.
- Using a rule on a different timeframe than it was designed for.
- Overfitting a small sample of past examples.
- Assuming the same behavior in abnormal volatility.

## Data and measurement
Good analysis starts with consistent data. For Fail To Deliver (FTD), confirm the data source, the time zone, and the sampling frequency. If the concept depends on settlement or schedule dates, align the calendar with the exchange rules. If it depends on price action, consider using adjusted data to handle corporate actions.

## Risk management notes
Risk control is essential when applying Fail To Deliver (FTD). Define the maximum loss per trade, the total exposure across related positions, and the conditions that invalidate the idea. A plan for fast exits is useful when markets move sharply.

## Variations and related terms
Many traders use Fail To Deliver (FTD) alongside broader concepts such as trend analysis, volatility regimes, and liquidity conditions. Similar tools may exist with different names or slightly different definitions, so clear documentation prevents confusion.

## Practical checklist
- Define the time horizon for Fail To Deliver (FTD) and the market context.
- Identify the data inputs you trust, such as price, volume, or schedule dates.
- Write a clear entry and exit rule before committing capital.
- Size the position so a single error does not damage the account.
- Document the result to improve repeatability.
