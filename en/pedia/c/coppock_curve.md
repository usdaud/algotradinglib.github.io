# Coppock Curve

The Coppock Curve is a long-term momentum indicator originally designed to identify major market bottoms. It combines rate of change measures and a weighted moving average.

## Formula
Coppock Curve = WMA(ROC(14) + ROC(11), 10)

Lookback periods can vary by implementation.

## Interpretation
- Rising from a low level can signal a long-term buying opportunity
- It is not typically used for short-term trading

## Use Cases
The indicator is commonly applied to broad market indexes to identify cyclical turning points.

## Limitations
Signals are infrequent and can lag. It is best used as a trend confirmation tool rather than a timing mechanism.

## Inputs and Parameters

Most implementations of Coppock Curve use a lookback window and one or more smoothing steps. The lookback controls how quickly the indicator reacts; shorter values respond faster but produce more noise. Smoothing can be a simple moving average or another filter, and it should be consistent with the timeframe of the strategy.

When applying Coppock Curve across different instruments, normalize inputs so the indicator remains comparable. For price based indicators, using median or typical price can reduce distortion from single prints. Volume based indicators require clean volume data and consistent session definitions.

## Signal Construction

Signals are commonly derived from zero line crosses, threshold levels, or the direction of the indicator slope. A cross above zero suggests improving momentum, while a cross below suggests weakening conditions. Divergence between price and the indicator can warn of trend exhaustion.

Many traders require confirmation, such as a close beyond a level or a multi bar condition, to reduce false positives. Multi timeframe checks can improve robustness by aligning short term entries with longer term bias.

## Market Regime Behavior

Coppock Curve tends to behave differently in trending and ranging markets. In strong trends it can stay above or below its baseline for extended periods, which makes mean reversion signals risky. In ranges it can oscillate frequently and generate whipsaws.

Volatility regime shifts also matter. A sudden increase in volatility can change the amplitude of the indicator, so fixed thresholds may need to be adapted or paired with a volatility filter.

## Practical Use

A common approach is to use Coppock Curve as a confirmation layer rather than a standalone trigger. For example, a breakout setup can be filtered by requiring the indicator to be positive and rising. In mean reversion systems, the indicator can define the strength of the counter move before entry.

Position sizing can be linked to indicator strength. Stronger readings can justify larger position sizes, while weak readings can be used to scale down or avoid the trade.

## Backtesting Notes

Backtests should use realistic bar construction and avoid look ahead bias when computing indicators. If the indicator uses high and low values, ensure that signals are generated only after the bar closes.

It is also important to evaluate the effect of transaction costs and slippage. Indicators that trigger frequent signals can look good in frictionless tests but degrade in live trading.

## Common Mistakes

Common errors include overfitting the lookback period to a specific sample and ignoring market regime changes. Another mistake is treating the indicator as predictive rather than descriptive. It reflects recent price action and should be interpreted within context.

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
