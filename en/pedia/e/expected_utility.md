# Expected Utility

Expected utility is a fundamental concept in economics, finance, and decision theory, which provides a framework for making choices under uncertainty. It combines the utility (a measure of preference or satisfaction) that an individual derives from different outcomes with the probabilities of those outcomes. Through the lens of expected utility, individuals and organizations can theoretically make decisions that maximize their overall satisfaction or return.

## Conceptual Foundation

### Utility

The notion of utility is central to understanding decision-making processes. Utility represents the satisfaction or benefit derived from a particular outcome. In classical economics, utility is often assumed to be quantifiable, allowing for the comparison of different outcomes. When facing choices under certainty, an individual simply selects the option with the highest utility. However, in the real world, decisions are rarely made under conditions of absolute certainty.

### Probability

When outcomes are uncertain, probabilities come into play. Probabilities quantify the likelihood of various outcomes occurring and are essential in calculating expected utility. They provide a way to measure and compare the risk associated with different choices.

### Expected Utility

Expected utility theory formalizes the decision-making process under uncertainty. The expected utility \( E(U) \) of a random variable \( X \), representing different outcomes with corresponding probabilities, is given by:

\[ E(U) = \sum_{i} P_i \cdot U(X_i) \]

Where:

- \( E(U) \) is the expected utility.
- \( P_i \) is the probability of outcome \( X_i \).
- \( U(X_i) \) is the utility derived from outcome \( X_i \).

This framework allows for the evaluation of choices by considering both the utility of outcomes and their probabilities, leading to decisions that theoretically maximize overall satisfaction or return.

## Historical Context

The concept of utility dates back to early economic thought, but the formalization of expected utility theory is credited to John von Neumann and Oskar Morgenstern in their seminal work "Theory of Games and Economic Behavior" (1944). Their groundbreaking work laid the foundation for modern decision theory and has influenced various fields, including economics, finance, and behavioral science.

## Application in Various Fields

### Economics

In economics, expected utility theory is employed to model consumer behavior, investment choices, and risk management. It helps in understanding how individuals allocate resources under uncertainty, and informs various models of market behavior.

### Finance

In finance, expected utility is crucial for portfolio selection, risk assessment, and derivative pricing. The theory assists investors in making informed choices about which assets to include in their portfolios based on the expected return and risk associated with each asset.

### Behavioral Science

Expected utility theory also finds application in behavioral science to study how people make decisions under uncertainty. However, real-world observations have shown that individuals often deviate from the rational behavior predicted by the theory, leading to the development of alternative models such as Prospect Theory.

## Key Points in Expected Utility Theory

### Risk Aversion

Risk aversion is a key concept in expected utility theory. A risk-averse individual prefers a certain outcome over a gamble with higher or equal expected utility due to the diminishing marginal utility of wealth. This behavior is captured by a concave utility function, indicating that the marginal utility of wealth decreases as wealth increases.

### Certainty Equivalent

The certainty equivalent of a gamble is the guaranteed amount of money that an individual considers equally desirable as the gamble. It reflects the individual's risk preference and is used to evaluate their decision-making process under uncertainty.

### Stochastic Dominance

Stochastic dominance is a method for comparing random variables (or gambles) without specifying a particular utility function. If one gamble dominates another according to certain criteria, it will be preferred by all decision-makers who share these criteria.

### Utility Functions

Different utility functions represent different attitudes toward risk. Common forms include:

- **Linear Utility Function**: Represents risk-neutral behavior.
- **Concave Utility Function**: Represents risk-averse behavior.
- **Convex Utility Function**: Represents risk-seeking behavior.

The choice of utility function depends on the individual's risk preferences and the context of the decision-making problem.

## Criticisms and Limitations

Despite its widespread use, expected utility theory has faced criticisms and limitations:

### Violation of Rationality Assumptions

Real-world decision-makers often violate the rationality assumptions of expected utility theory. Behavioral anomalies, such as loss aversion and preference reversals, have been documented, challenging the predictive power of the theory.

### Alternative Models

Given the limitations of expected utility theory, alternative models have been proposed, including:

- **Prospect Theory**: Developed by Daniel Kahneman and Amos Tversky, Prospect Theory incorporates psychological factors and provides a more accurate description of how people make decisions under uncertainty.
- **Cumulative Prospect Theory**: An extension of Prospect Theory that accounts for varying probabilities and provides a better fit for observed behaviors.

### Computational Complexity

Calculating expected utility can be computationally complex, especially for decisions with a large number of possible outcomes and probabilities. This complexity can limit the practical application of the theory in certain contexts.

## Quantitative Examples

To illustrate the calculation of expected utility, consider the following examples:

### Example 1: Simple Lottery

An individual faces a lottery with two possible outcomes:

1. A payoff of $100 with a probability of 0.5.
2. A payoff of $0 with a probability of 0.5.

Assuming the individual's utility function is \( U(x) = \sqrt{x} \), the expected utility is calculated as follows:

\[ E(U) = 0.5 \cdot U(100) + 0.5 \cdot U(0) \]
\[ E(U) = 0.5 \cdot \sqrt{100} + 0.5 \cdot \sqrt{0} \]
\[ E(U) = 0.5 \cdot 10 + 0.5 \cdot 0 \]
\[ E(U) = 5 \]

### Example 2: Investment Decision

An investor is considering two investment options:

1. Investment A: A guaranteed return of $10,000.
2. Investment B: A 50% chance of a $20,000 return and a 50% chance of a $5,000 return.

Assuming the investor's utility function is \( U(x) = \ln(x) \):

**Investment A:**
\[ U(10,000) = \ln(10,000) \approx 9.21 \]

**Investment B:**
\[ E(U) = 0.5 \cdot U(20,000) + 0.5 \cdot U(5,000) \]
\[ E(U) = 0.5 \cdot \ln(20,000) + 0.5 \cdot \ln(5,000) \]
\[ E(U) = 0.5 \cdot 9.90 + 0.5 \cdot 8.52 \]
\[ E(U) = 9.21 \]

The investor is indifferent between the two investments since the expected utility is the same.

## Practical Use Cases

### Insurance

Insurance companies use expected utility theory to design and price insurance products. By understanding the risk preferences of their clients, insurers can offer policies that maximize expected utility for both parties.

### Project Management

In project management, expected utility theory helps in evaluating the potential outcomes of different project strategies and choosing the one that maximizes overall project value.

### Policy Making

Policymakers use expected utility theory to assess the potential impact of different policy options on societal welfare and make decisions that maximize the expected utility of the population.

## Conclusion

Expected utility theory provides a robust framework for making decisions under uncertainty by combining the utility of outcomes with their probabilities. Despite its limitations and criticisms, the theory remains a cornerstone of decision-making processes in various fields, including economics, finance, and behavioral science. By understanding and applying expected utility theory, decision-makers can make more informed and rational choices that maximize their overall satisfaction or return.