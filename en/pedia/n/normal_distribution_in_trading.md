# Normal Distribution

The normal [distribution](../d/distribution.md), also known as the [Gaussian distribution](../g/gaussian_distribution.md), is a continuous [probability distribution](../p/probability_distribution.md) that is symmetric around its mean, describing data that clusters around the mean. It is characterized by its bell-shaped curve and is defined mathematically by two parameters: the mean (μ) and the [standard deviation](../s/standard_deviation.md) (σ). This [distribution](../d/distribution.md) plays a crucial role in various fields, including trading, where it is used to model and analyze the behavior of [asset](../a/asset.md) prices.

## Key Characteristics

1. **Symmetry**: The normal [distribution](../d/distribution.md) is perfectly symmetric about its mean, which means that half of the values lie below the mean, and half lie above it.
2. **Mean, [Median](../m/median.md), and [Mode](../m/mode.md)**: In a normal [distribution](../d/distribution.md), the mean, [median](../m/median.md), and [mode](../m/mode.md) are all equal and located at the center of the [distribution](../d/distribution.md).
3. **[Standard Deviation](../s/standard_deviation.md)**: The [standard deviation](../s/standard_deviation.md) determines the [dispersion](../d/dispersion.md) or spread of the [distribution](../d/distribution.md). A smaller [standard deviation](../s/standard_deviation.md) indicates that the data points are close to the mean, while a larger [standard deviation](../s/standard_deviation.md) indicates that the data points are spread out over a wider [range](../r/range.md) of values.
4. **68-95-99.7 Rule ([Empirical Rule](../e/empirical_rule.md))**: Approximately 68% of the data within a normal [distribution](../d/distribution.md) falls within one [standard deviation](../s/standard_deviation.md) of the mean, about 95% falls within two standard deviations, and about 99.7% falls within three standard deviations.

## Importance in Trading

### Risk Management

In trading, the normal [distribution](../d/distribution.md) is heavily utilized in [risk management](../r/risk_management.md) to model potential future outcomes:

1. **[Value](../v/value.md) at [Risk](../r/risk.md) (VaR)**: VaR is a statistical technique used to measure the [risk](../r/risk.md) of loss on a portfolio. Using the normal [distribution](../d/distribution.md), traders can estimate the probability of a portfolio experiencing a loss above a certain threshold.

2. **Expected [Shortfall](../s/shortfall.md)**: While VaR gives a threshold [value](../v/value.md), the expected [shortfall](../s/shortfall.md) provides the average of losses that exceed this threshold, [offering](../o/offering.md) a more comprehensive view of the [tail risk](../t/tail_risk.md), which is the [risk](../r/risk.md) of extreme price movements.

### Pricing Models

Several pricing models in trading assume that returns are normally distributed:

1. **[Black-Scholes Model](../b/black-scholes_model.md)**: This model, used for pricing [European options](../e/european_options.md), relies on the assumption that the returns of the [underlying asset](../u/underlying_asset.md) follow a normal [distribution](../d/distribution.md). The model calculates the option price by [discounting](../d/discounting.md) the expected payoff at [maturity](../m/maturity.md) under the [risk](../r/risk.md)-[neutral](../n/neutral.md) measure.
 - Find more information on Black-Scholes Model

2. **Modern Portfolio Theory (MPT)**: Developed by [Harry Markowitz](../h/harry_markowitz.md), MPT uses the normal [distribution](../d/distribution.md) to assess the [expected return](../e/expected_return.md) and [risk](../r/risk.md) of a portfolio of assets. By considering the mean and variance ([standard deviation](../s/standard_deviation.md) squared), MPT helps in the construction of an optimal portfolio that maximizes [return](../r/return.md) for a given level of [risk](../r/risk.md).
 - For more insights, visit the concept on Modern Portfolio Theory

### Statistical Arbitrage

Statistical [arbitrage](../a/arbitrage.md) strategies often rely on the assumption that [asset](../a/asset.md) returns are normally distributed. These strategies employ statistical methods to identify mispricings between related assets and execute trades to [profit](../p/profit.md) from these inefficiencies. By understanding and utilizing the properties of the normal [distribution](../d/distribution.md), traders can devise strategies to exploit short-term price discrepancies.

### Technical Analysis

In [technical analysis](../t/technical_analysis.md), normal [distribution](../d/distribution.md) is used to create [Bollinger Bands](../b/bollinger_bands.md), a popular technical [indicator](../i/indicator.md):

1. **[Bollinger Bands](../b/bollinger_bands.md)**: These bands consist of a moving average (typically a 20-day simple moving average) and two standard deviations plotted above and below the moving average.
 - When the price of an [asset](../a/asset.md) moves towards the upper band, it is often considered [overbought](../o/overbought.md), indicating a potential sell signal.
 - Conversely, when the price moves towards the lower band, it is considered [oversold](../o/oversold.md), indicating a potential buy signal.
 - More about [Bollinger Bands](../b/bollinger_bands.md) can be found on John Bollinger's online platform

## Limitations in Real-World Trading

### Fat Tails and Kurtosis

While the normal [distribution](../d/distribution.md) is a convenient mathematical model, real-world [asset](../a/asset.md) returns often exhibit "fat tails," or excess [kurtosis](../k/kurtosis.md), meaning that extreme events (large price movements) are more likely than predicted by a normal [distribution](../d/distribution.md). This discrepancy can lead to underestimating the [risk](../r/risk.md) of rare, catastrophic [market](../m/market.md) events.

### Non-Normality of Returns

Financial returns are often skewed and do not perfectly follow a normal [distribution](../d/distribution.md). [Skewness](../s/skewness.md) refers to the asymmetry in the [distribution](../d/distribution.md), where returns might deviate more in one direction than the other. In such cases, relying solely on the normal [distribution](../d/distribution.md) can lead to inaccurate [risk](../r/risk.md) assessments and suboptimal trading decisions.

### Volatility Clustering

[Asset](../a/asset.md) returns often exhibit [volatility clustering](../v/volatility_clustering.md), where periods of high [volatility](../v/volatility.md) are followed by more high [volatility](../v/volatility.md), and periods of low [volatility](../v/volatility.md) are followed by more low [volatility](../v/volatility.md). This phenomenon contradicts the assumption of constant [volatility](../v/volatility.md) in the normal [distribution](../d/distribution.md):

1. **ARCH/[GARCH Models](../g/garch_models.md)**: To address [volatility clustering](../v/volatility_clustering.md), traders utilize Autoregressive Conditional [Heteroskedasticity](../h/heteroskedasticity.md) (ARCH) and Generalized Autoregressive Conditional [Heteroskedasticity](../h/heteroskedasticity.md) (GARCH) models that allow for changing [volatility](../v/volatility.md) over time.
 - Learn about these models in Robert Engle's ARCH work.

## Alternatives to Normal Distribution

Given these limitations, traders and [risk](../r/risk.md) managers also consider alternative distributions that better capture the characteristics of [asset](../a/asset.md) returns:

1. **[Log-Normal Distribution](../l/log-normal_distribution.md)**: This [distribution](../d/distribution.md) assumes that the logarithm of returns, rather than the returns themselves, is normally distributed. It prevents negative prices, which is suitable for modeling stock prices.

2. **Student's t-[Distribution](../d/distribution.md)**: This [distribution](../d/distribution.md) has heavier tails than the normal [distribution](../d/distribution.md), providing a better fit for the large price movements observed in [financial markets](../f/financial_market.md).

3. **Stable Distributions**: These distributions, such as the Lévy [distribution](../d/distribution.md), can model the heavy tails and [skewness](../s/skewness.md) observed in financial data while accommodating the self-similar properties over different time scales.

## Conclusion

The normal [distribution](../d/distribution.md) is a fundamental statistical tool in trading, providing a framework for [risk management](../r/risk_management.md), pricing, statistical [arbitrage](../a/arbitrage.md), and [technical analysis](../t/technical_analysis.md). Although it offers significant insights, traders must be aware of its limitations and consider alternative models to better capture the true behavior of [asset](../a/asset.md) prices in [financial markets](../f/financial_market.md).

Understanding the normal [distribution](../d/distribution.md)'s properties and when to apply alternative models allows traders to make more informed decisions, improving [risk management](../r/risk_management.md) and enhancing [trading strategies](../t/trading_strategies.md) in complex financial environments.
