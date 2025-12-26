# Mean-Variance Portfolio

Mean-variance portfolio theory, introduced by [Harry Markowitz](../h/harry_markowitz.md) in his seminal paper "Portfolio Selection" published in 1952, is a mathematical framework for constructing an investment portfolio in such a way that for a given level of [expected return](../e/expected_return.md), the [risk](../r/risk.md) (variance) is minimized, or equivalently, for a given level of [risk](../r/risk.md), the [expected return](../e/expected_return.md) is maximized. This theory marked the origin of modern portfolio theory (MPT).

#### Key Concepts

1. **[Expected Return](../e/expected_return.md)**: The mean [return](../r/return.md) of an [asset](../a/asset.md) or portfolio based on historical data or analyst forecasts. If \( r_i \) represents the [return](../r/return.md) of [asset](../a/asset.md) \( i \), and \( p_i \) the probability of such [return](../r/return.md), the [expected return](../e/expected_return.md) \( E(R) \) is calculated as:

 \[
 E(R) = \sum_{i} p_i \cdot r_i
 \]

2. **Variance and [Covariance](../c/covariance.md)**: Variance measures the [dispersion](../d/dispersion.md) of returns around their mean, representing [risk](../r/risk.md). For two assets, the [covariance](../c/covariance.md) indicates how their returns move together, and it's crucial for portfolio [risk](../r/risk.md) calculation. Mathematically:

 \[
 \text{Var}(R) = \sigma^2 = \sum_{i} p_i (r_i - E(R))^2
 \]

 \[
 \text{Cov}(R_A, R_B) = \sum_{i} p_i (r_A - E(R_A))(r_B - E(R_B))
 \]

3. **Portfolio [Expected Return](../e/expected_return.md) and Variance**: For a portfolio consisting of \( n \) assets, the [expected return](../e/expected_return.md) is the [weighted](../w/weighted.md) sum of the individual expected returns:

 \[
 E(R_p) = \sum_{i=1}^n w_i E(R_i)
 \]

 The variance of the portfolio, which takes into account the covariances between [asset](../a/asset.md) returns, is:

 \[
 \sigma_p^2 = \sum_{i=1}^n \sum_{j=1}^n w_i w_j \text{Cov}(R_i, R_j)
 \]

 Where \( w_i \) indicates the weight of [asset](../a/asset.md) \( i \) in the portfolio.

4. **[Efficient Frontier](../e/efficient_frontier.md)**: A graphical representation of the set of portfolios that provide the highest [expected return](../e/expected_return.md) for a defined level of [risk](../r/risk.md). The portfolios on the [efficient frontier](../e/efficient_frontier.md) are considered optimal. The [efficient frontier](../e/efficient_frontier.md) is typically depicted in a plot of portfolio [return](../r/return.md) (y-axis) against [risk](../r/risk.md) (x-axis).

5. **[Capital](../c/capital.md) [Market](../m/market.md) Line (CML)**: When a [risk-free asset](../r/risk-free_asset.md) is introduced into the portfolio mix, the [Capital](../c/capital.md) [Market](../m/market.md) Line can be derived, which represents portfolios that optimally combine [risk](../r/risk.md)-free assets with the [market portfolio](../m/market_portfolio.md).

 \[
 E(R_p) = R_f + \frac{E(R_m) - R_f}{\sigma_m} \sigma_p
 \]

 Where \( R_f \) is the [risk](../r/risk.md)-free rate, \( E(R_m) \) is the [expected return](../e/expected_return.md) of the [market portfolio](../m/market_portfolio.md), and \( \sigma_m \) is the [standard deviation](../s/standard_deviation.md) of the [market](../m/market.md) returns.

6. **[Sharpe Ratio](../s/sharpe_ratio.md)**: An [index](../i/index_instrument.md) that measures the [excess return](../e/excess_return.md) per unit of [risk](../r/risk.md) of an investment. It is calculated as:

 \[
 \text{[Sharpe Ratio](../s/sharpe_ratio.md)} = \frac{E(R_p) - R_f}{\sigma_p}
 \]

#### Optimization Process

The process of [mean-variance optimization](../m/mean-variance_optimization.md) involves the following steps:

1. **Identify Input Estimates**: Determine the expected returns, variances, and covariances for all assets in the portfolio.
2. **Construct Portfolios**: Generate a set of portfolios with different weights.
3. **Calculate Portfolio [Return](../r/return.md) and [Risk](../r/risk.md)**: For each portfolio, compute the [expected return](../e/expected_return.md) and [risk](../r/risk.md).
4. **Efficient Portfolio Series**: Identify portfolios that lie on the [efficient frontier](../e/efficient_frontier.md).
5. **Choose Optimal Portfolio**: Select the optimum portfolio based on [investor](../i/investor.md) preferences regarding [risk](../r/risk.md) and [return](../r/return.md), which maximizes the [Sharpe Ratio](../s/sharpe_ratio.md).

#### Applications and Implications

1. **Portfolio Construction**: This theory is extensively used in constructing diversified investment portfolios for mutual funds, [hedge](../h/hedge.md) funds, pension funds, etc. Companies such as **BlackRock** and **Vanguard** employ advanced versions of MVT in their [portfolio management](../p/portfolio_management.md) strategies.

2. **[Risk Management](../r/risk_management.md)**: Mean-[variance analysis](../v/variance_analysis.md) helps investors understand the [trade](../t/trade.md)-off between [risk](../r/risk.md) and [return](../r/return.md), allowing them to make better [risk management](../r/risk_management.md) decisions.

3. **Passive vs. [Active Management](../a/active_management.md)**: MVT has implications in the debate between active and passive [portfolio management](../p/portfolio_management.md). It provides a foundation for the development of [index](../i/index_instrument.md) funds and [exchange](../e/exchange.md)-traded funds (ETFs).

#### Criticisms and Limitations

1. **Assumption of Normality**: Returns are assumed to follow a [normal distribution](../n/normal_distribution_in_trading.md), which may not [hold](../h/hold.md) true in real markets.
2. **Estimation of Parameters**: Accurate estimation of expected returns, variances, and covariances is challenging.
3. **Changing Dynamics**: [Market](../m/market.md) conditions are dynamic, and historical data may not accurately predict future performance.
4. **[Transaction Costs](../t/transaction_costs.md) and [Taxes](../t/taxes.md)**: MVT doesn’t account for [transaction costs](../t/transaction_costs.md) and [taxes](../t/taxes.md), which are significant in real-world [investing](../i/investing.md).

#### Advances and Extensions

1. **Post-Modern Portfolio Theory (PMPT)**: Enhances MPT by addressing its limitations, considering more realistic assumptions about [return](../r/return.md) distributions, and highlighting [downside risk](../d/downside_risk.md).

2. **[Black-Litterman Model](../b/black-litterman_model.md)**: An advanced portfolio construction model that incorporates [investor](../i/investor.md) views into the [covariance](../c/covariance.md) structure of returns.

3. **[Robust](../r/robust.md) [Portfolio Optimization](../p/portfolio_optimization.md)**: Attempts to create portfolios that are less sensitive to errors in the input estimates, enhancing the stability of investment decisions.

4. **[Machine Learning](../m/machine_learning.md) in [Portfolio Management](../p/portfolio_management.md)**: Companies such as **AQR Capital Management** are leveraging [machine learning](../m/machine_learning.md) techniques to improve the estimation of model parameters and incorporate non-linear relationships among [asset](../a/asset.md) returns.

In conclusion, mean-variance portfolio theory has been a cornerstone of modern [finance](../f/finance.md), providing a systematic and quantitative approach for portfolio construction and management. Despite its limitations, it remains a fundamental tool for investors seeking to optimize the [risk](../r/risk.md)-[return](../r/return.md) characteristics of their investment portfolios.
