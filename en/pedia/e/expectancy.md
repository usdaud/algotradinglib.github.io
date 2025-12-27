# Expectancy

Expectancy is the average amount a strategy expects to win or lose per trade. It connects win rate and payoff size into a single measure of trade quality.

## Formula
A common formula is:
Expectancy = (Win Rate x Average Win) - (Loss Rate x Average Loss)
Loss rate is one minus win rate. The result can be expressed in currency, points, or as a multiple of risk per trade.

## Interpretation
Positive expectancy means that, on average, the strategy makes money per trade. A strategy can have a low win rate and still be profitable if average wins are large. Conversely, a high win rate can still lose money if losses are large.

## Use in Strategy Evaluation
Expectancy is useful for comparing strategies with different trade frequencies and win rates. It also helps identify whether changes in execution costs or slippage will push a strategy from positive to negative performance.

## Limitations
Expectancy depends on the distribution of outcomes and can be unstable with small sample sizes. It does not capture tail risk or drawdown behavior. It should be used alongside risk metrics and cost analysis.

## Conclusion
Expectancy is a simple but powerful measure of trade quality. It provides a direct link between win rate, payoff, and profitability.
