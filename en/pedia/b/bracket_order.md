# Bracket Order

A bracket order is an entry order paired with a take profit and a stop loss order. It allows traders to define risk and reward at the moment of entry.

## How It Works
A bracket order consists of three linked orders. The entry order opens the position. A profit target order and a stop loss order are placed around the entry price. When one exit order fills, the other is canceled automatically.

## Use Cases
Bracket orders are useful for strategies with predefined risk limits. They automate exit logic in fast markets and reduce the need for constant monitoring. They also enforce discipline by preventing impulsive changes during volatile conditions.

## Practical Considerations
Not all venues support bracket order logic directly, so the functionality may be implemented by the broker. Partial fills on the entry can lead to mismatched exit sizes if not handled carefully. Gap risk can still cause losses beyond the stop price.

## Conclusion
Bracket orders help standardize trade management, but they are only effective when combined with sound entry logic and realistic expectations about execution.
