# Normal Inverse Gaussian Distribution

The Normal Inverse Gaussian (NIG) distribution is a continuous probability distribution that has been widely utilized in the field of [financial modeling](../f/financial_modeling.md) and [algorithmic trading](../a/algorithmic_trading.md). This distribution belongs to the subclass of the generalized hyperbolic distributions and is particularly noteworthy for its ability to capture [skewness and kurtosis](../s/skewness_and_kurtosis.md) in data, which are vital characteristics in [financial time series](../f/financial_time_series.md).

## Mathematical Definition

A random variable \(X\) is said to follow a Normal Inverse [Gaussian distribution](../g/gaussian_distribution.md) if its [probability density function](../p/probability_density_function.md) (PDF) can be expressed as:

\[ f(x; \alpha, \beta, \delta, \mu) = \frac{\alpha \delta K_1(\alpha \sqrt{\delta^2 + (x - \mu)^2})}{\pi \sqrt{\delta^2 + (x - \mu)^2}} \exp(\delta \sqrt{\alpha^2 - \beta^2} + \beta (x - \mu)), \]

where \( K_1 \) is the modified Bessel function of the second kind with an index of 1, and the parameters \(\alpha, \beta, \delta, \mu \) must satisfy the condition \( \alpha > |\beta| \).

- \( \alpha \): Shape parameter that determines the steepness and kurtosis of the distribution.
- \( \beta \): Asymmetry parameter; when \( \beta = 0 \), the distribution is symmetric.
- \( \delta \): Scale parameter that affects the spread of the distribution.
- \( \mu \): Location parameter that shifts the distribution along the x-axis.

## Properties

### Moments

The NIG distribution has well-defined moments, provided by the following equations:

- **Mean**: \( \mathbb{E}[X] = \mu + \delta \frac{\beta}{\sqrt{\alpha^2 - \beta^2}} \)
- **Variance**: \( \text{Var}(X) = \delta \frac{\alpha^2}{(\alpha^2 - \beta^2)^{3/2}} \)
- **Skewness**: \( \text{Skewness}(X) = 3\beta / \alpha \sqrt{\delta / \alpha (\alpha^2 - \beta^2)} \)
- **Kurtosis**: \( \text{Kurtosis}(X) = 3(1 + 4\frac{\beta^2}{\alpha^2}) / (\delta / \alpha (\alpha^2 - \beta^2)) + 3 \)

### Characteristic Function

The characteristic function of a NIG-distributed random variable is given by:

\[ \phi_X(t) = \exp \left(i \mu t + \delta \left( \sqrt{\alpha^2 - \beta^2} - \sqrt{\alpha^2 - (\beta + it)^2} \right) \right) \]

### Relationship with Other Distributions

- **Normal Distribution**: The NIG distribution becomes a normal distribution in the special case where \(\delta \to \infty\) and \(\alpha = \gamma^2\).
- **Inverse [Gaussian Distribution](../g/gaussian_distribution.md)**: When \(\beta = 0\), the distribution simplifies to an Inverse [Gaussian distribution](../g/gaussian_distribution.md).
- **Generalized Hyperbolic Distribution**: The NIG distribution is a special case of the generalized hyperbolic distribution.

## Applications in Finance

The ability of the NIG distribution to model fat tails and skewness makes it particularly useful in financial applications. Some key uses include:

### Asset Pricing

The NIG distribution can provide a better fit for the returns of financial assets compared to the normal distribution. This improved fit helps in creating more accurate pricing models.

### Risk Management

Since financial returns often exhibit heavy tails and skewness, using the NIG distribution allows for more accurate quantification of Value at Risk (VaR) and Conditional Value at Risk (CVaR).

### Option Pricing

The NIG-based models help in deriving closed-form solutions for European option pricing, facilitating more accurate pricing and hedging of options.

### Algorithmic Trading

[Algorithmic trading](../a/algorithmic_trading.md) strategies often require sophisticated models to predict short-term price movements. The NIG distribution is employed to model the underlying asset prices more accurately, offering a competitive edge in high-frequency trading.

## Parameter Estimation

Parameter estimation for NIG distribution can be performed using various methods:

### Maximum Likelihood Estimation (MLE)

MLE is a commonly used method for estimating the parameters of the NIG distribution. Given a set of observed data points \(x_1, x_2, ..., x_n\), the log-likelihood function is maximized to find the parameter estimates.

### Method of Moments

In this approach, the sample moments (mean, variance, skewness, kurtosis) are equated to the theoretical moments of the NIG distribution, and the resulting system of equations is solved to estimate the parameters.

### Bayesian Inference

Bayesian methods involve specifying prior distributions for the parameters and using observed data to update these priors, resulting in posterior distributions that reflect both prior beliefs and observed data.

## Software and Implementation

Several software packages and libraries facilitate the implementation of the NIG distribution in financial models:

- **R**: The GeneralizedHyperbolic package for R includes functionalities for NIG distribution.
- **Python**: Packages like `scipy` and `statsmodels` can be extended to include NIG distribution using custom implementation.
- **MATLAB**: MATLAB's Statistics and Machine Learning Toolbox contains functions to work with the Generalized Hyperbolic Distribution, including NIG.

### Example Code (Python)

```python
import numpy as np
from scipy.stats import norm, invgauss
from scipy.special import kv

def nig_pdf(x, alpha, beta, delta, mu):
    gamma = np.sqrt(alpha**2 - beta**2)
    psi = np.sqrt(delta**2 + (x - mu)**2)
    return (alpha / np.pi) * np.exp(delta * gamma + beta * (x - mu)) * kv(1, alpha * psi) / psi

# Example parameters
alpha = 1.2
beta = 0.7
delta = 0.5
mu = 0

# Generate data
x = np.linspace(-10, 10, 100)
pdf_values = nig_pdf(x, alpha, beta, delta, mu)

# Plot the PDF
import matplotlib.pyplot as plt
plt.plot(x, pdf_values)
plt.title("NIG Distribution")
plt.xlabel("x")
plt.ylabel("Density")
plt.show()
```

## Real-World Examples

### Investment Banks

Investment banks, such as Goldman Sachs and Morgan Stanley, often utilize sophisticated statistical models incorporating NIG distributions to better manage risk and trade [derivatives](../d/derivatives.md).

### Hedge Funds

Hedge funds leverage NIG models for [portfolio optimization](../p/portfolio_optimization.md) and [risk management](../r/risk_management.md) to enhance returns while minimizing risk.

### Academic Research

Numerous academic papers and research articles have been published that utilize the NIG distribution for modeling [financial time series](../f/financial_time_series.md) and other economic phenomena.

## References

1. Barndorff-Nielsen, O. E. (1995). "Normal Inverse Gaussian Distributions and Stochastic Volatility Modelling." Scandinavian Journal of statistics, 22(1), 1-13.
2. Prause, K. (1999). "The generalized hyperbolic model: Estimation, financial [derivatives](../d/derivatives.md), and risk measures," PhD Thesis, University of Freiburg.
3. Rydberg, T. H. (1999). “Generalized Hyperbolic Diffusion Processes with Applications in Finance," [Mathematical Finance](../m/mathematical_finance.md), 9(2), 183-201.
4. McNeil, A. J., Frey, R., & Embrechts, P. (2005). "[Quantitative Risk Management](../q/quantitative_risk_management.md): Concepts, Techniques, and Tools." Princeton University Press.

---

For more information, you may visit the following companies' websites:
- [Goldman Sachs](https://www.goldmansachs.com/)
- [Morgan Stanley](https://www.morganstanley.com/)
