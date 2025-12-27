# Avellaneda-Stoikov Model

The Avellaneda-Stoikov model is a market making framework that determines optimal bid and ask quotes based on inventory risk, volatility, and order arrival dynamics. It balances expected profit from the spread against the risk of holding inventory.

## Core Idea
A market maker sets quotes around a reservation price that shifts with inventory. As inventory grows, quotes are adjusted to encourage trades that reduce risk.

## Key Equations
A common formulation is:
- Reservation price: r = mid - inventory * gamma * sigma^2 * (T - t)
- Optimal spread: s = gamma * sigma^2 * (T - t) + (2 / gamma) * ln(1 + gamma / k)

Where:
- mid is the mid price
- inventory is current position
- gamma is risk aversion
- sigma is volatility
- T - t is time horizon
- k is the order arrival parameter

## Practical Use
The model provides a structured way to quote tighter spreads when risk is low and widen spreads when inventory risk or volatility increases. It is widely used in high frequency and electronic market making research.

## Assumptions and Limitations
The model assumes a specific order arrival process and constant volatility, which may not hold in real markets. It also requires reliable parameter estimation and fast execution to be effective.

## Model Intuition

The model balances expected spread capture against inventory risk. When inventory grows, the reservation price shifts so quotes are skewed to attract trades that reduce the position.

This creates a feedback loop that stabilizes inventory while still providing liquidity.

## Parameter Estimation

Key parameters include volatility, order arrival intensity, and risk aversion. Volatility can be estimated from recent returns, while order arrival rates can be estimated from historical quote and trade data.

Parameter estimates should be updated regularly because microstructure conditions change quickly.

## Inventory Control

Inventory is the primary risk. Limits are often applied so the model reduces quoting or widens spreads when inventory approaches a threshold. Some implementations also hedge inventory with correlated instruments.

## Implementation Outline

A simplified flow is: compute mid price, estimate volatility, compute reservation price, compute optimal spread, set bid and ask quotes, update on each market event.

Latency matters because stale quotes can be picked off. Fast updates and cancellation logic are essential.

## Limitations and Stress Tests

The model assumes stable market conditions and a specific order arrival process. In fast markets, order flow can change and quotes may be too aggressive. Stress tests should include volatility spikes and one sided order flow.

## Example Scenario

Consider a liquid instrument with stable spreads and average volatility. A rule based implementation can be tested on a multi year sample and then on an out of sample period. The goal is to verify that the behavior of Avellaneda-Stoikov Model is consistent across regimes and that the edge does not depend on a narrow set of conditions.

## Implementation Checklist

- Confirm data quality and consistent timestamps
- Define entry and exit rules in plain language
- Validate position sizing and risk limits
- Track execution costs and slippage
- Review performance by regime and by instrument

## Example Scenario

Consider a liquid instrument with stable spreads and average volatility. A rule based implementation can be tested on a multi year sample and then on an out of sample period. The goal is to verify that the behavior of Avellaneda-Stoikov Model is consistent across regimes and that the edge does not depend on a narrow set of conditions.

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
