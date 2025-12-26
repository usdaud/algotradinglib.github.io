# Autoregressive Integrated Moving Average (ARIMA)

The Autoregressive Integrated Moving Average (ARIMA) model is a powerful statistical tool used for [time series forecasting](../t/time_series_forecasting.md). It is designed to identify and exploit patterns in [time series](../t/time_series.md) data, making it particularly useful in the field of [algorithmic trading](../a/accountability.md), where accurate predictions of future prices can lead to profitable [trading strategies](../t/trading_strategies.md). ARIMA models can [handle](../h/handle.md) a variety of [time series](../t/time_series.md) characteristics, including trends and [seasonality](../s/seasonality.md), making them a versatile choice for traders and data scientists alike.

## Components of ARIMA

ARIMA models are composed of three main components:
1. **Autoregressive (AR) term**: This component uses past values of the series to model the current [value](../v/value.md). The number of lagged observations included is denoted by the parameter `p`.
2. **Integrated (I) term**: This component represents the differencing applied to the series to make it stationary, which is a prerequisite for many [time series](../t/time_series.md) models to function correctly. The level of differencing is indicated by the parameter `d`.
3. **Moving Average (MA) term**: This component uses past forecast errors in a regression model to predict future values. The number of lagged forecast errors is denoted by the parameter `q`.

### Autoregressive (AR) Term
The autoregressive part of the ARIMA model is essentially a regression of the [time series](../t/time_series.md) on itself. It assumes that the current [value](../v/value.md) of the series can be explained by a linear combination of its previous values. Mathematically, the AR term can be expressed as:

\[ Y_t = \phi_1 Y_{t-1} + \phi_2 Y_{t-2} +... + \phi_p Y_{t-p} + \epsilon_t \]

Where:
- \( Y_t \) is the current [value](../v/value.md) of the series.
- \( \phi_1, \phi_2,..., \phi_p \) are the coefficients.
- \( \epsilon_t \) is the [error term](../e/error_term.md).

### Integrated (I) Term
The integrated part of the ARIMA model involves differencing the [time series](../t/time_series.md) data to make it stationary. Stationarity means that the statistical properties of the series, such as mean and variance, are constant over time. A non-stationary series can have trends, [seasonality](../s/seasonality.md), and other structures that need to be eliminated to apply ARIMA effectively. The differencing process can be mathematically represented as:

\[ Y'_t = Y_t - Y_{t-1} \]

For first-[order](../o/order.md) differencing, this can be written as:

\[ Y''_t = Y'_t - Y'_{t-1} \]

Where:
- \( Y'_t \) is the first-differenced series.
- \( Y''_t \) is the second-differenced series.

The parameter `d` indicates the number of times differencing is applied.

### Moving Average (MA) Term
The moving average part of the ARIMA model involves using past forecast errors to predict future values. This component accounts for the unexplained part of the series by incorporating the errors from previous periods. The mathematical representation of the MA term is:

\[ Y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} +... + \theta_q \epsilon_{t-q} \]

Where:
- \( \mu \) is the mean of the series.
- \( \epsilon_t, \epsilon_{t-1}, \epsilon_{t-2},..., \epsilon_{t-q} \) are the forecast errors.
- \( \theta_1, \theta_2,..., \theta_q \) are the coefficients.

## Model Identification

Before an ARIMA model can be constructed, it's crucial to identify the appropriate values of the parameters `p`, `d`, and `q`. This process involves several steps:

1. **Differencing to achieve stationarity**: Plot the [time series](../t/time_series.md) and difference it until it appears stationary. The number of differences applied [will](../w/will.md) determine the parameter `d`.
2. **[Autocorrelation](../a/autocorrelation.md) Function (ACF) and Partial [Autocorrelation](../a/autocorrelation.md) Function (PACF)**: Examine the ACF and PACF plots to identify the potential values of `p` and `q`.
 - The ACF plot shows the [correlation](../c/correlation.md) between the [time series](../t/time_series.md) and its past values.
 - The PACF plot shows the partial [correlation](../c/correlation.md) after removing the influence of earlier lags.

### ACF and PACF Interpretation
- **AR Model (Autoregressive)**: If the series is an AR process, the PACF [will](../w/will.md) show a significant spike at the lag corresponding to the [order](../o/order.md) `p`, with all other lags being insignificant. The ACF [will](../w/will.md) show a gradual decay.
- **MA Model (Moving Average)**: If the series is an MA process, the ACF [will](../w/will.md) show a significant spike at the lag corresponding to the [order](../o/order.md) `q`, with all other lags being insignificant. The PACF [will](../w/will.md) show a gradual decay.
- **ARMA Model**: For mixed ARMA processes, the identification is more complex and usually involves a combination of significant spikes in both ACF and PACF plots.

## Building the ARIMA Model

Once the parameters `p`, `d`, and `q` are determined, the next step is to fit the ARIMA model to the [time series](../t/time_series.md) data. This involves estimating the coefficients and validating the model through residual diagnostics.

### Parameter Estimation
The parameters of the ARIMA model are typically estimated using the Maximum Likelihood Estimation (MLE) method. This method finds the parameter values that maximize the likelihood function, ensuring that the observed data is most probable under the fitted model.

### Model Diagnostics
After fitting the model, it's essential to validate it to ensure that the residuals (the differences between the observed and fitted values) resemble [white noise](../w/white_noise_in_trading.md), indicating that all patterns have been adequately captured by the model.

- **[Residual Analysis](../r/residual_analysis_in_trading.md)**: Plot the residuals and examine their ACF and PACF plots. They should show no significant correlations, indicating that the residuals are random.
- **Ljung-Box Test**: This statistical test checks whether any group of autocorrelations in the residuals is different from zero. A significant result suggests that the model has not adequately captured the [time series](../t/time_series.md) structure.

## Model Validation and Forecasting

Once the model diagnostics indicate a good fit, the ARIMA model can be used for [forecasting](../f/forecasting.md). It's important to evaluate the model's performance using out-of-sample data to ensure its predictive power.

### Forecast Accuracy Metrics
Common metrics to assess [forecast accuracy](../f/forecast_accuracy.md) include:
- **Mean Absolute Error (MAE)**: Measures the average magnitude of forecast errors.
- **Root [Mean Squared Error](../m/mean_squared_error.md) (RMSE)**: Averages the squares of the forecast errors, giving more weight to larger errors.
- **Mean Absolute Percentage Error (MAPE)**: Measures the prediction accuracy as a percentage.

### Forecasting
The ARIMA model can generate forecasts by projecting the [time series](../t/time_series.md) into the future, using the fitted parameters and past values. The [forecasting](../f/forecasting.md) process involves:
1. Predicting future values using the ARIMA model equations.
2. Constructing [confidence intervals](../c/confidence_intervals.md) around the forecasts to account for [uncertainty](../u/uncertainty_in_trading.md).

## Seasonal ARIMA (SARIMA)

For [time series](../t/time_series.md) with [seasonality](../s/seasonality.md), the Seasonal ARIMA (SARIMA) model extends the basic ARIMA framework by incorporating seasonal autoregressive and moving average terms. The SARIMA model is denoted as:

\[ SARIMA(p, d, q) \times (P, D, Q)_s \]

Where:
- \( (P, D, Q) \) are the seasonal components analogous to \( (p, d, q) \).
- \( s \) is the seasonal period (e.g., 12 for monthly data with annual [seasonality](../s/seasonality.md)).

### Seasonal Differencing
Seasonal differencing involves subtracting the [value](../v/value.md) from the same season in the previous period. For example, first-[order](../o/order.md) seasonal differencing can be represented as:

\[ Y'_t = Y_t - Y_{t-s} \]

Where \( s \) is the seasonal period.

### SARIMA Model Identification
Identifying SARIMA models requires analyzing seasonal lags in the ACF and PACF plots and applying the same principles used for non-seasonal ARIMA models.

## ARIMA in Algorithmic Trading

In [algorithmic trading](../a/accountability.md), ARIMA models are used to forecast [asset](../a/asset.md) prices, [volatility](../v/volatility.md), and other financial metrics. Accurate forecasts enable traders to design strategies that exploit predicted [market](../m/market.md) movements.

### Practical Considerations
- **Data Frequency**: ARIMA models can be applied to various data frequencies, such as daily, hourly, or minute-by-minute trading data.
- **Stationarity**: Ensuring data stationarity is critical for model accuracy, often requiring transformation techniques like logarithms or differencing.
- **Outliers and [Structural Breaks](../s/structural_breaks_in_trading.md)**: [Financial time series](../f/financial_time_series.md) may contain outliers or abrupt changes. ARIMA models need to account for these factors to prevent biased forecasts.

### Example Use Case
A [trader](../t/trader.md) might use an ARIMA model to forecast the closing prices of a stock. By fitting a model to historical price data, the [trader](../t/trader.md) can predict future prices and develop a [trading strategy](../t/trading_strategy.md) based on these predictions. For instance, if the forecast indicates a rising [trend](../t/trend.md), the [trader](../t/trader.md) might take a long position, while a declining [trend](../t/trend.md) might prompt a short position.

## Software and Tools for ARIMA

Several [software tools](../s/software_tools_for_trading.md) and libraries facilitate the implementation of ARIMA models:

### Python
- **Statsmodels**: A comprehensive library for statistical modeling, including ARIMA and SARIMA.
 - Documentation: Statsmodels
- **pmdarima**: An extension of Statsmodels for automatic ARIMA fitting.
 - Documentation: pmdarima

### R
- **forecast**: A widely-used package for [time series forecasting](../t/time_series_forecasting.md), supporting ARIMA and other models.
 - Documentation: forecast

### MATLAB
- **[Econometrics](../e/econometrics_in_trading.md) Toolbox**: Provides functions for ARIMA modeling and Bayesian analysis.
 - Documentation: Econometrics Toolbox

## Conclusion

The ARIMA model is a versatile and powerful tool for [time series forecasting](../t/time_series_forecasting.md), with extensive applications in [algorithmic trading](../a/accountability.md). By capturing patterns in historical data, ARIMA models enable traders to make informed decisions, enhancing their profitability. Proper model identification, validation, and application are essential to harness the full potential of ARIMA models in predicting future [market](../m/market.md) movements.