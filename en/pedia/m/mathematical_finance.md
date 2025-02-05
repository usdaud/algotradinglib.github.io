# Mathematical Finance

Mathematical [finance](../f/finance.md), also known as [quantitative finance](../q/quantitative_finance.md), is a field of applied mathematics concerned with the [financial markets](../f/financial_market.md). It uses [mathematical models](../m/mathematical_models_in_trading.md) and computational techniques to analyze [financial markets](../f/financial_market.md), derive pricing models, manage [risk](../r/risk.md), and optimize portfolios. Below are some critical areas covered under the umbrella of mathematical [finance](../f/finance.md):

## 1. Financial Modeling

### 1.1 Black-Scholes Model
The [Black-Scholes model](../b/black-scholes_model.md) is one of the most famous [mathematical models](../m/mathematical_models_in_trading.md) for pricing [options](../o/options.md) and other financial [derivatives](../d/derivatives.md). It provides a theoretical estimate of the price of European-style [options](../o/options.md) and is based on several assumptions including constant [volatility](../v/volatility.md) and the [log-normal distribution](../l/log-normal_distribution.md) of stock prices.

#### The Black-Scholes Formula
\[
C(S, t) = S_0N(d_1) - Xe^{-rt}N(d_2)
\]
Where:
- \(d_1 = \frac{\ln(\frac{S_0}{X}) + (r + \frac{\sigma^2}{2})t}{\sigma\sqrt{t}}\)
- \(d_2 = d_1 - \sigma\sqrt{t}\)
- \(N(\cdot)\) is the [cumulative distribution function](../c/cumulative_distribution_function_in_trading.md) of the standard [normal distribution](../n/normal_distribution_in_trading.md)
- \(S_0\) is the current stock price
- \(X\) is the [strike price](../s/strike_price.md)
- \(r\) is the [risk](../r/risk.md)-free [interest rate](../i/interest_rate.md)
- \(\sigma\) is the [volatility](../v/volatility.md) of the stock
- \(t\) is the time until the option's expiration

### 1.2 Binomial Option Pricing Model
The [binomial option pricing model](../b/binomial_option_pricing_model.md) is another discrete-time model for pricing [options](../o/options.md). Unlike the [Black-Scholes model](../b/black-scholes_model.md), it uses a simple tree of possible future stock prices constructed iteratively. This model is particularly useful for American [options](../o/options.md) where the holder has the right to [exercise](../e/exercise.md) the option at any time before expiration.

#### The Binomial Formula
\[
C = \frac{1}{(1+r)^t} \left[ pC_u + (1-p)C_d \right]
\]
Where:
- \(p = \frac{e^{r\[Delta](../d/delta.md) t} - d}{u - d}\)
- \(u\) is the [factor](../f/factor.md) by which the price increases
- \(d\) is the [factor](../f/factor.md) by which the price decreases
- \(C_u\) and \(C_d\) are the option values at the respective nodes

## 2. Risk Management

### 2.1 Value at Risk (VaR)
[Value](../v/value.md) at [Risk](../r/risk.md) is a statistical technique used to measure the [risk](../r/risk.md) of loss on a portfolio. This measure estimates the potential loss in [value](../v/value.md) of a portfolio over a defined period for a given [confidence interval](../c/confidence_interval.md). 

#### VaR Formula
\[
\text{VaR} = \Phi^{-1}(1 - \[alpha](../a/alpha.md)) \cdot \sigma_P \cdot \sqrt{T}
\]
Where:
- \(\Phi^{-1}\) is the inverse of the [cumulative distribution function](../c/cumulative_distribution_function_in_trading.md) of the standard [normal distribution](../n/normal_distribution_in_trading.md)
- \(\[alpha](../a/alpha.md)\) is the confidence level
- \(\sigma_P\) is the portfolio's [standard deviation](../s/standard_deviation.md)
- \(T\) is the [time horizon](../t/time_horizon.md)

### 2.2 Conditional Value at Risk (CVaR)
Conditional [Value](../v/value.md) at [Risk](../r/risk.md), also known as Expected [Shortfall](../s/shortfall.md), is a [risk](../r/risk.md) measure that provides an average of losses that occur beyond the VaR threshold. It is considered to be a more coherent measure of [risk](../r/risk.md) compared to VaR.

#### CVaR Formula
\[
\text{CVaR} = \mathbb{E}[L | L \geq \text{VaR}]
\]
Where:
- \(L\) is the [loss distribution](../l/loss_distribution.md)
- \(\mathbb{E}[\cdot]\) denotes the [expected value](../e/expected_value.md)

## 3. Portfolio Optimization

### 3.1 Mean-Variance Optimization
Introduced by [Harry Markowitz](../h/harry_markowitz.md) in 1952, [Mean-Variance Optimization](../m/mean-variance_optimization.md) is a quantitative tool used to construct portfolios that maximize [return](../r/return.md) for a given level of [risk](../r/risk.md). The [efficient frontier](../e/efficient_frontier.md) represents the set of optimal portfolios.

#### Mean-Variance Optimization Formula
\[
\frac{\text{E}[R_P] - R_f}{\sigma_P}
\]
Where:
- \(E[R_P]\) is the [expected return](../e/expected_return.md) of the portfolio
- \(R_f\) is the [risk](../r/risk.md)-free rate
- \(\sigma_P\) is the [standard deviation](../s/standard_deviation.md) of portfolio [return](../r/return.md)

### 3.2 Capital Asset Pricing Model (CAPM)
CAPM is a model used to determine the theoretical [expected return](../e/expected_return.md) on an [asset](../a/asset.md) based on its [systematic risk](../s/systematic_risk.md). It is widely used to price risky securities and to calculate the [cost of capital](../c/cost_of_capital.md).

#### CAPM Formula
\[
E[R_i] = R_f + \beta_i (E[R_m] - R_f)
\]
Where:
- \(E[R_i]\) is the [expected return](../e/expected_return.md) of the [asset](../a/asset.md)
- \(R_f\) is the [risk](../r/risk.md)-free rate
- \(\beta_i\) is the [beta](../b/beta.md) of the [asset](../a/asset.md)
- \(E[R_m]\) is the [expected return](../e/expected_return.md) of the [market](../m/market.md)

## 4. Time Series Analysis

### 4.1 Autoregressive Integrated Moving Average (ARIMA)
ARIMA models are used to understand and predict future points in a [time series](../t/time_series.md). They are particularly suited to datasets with trends and are characterized by parameters p, d, and q.

#### ARIMA Model
\[
ARIMA(p, d, q)
\]
Where:
- \(p\) is the number of lag observations included in the model
- \(d\) is the degree of differencing
- \(q\) is the size of the moving average window

### 4.2 Generalized Autoregressive Conditional Heteroskedasticity (GARCH)
[GARCH models](../g/garch_models.md) are used to estimate the [volatility](../v/volatility.md) of returns in [financial markets](../f/financial_market.md). The model captures the time-varying [volatility](../v/volatility.md) by including past variances and past errors.

#### GARCH Model
\[
\sigma_t^2 = \alpha_0 + \alpha_1 \epsilon_{t-1}^2 + \beta_1 \sigma_{t-1}^2
\]
Where:
- \(\sigma_t^2\) is the conditional variance
- \(\alpha_0\), \(\alpha_1\), \(\beta_1\) are the coefficients
- \(\epsilon_{t-1}^2\) is the lagged squared residual

## 5. Stochastic Calculus

### 5.1 Itô's Lemma
Itô's Lemma is a fundamental result in [stochastic calculus](../s/stochastic_calculus.md), which is used to determine the differential of a function of a stochastic process. It is particularly useful for option pricing.

#### Itô's Lemma
If \(X_t\) is a function of a stochastic process \(Y_t\), then:
\[
dX_t = \left( \frac{\partial X}{\partial t} + \frac{\partial X}{\partial Y} \mu_t + \frac{1}{2} \frac{\partial^2 X}{\partial Y^2} \sigma_t^2 \right) dt + \frac{\partial X}{\partial Y} \sigma_t dW_t
\]
Where:
- \(\mu_t\) and \(\sigma_t\) are the drift and [volatility](../v/volatility.md)
- \(dW_t\) is the Wiener process

### 5.2 Martingales
A martingale is a stochastic process that represents a fair game, where the conditional expectation of the next [value](../v/value.md), given all previous values, is equal to the [present value](../p/present_value.md).

#### Martingale Definition
\[
\mathbb{E}[X_{t+1} | \mathcal{F}_t] = X_t
\]
Where:
- \(\mathcal{F}_t\) is the filtration or information up to time \(t\)
- \(X_t\) is the [value](../v/value.md) of the process at time \(t\)

## 6. Computational Methods

### 6.1 Monte Carlo Simulation
[Monte Carlo Simulation](../m/monte_carlo_simulation.md) is a computational algorithm that uses repeated random [sampling](../s/sampling.md) to obtain numerical results. It is widely used in [finance](../f/finance.md) to model the probability of different outcomes.

#### Monte Carlo Steps:
1. Define a domain of possible inputs
2. Generate random inputs
3. Perform a deterministic computation on the inputs
4. Aggregate the results

### 6.2 Finite Difference Methods
[Finite difference methods](../f/finite_difference_methods.md) are numerical techniques for solving differential equations by approximating them with difference equations. They are often used to solve the Black-Scholes PDE.

#### Finite Difference Scheme:
- Explicit scheme
- Implicit scheme
- Crank-Nicolson scheme

## Companies and Institutions Specializing in Mathematical Finance

### 6.1 Quantitative Brokers (https://www.quantitativebrokers.com/)
Quantitative Brokers provides advanced algorithms and analytics for agency [execution](../e/execution.md) and trading. Their methodologies are deeply rooted in mathematical [finance](../f/finance.md) and computational techniques.

### 6.2 WorldQuant (https://www.worldquant.com/)
WorldQuant is a quantitative [investment management](../i/investment_management.md) [firm](../f/firm.md) that uses sophisticated [mathematical models](../m/mathematical_models_in_trading.md) to develop [trading strategies](../t/trading_strategies.md) and manage portfolios.

### 6.3 Jane Street (https://www.janestreet.com/)
Jane Street is a trading [firm](../f/firm.md) and [liquidity](../l/liquidity.md) provider with a focus on using advanced quantitative methods for trading in global [financial markets](../f/financial_market.md).

### 6.4 Renaissance Technologies (https://www.rentec.com/)
Renaissance Technologies is a highly renowned quantitative investment [firm](../f/firm.md) known for its Medallion [Fund](../f/fund.md), which utilizes sophisticated [mathematical models](../m/mathematical_models_in_trading.md) for [trading strategies](../t/trading_strategies.md).

### 6.5 Two Sigma (https://www.twosigma.com/)
Two Sigma is a top-tier quantitative [hedge fund](../h/hedge_fund.md) that leverages [data science](../d/data_science_in_trading.md), [machine learning](../m/machine_learning.md), and applied mathematics to devise investment strategies.

## Conclusion

Mathematical [finance](../f/finance.md) is an extensive and complex field that incorporates various mathematical and computational techniques to address problems in [financial markets](../f/financial_market.md), such as pricing, [risk management](../r/risk_management.md), and [portfolio optimization](../p/portfolio_optimization.md). It continues to evolve, driven by advances in computational power and the availability of extensive data.
