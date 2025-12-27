# Bond Carry and Roll-Down

Bond carry and roll-down describe two sources of return in fixed income beyond price changes from yield shifts.

## Carry
Carry is the income earned from holding the bond, typically the coupon yield minus funding costs and hedging expenses.

## Roll-Down
Roll-down is the price gain that occurs when a bond ages and moves down the yield curve, assuming the curve shape is stable. In an upward sloping curve, a bond can gain price as it rolls into lower yields.

## Use in Trading
Traders and portfolio managers use carry and roll-down analysis to identify attractive points on the yield curve and to structure trades that benefit from stable rates.

## Risks
The strategy is exposed to curve shifts, changes in funding rates, and liquidity conditions. A steep curve can flatten quickly, eroding roll-down benefits.

## Return Drivers

Fixed income strategies often decompose returns into carry, roll down, and price changes from yield shifts. Understanding these components helps separate stable income from market risk.

## Curve Risk

Changes in curve level, slope, or curvature can materially affect outcomes. A position that benefits from roll down can lose money if the curve flattens or inverts.

## Implementation Details

Execution depends on liquidity, bid ask spreads, and the ability to finance positions. Many strategies require consistent funding and access to repo or derivatives to manage exposure.

## Hedging and Risk

Duration and convexity should be measured and controlled. Hedging with futures or swaps can reduce unwanted rate exposure, but basis risk remains.

## Pitfalls

Overreliance on historical curve behavior and underestimation of liquidity risk are common pitfalls. Stress testing across multiple rate regimes is important.

## Example Scenario

Consider a liquid instrument with stable spreads and average volatility. A rule based implementation can be tested on a multi year sample and then on an out of sample period. The goal is to verify that the behavior of Bond Carry and Roll-Down is consistent across regimes and that the edge does not depend on a narrow set of conditions.

## Implementation Checklist

- Confirm data quality and consistent timestamps
- Define entry and exit rules in plain language
- Validate position sizing and risk limits
- Track execution costs and slippage
- Review performance by regime and by instrument

## Example Scenario

Consider a liquid instrument with stable spreads and average volatility. A rule based implementation can be tested on a multi year sample and then on an out of sample period. The goal is to verify that the behavior of Bond Carry and Roll-Down is consistent across regimes and that the edge does not depend on a narrow set of conditions.

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

## Checklist

- Define the exact rule in plain language
- Validate data quality and timing
- Quantify execution costs
- Set risk limits and stop logic
- Review performance by regime

## Checklist

- Define the exact rule in plain language
- Validate data quality and timing
- Quantify execution costs
- Set risk limits and stop logic
- Review performance by regime

## Checklist

- Define the exact rule in plain language
- Validate data quality and timing
- Quantify execution costs
- Set risk limits and stop logic
- Review performance by regime
