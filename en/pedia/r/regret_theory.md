# Regret Theory

Regret Theory is a behavioral economic theory that delves into how individuals anticipate and deal with regret associated with uncertain decision-making. Unlike classical economic theories that assume agents are rational and always strive to maximize [expected utility](../e/expected_utility.md), Regret Theory posits that emotional factors, like regret, significantly influence decision-making.

## Historical Background
Regret Theory was introduced in the mid-1980s by economists Graham Loomes and Robert Sugden. Their research provided a framework for understanding how regret and its anticipation affect people’s choices, challenging the [Expected Utility](../e/expected_utility.md) Theory, which had long dominated economic thought. 

## Key Components of Regret Theory

### Regret and Rejoice
In Regret Theory, there are two primary emotional responses driving decision-making: regret and rejoice. Regret occurs when a realized outcome of a decision is worse than the outcome of an alternative choice that could have been made. Conversely, rejoice happens when the outcome is better than the alternative choice.

### Comparative Nature
A fundamental aspect of Regret Theory is its comparative nature. Regret or rejoice is not experienced in isolation but always in a relational context with other possible outcomes. 

### Utility Function Modification
In [Expected Utility](../e/expected_utility.md) Theory, individuals aim to maximize their [utility](../u/utility.md). However, in Regret Theory, the [utility](../u/utility.md) function is modified to incorporate regret or rejoice. Therefore, the anticipated regret or rejoice affects the overall [utility](../u/utility.md) derived from a particular choice.

### Decision Weights
Under Regret Theory, decision weights are adjusted to account for potential regret. This leads to different probabilities being assigned to outcomes compared to those in traditional expected [utility maximization](../u/utility_maximization.md).

## Mathematical Formulation

The [utility](../u/utility.md), `U`, experienced by a decision-maker, can be depicted as:

\[ U(a,x) = \sum_{s \in S} p(s) u(a, s) - R(a, x) \]

where:
- \( a \) is the action taken,
- \( x \) is the actual outcome,
- \( p(s) \) is the probability of state \( s \),
- \( u(a, s) \) is the [utility](../u/utility.md) from taking action \( a \) in state \( s \),
- \( R(a, x) \) is the regret function that quantifies regret for choosing action \( a \) when outcome \( x \) is realized.

## Implications for Decision-Making

### Risk Aversion and Preference for Certainty
Regret Theory implies that individuals may exhibit more [risk-averse](../r/risk-averse.md) behavior as they try to minimize possible regret. Thus, they might prefer [options](../o/options.md) with more certain outcomes, even if these are suboptimal according to the [Expected Utility](../e/expected_utility.md) Theory.

### Status Quo Bias
Individuals might stick with a known, albeit suboptimal, decision rather than switch to a potentially better but uncertain alternative, reflecting a status quo bias driven by potential regret.

### Choice Overload
Regret Theory can explain why individuals may suffer from choice overload. The more [options](../o/options.md) one has, the more potential for regret there is, which can lead to decision paralysis.

## Applications in Finance and Trading

### Asset Allocation
In [asset allocation](../a/asset_allocation.md), investors may prefer diversified portfolios not just to optimize returns but to spread the regret associated with any single underperforming [asset](../a/asset.md). 

### Financial Product Design
Financial products can be designed to minimize regret. For example, [insurance](../i/insurance.md) products or structured products with some [capital](../c/capital.md) guarantee can appeal to an [investor](../i/investor.md)'s aversion to potential regret.

### Behavioral Finance
Regret Theory is foundational in [behavioral finance](../b/behavioral_finance.md), explaining why investors might [hold](../h/hold.md) onto losing investments to avoid the regret associated with realizing a loss.

## Algorithmic Trading

### Risk Management Algorithms
[Algorithmic trading strategies](../a/algorithmic_trading_strategies.md) can incorporate regret metrics to adjust [risk](../r/risk.md) exposure dynamically. Algorithms may reduce [trade](../t/trade.md) sizes or shift [fund](../f/fund.md) allocation to safer assets if potential regret exceeds a certain threshold.

### Reinforcement Learning
Regret minimization algorithms are a crucial part of reinforcement learning frameworks. These algorithms aim to minimize cumulative regret and are extensively used in high-frequency trading to balance exploration and exploitation.

## Practical Tools and Frameworks

### Regret Minimization Algorithms
Several [open](../o/open.md)-source libraries, such as the following, implement regret minimization algorithms:
- **libact**:  [libact](https://libact.readthedocs.io/en/latest/)
- **OpenAI Baselines**: [OpenAI Baselines](https://github.com/openai/baselines)

### Decision Support Tools
Decision support tools that incorporate Regret Theory are also prevalent. These tools use past data to help forecast potential regret and make suggestions accordingly.

## Example in Regret Theory Calculation

### Scenario
Imagine an [investor](../i/investor.md) choosing between two [stocks](../s/stock.md): Stock A and Stock B. The outcomes (profits or losses) depend on [market](../m/market.md) conditions:

- If the [market](../m/market.md) is favorable (with probability 0.6), Stock A returns $1000 and Stock B returns $800.
- If the [market](../m/market.md) is unfavorable (with probability 0.4), Stock A loses $500 and Stock B loses $200.

### Calculation
1. **[Expected Utility](../e/expected_utility.md) Without Regret**:
    - Stock A: \(0.6 \times 1000 + 0.4 \times (-500) = 600 - 200 = 400\)
    - Stock B: \(0.6 \times 800 + 0.4 \times (-200) = 480 - 80 = 400\)

Without regret, both [stocks](../s/stock.md) have the same [expected utility](../e/expected_utility.md).

2. **Regret Calculation**:
    - If choosing Stock A and the [market](../m/market.md) is unfavorable, the regret is \(| -500 - (-200) | = 300\)
    - If choosing Stock B and the [market](../m/market.md) is favorable, the regret is \(| 800 - 1000 | = 200\)

3. **Including Regret in [Utility](../u/utility.md)**:
    Implement a regret weight, \( R_w \), of 0.5 for simplification:
    - Stock A: \(0.6 \times 1000 + 0.4 \times (-500) - 0.4 \times 300 = 400 - 120 = 280\)
    - Stock B: \(0.6 \times 800 + 0.4 \times (-200) - 0.6 \times 200 = 400 - 120 = 280\)

While both seem equal again, the decision shifts subtly as probabilities and regret weights change. 

## Empirical Studies

### Financial Decisions
Studies have shown that real investors often act in ways consistent with Regret Theory. They may overly diversify or avoid selling losing [stocks](../s/stock.md), aligning with regret minimization behavior.

### Market Behavior
Regret Theory also provides insights into [market](../m/market.md) phenomena like [bubbles](../b/bubble.md) and crashes, where collective regret or anticipation of regret can lead to drastic [market](../m/market.md) shifts.

## Criticisms and Limitations

- **Rationality Assumption**: Traditionalists argue that emphasizing regret undermines the rationality assumption in [economics](../e/economics.md).
- **Complex Modeling**: Accurately modeling and quantifying regret is complex and computationally intensive.
- **Subjectivity**: Regret and its impact are subjective, varying greatly among individuals, making it challenging to generalize.

---

In summary, Regret Theory enriches our understanding of financial decision-making by [accounting](../a/accounting.md) for the emotional dimensions of regret and rejoice. This non-traditional approach offers a realistic perspective that aligns closely with observed behaviors in [financial markets](../f/financial_market.md), making it a valuable tool for both investors and financial analysts.