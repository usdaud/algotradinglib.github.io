# Normal Distribution in Trading

The normal distribution, also known as the [Gaussian distribution](../g/gaussian_distribution.md), is a continuous probability distribution that is symmetric around its mean, describing data that clusters around the mean. It is characterized by its bell-shaped curve and is defined mathematically by two parameters: the mean (μ) and the standard deviation (σ). This distribution plays a crucial role in various fields, including trading, where it is used to model and analyze the behavior of asset prices.

## Key Characteristics

1. **Symmetry**: The normal distribution is perfectly symmetric about its mean, which means that half of the values lie below the mean, and half lie above it.
2. **Mean, Median, and Mode**: In a normal distribution, the mean, median, and mode are all equal and located at the center of the distribution.
3. **Standard Deviation**: The standard deviation determines the dispersion or spread of the distribution. A smaller standard deviation indicates that the data points are close to the mean, while a larger standard deviation indicates that the data points are spread out over a wider range of values.
4. **68-95-99.7 Rule (Empirical Rule)**: Approximately 68% of the data within a normal distribution falls within one standard deviation of the mean, about 95% falls within two standard deviations, and about 99.7% falls within three standard deviations.

## Importance in Trading

### Risk Management

In trading, the normal distribution is heavily utilized in [risk management](../r/risk_management.md) to model potential future outcomes:

1. **Value at Risk (VaR)**: VaR is a statistical technique used to measure the risk of loss on a portfolio. Using the normal distribution, traders can estimate the probability of a portfolio experiencing a loss above a certain threshold.
   
2. **Expected Shortfall**: While VaR gives a threshold value, the expected shortfall provides the average of losses that exceed this threshold, offering a more comprehensive view of the [tail risk](../t/tail_risk.md), which is the risk of extreme price movements.

### Pricing Models

Several pricing models in trading assume that returns are normally distributed:

1. **[Black-Scholes Model](../b/black-scholes_model.md)**: This model, used for pricing [European options](../e/european_options.md), relies on the assumption that the returns of the underlying asset follow a normal distribution. The model calculates the option price by discounting the expected payoff at maturity under the risk-neutral measure.
   - Find more information on [Black-Scholes Model](https://www.investopedia.com/terms/b/blackscholes.asp)

2. **Modern Portfolio Theory (MPT)**: Developed by Harry Markowitz, MPT uses the normal distribution to assess the expected return and risk of a portfolio of assets. By considering the mean and variance (standard deviation squared), MPT helps in the construction of an optimal portfolio that maximizes return for a given level of risk.
   - For more insights, visit the concept on [Modern Portfolio Theory](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)

### Statistical Arbitrage

Statistical [arbitrage](../a/arbitrage.md) strategies often rely on the assumption that asset returns are normally distributed. These strategies employ statistical methods to identify mispricings between related assets and execute trades to profit from these inefficiencies. By understanding and utilizing the properties of the normal distribution, traders can devise strategies to exploit short-term price discrepancies.

### Technical Analysis

In [technical analysis](../t/technical_analysis.md), normal distribution is used to create [Bollinger Bands](../b/bollinger_bands.md), a popular technical indicator:

1. **[Bollinger Bands](../b/bollinger_bands.md)**: These bands consist of a moving average (typically a 20-day simple moving average) and two standard deviations plotted above and below the moving average. 
   - When the price of an asset moves towards the upper band, it is often considered overbought, indicating a potential sell signal.
   - Conversely, when the price moves towards the lower band, it is considered oversold, indicating a potential buy signal.
   - More about [Bollinger Bands](../b/bollinger_bands.md) can be found on [John Bollinger's website](https://www.bollingerbands.com)

## Limitations in Real-World Trading

### Fat Tails and Kurtosis

While the normal distribution is a convenient mathematical model, real-world asset returns often exhibit "fat tails," or excess kurtosis, meaning that extreme events (large price movements) are more likely than predicted by a normal distribution. This discrepancy can lead to underestimating the risk of rare, catastrophic market events.

### Non-Normality of Returns

Financial returns are often skewed and do not perfectly follow a normal distribution. Skewness refers to the asymmetry in the distribution, where returns might deviate more in one direction than the other. In such cases, relying solely on the normal distribution can lead to inaccurate risk assessments and suboptimal trading decisions.

### Volatility Clustering

Asset returns often exhibit [volatility clustering](../v/volatility_clustering.md), where periods of high volatility are followed by more high volatility, and periods of low volatility are followed by more low volatility. This phenomenon contradicts the assumption of constant volatility in the normal distribution:

1. **ARCH/[GARCH Models](../g/garch_models.md)**: To address [volatility clustering](../v/volatility_clustering.md), traders utilize Autoregressive Conditional Heteroskedasticity (ARCH) and Generalized Autoregressive Conditional Heteroskedasticity (GARCH) models that allow for changing volatility over time. 
   - Learn about these models on [Robert Engle's ARCH resource page](http://www.engle-newyork.com)

## Alternatives to Normal Distribution

Given these limitations, traders and risk managers also consider alternative distributions that better capture the characteristics of asset returns:

1. **[Log-Normal Distribution](../l/log-normal_distribution.md)**: This distribution assumes that the logarithm of returns, rather than the returns themselves, is normally distributed. It prevents negative prices, which is suitable for modeling stock prices.
  
2. **Student's t-Distribution**: This distribution has heavier tails than the normal distribution, providing a better fit for the large price movements observed in financial markets.
  
3. **Stable Distributions**: These distributions, such as the Lévy distribution, can model the heavy tails and skewness observed in financial data while accommodating the self-similar properties over different time scales.

## Conclusion

The normal distribution is a fundamental statistical tool in trading, providing a framework for [risk management](../r/risk_management.md), pricing, statistical [arbitrage](../a/arbitrage.md), and [technical analysis](../t/technical_analysis.md). Although it offers significant insights, traders must be aware of its limitations and consider alternative models to better capture the true behavior of asset prices in financial markets.

Understanding the normal distribution's properties and when to apply alternative models allows traders to make more informed decisions, improving [risk management](../r/risk_management.md) and enhancing [trading strategies](../t/trading_strategies.md) in complex financial environments.
