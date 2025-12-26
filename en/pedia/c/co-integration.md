# Co-integration

## Introduction to Co-integration

Co-integration is a statistical property of a collection of [time series](../t/time_series.md) variables that indicates a long-term [equilibrium](../e/equilibrium.md) relationship between them. In the context of [financial markets](../f/financial_market.md), co-integration is used to identify pairs or sets of assets whose prices move together in a way that they maintain a stable, long-term relationship despite short-term deviations. This concept is particularly valuable in [algorithmic trading](../a/algorithmic_trading.md) strategies, specifically in [pairs trading](../p/pairs_trading.md), as it allows traders to exploit temporary divergences from the [equilibrium](../e/equilibrium.md) relationship for [profit](../p/profit.md).

## What is Co-integration?

Co-integration differs from simple [correlation](../c/correlation.md). While [correlation](../c/correlation.md) measures the degree to which two variables move together in the short term, co-integration ensures that any [divergence](../d/divergence.md) between two co-integrated series is mean-reverting over the long term. Essentially, if two or more series are co-integrated, there exists a linear combination of these series that is stationary, even if the individual series themselves are non-stationary.

Mathematically, suppose \( X_t \) and \( Y_t \) are two non-stationary [time series](../t/time_series.md). They are co-integrated if there exists a parameter \( \[beta](../b/beta.md) \) such that:
\[ Z_t = Y_t - \[beta](../b/beta.md) X_t \]
is stationary. Here, \( Z_t \) is the residual of the series, and if \( Z_t \) is stationary, it means that \( Y_t \) and \( X_t \) move together in the long term.

## Testing for Co-integration

Several tests can be used to [check](../c/check.md) for co-integration between [time series](../t/time_series.md):

1. **Engle-Granger Two-Step Method**:
 - **Step 1**: Regress one [time series](../t/time_series.md) on the other using Ordinary Least Squares (OLS). This provides an estimate of \( \[beta](../b/beta.md) \).
 - **Step 2**: Test the residuals from this regression for stationarity using tests such as the Augmented Dickey-Fuller (ADF) test.

2. **Johansen Test**: This multivariate test is used when more than two [time series](../t/time_series.md) are being tested for co-integration. It provides both the number of co-integrating relationships and their parameters.

3. **Phillips-Ouliaris Test**: Similar to the Engle-Granger method but includes adjustments for residual [autocorrelation](../a/autocorrelation.md) and heteroscedasticity.

## Application in Pairs Trading

[Pairs trading](../p/pairs_trading.md) is a popular [market](../m/market.md)-[neutral](../n/neutral.md) [trading strategy](../t/trading_strategy.md) that involves taking long and short positions in two co-integrated assets. The idea is to identify a pair of assets that exhibit a stable, long-term relationship and then [trade](../t/trade.md) on deviations from this relationship.

### Steps in Pairs Trading

1. **Identify Pairs**: Use historical price data to identify pairs of assets that are co-integrated.
2. **Model the Spread**: Calculate the spread (the residual) between the co-integrated pair.
3. **[Trading Signals](../t/trading_signals.md)**: Implement [trading rules](../t/trading_rules.md) based on the spread. Common rules include:
 - **[Mean Reversion](../m/mean_reversion.md)**: If the spread widens beyond a certain threshold, short the over-performing [asset](../a/asset.md) and long the under-performing [asset](../a/asset.md) in expectation of the spread reverting to its mean.
 - **Stop Loss/[Profit](../p/profit.md) Target**: Set thresholds to close positions if the spread widens further (stop loss) or reverts to the mean as expected ([profit](../p/profit.md) target).

4. **[Execution](../e/execution.md)**: Execute trades algorithmically to ensure timely and accurate [order](../o/order.md) placement.

### Example Execution
Suppose we find that the stock prices of Company A (Stock A) and Company B (Stock B) are co-integrated. If the historical spread has a mean of 0 and a [standard deviation](../s/standard_deviation.md) of 1:
- When the spread widens to 2 standard deviations (e.g., \( Y_t = 2 \sigma \)), short Stock A and long Stock B.
- When the spread reverts to 0, close the position to capture profits.

## Risks in Co-integration Trading

While co-integration-based [trading strategies](../t/trading_strategies.md) can be profitable, they come with risks, including:
- **Breakdown of Co-integration**: The economic relationship between assets may change over time due to structural changes in the [market](../m/market.md) or fundamentals of the companies.
- **[Mean Reversion](../m/mean_reversion.md) Failure**: The spread may not revert to the mean in the anticipated period, leading to potential losses.
- **[Model Risk](../m/model_risk.md)**: Incorrect specification of the co-integration model can lead to misidentification of trading opportunities.

## Companies Utilizing Co-integrated Strategies

Various [hedge](../h/hedge.md) funds and [proprietary trading](../p/proprietary_trading.md) firms employ co-integration in their [algorithmic trading](../a/algorithmic_trading.md) strategies. Firms known for such [quantitative approaches](../q/quantitative_approaches.md) include:

- **AQR [Capital](../c/capital.md) Management**: AQR is known for its quantitative approach to trading and may utilize co-integration among other strategies.

- **Two Sigma Investments**: Two Sigma uses [machine learning](../m/machine_learning.md) and statistical modeling, likely incorporating co-integration in its strategies.

- **Citadel LLC**: Known for its use of advanced [quantitative strategies](../q/quantitative_strategies_in_trading.md).

## Conclusion

Co-integration is a [robust](../r/robust.md) statistical tool that, when applied correctly, can [offer](../o/offer.md) significant advantages in [algorithmic trading](../a/algorithmic_trading.md), specifically in [pairs trading](../p/pairs_trading.md) strategies. By focusing on the long-term [equilibrium](../e/equilibrium.md) relationships between financial assets, traders can devise strategies to exploit short-term deviations, potentially leading to profitable trading opportunities. However, as with any [trading strategy](../t/trading_strategy.md), it is crucial to be aware of the risks and continuously validate models to adapt to changing [market](../m/market.md) conditions.
