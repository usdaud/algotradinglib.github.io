# Daily Bar

A daily bar summarizes a full trading session into a single open, high, low, and close value. It is a common unit for analysis because it smooths intraday noise while preserving key price information.

## Components
- Open: first traded price of the session
- High: highest price reached during the session
- Low: lowest price reached during the session
- Close: last traded price of the session

## Why It Matters
Daily bars are used to define trends, calculate indicators, and evaluate price patterns. Many institutional strategies and risk models are built on daily data because it is consistent and widely available.

## Common Uses
- Trend identification using moving averages or breakouts
- Risk estimation using daily volatility
- Pattern analysis such as candlestick formations

## Data Considerations
Daily bars can differ across data vendors due to session definitions, time zones, and holiday schedules. For global assets, the trading day may not align with calendar days, so consistent session boundaries are critical.

## Intraday Context
A single bar can represent very different intraday paths. Two sessions with the same OHLC can have different volatility or trend behavior. Strategies that depend on intraday momentum should validate the daily signal with higher frequency data.

## Relationship to Indicators
Many indicators, such as moving averages, RSI, and ATR, are computed on daily bars. The indicator behavior depends on how gaps and session boundaries are treated. A consistent data pipeline is essential to avoid mismatched signals.

## Backtesting Notes
Signals should be generated after the daily close to avoid look ahead bias. If a strategy assumes execution at the close, the backtest should model closing auction liquidity and slippage.

## Limitations
Daily bars hide intraday path information. Large intraday swings can occur without being visible in a single bar, so strategies that depend on intraday behavior need higher frequency data.

## Practical Notes
If a strategy uses daily bars, ensure that signals are generated after the close to avoid look ahead bias. For markets that trade nearly 24 hours, define a cut off time and stick to it.

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
