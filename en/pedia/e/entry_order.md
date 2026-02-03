# Entry Order

An entry order is any order used to open a new position. It can be market, limit, stop, or conditional depending on the strategy and desired execution behavior.

## Types of Entry Orders
- Market order: immediate execution at current prices
- Limit order: execution at a specified price or better
- Stop order: triggers when price reaches a level
- Stop limit: combines stop trigger with a limit price

## Choosing an Entry Method
The choice depends on urgency, liquidity, and risk tolerance. Market orders guarantee execution but can incur slippage. Limit orders control price but may not fill.

## Risk Controls
Entry orders should be aligned with position sizing and stop placement. Many traders define the stop level before entry to ensure risk is acceptable.

## Practical Notes
Avoid using entry orders during illiquid periods or around high impact news unless the strategy explicitly targets those conditions.

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
