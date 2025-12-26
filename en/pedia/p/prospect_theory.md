# Prospect Theory

Prospect Theory is a behavioral economic theory developed by Daniel Kahneman and Amos Tversky in 1979. It describes how individuals assess their potential losses and gains when making decisions under [uncertainty](../u/uncertainty_in_trading.md). Unlike traditional economic theories that assume [rational behavior](../r/rational_behavior.md), Prospect Theory accounts for the psychological nuances involved in decision-making. This makes it particularly relevant to fields like [finance](../f/finance.md), trading, and [investing](../i/investing.md), where real-world decisions often deviate from purely rational models.

## Key Components

### 1. Value Function
The [value](../v/value.md) function is central to Prospect Theory and it describes how people [value](../v/value.md) potential gains and losses. Unlike traditional [utility theory](../u/utility_theory_in_trading.md) which considers the absolute [value](../v/value.md) of an outcome, the [value](../v/value.md) function in Prospect Theory is:

- **Reference-dependent**: The [value](../v/value.md) of an outcome is determined relative to a reference point (usually the status quo or the current state).
- **[Loss Aversion](../l/loss_aversion.md)**: Losses loom larger than gains. The disutility of losing $100 is greater than the [utility](../u/utility.md) of gaining $100.
- **Diminishing Sensitivity**: The [value](../v/value.md) function is concave for gains and convex for losses. This means that the marginal [value](../v/value.md) of gains decreases with size, and similarly, the marginal disutility of losses decreases with size.

Mathematically, the [value](../v/value.md) function \(v\) can be represented as:
\[ v(x) = \begin{cases}
 (x - \[lambda](../l/lambda.md))^\[alpha](../a/alpha.md) & \text{if } x \geq \[lambda](../l/lambda.md) \\
 -\[kappa](../k/kappa.md) (\[lambda](../l/lambda.md) - x)^\[beta](../b/beta.md) & \text{if } x < \[lambda](../l/lambda.md)
 \end{cases}
\]
Where:
- \(x\) is the outcome.
- \(\[lambda](../l/lambda.md)\) is the reference point.
- \(\[alpha](../a/alpha.md)\) and \(\[beta](../b/beta.md)\) are parameters reflecting diminishing sensitivity.
- \(\[kappa](../k/kappa.md)\) reflects [loss aversion](../l/loss_aversion.md).

### 2. Probability Weighting Function
The probability weighting function describes how people perceive the probability of outcomes. People tend to overweigh small probabilities and underweigh large probabilities. This is contrary to the [expected utility](../e/expected_utility.md) theory where probabilities are considered linearly.

This function can be represented as:
\[ \pi(p) = \frac{p^\[gamma](../g/gamma.md)}{(p^\[gamma](../g/gamma.md) + (1-p)^\[gamma](../g/gamma.md))^{1/\[gamma](../g/gamma.md)}} \]
Where:
- \(p\) is the probability of the outcome.
- \(\pi(p)\) is the decision weight.
- \(\[gamma](../g/gamma.md)\) is an exponent that determines the curvature of the weighting function.

## How It Works

### Decision-Making Process
Prospect Theory proposes a two-stage process for decision-making under [risk](../r/risk.md):

1. **Editing Phase**: Potential outcomes and probabilities are simplified using a series of cognitive operations, such as coding (setting reference points), combination ([aggregation](../a/aggregation.md) of probabilities), segregation (separating riskless from risky components), and cancellation (canceling out common attributes).
2. **Evaluation Phase**: Each edited prospect is evaluated by combining the [value](../v/value.md) of outcomes and decisions weights. The prospect with the highest [value](../v/value.md) is chosen.

### Cumulative Prospect Theory
An advancement over the original model is Cumulative Prospect Theory (CPT), which extends the theory to account for [multiple](../m/multiple.md) or compound outcomes. In CPT, outcomes are ordered and cumulative probabilities are used in the weighting function, allowing for a more comprehensive model that includes scenarios like [portfolio optimization](../p/portfolio_optimization.md).

## Examples in Real Life

### Financial Markets
Investors often deviate from the [rational behavior](../r/rational_behavior.md) predicted by traditional financial theories. Examples include:

- **[Loss Aversion](../l/loss_aversion.md)**: Investors are more likely to [hold](../h/hold.md) on to losing [stocks](../s/stock.md), hoping they [will](../w/will.md) rebound, rather than selling them at a loss.
- **Over-weighing Small Probabilities**: Investors might over-invest in highly speculative [stocks](../s/stock.md) with small chances of huge gains, akin to buying lottery tickets.
- **[Risk](../r/risk.md) Behavior in Gains vs. Losses**: Investors tend to be [risk-averse](../r/risk-averse.md) when facing gains but become [risk](../r/risk.md)-seeking when facing potential losses.

### Behavioral Biases
[Behavioral biases](../b/behavioral_biases_in_trading.md) explained by Prospect Theory include:

- **[Endowment Effect](../e/endowment_effect.md)**: People [value](../v/value.md) what they own more than identical items they do not own.
- **Status Quo Bias**: Preference for the current state of affairs, leading to under-reaction in trading.
- **[Disposition](../d/disposition.md) Effect**: The tendency to sell winning investments and [hold](../h/hold.md) onto losing investments.

### Insurance and Gambling
Prospect Theory explains why people purchase [insurance](../i/insurance.md) and gamble:

- **[Insurance](../i/insurance.md)**: Even though the [expected value](../e/expected_value.md) of [insurance](../i/insurance.md) is negative, people overweigh the small probability of a catastrophe.
- **Gambling**: Similarly, gamblers overweigh small probabilities of large wins, resulting in higher stakes in lotteries and casinos.

## Implications for Algorithmic Trading

[Algorithmic trading](../a/algorithmic_trading.md) relies heavily on models that predict [market](../m/market.md) movements and make trading decisions. Understanding Prospect Theory allows developers to:

- Incorporate human decision-making biases into algorithms, improving prediction models.
- Design algorithms that exploit [behavioral biases](../b/behavioral_biases_in_trading.md) in the [market](../m/market.md) (e.g., exploiting the [disposition](../d/disposition.md) effect).
- Enhance [risk management](../r/risk_management.md) strategies by considering how traders perceive [risk](../r/risk.md) differently from traditional models.

## Conclusion

Prospect Theory provides a more realistic framework for understanding decision-making under [risk](../r/risk.md) than traditional rational models. Its insights into how people actually perceive gains, losses, and probabilities make it invaluable in fields like trading and [finance](../f/finance.md). By integrating these behavioral insights, financial professionals and algorithm developers can create better strategies, mitigate [risk](../r/risk.md), and ultimately improve financial outcomes.

For further reading and a comprehensive dive into this theory, you may refer to the following resources:

- Daniel Kahneman's Nobel Prize Lecture
- Kahneman's book "Thinking, Fast and Slow"
- Amos Tversky's article in JSTOR