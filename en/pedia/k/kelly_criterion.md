# Kelly Criterion

The Kelly Criterion is a formula used to determine the optimal size of a series of bets in [order](../o/order.md) to maximize logarithm of [wealth](../w/wealth.md), thereby optimizing the growth rate of [capital](../c/capital.md). It is frequently employed in situations involving repeated investments or bets, including [actuarial science](../a/actuarial_science.md), stock trading, and especially [algorithmic trading](../a/algorithmic_trading.md). Developed by John L. Kelly Jr. in 1956, the Kelly Criterion helps traders and gamblers calculate the most appropriate fraction of their bankroll to [risk](../r/risk.md) on a single [trade](../t/trade.md) or bet, enhancing the compound growth over time while minimizing the [risk](../r/risk.md) of ruin.

## Basic Formula

The Kelly formula can be mathematically represented as follows:

```
f* = (bp - q) / b
```

Where:
- `f*` is the fraction of the current bankroll to wager.
- `b` is the net odds received on the wager (odds given as "b to 1").
- `p` is the probability of winning.
- `q` is the probability of losing, which is equal to `1 - p`.

### Example Calculation

Consider a stock that has a 60% chance (p = 0.60) of increasing in [value](../v/value.md) by one unit within a short time frame, and a 40% chance (q = 0.40) of decreasing by one unit. The net odds `b` would thus be 1:1.

Substituting these values into the Kelly formula provides:

```
f* = (1 * 0.60 - 0.40) / 1
   = 0.20
```

This calculation suggests that an [investor](../i/investor.md) should [risk](../r/risk.md) 20% of their bankroll on this particular stock.

## Practical Application

The Kelly Criterion is especially useful for [portfolio management](../p/portfolio_management.md) and [algorithmic trading](../a/algorithmic_trading.md). In trading, it allows for the calibration of [trade](../t/trade.md) sizes based on the edge (expectation of [profit](../p/profit.md)) and variance ([risk](../r/risk.md)). Algorithmic traders rely on this formula to stabilize and optimize the growth of their [capital](../c/capital.md) over long periods.

### Limitations and Considerations

1. **Assumption of Known Probabilities**: The Kelly Criterion assumes that the probabilities (p and q) and [return](../r/return.md) (b) on a given [trade](../t/trade.md) are known, which in practice, can be difficult to estimate accurately.

2. **[Risk](../r/risk.md) of Over-Betting**: Though it maximizes logarithmic growth of [wealth](../w/wealth.md), the Kelly Criterion can suggest large bet sizes which can be impractical or psychologically challenging for many traders. A commonly recommended modification is to use a fraction of the Kelly bet size (half-Kelly, quarter-Kelly, etc.) to manage [volatility](../v/volatility.md) and drawdowns more effectively.

3. **[Market](../m/market.md) Conditions**: The performance of the Kelly Criterion can be sensitive to [market](../m/market.md) conditions. Under volatile or extreme [market](../m/market.md) conditions, the criterion’s suggestions may lead to substantial [volatility](../v/volatility.md) in returns.

## Kelly in Algorithmic Trading

[Algorithmic trading](../a/algorithmic_trading.md) involves the use of software to automate trading decisions based on [mathematical models](../m/mathematical_models_in_trading.md), and the Kelly Criterion is often incorporated within these models to ensure optimal bet sizing. Various firms and software providers [leverage](../l/leverage.md) the Kelly Criterion to enhance [trading performance](../t/trading_performance.md).

### Firms Using Kelly Criterion

- **Numerai**: [Numerai](https://numer.ai/) is a [hedge fund](../h/hedge_fund.md) that applies machine [learning algorithms](../l/learning_algorithms_in_trading.md) to trading data. They often incorporate advanced [risk management](../r/risk_management.md) techniques, including those based on the Kelly Criterion.
  
- **Bridgewater Associates**: [Bridgewater](https://www.bridgewater.com/) is one of the world’s largest [hedge](../h/hedge.md) funds, known for its systematic and [quantitative approaches](../q/quantitative_approaches.md) to trading that often includes [risk](../r/risk.md) assessment methodologies akin to the Kelly Criterion.
  
- **Two Sigma**: [Two Sigma](https://www.twosigma.com/) applies [artificial intelligence](../a/artificial_intelligence_in_trading.md), machine learning, and distributed computing to [financial markets](../f/financial_market.md). The [firm](../f/firm.md) utilizes sophisticated [risk management](../r/risk_management.md) and allocation strategies, many of which are influenced by principles similar to the Kelly Criterion.

## Historical Context and Development

John L. Kelly Jr. developed the Kelly Criterion originally for applications in telecommunications while working at Bell Labs, but it gained prominence in the [finance](../f/finance.md) sector notably through the work of noted investors like Warren Buffett and Bill Gross. Its application has expanded significantly in [quantitative finance](../q/quantitative_finance.md) and [algorithmic trading](../a/algorithmic_trading.md) due to its mathematical rigor and [utility](../u/utility.md) in managing and optimizing growth.

## Mathematical Derivation

To better understand the derivation of the Kelly Criterion, it helps to consider the objective: to maximize the expected logarithm of [wealth](../w/wealth.md). This approach is rooted in [utility theory](../u/utility_theory_in_trading.md), aiming to optimize the growth rate of an investment rather than its absolute [value](../v/value.md).

Given a current [capital](../c/capital.md) `W`, and a fraction `f` to be wagered, the formula for the expected logarithm of future [wealth](../w/wealth.md) `E[log(W)]` can be illustrated as:

```
E[log(W)] = p * log(W + f * W + b * f * W) + (1 - p) * log(W - f * W)
```

Maximizing this expectation with respect to `f` leads to the Kelly Criterion as derived earlier. This derivation relies on calculus and principles of [convex optimization](../c/convex_optimization.md).

## Alternative Bet Sizing Strategies

While the Kelly Criterion is optimally efficient from a mathematical standpoint, other methods exist for bet sizing that cater to different [risk](../r/risk.md) tolerances and [market](../m/market.md) conditions:

1. **Fixed Fractional Betting**: Allocating a fixed percentage of one's total [capital](../c/capital.md) per [trade](../t/trade.md), irrespective of individual [trade](../t/trade.md) odds.
2. **Martingale System**: Increasing the bet size after a loss, a risky strategy typically de-emphasized in professional trading.
3. **Anti-Martingale System**: Increasing the bet size after a win, somewhat akin to the Kelly approach but simpler in application.

## Conclusion

The Kelly Criterion represents a powerful tool for [risk management](../r/risk_management.md) and [capital](../c/capital.md) growth in trading. Its mathematical foundation ensures a systematic increase in the logarithm of [wealth](../w/wealth.md), though practical applications require careful consideration of [forecast accuracy](../f/forecast_accuracy.md), [market](../m/market.md) conditions, and [risk tolerance](../r/risk_tolerance.md). In the fast-paced world of [algorithmic trading](../a/algorithmic_trading.md), the Kelly Criterion continues to stand out as a pivotal approach to optimizing bet sizes and managing investment risks efficiently.
