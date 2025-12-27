# All or None Order (AON)

An All or None (AON) order is an order that must be filled entirely or not at all. It prevents partial fills by requiring the full quantity to be executed in one match.

## How It Works
If the market cannot fill the entire size immediately, the order remains open until a matching order appears or the order is canceled. AON orders can be combined with limit prices.

## Use Cases
AON orders are used when the trader requires a specific position size and wants to avoid partial execution. This can be important for strategies that need a full hedge or when partial fills create operational complexity.

## Trade-Offs
AON orders can reduce execution probability and may result in missed opportunities, especially in thin markets. They can also experience longer waiting times and may not display in some market data feeds.

## Practical Notes
AON functionality varies by venue and broker. Some venues handle AON orders off-book or with special priority rules. Traders should verify how their platform handles visibility and execution priority.

## Execution Mechanics

Orders are prioritized by price and time, so where an order sits in the book matters. Some order types trigger additional logic, such as converting a stop to a market or limit order when a trigger price is reached.

Partial fills are common in fragmented markets. Systems should handle partial execution, update remaining quantity, and avoid duplicate or conflicting orders.

## Liquidity and Slippage

The bid ask spread and displayed depth determine the immediate cost of execution. Aggressive orders pay the spread but reduce the risk of missing the move, while passive orders reduce costs but may not fill.

Slippage increases during volatility spikes and around news events. Using price limits and time in force constraints can reduce unexpected fills.

## When to Use

This order type is most useful when execution quality or timing is more important than immediate fill. It can be combined with time windows, participation limits, or price caps to control the trade off between urgency and cost.

## Monitoring and Controls

Live orders should be monitored for stale prices, partial fills, and changes in market conditions. Automated controls like maximum order size, price bands, and kill switches reduce operational risk.

Post trade review is important. Comparing execution to mid price or a benchmark helps detect routing or logic issues.

## Failure Modes

Common failures include missing fills due to price gaps, excessive queue position leading to no execution, and accidental aggressive fills due to incorrect limits. Validation and guardrails should catch these before orders hit the market.

## Example Workflow

A typical workflow is: compute desired size, choose order type, set price and time constraints, submit order, monitor fills, and adjust or cancel if conditions change. This keeps the execution aligned with the original intent.

## Example Scenario

Consider a liquid instrument with stable spreads and average volatility. A rule based implementation can be tested on a multi year sample and then on an out of sample period. The goal is to verify that the behavior of All or None Order (AON) is consistent across regimes and that the edge does not depend on a narrow set of conditions.

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
