# Data Snooping

Data snooping is the practice of repeatedly searching historical data for patterns until something appears significant. This can produce strategies that look strong in backtests but fail in live trading.

## Why It Happens
Researchers often test many ideas, tweak parameters, and select the best result. Without proper controls, random noise can masquerade as predictive signal. The more tests performed, the higher the chance of false discoveries.

## Consequences
Data snooping inflates performance estimates and increases the risk of deploying fragile strategies. It leads to overconfidence and underestimation of risk. In production, these strategies often decay quickly.

## Mitigation Techniques
Use holdout datasets and strict train test splits. Apply walk-forward testing and limit the number of parameter variations. Use statistical corrections for multiple testing and favor simpler models with clear economic rationale.

## Conclusion
Avoiding data snooping is essential for building strategies that survive real markets. Discipline in research is as important as creativity.
