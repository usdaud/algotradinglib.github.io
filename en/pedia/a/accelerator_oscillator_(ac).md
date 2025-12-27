# Accelerator Oscillator (AC)

The Accelerator Oscillator (AC) is a momentum indicator developed by Bill Williams. It measures the acceleration or deceleration of market momentum by comparing the Awesome Oscillator to its own short-term average. The indicator is displayed as a histogram that oscillates around zero.

## Calculation
AC is derived from the Awesome Oscillator (AO):
- Median Price = (High + Low) / 2
- AO = SMA(Median Price, 5) - SMA(Median Price, 34)
- AC = AO - SMA(AO, 5)

The histogram shows whether the short-term momentum is speeding up or slowing down relative to the recent average of momentum.

## Interpretation
- AC above zero suggests bullish acceleration; below zero suggests bearish acceleration.
- Rising bars indicate increasing momentum; falling bars indicate decreasing momentum.
- The color or direction of the bars is often used for signal confirmation.

## Common Signals
- Zero-line cross: a move from negative to positive suggests strengthening bullish momentum, and the reverse for bearish momentum.
- Consecutive bar shift: two or more bars rising above zero can reinforce trend continuation.
- Divergence: price making a higher high while AC makes a lower high can warn of weakening momentum.

## Practical Use
Traders often use AC as a filter rather than a standalone trigger. It is commonly combined with trend or volatility tools to avoid false signals in choppy markets. It can also be used to time entries on pullbacks when the broader trend is clear.

## Limitations
AC reacts to price changes and can lag during fast reversals. In ranging markets, the histogram can flip frequently and produce whipsaws. It should be interpreted in context with price structure and volatility.

## Inputs and Parameters

Most implementations of Accelerator Oscillator (AC) use a lookback window and one or more smoothing steps. The lookback controls how quickly the indicator reacts; shorter values respond faster but produce more noise. Smoothing can be a simple moving average or another filter, and it should be consistent with the timeframe of the strategy.

When applying Accelerator Oscillator (AC) across different instruments, normalize inputs so the indicator remains comparable. For price based indicators, using median or typical price can reduce distortion from single prints. Volume based indicators require clean volume data and consistent session definitions.

## Signal Construction

Signals are commonly derived from zero line crosses, threshold levels, or the direction of the indicator slope. A cross above zero suggests improving momentum, while a cross below suggests weakening conditions. Divergence between price and the indicator can warn of trend exhaustion.

Many traders require confirmation, such as a close beyond a level or a multi bar condition, to reduce false positives. Multi timeframe checks can improve robustness by aligning short term entries with longer term bias.

## Market Regime Behavior

Accelerator Oscillator (AC) tends to behave differently in trending and ranging markets. In strong trends it can stay above or below its baseline for extended periods, which makes mean reversion signals risky. In ranges it can oscillate frequently and generate whipsaws.

Volatility regime shifts also matter. A sudden increase in volatility can change the amplitude of the indicator, so fixed thresholds may need to be adapted or paired with a volatility filter.

## Practical Use

A common approach is to use Accelerator Oscillator (AC) as a confirmation layer rather than a standalone trigger. For example, a breakout setup can be filtered by requiring the indicator to be positive and rising. In mean reversion systems, the indicator can define the strength of the counter move before entry.

Position sizing can be linked to indicator strength. Stronger readings can justify larger position sizes, while weak readings can be used to scale down or avoid the trade.

## Backtesting Notes

Backtests should use realistic bar construction and avoid look ahead bias when computing indicators. If the indicator uses high and low values, ensure that signals are generated only after the bar closes.

It is also important to evaluate the effect of transaction costs and slippage. Indicators that trigger frequent signals can look good in frictionless tests but degrade in live trading.

## Common Mistakes

Common errors include overfitting the lookback period to a specific sample and ignoring market regime changes. Another mistake is treating the indicator as predictive rather than descriptive. It reflects recent price action and should be interpreted within context.

## Example Scenario

Consider a liquid instrument with stable spreads and average volatility. A rule based implementation can be tested on a multi year sample and then on an out of sample period. The goal is to verify that the behavior of Accelerator Oscillator (AC) is consistent across regimes and that the edge does not depend on a narrow set of conditions.

## Implementation Checklist

- Confirm data quality and consistent timestamps
- Define entry and exit rules in plain language
- Validate position sizing and risk limits
- Track execution costs and slippage
- Review performance by regime and by instrument
