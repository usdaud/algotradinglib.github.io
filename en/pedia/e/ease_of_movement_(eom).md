# Ease of Movement (EOM)

Ease of Movement is a volume based indicator that measures how easily price moves with respect to volume. It combines price range and volume to identify when price advances or declines with little resistance.

## Formula
Distance Moved = ((High + Low) / 2) - ((Prior High + Prior Low) / 2)
Box Ratio = Volume / (High - Low)
EOM = Distance Moved / Box Ratio

Many implementations smooth EOM with a moving average.

## Interpretation
- Positive values suggest price is rising with relatively low volume resistance
- Negative values suggest price is falling with little resistance
- Large absolute values indicate efficient price movement

## Use in Trading
EOM is used to confirm trends and to identify potential breakouts when price advances with ease. It can also help spot weak moves where price rises but EOM remains flat.

## Limitations
The indicator can be noisy in low volume markets. It is sensitive to the chosen lookback period and smoothing method.

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
