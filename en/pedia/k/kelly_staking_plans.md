# Kelly Staking Plans

The [Kelly Criterion](../k/kelly_criterion.md) is a formula used to determine the optimal size of a series of bets or investments. It was derived by John L. Kelly Jr. in 1956 while working at Bell Labs. In the context of financial investments and particularly [algorithmic trading](../a/algorithmic_trading.md), the [Kelly Criterion](../k/kelly_criterion.md) has been adapted to determine the proportion of [capital](../c/capital.md) to allocate to a particular [trading strategy](../t/trading_strategy.md) to maximize long-term growth.

## Foundation of the Kelly Criterion

The [Kelly Criterion](../k/kelly_criterion.md) maximizes the logarithm of [wealth](../w/wealth.md), ensuring long-term growth based on several outcomes with varying probabilities. The basic formula for the [Kelly Criterion](../k/kelly_criterion.md) in its simplest form is:

```
f* = (bp - q) / b
```

Where:
- `f*` is the fraction of the current bankroll to wager;
- `b` is the odds received on the bet (net odds);
- `p` is the probability of winning;
- `q` is the probability of losing, where `q = 1 - p`.

This formula calculates the optimal bet size that maximizes the expected logarithmic growth of [capital](../c/capital.md).

### Illustration

Imagine a scenario where a [trader](../t/trader.md) is considering a stock investment:
- The stock has a 60% chance of increasing in [value](../v/value.md) (`p = 0.6`);
- The stock has a 40% chance of decreasing in [value](../v/value.md) (`q = 0.4`).

Assume the [return](../r/return.md) on success is 1:1 (`b = 1`), so the investment either doubles or loses its stake. Using the Kelly formula:

```
f* = (1 * 0.6 - 0.4) / 1 = 0.2 or 20%
```

This result suggests that, to maximize the expected logarithmic growth of [capital](../c/capital.md), 20% of the current bankroll should be allocated to this stock.

## Application in Algorithmic Trading

[Algorithmic trading](../a/algorithmic_trading.md) involves the use of computer programs to automatically make trading decisions and execute trades. The [Kelly Criterion](../k/kelly_criterion.md) fits well with this approach, given that these programs are designed to process large amounts of data and identify statistically significant trading opportunities.

### Implementing Kelly Staking in Algorithms

Developing an algorithm that uses the [Kelly Criterion](../k/kelly_criterion.md) involves several key steps:

1. **Modeling Probabilities**: Estimate the probability of various outcomes for trades. This could be done through [historical data analysis](../h/historical_data_analysis.md), [machine learning](../m/machine_learning.md) models, or other [predictive analytics](../p/predictive_analytics.md) techniques.
2. **Calculating Returns**: Define the potential returns (`b`) for each [trade](../t/trade.md). This involves understanding [market dynamics](../m/market_dynamics.md) and how much [profit](../p/profit.md) or loss is expected.
3. **Computing Fraction**: Apply the Kelly formula to compute the fraction of the bankroll to be allocated to each [trade](../t/trade.md).
4. **[Execution](../e/execution.md)**: Implement [trade](../t/trade.md) [execution](../e/execution.md) strategies within the algorithm that respect the calculated fraction, adjusting for [transaction costs](../t/transaction_costs.md), [slippage](../s/slippage.md), and other [market](../m/market.md) factors.

### Practical Considerations

1. **Overbetting and [Risk](../r/risk.md) of Ruin**: Strictly following the [Kelly Criterion](../k/kelly_criterion.md) can lead to large bet sizes, which might be impractical or excessively risky in real-world trading. To mitigate this, traders often use a "fractional Kelly" approach by wagering only a portion (such as half) of the Kelly-recommended amount.

2. **[Market](../m/market.md) Frictions**: Real-world markets introduce complexities such as [transaction costs](../t/transaction_costs.md), [bid](../b/bid.md)-ask [spreads](../s/spreads.md), and [slippage](../s/slippage.md), which can affect the accuracy of Kelly-based strategies. Algorithms must account for these factors to avoid overestimating the optimal bet size.

3. **[Diversification](../d/diversification.md)**: The [Kelly Criterion](../k/kelly_criterion.md) typically addresses betting on a single event. In a diversified [trading strategy](../t/trading_strategy.md) involving [multiple](../m/multiple.md) assets, the formula needs to be adapted to allocate the total [capital](../c/capital.md) across different assets simultaneously. This requires understanding the co-movement between different assets and balancing the portfolio accordingly.

4. **Recalibration**: Probabilities and potential returns are not static. Continuous monitoring and recalibration of probabilities and returns are necessary to keep the staking plan aligned with the current [market](../m/market.md) conditions.

## Kelly Criterion Variants

Beyond the basic Kelly formula, several variants and extensions exist to address different investment scenarios:

### Continuous Kelly Criterion

In continuous markets, such as [stocks](../s/stock.md) and currencies, the discrete nature of the Kelly formula can be extended to continuous models. This approach involves using [stochastic calculus](../s/stochastic_calculus.md) and differential equations to determine optimal investment strategies over time.

### Kelly for Multiple Outcomes

For investments with [multiple](../m/multiple.md) possible outcomes beyond binary win/loss, the Kelly formula can be expanded to account for these [multiple](../m/multiple.md) states. The generalized formula considers the expected returns and probabilities for each possible outcome.

### Fractional Kelly

A common adaptation in practice is to use a fraction of the Kelly recommendation to reduce [risk](../r/risk.md) and [volatility](../v/volatility.md). For instance, multiplying the Kelly fraction by a [factor](../f/factor.md) (like 0.5) to get a "half-Kelly" wager introduces a more conservative approach while still capturing some benefits of the original criterion.

### Bayesian Kelly

Incorporating [Bayesian inference](../b/bayesian_inference.md) allows traders to update probabilities dynamically as new information arrives. Bayesian Kelly methods combine prior beliefs about probabilities with new [market](../m/market.md) data to refine investment decisions over time.

## Historical Use and Criticism

While the [Kelly Criterion](../k/kelly_criterion.md) has strong theoretical foundations, its practical use in [financial markets](../f/financial_market.md) varies:

- **Success Stories**: Some prominent investors, such as Ed Thorp, have successfully utilized [Kelly Criterion](../k/kelly_criterion.md)-based strategies in [financial markets](../f/financial_market.md), documenting significant long-term [wealth](../w/wealth.md) growth.

- **Criticism**: Critics argue that strict adherence to the Kelly formula can lead to excessive [volatility](../v/volatility.md) and drawdowns, making it unsuitable for [risk-averse](../r/risk-averse.md) investors. Moreover, the formula’s sensitivity to incorrect probability estimates can lead to suboptimal or even detrimental outcomes.

## Modern Implementations

Several fintech companies and trading platforms integrate the [Kelly Criterion](../k/kelly_criterion.md) into their [trading algorithms](../t/trading_algorithms.md) and [portfolio management](../p/portfolio_management.md) tools:

- **Algonox**: Specializes in [algorithmic trading](../a/algorithmic_trading.md) solutions, integrating [mathematical models](../m/mathematical_models_in_trading.md), including Kelly-based strategies. [Algonox](https://www.algonox.com/)
- **[QuantConnect](../q/quantconnect.md)**: An [open](../o/open.md) [algorithmic trading](../a/algorithmic_trading.md) platform that provides tools for designing, testing, and executing strategies, with support for [Kelly Criterion](../k/kelly_criterion.md) implementations. [QuantConnect](https://www.quantconnect.com/)
- **Tradeworx**: Leveraging advanced analytics and [quantitative models](../q/quantitative_models.md), Tradeworx employs sophisticated strategies, including Kelly-based approaches, to manage [hedge](../h/hedge.md) funds. [Tradeworx](http://www.tradeworx.com/)

## Conclusion

The [Kelly Criterion](../k/kelly_criterion.md) offers a [robust](../r/robust.md) framework for determining bet sizing in trading and investment, balancing [risk](../r/risk.md) and reward to maximize long-term [capital](../c/capital.md) growth. While its theoretical foundations are strong, practical implementation requires careful consideration of [market](../m/market.md) realities, such as [transaction costs](../t/transaction_costs.md), [diversification](../d/diversification.md), and probability estimation accuracy. Adaptations like fractional Kelly and Bayesian approaches provide additional flexibility to align the criterion with real-world investment scenarios. As [algorithmic trading](../a/algorithmic_trading.md) continues to evolve, the [Kelly Criterion](../k/kelly_criterion.md) remains a valuable tool in the arsenal of [quantitative finance](../q/quantitative_finance.md) and investment professionals.
