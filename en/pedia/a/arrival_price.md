# Arrival Price

Arrival price is the benchmark price at the moment a trade decision is made. It is used to measure the cost of execution relative to the price that was available when the order was released. For a buy order, execution above arrival price is a cost. For a sell order, execution below arrival price is a cost.

## Why It Matters
Arrival price connects strategy decisions to execution reality. It helps separate signal quality from trading costs and allows traders to compare different execution methods. Many transaction cost analysis reports use arrival price as the primary benchmark.

## Calculation
Arrival price is usually the mid price, last price, or a quote snapshot at decision time. The implementation shortfall metric compares the final average execution price to arrival price. Costs can be expressed in absolute terms, basis points, or as a percentage of notional value.

## Practical Use
Traders track arrival price to evaluate brokers, algorithms, and routing rules. It is also used to set expectations for slippage and to decide when to use passive versus aggressive execution. Consistent measurement across strategies makes comparisons meaningful.

## Limitations
The choice of arrival price matters. A stale quote or a low liquidity market can distort the benchmark. In fast markets, the difference between signal time and order release time can be large, so controls should record both timestamps.

## Conclusion
Arrival price is a simple but powerful benchmark for execution quality. It links trading decisions to realized costs and supports disciplined performance analysis.
