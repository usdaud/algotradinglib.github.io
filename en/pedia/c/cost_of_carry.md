# Cost of Carry

Cost of carry is the net cost of holding an asset over time. It is used to relate spot prices to futures prices and includes financing, storage, and income from the asset.

## Formula
For a basic model:
F = S * e^{(r + c - y) * T}

Where:
- F is futures price
- S is spot price
- r is funding rate
- c is carrying costs (storage, insurance)
- y is yield or income
- T is time to expiration

## Trading Use
Cost of carry models help identify when futures are rich or cheap relative to spot. This supports arbitrage and hedging strategies.

## Limitations
Real markets include frictions, credit constraints, and liquidity effects that can cause persistent deviations from theoretical prices.

## Computation Details

Compute the metric on consistent sampling intervals. If the input uses prices, decide whether to use close, typical, or average prices. If the input uses returns, document the return type and whether log or simple returns are used.

When the metric is annualized, use a consistent period count, such as 252 for trading days. The result should be comparable across instruments only if the same conventions are used.

## Interpretation

Metrics provide a summary of behavior rather than a full distribution. High values can indicate opportunity or risk depending on the context. It is helpful to compare the current value to its own history rather than rely on a fixed threshold.

## Applications

Metrics support position sizing, risk limits, and performance evaluation. They also help identify regime changes when the metric shifts outside its normal range.

Combining the metric with trend or liquidity indicators can reduce false signals.

## Pitfalls and Data Issues

Common pitfalls include using data with gaps, mixing adjusted and unadjusted prices, or using too short a window. For thinly traded assets, the metric can be distorted by outliers.

## Example Scenario

Consider a liquid instrument with stable spreads and average volatility. A rule based implementation can be tested on a multi year sample and then on an out of sample period. The goal is to verify that the behavior of Cost of Carry is consistent across regimes and that the edge does not depend on a narrow set of conditions.

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
