# Advance-Decline Ratio (AD Ratio)

The Advance-Decline Ratio is a market breadth indicator that compares the number of advancing stocks to the number of declining stocks within a market or index. It helps assess the internal strength or weakness of a market move.

## Calculation
AD Ratio = Advancing Issues / Declining Issues

Some variants use a moving average or convert the ratio into a percentage. When declines are zero, the ratio is undefined, so many platforms cap or smooth the value to avoid distortions.

## Interpretation
- A ratio above 1 indicates more advancers than decliners, signaling broad participation.
- A ratio below 1 indicates more decliners than advancers, signaling broad weakness.
- Extreme readings can indicate overbought or oversold conditions depending on context.

## Use in Trading
AD Ratio is commonly used to confirm trends. A rising market with a rising AD Ratio suggests healthy participation. If price rises while the ratio weakens, the move may be narrowing and vulnerable to reversal.

## Limitations
Breadth indicators can be noisy, especially in markets with sector concentration. Index weighting can also obscure breadth signals if a few large stocks dominate price action. It is best used alongside price trend and volume data.

## Inputs and Parameters

Most implementations of Advance-Decline Ratio (AD Ratio) use a lookback window and one or more smoothing steps. The lookback controls how quickly the indicator reacts; shorter values respond faster but produce more noise. Smoothing can be a simple moving average or another filter, and it should be consistent with the timeframe of the strategy.

When applying Advance-Decline Ratio (AD Ratio) across different instruments, normalize inputs so the indicator remains comparable. For price based indicators, using median or typical price can reduce distortion from single prints. Volume based indicators require clean volume data and consistent session definitions.

## Signal Construction

Signals are commonly derived from zero line crosses, threshold levels, or the direction of the indicator slope. A cross above zero suggests improving momentum, while a cross below suggests weakening conditions. Divergence between price and the indicator can warn of trend exhaustion.

Many traders require confirmation, such as a close beyond a level or a multi bar condition, to reduce false positives. Multi timeframe checks can improve robustness by aligning short term entries with longer term bias.

## Market Regime Behavior

Advance-Decline Ratio (AD Ratio) tends to behave differently in trending and ranging markets. In strong trends it can stay above or below its baseline for extended periods, which makes mean reversion signals risky. In ranges it can oscillate frequently and generate whipsaws.

Volatility regime shifts also matter. A sudden increase in volatility can change the amplitude of the indicator, so fixed thresholds may need to be adapted or paired with a volatility filter.

## Practical Use

A common approach is to use Advance-Decline Ratio (AD Ratio) as a confirmation layer rather than a standalone trigger. For example, a breakout setup can be filtered by requiring the indicator to be positive and rising. In mean reversion systems, the indicator can define the strength of the counter move before entry.

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
