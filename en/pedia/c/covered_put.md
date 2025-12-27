# Covered Put

A covered put is an options strategy that combines a short stock position with a short put option on the same stock. It is the mirror image of a covered call.

## Structure
- Short the underlying stock
- Sell a put option at a chosen strike

## Payoff Profile
- Limited upside if the stock falls
- Premium income from the sold put
- Large losses if the stock rises sharply

## Use Cases
Covered puts are used when a trader has a bearish outlook and wants to generate premium income. It can also be used as an alternative to a short call position.

## Risks
The strategy has significant risk if the stock rises. The short put adds additional downside risk if the stock falls significantly beyond the strike.

## Position Greeks

Options spreads and multi leg structures have combined exposures to delta, gamma, theta, and vega. Long options add positive gamma and vega but negative theta, while short options do the opposite. The net Greek profile can change rapidly as price moves or time passes.

Before entry, check how the position behaves for small moves and for large moves. A position that looks balanced at entry can become highly directional if the underlying approaches a short strike.

## Break Even and Payoff

Define K1, K2, and K3 as the relevant strikes and P as the net premium paid (positive for debit, negative for credit). For a simple vertical, max profit is the strike width minus P, and max loss is P. For ratio or butterfly structures, break even points depend on the strike distances and premium.

A quick way to verify payoff is to evaluate the position at expiration for regions below the lowest strike, between strikes, and above the highest strike. This avoids surprises when the trade is stressed.

## Volatility and Time

Implied volatility changes can materially affect the value of a spread. Long dated options usually carry more vega, so calendar and diagonal structures are sensitive to volatility shifts. Time decay generally helps positions that are net short options and hurts positions that are net long.

Event risk can dominate normal time decay. Earnings or macro releases can cause large moves and implied volatility spikes, so holding spreads through events should be deliberate.

## Adjustments

Common adjustments include rolling the short strike, closing part of the position, or converting to a different structure. For example, a vertical that moves in the money can be rolled up to harvest intrinsic value while keeping risk defined.

Adjustments should be planned before entry. If the only acceptable action is to hold to expiration, the risk profile must be acceptable in all price scenarios.

## Assignment and Exercise

Short options can be assigned early, especially when they are deep in the money and have little time value. Dividend dates and interest rates can increase assignment risk for calls.

Traders should monitor early exercise risk and understand the broker rules for assignment. Having a plan for unexpected assignment helps avoid forced liquidations.

## Risk Management

Define max loss in cash terms and size the trade accordingly. Avoid concentrating too many trades in correlated underlyings or the same expiration. Track the effect of a volatility shock and a gap move to ensure the position remains within risk limits.

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
