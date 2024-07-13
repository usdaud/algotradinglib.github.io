# Modern Portfolio Theory (MPT)

Modern Portfolio Theory (MPT), developed by [Harry Markowitz](../h/harry_markowitz.md) and introduced in his 1952 paper "Portfolio Selection", revolutionized the way financial professionals construct investment portfolios. The model focuses on maximizing the [expected return](../e/expected_return.md) for a given level of [market risk](../m/market_risk.md), or equivalently, minimizing the [risk](../r/risk.md) for a given level of [expected return](../e/expected_return.md), through [diversification](../d/diversification.md). It forms the bedrock for numerous financial strategies and has influenced a vast amount of academic and practical advancements in [investment management](../i/investment_management.md), [risk](../r/risk.md) assessment, and [algorithmic trading](../a/accountability.md).

## Key Concepts of Modern Portfolio Theory

### 1. Risk and Return

At the heart of Modern Portfolio Theory is the balance between [risk](../r/risk.md) and [return](../r/return.md). Each [asset](../a/asset.md) in a portfolio has an [expected return](../e/expected_return.md) and an associated level of [risk](../r/risk.md), mainly quantified as the [standard deviation](../s/standard_deviation.md) of the [asset](../a/asset.md)'s [return](../r/return.md). MPT contends that investors should be compensated for taking on additional [risk](../r/risk.md), known as the [risk premium](../r/risk_premium.md).

- **[Expected Return](../e/expected_return.md):** The [weighted average](../w/weighted_average.md) of probable returns for an [asset](../a/asset.md), based on historical performance or [predictive models](../p/predictive_models_in_trading.md).
- **[Standard Deviation](../s/standard_deviation.md) ([Risk](../r/risk.md)):** A measure of the [volatility](../v/volatility.md) or total [risk](../r/risk.md) of the [asset](../a/asset.md)’s returns.

### 2. Diversification

[Diversification](../d/diversification.md) is a central tenet of MPT. By holding a portfolio of varied, non-correlated assets, an [investor](../i/investor.md) can achieve a higher [expected return](../e/expected_return.md) per unit of [risk](../r/risk.md). The principle hinges on the reduction of [unsystematic risk](../u/unsystematic_risk.md)—[risk](../r/risk.md) specific to individual investments—through this process. [Systematic risk](../s/systematic_risk.md), which affects the entire [market](../m/market.md), cannot be eliminated but can be managed.

### 3. The Efficient Frontier

The [Efficient Frontier](../e/efficient_frontier.md) represents the set of optimal portfolios that [offer](../o/offer.md) the highest [expected return](../e/expected_return.md) for a given level of [risk](../r/risk.md). Portfolios that lie below the [efficient frontier](../e/efficient_frontier.md) are sub-optimal, [offering](../o/offering.md) lower returns for higher levels of [risk](../r/risk.md). The graphical representation of the [Efficient Frontier](../e/efficient_frontier.md) provides investors with a visual tool to gauge [risk](../r/risk.md) and [return](../r/return.md) [trade](../t/trade.md)-offs.

### 4. The Capital Market Line (CML)

The CML is a line that graphs the [risk](../r/risk.md)-reward profile of efficient portfolios. It is tangent to the [Efficient Frontier](../e/efficient_frontier.md) at the [market portfolio](../m/market_portfolio.md)—an optimal portfolio of all available assets in the [market](../m/market.md), assumed to be perfectly priced.

### 5. The Security Market Line (SML)

The SML represents the [expected return](../e/expected_return.md) of assets or portfolios as a function of their [beta](../b/beta.md), which measures an [asset](../a/asset.md)’s [volatility](../v/volatility.md) relative to the [market](../m/market.md). All correctly priced investments should lie on the SML in a healthy, efficient [market](../m/market.md).

### 6. Portfolio Construction

In constructing a portfolio, investors:
1. **Identify their [Risk Tolerance](../r/risk_tolerance.md):** Determine the maximum level of [risk](../r/risk.md) they are willing to accept.
2. **Estimate Expected Returns and Risks:** Use historical data or financial models to estimate each [security](../s/security.md)'s potential returns and associated risks.
3. **Calculate Correlations:** Assess how different assets move relative to one another.
4. **Optimize**: Use mathematical algorithms and [optimization](../o/optimization.md) techniques to find the [asset](../a/asset.md) mix that lies on the [Efficient Frontier](../e/efficient_frontier.md).

## Mathematical Basis of MPT

### Expected Return of a Portfolio

The [expected return](../e/expected_return.md) \( E(R_p) \) of a portfolio of \( n \) assets is given by:

\[ E(R_p) = \sum_{i=1}^{n} w_i E(R_i) \]

Where:
- \( w_i \) is the weight of [asset](../a/asset.md) \( i \) in the portfolio.
- \( E(R_i) \) is the [expected return](../e/expected_return.md) of [asset](../a/asset.md) \( i \).

### Portfolio Variance

The portfolio’s total variance \( \sigma_p^2 \) is:

\[ \sigma_p^2 = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \sigma_{ij} \]

Where:
- \( \sigma_{ij} \) is the [covariance](../c/covariance.md) of the returns between [asset](../a/asset.md) \( i \) and \( j \).

### Covariance and Correlation

[Covariance](../c/covariance.md) \( \sigma_{ij} \) measures how two assets move together:

\[ \sigma_{ij} = \rho_{ij} \sigma_i \sigma_j \]

Where:
- \( \rho_{ij} \) is the [correlation coefficient](../c/correlation_coefficient.md) between the returns of assets \( i \) and \( j \).
- \( \sigma_i \) and \( \sigma_j \) are the standard deviations of assets \( i \) and \( j \).

### Optimization Algorithms

Advanced algorithms—such as quadratic programming, [genetic algorithms](../g/genetic_algorithms_in_trading.md), and Monte Carlo simulations—are often used in practice to solve the [optimization](../o/optimization.md) problem and identify the [asset](../a/asset.md) weights that maximize [expected return](../e/expected_return.md) for a given level of [risk](../r/risk.md).

## Practical Application in Algo-Trading

[Algorithmic trading](../a/accountability.md), or algo-trading, leverages MPT by automating [portfolio rebalancing](../p/portfolio_rebalancing.md), [risk](../r/risk.md) assessment, and [optimization](../o/optimization.md) processes based on real-time data.

### Steps in Algo-Trading Utilizing MPT

1. **Data Feed Integration:** Real-time data feed from [financial markets](../f/financial_market.md).
2. **Model Training:** Using historical data to train [predictive models](../p/predictive_models_in_trading.md) that generate expected returns and [risk](../r/risk.md) assessments.
3. **[Optimization](../o/optimization.md) Engine:** Implementing algorithms to process incoming data and rebalance portfolio [holdings](../h/holdings.md) to maintain optimal allocation.
4. **[Execution](../e/execution.md):** Automated [execution](../e/execution.md) through trading platforms to make real-time adjustments.

### Algorithm Examples

- **[Mean-Variance Optimization](../m/mean-variance_optimization.md):** The traditional MPT [optimization](../o/optimization.md) problem where the goal is to maximize [expected return](../e/expected_return.md) for a given [risk](../r/risk.md) level.
- **[Risk Parity](../r/risk_parity.md):** Allocating [capital](../c/capital.md) across assets such that each contributes equally to the portfolio’s overall [risk](../r/risk.md).
- **Bayesian [Portfolio Optimization](../p/portfolio_optimization.md):** Incorporating beliefs and [multiple](../m/multiple.md) data sources into the [optimization](../o/optimization.md) framework to refine [asset](../a/asset.md) [return](../r/return.md) estimates and [covariance](../c/covariance.md) structures.

## Criticisms and Limitations of MPT

### Assumptions

MPT is based on several simplifying assumptions which are often criticized:
1. **[Normal Distribution](../n/normal_distribution_in_trading.md) of Returns:** [Asset](../a/asset.md) returns are normally distributed, which may not be valid due to fat tails and [skewness](../s/skewness.md).
2. **Fixed Correlations:** Assumes stable correlations over time, while correlations can change in stressful [market](../m/market.md) conditions.
3. **Rational Investors:** Assumes investors are rational and markets are efficient, which [behavioral economics](../b/behavioral_economics.md) has frequently disputed.

### Real-World Constraints

Real-world investors face constraints not accounted for in classical MPT, such as:
- **[Transaction Costs](../t/transaction_costs.md):** Buying and selling assets incur costs that are not modeled in MPT.
- **[Liquidity](../l/liquidity.md):** Some assets may not be [liquid](../l/liquid.md) enough to [trade](../t/trade.md) at desired prices.
- **[Taxes](../t/taxes.md):** [Taxes](../t/taxes.md) on investment returns can significantly impact net returns.

## Extensions and Evolutions of MPT

Several advances and theories have built on the foundational concepts of MPT.

### Post-Modern Portfolio Theory (PMPT)

PMPT addresses some of the oversights of MPT, especially by focusing on [downside risk](../d/downside_risk.md)—[risk](../r/risk.md) of returns falling below a specified target level—rather than overall [risk](../r/risk.md).

### Black-Litterman Model

The [Black-Litterman model](../b/black-litterman_model.md) integrates [investor](../i/investor.md) views and [market](../m/market.md) [equilibrium](../e/equilibrium.md) to provide more [robust](../r/robust.md) estimates for returns, resolving some shortcomings related to subjective estimation in MPT.

### Behavioral Portfolio Theory (BPT)

BPT integrates psychological factors and [cognitive biases](../c/cognitive_biases_in_trading.md) into portfolio construction, contrasting sharply with the rational [investor](../i/investor.md) assumption.

### Machine Learning Integration

In modern algo-trading and fintech applications, [machine learning algorithms](../m/machine_learning_algorithms_in_trading.md) are increasingly employed to refine predictions of [asset](../a/asset.md) returns, identify patterns, and dynamically adjust portfolios according to real-time data inputs.

## Notable Fintech Companies and Tools Utilizing MPT

Several fintech companies [offer](../o/offer.md) tools and platforms that [leverage](../l/leverage.md) MPT principles:

### [Betterment](https://www.betterment.com/)
An automated investment service provider that uses MPT to create diversified portfolios tailored to individual [risk](../r/risk.md) preferences.

### [Wealthfront](https://www.wealthfront.com/)
A robo-advisor deploying MPT principles to automate [portfolio management](../p/par.md) and optimize investors' returns.

### [Portfolio Visualizer](https://www.portfoliovisualizer.com/)
Provides a suite of tools for detailed [portfolio analysis](../p/portfolio_analysis.md), utilizing MPT for efficient allocation and performance analysis.

## Conclusion

Modern Portfolio Theory remains a cornerstone of [investment strategy](../i/investment_strategy.md) and financial theory, providing powerful methodologies for portfolio construction and [risk management](../r/risk_management.md). While its assumptions and limitations necessitate further extensions and adaptations, MPT's principles continue to underpin modern innovations in both traditional [finance](../f/finance.md) and the burgeoning fields of [algorithmic trading](../a/accountability.md) and fintech. The constant evolution of these strategies ensures their relevance in effectively navigating the complexities of global [financial markets](../f/financial_market.md).

[Harry Markowitz on Nobel Prize](https://www.nobelprize.org/prizes/economic-sciences/1990/markowitz/biographical/)