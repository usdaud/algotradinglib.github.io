# Kalman Gain

## Introduction to Kalman Filter
The [Kalman Filter](../k/kalman_filter_in_trading.md) is an algorithm that uses a series of measurements observed over time, containing statistical [noise](../n/noise.md) and other inaccuracies, and produces estimates of unknown variables that tend to be more accurate than those based on a single measurement alone. The algorithm works in a two-step process: **predict** and **update**.

## Kalman Gain
Kalman [Gain](../g/gain.md), a fundamental part of the [Kalman Filter](../k/kalman_filter_in_trading.md) algorithm, helps in adjusting the weights of the predicted and observed values. The Kalman [Gain](../g/gain.md) determines how much of the new measurement should be incorporated into the updated estimate. Essentially, it balances the [trust](../t/trust.md) between predicted values and measured values. 

The formula for Kalman [Gain](../g/gain.md) \( K_t \) is:
\[ K_t = \frac{P_{t|t-1} H_t^T}{H_t P_{t|t-1} H_t^T + R_t} \]
Where:
- \( P_{t|t-1} \) is the predicted estimate [covariance](../c/covariance.md).
- \( H_t \) is the measurement matrix.
- \( R_t \) is the measurement [noise](../n/noise.md) [covariance](../c/covariance.md).

## Application in Trading
In the context of trading, the [Kalman Filter](../k/kalman_filter_in_trading.md) and Kalman [Gain](../g/gain.md) can be utilized for various purposes including, but not limited to:
- **Predicting Stock Prices**: Using historical price data to predict future movements.
- **Estimating [Volatility](../v/volatility.md)**: Filtering out the [noise](../n/noise.md) to estimate the actual [volatility](../v/volatility.md) of a stock.
- **[Algorithmic Trading](../a/algorithmic_trading.md)**: Implementing the [Kalman Filter](../k/kalman_filter_in_trading.md) in conjunction with other [trading algorithms](../t/trading_algorithms.md) for better [signal processing](../s/signal_processing_in_trading.md) and decision making.

### Stock Price Prediction
Traders often use the [Kalman Filter](../k/kalman_filter_in_trading.md) to predict future stock prices. By feeding the algorithm with historical price data, traders can produce a smoothed estimate of the stock's direction. The Kalman [Gain](../g/gain.md) comes into play by adjusting the weights given to new observed prices versus predicted prices. For instance, during high [volatility](../v/volatility.md), the Kalman [Gain](../g/gain.md) adjusts to put more weight on new observations.

### Steps to Implement
1. **Initialization**: Define the initial values for the state, [covariance](../c/covariance.md) matrices, and [noise](../n/noise.md) covariances.
2. **Prediction**: Use current state estimates to predict the next state.
3. **Update**: Incorporate new measurements using Kalman [Gain](../g/gain.md) to refine predictions.

Here’s a Python snippet demonstrating the concept:

```python
[import](../i/import.md) numpy as np
```

# Define initial parameters
initial_price = 100
state_estimate = initial_price
estimate_covariance = 1
process_noise = 0.1
measurement_noise = 0.1

# Define prediction and measurement matrices
A = 1  # Transition matrix
H = 1  # Measurement matrix

# Function for Kalman Filter

```python
def kalman_filter(measured_price):
    global state_estimate, estimate_covariance

    # Prediction Step
    state_estimate = A * state_estimate
    estimate_covariance = A * estimate_covariance * A + process_noise

    # Update Step
    kalman_gain = estimate_covariance * H / (H * estimate_covariance * H + measurement_noise)
    state_estimate = state_estimate + kalman_gain * (measured_price - H * state_estimate)
    estimate_covariance = (1 - kalman_gain * H) * estimate_covariance

    [return](../r/return.md) state_estimate
```

# Example usage with a series of measured prices

```python
measured_prices = [102, 101, 104, 107]
filtered_prices = [kalman_filter(p) for p in measured_prices]
print(filtered_prices)
```