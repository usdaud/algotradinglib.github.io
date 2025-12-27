# Debit Spread

A debit spread is an options strategy that involves buying one option and selling another with the same expiration but a different strike, resulting in a net cost to enter the trade.

## Structure
- Buy an option at a more expensive strike
- Sell an option at a cheaper strike
- Net result is a debit paid upfront

## Payoff Profile
- Maximum loss is the premium paid
- Maximum profit is the strike difference minus the premium
- Breakeven is based on the long strike plus or minus the premium, depending on calls or puts

## Greeks
Debit spreads are typically net long delta and gamma, and net short theta, but the exact exposure depends on strikes and expiration. Vega can be positive or negative depending on the spread width and moneyness.

## Use Cases
Debit spreads are used to take directional views with defined risk. They are common when traders expect a moderate move but want to reduce cost versus buying a single option.

## Volatility Sensitivity
Implied volatility changes can materially affect the spread value. A volatility drop after entry can reduce profits even if the price moves in the expected direction.

## Adjustment Ideas
If the underlying moves favorably, traders may roll the short strike to capture additional profit. If the move stalls, some traders close the spread to reduce time decay exposure.

## Risks
Time decay works against the position, especially if the underlying stalls. Implied volatility drops can also reduce the spread value.

## Implementation Notes
Before entry, model the payoff across a range of prices. This helps identify where the strategy is most sensitive and whether the risk is acceptable.

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
