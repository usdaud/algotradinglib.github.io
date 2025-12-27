# All-Time Low (ATL)

An all-time low is the lowest price a security has reached in its recorded trading history. It can indicate extreme weakness or distress and is often monitored for breakdown strategies.

## Significance
An ATL suggests sustained selling pressure and a lack of historical support below the current price. It can also signal capitulation, after which reversals sometimes occur.

## Use in Trading
- Breakdown strategies may sell short on new ATL levels, using tight risk controls.
- Mean reversion traders watch for exhaustion signals near ATL for potential bounces.
- Risk managers track ATL levels to assess downside exposure.

## Data Considerations
Like ATHs, ATL values depend on whether prices are adjusted for corporate actions. Comparing across data sources without adjustment can be misleading.

## Limitations
ATL breakouts can be driven by temporary shocks, liquidity gaps, or market-wide events. It is risky to interpret ATLs without considering fundamentals, liquidity, and broader market context.

## Why Levels Matter

All time levels attract attention because there is no recent reference beyond them. This can concentrate order flow and create momentum once the level is breached. It can also trigger risk management actions such as stop orders and rebalancing.

## Breakout Mechanics

A valid break is often defined by a close beyond the level and evidence of participation, such as expanded volume or a strong range. Some traders wait for a retest to avoid false breaks.

Stops are commonly placed on the other side of the level or below the breakout bar, depending on the timeframe.

## Retest and Failure

After a breakout, price may retest the level. A successful retest can confirm support or resistance. A quick reversal back below the level is a common failure sign.

Failures can lead to sharp moves in the opposite direction as trapped traders exit.

## Data Adjustments

Corporate actions such as splits or large dividends can change historical highs or lows. Use adjusted data when evaluating long term levels, and keep the data source consistent across analysis.

## Risk Management

Because the market is in price discovery, volatility can expand. Position sizing should reflect the wider range and potential gaps. Partial profits and trailing stops can reduce exposure.

## Example Scenario

Consider a liquid instrument with stable spreads and average volatility. A rule based implementation can be tested on a multi year sample and then on an out of sample period. The goal is to verify that the behavior of All-Time Low (ATL) is consistent across regimes and that the edge does not depend on a narrow set of conditions.

## Implementation Checklist

- Confirm data quality and consistent timestamps
- Define entry and exit rules in plain language
- Validate position sizing and risk limits
- Track execution costs and slippage
- Review performance by regime and by instrument

## Example Scenario

Consider a liquid instrument with stable spreads and average volatility. A rule based implementation can be tested on a multi year sample and then on an out of sample period. The goal is to verify that the behavior of All-Time Low (ATL) is consistent across regimes and that the edge does not depend on a narrow set of conditions.

## Implementation Checklist

- Confirm data quality and consistent timestamps
- Define entry and exit rules in plain language
- Validate position sizing and risk limits
- Track execution costs and slippage
- Review performance by regime and by instrument

## Operational Notes

Definitions and conventions should be consistent across datasets and venues. A small difference in data fields or session boundaries can change outcomes, especially for short term strategies. Document inputs and assumptions so results can be reproduced.

If the concept depends on exchange rules or broker behavior, confirm those rules for the specific venue. Operational details often explain why a trade behaved differently than expected.

## Stress Scenarios

During volatility spikes, liquidity can evaporate and price gaps can appear. Under these conditions, indicators can lag, order types can misfire, and spreads can widen sharply.

Stress testing the concept against fast markets, thin liquidity, and sudden news helps reveal hidden risks. If a strategy only works in calm conditions, size and timing should reflect that.

## Documentation Tips

Keep a short checklist of the rules, parameters, and decision points. Record how the concept is used in live trading and compare it to backtest assumptions. This makes future refinement easier and reduces drift in execution.

## Common Questions

Traders often ask how sensitive results are to parameter choices, how the concept behaves in different regimes, and whether it scales with size. Answering these questions early improves reliability and prevents overfitting.

## Checklist

- Define the exact rule in plain language
- Validate data quality and timing
- Quantify execution costs
- Set risk limits and stop logic
- Review performance by regime
