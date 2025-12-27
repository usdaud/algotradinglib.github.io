# Algorithmic Trading Backtesting

Backtesting simulates a trading strategy on historical data to estimate performance before capital is deployed. A good backtest focuses on realism, repeatability, and robustness rather than only on headline returns.

## Data Preparation
High quality data is the foundation of any backtest. Prices must be correctly adjusted for corporate actions, and symbols should be mapped through ticker changes. Survivorship bias must be removed when using index or universe data. Timestamp accuracy matters when evaluating intraday strategies.

## Simulation Mechanics
A backtest should model how orders would have executed in the market. That includes bid-ask spreads, commissions, slippage, and partial fills. The fill model should reflect the order type, trade size, and liquidity conditions. Without this, the results may be overly optimistic.

## Performance Metrics
Key metrics include return, volatility, drawdown, Sharpe ratio, profit factor, win rate, and turnover. Evaluate stability across different time windows rather than only the full sample period. A strategy that performs only in one regime is fragile.

## Common Sources of Bias
Look-ahead bias occurs when future information leaks into the signal or execution logic. Data snooping happens when parameters are repeatedly tuned until the backtest looks good. Both lead to inflated expectations and poor live performance.

## Validation and Robustness
Out-of-sample testing, walk-forward analysis, and stress scenarios provide stronger evidence of robustness. A strategy should be tested across multiple market regimes, including calm and volatile periods. Small changes in parameters should not cause large changes in performance.

## Conclusion
Backtesting is essential but not sufficient. The goal is to validate a strategy under realistic assumptions and to understand where it is likely to fail before real capital is at risk.
