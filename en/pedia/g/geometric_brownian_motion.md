# Geometric Brownian Motion

Geometric Brownian Motion (GBM) is a continuous-time stochastic process in which the logarithm of the randomly varying quantity follows a Brownian motion (also known as a Wiener process) with drift. GBM is widely used in financial mathematics and [economics](../e/economics.md) to model stock prices and other financial instruments. The mathematical formulation of GBM is crucial in the theory of option pricing and is a cornerstone in the famous [Black-Scholes model](../b/black-scholes_model.md). In this detailed overview, we [will](../w/will.md) explore the properties, formulation, applications, and limitations of GBM, as well as relevant numerical [simulation techniques](../s/simulation_techniques.md).

### Mathematical Formulation

Geometric Brownian Motion is represented by the following stochastic differential equation (SDE):

\[ dS_t = \mu S_t \, dt + \sigma S_t \, dW_t \]

where:
- \( S_t \) is the stock price at time \( t \).
- \( \mu \) is the drift coefficient, representing the [expected return](../e/expected_return.md) of the stock.
- \( \sigma \) is the [volatility](../v/volatility.md) coefficient, representing the stock's [risk](../r/risk.md) or [variability](../v/variability.md).
- \( W_t \) is a standard Brownian motion or Wiener process.
- \( dW_t \) represents the increment of the Brownian motion.

The unique characteristic of GBM is that the relative change in the stock price (\( \frac{dS_t}{S_t} \)) depends only on the current price, making the process both Markovian and log-normal.

### Solving the SDE

To solve the SDE for \( S_t \), we apply Ito's Lemma, which gives:

\[ S_t = S_0 \exp\left( \left( \mu - \frac{\sigma^2}{2} \right)t + \sigma W_t \right) \]

where:
- \( S_0 \) is the initial stock price at time \( t = 0 \).

This solution shows that \( S_t \), the stock price, has a [log-normal distribution](../l/log-normal_distribution.md) due to the exponential of a normally distributed variable.

### Properties of Geometric Brownian Motion

1. **[Log-Normal Distribution](../l/log-normal_distribution.md)**: The prices modeled by GBM are log-normally distributed, meaning that the logarithms of the prices are normally distributed.
2. **Non-Negativity**: GBM ensures that prices remain non-negative, a critical property for modeling real-world financial instruments.
3. **Markov Property**: GBM is a Markov process, implying that the future price prediction depends only on the current price and not on the past prices.
4. **Stationarity**: The increments of a GBM process, when appropriately normalized, are stationary.

### Applications of Geometric Brownian Motion

1. **Option Pricing**: GBM is extensively used in the [Black-Scholes model](../b/black-scholes_model.md) to derive the pricing of European call and [put options](../p/put_options.md).
 - Black-Scholes Formula: To price a European [call option](../c/call_option.md), the Black-Scholes formula takes the form:
 \[ C = S_0 N(d_1) - K e^{-rT} N(d_2) \]

 where:
 \[ d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}} \]
 \[ d_2 = d_1 - \sigma \sqrt{T} \]
 - \( C \) is the [call option](../c/call_option.md) price.
 - \( K \) is the [strike price](../s/strike_price.md).
 - \( T \) is the time to [maturity](../m/maturity.md).
 - \( r \) is the [risk](../r/risk.md)-free [interest rate](../i/interest_rate.md).
 - \( N(\cdot) \) is the [cumulative distribution function](../c/cumulative_distribution_function_in_trading.md) of the standard [normal distribution](../n/normal_distribution_in_trading.md).

2. **Stock Price Modeling**: GBM is used to simulate future stock prices, enabling [risk](../r/risk.md) assessment and [portfolio management](../p/portfolio_management.md).
3. **[Risk Management](../r/risk_management.md)**: By simulating the future [distribution](../d/distribution.md) of [asset](../a/asset.md) prices, firms can quantify potential risks and set appropriate [capital](../c/capital.md) reserves.
4. **Monte Carlo Simulations**: GBM is utilized to perform Monte Carlo simulations to evaluate complex [derivative](../d/derivative.md) products and investment strategies.

### Numerical Simulation of Geometric Brownian Motion

#### Discretization Scheme

To simulate GBM numerically, we need to discretize the continuous-time process. One common discretization scheme is the Euler-Maruyama method:

\[ S_{t+\[Delta](../d/delta.md) t} = S_t \exp\left( \left( \mu - \frac{\sigma^2}{2} \right)\[Delta](../d/delta.md) t + \sigma \sqrt{\[Delta](../d/delta.md) t} Z_t \right) \]

where \( Z_t \) is a standard normal random variable.

#### Implementation Example

Here is an example in Python to simulate GBM:

```python
[import](../i/import.md) numpy as np
[import](../i/import.md) matplotlib.pyplot as plt

# Parameters
S0 = 100  # initial stock price
mu = 0.05  # drift
sigma = 0.2  # [volatility](../v/volatility.md)
T = 1.0  # [time horizon](../t/time_horizon.md)
N = 252  # number of time steps
dt = T / N  # time step
t = np.linspace(0, T, N)
np.random.seed(42)  # for reproducibility

# Simulation
S = np.zeros(N)
S[0] = S0
for i in [range](../r/range.md)(1, N):
    Z = np.random.standard_normal()
    S[i] = S[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, S)
plt.title('Geometric Brownian Motion [Simulation](../s/simulation_in_trading.md)')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.show()
```

### Limitations of Geometric Brownian Motion

1. **Constant [Volatility](../v/volatility.md)**: GBM assumes a constant [volatility](../v/volatility.md) over time, which is unrealistic in real markets where [volatility](../v/volatility.md) can change.
2. **[Log-Normal Distribution](../l/log-normal_distribution.md)**: Real stock returns may have heavier tails (fat tails) than a [log-normal distribution](../l/log-normal_distribution.md), leading to an underestimation of extreme events.
3. **No [Mean Reversion](../m/mean_reversion.md)**: GBM does not account for [mean reversion](../m/mean_reversion.md), a property observed in some financial instruments where prices tend to revert to a long-term mean.
4. **No Jumps**: GBM does not model sudden, large movements (jumps) in stock prices that can occur due to unforeseen events.

### Extensions and Alternatives to GBM

1. **[Stochastic Volatility Models](../s/stochastic_volatility_models.md)**: Models like the [Heston model](../h/heston_model.md) incorporate stochastic [volatility](../v/volatility.md) to address the limitation of constant [volatility](../v/volatility.md).
2. **Jump-Diffusion Models**: The [Merton model](../m/merton_model.md) includes jumps in addition to the diffusion process, allowing for sudden price changes.
3. **Mean-Reverting Processes**: Mean-reverting models like the Ornstein-Uhlenbeck process are used for assets that exhibit mean-reverting behavior.
4. **ARCH/[GARCH Models](../g/garch_models.md)**: These models allow [volatility](../v/volatility.md) to change over time based on past [market](../m/market.md) behavior.

In conclusion, Geometric Brownian Motion is a foundational concept in financial mathematics, providing a simple yet powerful framework for modeling stock prices and other financial instruments. Despite its limitations, it serves as a building block for more sophisticated models and remains widely used in academia and [industry](../i/industry.md) for option pricing, [risk management](../r/risk_management.md), and financial simulations.

For more information, you might want to delve further into resources provided by financial institutions and universities that specialize in financial mathematics and [stochastic processes](../s/stochastic_processes.md).
