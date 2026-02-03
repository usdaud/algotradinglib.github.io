# Effective Spread

Effective spread measures the actual trading cost by comparing the execution price to the midpoint of the bid ask spread at the time of the trade. It captures price improvement or price impact relative to the quoted spread.

## Formula
Effective Spread = 2 * |Execution Price - Midpoint|

It is often expressed in price terms or basis points.

## Interpretation
- Lower effective spread indicates better execution quality
- Higher values can indicate slippage or market impact

## Use in Trading
Traders and brokers use effective spread to evaluate execution algorithms, routing quality, and venue performance.

## Limitations
Accurate measurement requires precise timestamps for quotes and trades. In fast markets, midpoints can change quickly, which can distort the metric.

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
