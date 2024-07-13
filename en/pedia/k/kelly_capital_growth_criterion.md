# Kelly Capital Growth Criterion

The Kelly [Capital](../c/capital.md) Growth Criterion, often simply referred to as the [Kelly criterion](../k/kelly_criterion.md), is a mathematical formula used to determine the optimal size of a series of bets to maximize the logarithm of [wealth](../w/wealth.md) over the long term. This criterion is widely applicable in various domains including [finance](../f/finance.md), gambling, and [investment management](../i/investment_management.md), directly influencing strategies in [algorithmic trading](../a/algorithmic_trading.md).

## Origin and Development

The [Kelly criterion](../k/kelly_criterion.md) was developed by John L. Kelly Jr., a researcher at Bell Labs, in his 1956 paper "A New Interpretation of Information Rate". The criterion originally emerged to improve signal [noise](../n/noise.md) in telecommunications but quickly found its application in gambling, and eventually, in financial investment to solve the dual problems of [risk](../r/risk.md) and [return](../r/return.md).

## The Basic Formula

The Kelly formula is given by:

\[ f^* = \frac{bp - q}{b} \]

Where:
- \( f^* \) is the fraction of the current bankroll to bet,
- \( b \) is the net odds received on the wager (the odds minus 1),
- \( p \) is the probability of winning,
- \( q \) is the probability of losing, which is \( 1 - p \).

For example, if a bet has even odds (\( b = 1 \)), a 60% chance of winning (\( p = 0.6 \)), and a 40% chance of losing (\( q = 0.4 \)), the Kelly fraction would be:

\[ f^* = \frac{(1 \cdot 0.6) - 0.4}{1} = 0.2 \]

This result suggests that one should bet 20% of their bankroll on the opportunity to maximize long-term growth.

## Application in Algorithmic Trading

In [algorithmic trading](../a/algorithmic_trading.md), the [Kelly criterion](../k/kelly_criterion.md) is utilized to determine the proportion of the [trading account](../t/trading_account.md) to allocate on a particular [trade](../t/trade.md). It provides a systematic approach to [risk management](../r/risk_management.md) and [portfolio optimization](../p/portfolio_optimization.md). While calculating the exact probabilities and outcomes in [financial markets](../f/financial_market.md) is significantly more complex than in gambling scenarios, adaptations and approximations of the [Kelly criterion](../k/kelly_criterion.md) are instrumental in [portfolio management](../p/portfolio_management.md) strategies.

### Advantages

1. **Maximization of Logarithmic [Wealth](../w/wealth.md)**: The [Kelly criterion](../k/kelly_criterion.md) maximizes the logarithm of [wealth](../w/wealth.md), which aligns with the principle of [utility maximization](../u/utility_maximization.md) under relative [wealth](../w/wealth.md).
2. **Avoidance of Ruin**: By limiting the bet size, it inherently avoids the [risk](../r/risk.md) of complete ruin, a common problem with betting or over-leveraging in trading.
3. **[Compounding](../c/compounding.md) Growth**: Small positive returns compounded over time lead to significant growth, which is the primary advantage of using the [Kelly criterion](../k/kelly_criterion.md) in trading.

### Disadvantages

1. **Parameter Sensitivity**: The [Kelly criterion](../k/kelly_criterion.md) requires precise estimation of probabilities and returns, which can be challenging to determine accurately.
2. **[Volatility](../v/volatility.md)**: Full Kelly bets can lead to high [volatility](../v/volatility.md) in account [value](../v/value.md), which might be unsuitable for all investors.
3. **[Overfitting](../o/overfitting.md) [Risk](../r/risk.md)**: Using historical data to estimate probabilities might lead to [overfitting](../o/overfitting.md) and poor future performance.

## Alternative and Modified Approaches

Due to its high [volatility](../v/volatility.md), many practitioners use a "fractional Kelly" strategy, betting a consistent fraction (like half) of the Kelly amount. This approach reduces [volatility](../v/volatility.md) while preserving much of the growth benefit.

\[ f_{\text{fractional}} = c \cdot f^* \]

Where \( c \) is a fraction less than 1 (commonly 0.5).

### Kelly and Modern Portfolio Theory (MPT)

The principles of the [Kelly criterion](../k/kelly_criterion.md) can be integrated with Modern Portfolio Theory, which emphasizes on [diversification](../d/diversification.md) to optimize the [risk](../r/risk.md)-[return](../r/return.md) [trade](../t/trade.md)-off. The [Kelly criterion](../k/kelly_criterion.md) can be applied within the framework of MPT to determine the optimal allocation across portfolios of [multiple](../m/multiple.md) assets.

### Practical Application in Financial Markets

#### Hedge Funds and Investment Firms

Several [hedge](../h/hedge.md) funds and investment firms are known to use [Kelly criterion](../k/kelly_criterion.md) and similar strategies as part of their [trading algorithms](../t/trading_algorithms.md). Firms like Renaissance Technologies, founded by Jim Simons, notoriously employ quantitative and algorithmic strategies to [yield](../y/yield.md) high returns. More details on their approach can be found on [Renaissance Technologies' official site](https://www.rentec.com/).

#### Retail Traders and Robo-Advisors

With the advent of robo-advisors and automated trading platforms, retail traders now have access to sophisticated tools that incorporate [risk management](../r/risk_management.md) principles. Platforms like Betterment and Wealthfront use algorithms that can be tailored to [investor](../i/investor.md) [risk profiles](../r/risk_profiles.md), indirectly applying concepts similar to the [Kelly criterion](../k/kelly_criterion.md).

## Conclusion

The Kelly [Capital](../c/capital.md) Growth Criterion is a powerful tool in the arsenal of traders and investors. By focusing on the long-term maximization of [wealth](../w/wealth.md) through mathematically optimal bet sizing, it provides a structured approach to balancing [risk](../r/risk.md) and reward. However, its practical application requires careful estimation of probabilities and sensible adjustments to mitigate the inherent [volatility](../v/volatility.md).

Understanding and correctly implementing the [Kelly criterion](../k/kelly_criterion.md) can significantly enhance the performance of trading and investment strategies, making it a crucial concept in the realm of [quantitative finance](../q/quantitative_finance.md) and [algorithmic trading](../a/algorithmic_trading.md).
