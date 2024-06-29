# Kelly Criterion

The Kelly Criterion is a formula used to determine the optimal size of a series of bets in order to maximize logarithm of wealth, thereby optimizing the growth rate of capital. It is frequently employed in situations involving repeated investments or bets, including actuarial science, stock trading, and especially algorithmic trading. Developed by John L. Kelly Jr. in 1956, the Kelly Criterion helps traders and gamblers calculate the most appropriate fraction of their bankroll to risk on a single trade or bet, enhancing the compound growth over time while minimizing the risk of ruin.

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

Consider a stock that has a 60% chance (p = 0.60) of increasing in value by one unit within a short time frame, and a 40% chance (q = 0.40) of decreasing by one unit. The net odds `b` would thus be 1:1.

Substituting these values into the Kelly formula provides:

```
f* = (1 * 0.60 - 0.40) / 1
   = 0.20
```

This calculation suggests that an investor should risk 20% of their bankroll on this particular stock.

## Practical Application

The Kelly Criterion is especially useful for portfolio management and algorithmic trading. In trading, it allows for the calibration of trade sizes based on the edge (expectation of profit) and variance (risk). Algorithmic traders rely on this formula to stabilize and optimize the growth of their capital over long periods.

### Limitations and Considerations

1. **Assumption of Known Probabilities**: The Kelly Criterion assumes that the probabilities (p and q) and return (b) on a given trade are known, which in practice, can be difficult to estimate accurately.

2. **Risk of Over-Betting**: Though it maximizes logarithmic growth of wealth, the Kelly Criterion can suggest large bet sizes which can be impractical or psychologically challenging for many traders. A commonly recommended modification is to use a fraction of the Kelly bet size (half-Kelly, quarter-Kelly, etc.) to manage volatility and drawdowns more effectively.

3. **Market Conditions**: The performance of the Kelly Criterion can be sensitive to market conditions. Under volatile or extreme market conditions, the criterion’s suggestions may lead to substantial volatility in returns.

## Kelly in Algorithmic Trading

Algorithmic trading involves the use of software to automate trading decisions based on mathematical models, and the Kelly Criterion is often incorporated within these models to ensure optimal bet sizing. Various firms and software providers leverage the Kelly Criterion to enhance trading performance.

### Firms Using Kelly Criterion

- **Numerai**: [Numerai](https://numer.ai/) is a hedge fund that applies machine learning algorithms to trading data. They often incorporate advanced risk management techniques, including those based on the Kelly Criterion.
  
- **Bridgewater Associates**: [Bridgewater](https://www.bridgewater.com/) is one of the world’s largest hedge funds, known for its systematic and quantitative approaches to trading that often includes risk assessment methodologies akin to the Kelly Criterion.
  
- **Two Sigma**: [Two Sigma](https://www.twosigma.com/) applies artificial intelligence, machine learning, and distributed computing to financial markets. The firm utilizes sophisticated risk management and allocation strategies, many of which are influenced by principles similar to the Kelly Criterion.

## Historical Context and Development

John L. Kelly Jr. developed the Kelly Criterion originally for applications in telecommunications while working at Bell Labs, but it gained prominence in the finance sector notably through the work of noted investors like Warren Buffett and Bill Gross. Its application has expanded significantly in quantitative finance and algorithmic trading due to its mathematical rigor and utility in managing and optimizing growth.

## Mathematical Derivation

To better understand the derivation of the Kelly Criterion, it helps to consider the objective: to maximize the expected logarithm of wealth. This approach is rooted in utility theory, aiming to optimize the growth rate of an investment rather than its absolute value.

Given a current capital `W`, and a fraction `f` to be wagered, the formula for the expected logarithm of future wealth `E[log(W)]` can be illustrated as:

```
E[log(W)] = p * log(W + f * W + b * f * W) + (1 - p) * log(W - f * W)
```

Maximizing this expectation with respect to `f` leads to the Kelly Criterion as derived earlier. This derivation relies on calculus and principles of convex optimization.

## Alternative Bet Sizing Strategies

While the Kelly Criterion is optimally efficient from a mathematical standpoint, other methods exist for bet sizing that cater to different risk tolerances and market conditions:

1. **Fixed Fractional Betting**: Allocating a fixed percentage of one's total capital per trade, irrespective of individual trade odds.
2. **Martingale System**: Increasing the bet size after a loss, a risky strategy typically de-emphasized in professional trading.
3. **Anti-Martingale System**: Increasing the bet size after a win, somewhat akin to the Kelly approach but simpler in application.

## Conclusion

The Kelly Criterion represents a powerful tool for risk management and capital growth in trading. Its mathematical foundation ensures a systematic increase in the logarithm of wealth, though practical applications require careful consideration of forecast accuracy, market conditions, and risk tolerance. In the fast-paced world of algorithmic trading, the Kelly Criterion continues to stand out as a pivotal approach to optimizing bet sizes and managing investment risks efficiently.
