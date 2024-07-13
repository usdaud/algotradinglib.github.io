# Markowitz Portfolio Theory

Markowitz Portfolio Theory, also known as Modern Portfolio Theory (MPT), is an investment theory developed by [Harry Markowitz](../h/harry_markowitz.md) in 1952. This theory emphasizes the role of [diversification](../d/diversification.md) to effectively manage [risk](../r/risk.md) and optimize returns in a portfolio of assets. The core principle of MPT is that an [investor](../i/investor.md) can look at [risk](../r/risk.md) and [return](../r/return.md) simultaneously through statistical measures, allowing them to construct an "[efficient frontier](../e/efficient_frontier.md)" of optimal portfolios [offering](../o/offering.md) the maximum [expected return](../e/expected_return.md) for a given level of [risk](../r/risk.md).

## Key Concepts of Markowitz Portfolio Theory

### 1. Expected Return
[Expected return](../e/expected_return.md) is the [weighted average](../w/weighted_average.md) of the probable returns of the assets in a portfolio. The weights are the proportions of the total portfolio's [value](../v/value.md) invested in each [asset](../a/asset.md).

Formula:
\[ E(R_p) = \sum_{i=1}^{n} w_i E(R_i) \]
Where:
- \(E(R_p)\) is the [expected return](../e/expected_return.md) of the portfolio,
- \(w_i\) is the proportion of the portfolio invested in [asset](../a/asset.md) \(i\),
- \(E(R_i)\) is the [expected return](../e/expected_return.md) of [asset](../a/asset.md) \(i\).

### 2. Risk (Variance and Standard Deviation)
[Risk](../r/risk.md) in MPT is primarily measured by the variance or [standard deviation](../s/standard_deviation.md) of returns. Variance measures the [dispersion](../d/dispersion.md) of the returns of an [asset](../a/asset.md) or portfolio, while [standard deviation](../s/standard_deviation.md) is the square root of variance, providing a measure of spread in the same unit as the returns.

Formula for [portfolio variance](../p/portfolio_variance.md):

\[ \sigma_p^2 = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \sigma_{ij} \]
Where:
- \(\sigma_p^2\) is the variance of the portfolio,
- \(w_i\) and \(w_j\) are the weights of the assets \(i\) and \(j\) in the portfolio,
- \(\sigma_{ij}\) is the [covariance](../c/covariance.md) between the returns of assets \(i\) and \(j\).

[Covariance](../c/covariance.md) measures how two assets move in relation to each other. A positive [covariance](../c/covariance.md) means the assets move together, while a negative [covariance](../c/covariance.md) means they move inversely.

### 3. Diversification
[Diversification](../d/diversification.md) involves spreading investments across various assets to reduce [risk](../r/risk.md). According to MPT, [diversification](../d/diversification.md) lowers the portfolio's [risk](../r/risk.md) as the [unsystematic risk](../u/unsystematic_risk.md) of individual assets can be minimized.

### 4. Efficient Frontier
The [Efficient Frontier](../e/efficient_frontier.md) represents the set of portfolios that [will](../w/will.md) provide the highest [expected return](../e/expected_return.md) for a given level of [risk](../r/risk.md). Portfolios along this frontier are considered optimally diversified.

### 5. Capital Market Line (CML) and Security Market Line (SML)
The [Capital](../c/capital.md) [Market](../m/market.md) Line extends the concept of the [Efficient Frontier](../e/efficient_frontier.md) to include a [risk-free asset](../r/risk-free_asset.md). It represents the portfolios that optimally combine [risk](../r/risk.md) and [return](../r/return.md) when a [risk-free asset](../r/risk-free_asset.md) is included. The [Security](../s/security.md) [Market](../m/market.md) Line, on the other hand, represents the [expected return](../e/expected_return.md) of an [asset](../a/asset.md) as a function of its [beta](../b/beta.md) with the [market portfolio](../m/market_portfolio.md) ([systematic risk](../s/systematic_risk.md)).

## Application of MPT in Algorithmic Trading
In [algorithmic trading](../a/algorithmic_trading.md), Markowitz Portfolio Theory can be used to automate the selection and [rebalancing](../r/rebalancing.md) of portfolios to optimize returns for a given level of [risk](../r/risk.md).
- **Automated Portfolio Construction**: Using MPT, algorithms can construct portfolios that are positioned on the [efficient frontier](../e/efficient_frontier.md), ensuring optimal [diversification](../d/diversification.md) and [risk management](../r/risk_management.md).
- **[Risk Management](../r/risk_management.md) Algorithms**: By incorporating variance and [covariance](../c/covariance.md) into algorithmic models, traders can better manage and mitigate [risk](../r/risk.md).
- **[Rebalancing Algorithms](../r/rebalancing_algorithms.md)**: Automated systems can periodically adjust portfolio weights to maintain an optimal [risk](../r/risk.md)-[return](../r/return.md) profile as [market](../m/market.md) conditions change.

## Software and Tools Implementing MPT
Several financial [software platforms](../s/software_platforms_for_trading.md) and tools implement Markowitz Portfolio Theory, [offering](../o/offering.md) both individual and institutional investors tools to optimize their portfolios.

### Example Platforms:
- **[Kensho](https://www.s&pglobal.com/marketintelligence/en/campaigns/kensho)**: Provides comprehensive AI-driven analytics, including [portfolio optimization](../p/portfolio_optimization.md) using MPT.
- **[Portfolio Visualizer](https://www.portfoliovisualizer.com/)**: A [robust](../r/robust.md) tool for [backtesting](../b/backtesting.md) and [portfolio optimization](../p/portfolio_optimization.md), incorporating MPT principles.
- **[QuantConnect](https://www.quantconnect.com/)**: [Open](../o/open.md)-source platform that allows algorithmic traders to build, backtest and deploy algorithms, including those based on MPT.

## Advanced Considerations
### 1. Constraints in MPT
Practical portfolios might face constraints such as minimum/maximum investment levels, sector caps, and tax considerations. These real-world constraints can be incorporated into MPT by using techniques such as quadratic programming.

### 2. Inclusion of Alternative Assets
Beyond traditional equities and bonds, modern investors might include alternative assets such as [real estate](../r/real_estate.md), commodities, and [private equity](../p/private_equity.md). These assets often have different [return](../r/return.md) distributions and correlations, which can be incorporated into MPT models to further enhance [diversification](../d/diversification.md).

### 3. Behavioral Factors
MPT assumes [rational behavior](../r/rational_behavior.md) and efficient markets. However, [behavioral finance](../b/behavioral_finance.md) highlights that investors often exhibit irrational behaviors and markets can be affected by sentiment. Incorporating behavioral factors into [portfolio optimization](../p/portfolio_optimization.md) is an evolving field seeking to address these limitations.

### 4. Dynamic Portfolio Allocation
Static portfolio allocation might not adapt well to changing [market](../m/market.md) conditions. Dynamic [portfolio allocation models](../p/portfolio_allocation_models.md) adjust [asset](../a/asset.md) weights in response to [market](../m/market.md) changes, macroeconomic indicators, and other variables, aiming to keep the portfolio on the [efficient frontier](../e/efficient_frontier.md) continuously.

## Critiques and Limitations
Markowitz Portfolio Theory, while fundamental, has been criticized and evolved over time. Some key critiques include:
- **Assumption of [Normal Distribution](../n/normal_distribution_in_trading.md) of Returns**: MPT assumes returns are normally distributed, which may not [hold](../h/hold.md) true for all assets, especially in turbulent markets where tail risks are prominent.
- **Estimation Errors**: Estimating the inputs (expected returns, variances, and covariances) accurately is challenging and errors can lead to suboptimal portfolios.
- **Ignoring Higher Moments**: Traditional MPT only considers mean and variance, but higher moments of the [return](../r/return.md) [distribution](../d/distribution.md) like [skewness and kurtosis](../s/skewness_and_kurtosis.md) can also impact investment decisions.

## Conclusion
Markowitz Portfolio Theory has laid the foundation for modern investment strategies by introducing a structured approach to [risk](../r/risk.md) and [return](../r/return.md) [optimization](../o/optimization.md) through [diversification](../d/diversification.md). Despite its limitations and the evolving nature of [financial markets](../f/financial_market.md), the principles of MPT remain integral to [portfolio management](../p/portfolio_management.md) and [algorithmic trading](../a/algorithmic_trading.md) strategies. Its applications and enhancements continue to evolve, incorporating new assets, methods, and behavioral insights, thus maintaining its relevance in the ever-advancing world of [finance](../f/finance.md).
