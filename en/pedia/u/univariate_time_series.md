# Univariate Time Series in Algorithmic Trading

## Introduction

[Algorithmic trading](../a/algorithmic_trading.md), often termed `algo-trading`, involves the use of computer algorithms to execute [trading strategies](../t/trading_strategies.md). One of the essential components in designing these strategies is analyzing historical financial data to predict future price movements. A univariate time series comes into play as it consists of a sequence of observations of the same variable collected over time, making it particularly useful for this type of analysis.

A univariate time series strictly involves one type of data, such as the closing prices of a stock over time. The goal in algo-trading using univariate time series is to model this single variable's behavior and make future predictions based on past patterns.

## Key Concepts

### Time Series Data

Time series data is a sequence of data points collected or recorded at specific time intervals. Examples include daily stock prices, monthly sales figures, or annual revenue of a company. In the context of algo-trading, time series data typically refer to price, volume, or other financial metrics recorded at regular intervals.

### Stationarity

A crucial concept in [time series analysis](../t/time_series_analysis.md) is stationarity. A time series is considered stationary if its statistical properties like mean, variance, and [autocorrelation](../a/autocorrelation.md) are constant over time. Many time series models require the data to be stationary to make valid inferences.

**Statistical tests for stationarity:**
1. Augmented Dickey-Fuller (ADF) test
2. Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test
3. Phillips-Perron test

### Autoregressive Models (AR)

In an autoregressive model, the future value of a variable is assumed to be a linear function of several previous values of the same variable. The autoregressive model of order `p` (AR(P)) can be represented as:
\[ Y_t = \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \ldots + \phi_p Y_{t-p} + \epsilon_t \]

Where:
- \( Y_t \) is the variable at time \( t \)
- \( \phi_1, \phi_2, \ldots, \phi_p \) are parameters
- \( \epsilon_t \) is white noise

### Moving Average Models (MA)

The moving average model uses past forecast errors in a regression-like model. An MA model of order `q` (MA(Q)) is represented as:
\[ Y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \ldots + \theta_q \epsilon_{t-q} \]

Where:
- \( Y_t \) is the variable at time \( t \)
- \( \mu \) is the mean of the series
- \( \epsilon_t, \epsilon_{t-1}, \ldots, \epsilon_{t-q} \) are white noise
- \( \theta_1, \theta_2, \ldots, \theta_q \) are parameters

### Autoregressive Integrated Moving Average (ARIMA)

Combining AR and MA models, ARIMA is a more generalized model. An ARIMA model is characterized by three parameters `(p, d, q)`:
- `p`: number of lag observations in the model (lag order)
- `d`: number of times the raw observations are differenced (degree of differencing)
- `q`: size of the moving average window (order of moving average)

The general ARIMA model is represented as:
\[ Y_t = \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \ldots + \phi_p Y_{t-p} + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \ldots + \theta_q \epsilon_{t-q} \]

### Seasonal ARIMA (SARIMA)

In many [financial time series](../f/financial_time_series.md), seasonal effects play a significant role. SARIMA extends the ARIMA model to account for seasonality by adding seasonal components. The SARIMA model is denoted as ARIMA(p, d, q)(P, D, Q)m, where `m` is the frequency of the seasonality.

### Exponential Smoothing (ETS)

[Exponential smoothing](../e/exponential_smoothing.md) methods are another popular choice for [time series forecasting](../t/time_series_forecasting.md). These methods assign exponentially decreasing weights to past observations. Some common [exponential smoothing](../e/exponential_smoothing.md) techniques include:
- Simple [Exponential Smoothing](../e/exponential_smoothing.md) (SES)
- Holt’s Linear Trend Model
- Holt-Winters Seasonal Model

### GARCH Models

Generalized Autoregressive Conditional Heteroskedasticity (GARCH) models are used mainly for modeling time series data with [volatility clustering](../v/volatility_clustering.md), common in financial markets.

A simple GARCH(1,1) model can be written as:
\[
\begin{aligned}
  & Y_t = \sigma_t \epsilon_t \\
  & \sigma_t^2 = \alpha_0 + \alpha_1 Y_{t-1}^2 + \beta\sigma_{t-1}^2
\end{aligned}
\]

Where:
- \( Y_t \) is the return at time \( t \)
- \( \sigma_t \) is the conditional standard deviation
- \( \epsilon_t \) is white noise
- \( \alpha_0, \alpha_1 \) are parameters
- \( \beta \) is the lag coefficient for the variance

## Forecasting Algorithms

[Algorithmic trading](../a/algorithmic_trading.md) relies heavily on robust forecasting methods to make informed decisions. The choice of forecasting method depends on the peculiarities of the data and the specific requirements of the trading strategy.

### Linear Models

Linear models, such as [linear regression](../l/linear_regression.md), are straightforward and interpretable. They assume a linear relationship between the input variables (lags) and the output variable (future value).

### Machine Learning Models

More sophisticated methods involve machine learning algorithms that can model non-linear relationships and interactions in the data. Some popular machine learning algorithms for [time series forecasting](../t/time_series_forecasting.md) include:

- **Random Forests**: Ensemble method that builds multiple [decision trees](../d/decision_trees.md) and merges them to get a more accurate and stable prediction.
- **Gradient Boosting Machines (GBM)**: Builds trees sequentially, each one trying to correct errors from the previous one.
- **Support Vector Machines (SVM)**: Works by finding the hyperplane that best divides a dataset into classes.
- **Neural Networks (NN)**: Deep learning models can capture complex patterns in the data. Recurrent Neural Networks (RNNs) and Long Short-Term Memory networks (LSTMs) are tailored for sequential data.

### Deep Learning Models

Deep learning has gained traction in [time series forecasting](../t/time_series_forecasting.md) due to its ability to model complex patterns and structures. Two popular architectures include:

- **Recurrent Neural Networks (RNNs)**: Designed for sequential data, they have loops that enable the persistence of information across sequence steps.
- **Long Short-Term Memory (LSTM)**: A type of RNN that can capture long-term dependencies and address the vanishing gradient problem.

## Practical Applications in Algorithmic Trading

### Trend Following

One common strategy in algo-trading is [trend following](../t/trend_following.md). By analyzing historical price movements, algorithms aim to identify and capitalize on trends. Moving averages, [exponential smoothing](../e/exponential_smoothing.md), and ARIMA models can help detect these trends.

### Mean Reversion

[Mean reversion](../m/mean_reversion.md) strategies are based on the idea that asset prices tend to revert to their historical mean. Time series models that identify deviations from the mean, such as [Bollinger Bands](../b/bollinger_bands.md) or AR models, are useful for these strategies.

### Volatility Forecasting

Accurate [volatility forecasting](../v/volatility_forecasting.md) is crucial for [risk management](../r/risk_management.md) and options pricing. [GARCH models](../g/garch_models.md) are commonly used to predict volatility because they effectively capture time-varying [volatility clustering](../v/volatility_clustering.md) in financial data.

### Sentiment Analysis

Integrating univariate time series with other data sources, such as [social media sentiment](../s/social_media_sentiment.md), can enhance predictions. Machine learning models can combine these diverse data sources to derive more accurate and holistic insights.

## Challenges and Limitations

### Overfitting

One of the significant challenges in [time series forecasting](../t/time_series_forecasting.md) is overfitting, where the model performs well on the training data but poorly on unseen data. Regularization techniques, cross-validation, and pruning are ways to mitigate overfitting.

### Non-Stationarity

[Financial time series](../f/financial_time_series.md) data are often non-stationary, exhibiting trends, cycles, and structural breaks. Differencing, transformations, and advanced models like SARIMA and LSTM can handle non-stationarity to some extent.

### Data Quality

The quality of predictions heavily depends on the quality of the input data. Noisy, missing, or erroneous data can lead to inaccurate forecasts. Preprocessing steps like cleaning, normalization, and imputation are critical.

### Computational Complexity

Sophisticated models such as deep learning require significant computational resources and time for training. Efficient algorithms and hardware acceleration (e.g., GPUs) can alleviate some of these challenges.

## Conclusion

Univariate time series is a foundational element in [algorithmic trading](../a/algorithmic_trading.md). Despite its limitations, it offers valuable insights and predictive power. Combining traditional statistical models with modern machine learning and deep learning techniques can yield robust and scalable [trading strategies](../t/trading_strategies.md). As data quality and computational capabilities continue to improve, the potential for univariate [time series analysis](../t/time_series_analysis.md) in algo-trading will only grow.

For more detailed and practical implementations of these concepts, traders and data scientists can refer to the following companies and their respective pages:

- [Numerai](https://numer.ai/)
- [QuantConnect](https://www.quantconnect.com/)
- [Alpaca](https://alpaca.markets/)
- [Quantopian](https://www.quantopian.com/)

These platforms offer resources, data, and tools for designing, testing, and deploying [algorithmic trading](../a/algorithmic_trading.md) strategies.
