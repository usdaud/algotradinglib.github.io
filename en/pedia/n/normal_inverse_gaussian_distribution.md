# Normal Inverse Gaussian Distribution

The Normal Inverse Gaussian (NIG) [distribution](../d/distribution.md) is a continuous [probability distribution](../p/probability_distribution.md) that has been widely utilized in the field of [financial modeling](../f/financial_modeling.md) and [algorithmic trading](../a/algorithmic_trading.md). This [distribution](../d/distribution.md) belongs to the subclass of the generalized hyperbolic distributions and is particularly noteworthy for its ability to capture [skewness and kurtosis](../s/skewness_and_kurtosis.md) in data, which are vital characteristics in [financial time series](../f/financial_time_series.md).

## Mathematical Definition

A random variable \(X\) is said to follow a Normal Inverse [Gaussian distribution](../g/gaussian_distribution.md) if its [probability density function](../p/probability_density_function.md) (PDF) can be expressed as:

\[ f(x; \[alpha](../a/alpha.md), \[beta](../b/beta.md), \[delta](../d/delta.md), \mu) = \frac{\[alpha](../a/alpha.md) \[delta](../d/delta.md) K_1(\[alpha](../a/alpha.md) \sqrt{\[delta](../d/delta.md)^2 + (x - \mu)^2})}{\pi \sqrt{\[delta](../d/delta.md)^2 + (x - \mu)^2}} \exp(\[delta](../d/delta.md) \sqrt{\[alpha](../a/alpha.md)^2 - \[beta](../b/beta.md)^2} + \[beta](../b/beta.md) (x - \mu)), \]

where \( K_1 \) is the modified Bessel function of the second kind with an [index](../i/index_instrument.md) of 1, and the parameters \(\[alpha](../a/alpha.md), \[beta](../b/beta.md), \[delta](../d/delta.md), \mu \) must satisfy the condition \( \[alpha](../a/alpha.md) > |\[beta](../b/beta.md)| \).

- \( \[alpha](../a/alpha.md) \): Shape parameter that determines the steepness and [kurtosis](../k/kurtosis.md) of the [distribution](../d/distribution.md).
- \( \[beta](../b/beta.md) \): Asymmetry parameter; when \( \[beta](../b/beta.md) = 0 \), the [distribution](../d/distribution.md) is symmetric.
- \( \[delta](../d/delta.md) \): Scale parameter that affects the spread of the [distribution](../d/distribution.md).
- \( \mu \): Location parameter that shifts the [distribution](../d/distribution.md) along the x-axis.

## Properties

### Moments

The NIG [distribution](../d/distribution.md) has well-defined moments, provided by the following equations:

- **Mean**: \( \mathbb{E}[X] = \mu + \delta \frac{\beta}{\sqrt{\[alpha](../a/alpha.md)^2 - \[beta](../b/beta.md)^2}} \)
- **Variance**: \( \text{Var}(X) = \[delta](../d/delta.md) \frac{\[alpha](../a/alpha.md)^2}{(\[alpha](../a/alpha.md)^2 - \[beta](../b/beta.md)^2)^{3/2}} \)
- **[Skewness](../s/skewness.md)**: \( \text{[Skewness](../s/skewness.md)}(X) = 3\[beta](../b/beta.md) / \[alpha](../a/alpha.md) \sqrt{\[delta](../d/delta.md) / \[alpha](../a/alpha.md) (\[alpha](../a/alpha.md)^2 - \[beta](../b/beta.md)^2)} \)
- **[Kurtosis](../k/kurtosis.md)**: \( \text{[Kurtosis](../k/kurtosis.md)}(X) = 3(1 + 4\frac{\[beta](../b/beta.md)^2}{\[alpha](../a/alpha.md)^2}) / (\[delta](../d/delta.md) / \[alpha](../a/alpha.md) (\[alpha](../a/alpha.md)^2 - \[beta](../b/beta.md)^2)) + 3 \)

### Characteristic Function

The characteristic function of a NIG-distributed random variable is given by:

\[ \phi_X(t) = \exp \left(i \mu t + \delta \left( \sqrt{\[alpha](../a/alpha.md)^2 - \[beta](../b/beta.md)^2} - \sqrt{\[alpha](../a/alpha.md)^2 - (\[beta](../b/beta.md) + it)^2} \right) \right) \]

### Relationship with Other Distributions

- **[Normal Distribution](../n/normal_distribution_in_trading.md)**: The NIG [distribution](../d/distribution.md) becomes a [normal distribution](../n/normal_distribution_in_trading.md) in the special case where \(\[delta](../d/delta.md) \to \infty\) and \(\[alpha](../a/alpha.md) = \[gamma](../g/gamma.md)^2\).
- **Inverse [Gaussian Distribution](../g/gaussian_distribution.md)**: When \(\[beta](../b/beta.md) = 0\), the [distribution](../d/distribution.md) simplifies to an Inverse [Gaussian distribution](../g/gaussian_distribution.md).
- **Generalized Hyperbolic [Distribution](../d/distribution.md)**: The NIG [distribution](../d/distribution.md) is a special case of the generalized hyperbolic [distribution](../d/distribution.md).

## Applications in Finance

The ability of the NIG [distribution](../d/distribution.md) to model fat tails and [skewness](../s/skewness.md) makes it particularly useful in financial applications. Some key uses include:

### Asset Pricing

The NIG [distribution](../d/distribution.md) can provide a better fit for the returns of financial assets compared to the [normal distribution](../n/normal_distribution_in_trading.md). This improved fit helps in creating more accurate pricing models.

### Risk Management

Since financial returns often exhibit heavy tails and [skewness](../s/skewness.md), using the NIG [distribution](../d/distribution.md) allows for more accurate quantification of [Value](../v/value.md) at [Risk](../r/risk.md) (VaR) and Conditional [Value](../v/value.md) at [Risk](../r/risk.md) (CVaR).

### Option Pricing

The NIG-based models help in deriving closed-form solutions for [European option](../e/european_option.md) pricing, facilitating more accurate pricing and hedging of [options](../o/options.md).

### Algorithmic Trading

[Algorithmic trading](../a/algorithmic_trading.md) strategies often require sophisticated models to predict short-term price movements. The NIG [distribution](../d/distribution.md) is employed to model the [underlying asset](../u/underlying_asset.md) prices more accurately, [offering](../o/offering.md) a competitive edge in high-frequency trading.

## Parameter Estimation

Parameter estimation for NIG [distribution](../d/distribution.md) can be performed using various methods:

### Maximum Likelihood Estimation (MLE)

MLE is a commonly used method for estimating the parameters of the NIG [distribution](../d/distribution.md). Given a set of observed data points \(x_1, x_2,..., x_n\), the log-likelihood function is maximized to find the parameter estimates.

### Method of Moments

In this approach, the sample moments (mean, variance, [skewness](../s/skewness.md), [kurtosis](../k/kurtosis.md)) are equated to the theoretical moments of the NIG [distribution](../d/distribution.md), and the resulting system of equations is solved to estimate the parameters.

### Bayesian Inference

Bayesian methods involve specifying prior distributions for the parameters and using observed data to update these priors, resulting in posterior distributions that reflect both prior beliefs and observed data.

## Software and Implementation

Several software packages and libraries facilitate the implementation of the NIG [distribution](../d/distribution.md) in financial models:

- **R**: The GeneralizedHyperbolic package for R includes functionalities for NIG [distribution](../d/distribution.md).
- **Python**: Packages like `scipy` and `statsmodels` can be extended to include NIG [distribution](../d/distribution.md) using custom implementation.
- **MATLAB**: MATLAB's [Statistics](../s/statistics.md) and [Machine Learning](../m/machine_learning.md) Toolbox contains functions to work with the Generalized Hyperbolic [Distribution](../d/distribution.md), including NIG.

### Example Code (Python)

```python
[import](../i/import.md) numpy as np
from scipy.stats [import](../i/import.md) norm, invgauss
from scipy.special [import](../i/import.md) kv

def nig_pdf(x, [alpha](../a/alpha.md), [beta](../b/beta.md), [delta](../d/delta.md), mu):
    [gamma](../g/gamma.md) = np.sqrt([alpha](../a/alpha.md)**2 - [beta](../b/beta.md)**2)
    psi = np.sqrt([delta](../d/delta.md)**2 + (x - mu)**2)
    [return](../r/return.md) ([alpha](../a/alpha.md) / np.pi) * np.exp([delta](../d/delta.md) * [gamma](../g/gamma.md) + [beta](../b/beta.md) * (x - mu)) * kv(1, [alpha](../a/alpha.md) * psi) / psi

# Example parameters
[alpha](../a/alpha.md) = 1.2
[beta](../b/beta.md) = 0.7
[delta](../d/delta.md) = 0.5
mu = 0

# Generate data
x = np.linspace(-10, 10, 100)
pdf_values = nig_pdf(x, [alpha](../a/alpha.md), [beta](../b/beta.md), [delta](../d/delta.md), mu)

# Plot the PDF
[import](../i/import.md) matplotlib.pyplot as plt
plt.plot(x, pdf_values)
plt.title("NIG [Distribution](../d/distribution.md)")
plt.xlabel("x")
plt.ylabel("Density")
plt.show()
```

## Real-World Examples

### Investment Banks

[Investment banks](../i/investment_bank_(ib).md), such as Goldman Sachs and Morgan Stanley, often utilize sophisticated statistical models incorporating NIG distributions to better manage [risk](../r/risk.md) and [trade](../t/trade.md) [derivatives](../d/derivatives.md).

### Hedge Funds

[Hedge](../h/hedge.md) funds [leverage](../l/leverage.md) NIG models for [portfolio optimization](../p/portfolio_optimization.md) and [risk management](../r/risk_management.md) to enhance returns while minimizing [risk](../r/risk.md).

### Academic Research

Numerous academic papers and research articles have been published that utilize the NIG [distribution](../d/distribution.md) for modeling [financial time series](../f/financial_time_series.md) and other economic phenomena.

## References

1. Barndorff-Nielsen, O. E. (1995). "Normal Inverse Gaussian Distributions and Stochastic [Volatility](../v/volatility.md) Modelling." Scandinavian [Journal](../j/journal.md) of [statistics](../s/statistics.md), 22(1), 1-13.
2. Prause, K. (1999). "The generalized hyperbolic model: Estimation, financial [derivatives](../d/derivatives.md), and [risk measures](../r/risk_measures.md)," PhD Thesis, University of Freiburg.
3. Rydberg, T. H. (1999). “Generalized Hyperbolic Diffusion Processes with Applications in [Finance](../f/finance.md)," [Mathematical Finance](../m/mathematical_finance.md), 9(2), 183-201.
4. McNeil, A. J., Frey, R., & Embrechts, P. (2005). "[Quantitative Risk Management](../q/quantitative_risk_management.md): Concepts, Techniques, and Tools." Princeton University Press.

---

For more information, you may visit the following companies' websites:
- Goldman Sachs
- Morgan Stanley
