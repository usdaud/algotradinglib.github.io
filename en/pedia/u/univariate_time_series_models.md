# Univariate Time Series Models

[Univariate time series](../u/univariate_time_series.md) models are statistical techniques used for analyzing a sequence of data points collected over time. These models utilize past information in the series itself to forecast future values. They are the bedrock of many applications in fields such as [finance](../f/finance.md), [economics](../e/economics.md), engineering, and environmental science. In the realm of [algorithmic trading](../a/algorithmic_trading.md), [univariate time series](../u/univariate_time_series.md) models are pivotal for making informed investment decisions.

### 1. Introduction to Univariate Time Series

A [univariate time series](../u/univariate_time_series.md) consists of observations on a single variable sequentially indexed over time. The dataset is denoted as \(\{y_t\}\) for \(t = 1, 2, \ldots, T\), where \(y_t\) is the observation at time \(t\) and \(T\) is the total number of time periods. The primary challenge in [time series analysis](../t/time_series_analysis.md) is to model this temporal sequence to understand its [underlying](../u/underlying.md) process and make forecasts.

### 2. Components of Time Series

Any [time series](../t/time_series.md) data can be decomposed into several components:
- **[Trend](../t/trend.md)**: The long-term progression of the series, which can be upward, downward, or constant.
- **[Seasonality](../s/seasonality.md)**: Regularly repeating patterns or cycles in the series, typically related to calendar periods.
- **Cyclic variations**: Fluctuations in the series that are not of a fixed period, longer than seasonal cycles.
- **Irregular or random variations**: Unpredictable fluctuations due to random influences.

### 3. Autoregressive (AR) Models

[Autoregressive models](../a/autoregressive.md) predict future values based on past values. An AR model of [order](../o/order.md) \(p\) (AR(p)) is defined as:

\[ y_t = \phi_1 y_{t-1} + \phi_2 y_{t-2} + \cdots + \phi_p y_{t-p} + \epsilon_t \]

where \(\phi_1, \phi_2, \ldots, \phi_p\) are parameters and \(\epsilon_t\) is [white noise](../w/white_noise_in_trading.md). The model assumes that \(y_t\) linearly depends on its previous values.

### 4. Moving Average (MA) Models

Moving average models utilize past forecast errors in a regression-like model. An MA model of [order](../o/order.md) \(q\) (MA(q)) is given by:

\[ y_t = \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \cdots + \theta_q \epsilon_{t-q} \]

where \(\theta_1, \theta_2, \ldots, \theta_q\) are parameters and \(\epsilon_t\) is [white noise](../w/white_noise_in_trading.md). The model emphasizes recent errors in the series.

### 5. Autoregressive Integrated Moving Average (ARIMA) Models

ARIMA models combine the features of AR and MA models and integrate the concept of differencing the series to achieve stationarity. An ARIMA(p,d,q) model is described by:

\[ \[Delta](../d/delta.md)^d y_t = \phi_1 \[Delta](../d/delta.md)^{d-1} y_{t-1} + \cdots + \phi_p \[Delta](../d/delta.md)^{d-1} y_{t-p} + \theta_1 \epsilon_{t-1} + \cdots + \theta_q \epsilon_{t-q} + \epsilon_t \]

Here, \(d\) denotes the number of differencing steps needed to make the series stationary.

### 6. ARIMA Seasonal (SARIMA) Models

When data exhibit both non-seasonal and seasonal properties, SARIMA models come into play. A SARIMA(p,d,q)(P,D,Q,s) model includes seasonal terms:

\[ \Phi_P(B^s) (1 - B^s)^D y_t = \Theta_Q(B^s) \epsilon_t \]

where \(\Phi_P\) and \(\Theta_Q\) are polynomials of [order](../o/order.md) \(P\) and \(Q\) in the backshift operator \(B\), and \(s\) is the seasonal period.

### 7. Exponential Smoothing Methods

[Exponential smoothing](../e/exponential_smoothing.md) is an intuitive and practical approach to [time series forecasting](../t/time_series_forecasting.md), which applies [weighted averages](../w/weighted_averages_in_trading.md) to past observations. Three common types are:
- **Simple [Exponential Smoothing](../e/exponential_smoothing.md)**: For series without [trend](../t/trend.md)/[seasonality](../s/seasonality.md),

 \[ y_t = \[alpha](../a/alpha.md) y_{t-1} + (1 - \[alpha](../a/alpha.md)) S_{t-1} \]

 where \(0 < \[alpha](../a/alpha.md) < 1\) is the smoothing parameter.
- **Holt’s Linear [Trend](../t/trend.md) Method**: Extends simple smoothing by adding a [trend](../t/trend.md) component,

 \[ S_t = \[alpha](../a/alpha.md) y_t + (1 - \[alpha](../a/alpha.md))(S_{t-1} + T_{t-1}) \]

 \[ T_t = \[beta](../b/beta.md) (S_t - S_{t-1}) + (1 - \[beta](../b/beta.md)) T_{t-1} \]

- **Holt-Winters Method**: Incorporates both [trend](../t/trend.md) and seasonal components,

 \[ S_t = \[alpha](../a/alpha.md) \frac{y_t}{I_{t-s}} + (1 - \[alpha](../a/alpha.md)) (S_{t-1} + T_{t-1}) \]

 \[ T_t = \[beta](../b/beta.md) (S_t - S_{t-1}) + (1 - \[beta](../b/beta.md)) T_{t-1} \]

 \[ I_t = \[gamma](../g/gamma.md) \frac{y_t}{S_t} + (1 - \[gamma](../g/gamma.md)) I_{t-s} \]

### 8. Model Selection and Evaluation

Selection of an appropriate model involves balancing complexity with fit, often using information criteria such as the Akaike Information Criterion (AIC) or Bayesian Information Criterion (BIC). Once a model is selected, its accuracy can be assessed through measures like Mean Absolute Error (MAE), [Mean Squared Error](../m/mean_squared_error.md) (MSE), or Mean Absolute Percentage Error (MAPE).

### 9. Applications in Algorithmic Trading

[Univariate time series](../u/univariate_time_series.md) models are extensively used in [algorithmic trading](../a/algorithmic_trading.md) for prediction and decision making. For instance:
- **Price [Forecasting](../f/forecasting.md)**: ARIMA models can forecast future stock prices based on historical prices.
- **[Volatility](../v/volatility.md) Modeling**: [GARCH models](../g/garch_models.md) can predict future [market](../m/market.md) [volatility](../v/volatility.md), which is crucial for [risk management](../r/risk_management.md).
- **[Seasonality](../s/seasonality.md) Adjustments**: SARIMA models account for seasonal effects in price changes, which is essential for [commodities trading](../c/commodities_trading.md).

Several companies specialize in providing [algorithmic trading](../a/algorithmic_trading.md) tools and platforms, including:
- **[QuantConnect](../q/quantconnect.md)**- **[AlgoTrader](../a/algotrader.md)**- **Quantopian (Acquired by [Robinhood](../r/robinhood.md))**: No direct link as the service is integrated into [Robinhood](../r/robinhood.md).

### 10. Conclusion

[Univariate time series](../u/univariate_time_series.md) models are foundational techniques in [time series analysis](../t/time_series_analysis.md), [offering](../o/offering.md) a wide array of tools for understanding and predicting temporal data. From AR and MA models to complex ARIMA and SARIMA models, each serves specific purposes and is tailored to different characteristics of the dataset. In [algorithmic trading](../a/algorithmic_trading.md), these models provide an analytical framework to forecast prices and manage investment risks effectively.
