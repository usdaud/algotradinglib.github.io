# Skewness

In [probability theory](../p/probability_theory_in_trading.md) and [statistics](../s/statistics.md), skewness is a measure of the asymmetry of the [probability distribution](../p/probability_distribution.md) of a real-valued random variable about its mean. Skewness can be calculated as the third standardized moment of the [distribution](../d/distribution.md). It indicates the extent and direction of deviation from a [symmetrical distribution](../s/symmetrical_distribution.md).

## Types of Skewness:

1. **Positive Skew (Right Skew)**: In a positively skewed [distribution](../d/distribution.md), the tail on the right side is longer or fatter than the left side. The mean and [median](../m/median.md) [will](../w/will.md) be greater than the [mode](../m/mode.md). Examples include [income](../i/income.md) distributions where a small number of people earn disproportionately higher incomes.

2. **Negative Skew (Left Skew)**: In a negatively skewed [distribution](../d/distribution.md), the tail on the left side is longer or fatter than the right side. The mean and [median](../m/median.md) [will](../w/will.md) be less than the [mode](../m/mode.md). This is commonly observed in test scores where a large proportion of participants score highly.

## Mathematical Definition:

Skewness is typically denoted by the Greek letter \( \gamma_1 \) and is defined as:

\[ \gamma_1 = \frac{\mu_3}{\sigma^3} = \frac{E[(X - \mu)^3]}{\sigma^3} \]

where:
- \( \mu_3 \) is the third central moment,
- \( \sigma \) is the [standard deviation](../s/standard_deviation.md),
- \( \mu \) is the mean of the [distribution](../d/distribution.md),
- \( E \) denotes the expectation operator.

## Interpretation:

- **Skewness = 0**: The [distribution](../d/distribution.md) is perfectly symmetrical.
- **Skewness > 0**: Indicates a [distribution](../d/distribution.md) that is skewed to the right.
- **Skewness < 0**: Indicates a [distribution](../d/distribution.md) that is skewed to the left.

## Practical Applications:

Skewness is particularly useful in [finance](../f/finance.md) and trading for understanding the [distribution](../d/distribution.md) of [asset](../a/asset.md) returns, [risk analysis](../r/risk_analysis.md), and [portfolio management](../p/par.md). Traditional financial theories often assume a [normal distribution](../n/normal_distribution_in_trading.md) of returns, but in reality, financial returns can exhibit significant skewness. Understanding skewness helps in better [risk management](../r/risk_management.md) and strategy development.

### Financial Markets:

In [financial markets](../f/financial_market.md), skewness impacts [options](../o/options.md) pricing, [portfolio management](../p/par.md), and [risk](../r/risk.md) assessments. For example:

- **[Options](../o/options.md) Pricing**: Skewness affects the pricing of [options](../o/options.md) as the [Black-Scholes model](../b/black-scholes_model.md) assumes lognormal [distribution](../d/distribution.md) of [asset](../a/asset.md) prices. Negative skew suggests higher [demand](../d/demand.md) for puts relative to calls, implying higher premiums for [tail risk](../t/tail_risk.md) protection.
  
- **[Portfolio Management](../p/par.md)**: Portfolio managers aim to construct portfolios with desirable skew properties. [Positive skewness](../p/positive_skewness.md) is often preferred as it implies the potential for higher returns.

- **[Risk Management](../r/risk_management.md)**: Skewness informs [Value](../v/value.md) at [Risk](../r/risk.md) (VaR) models, helping in understanding the likelihood of extreme losses or gains.

## Skewness in Algorithmic Trading:

In [algorithmic trading](../a/accountability.md), skewness can be used for:

- **Signal Generation**: Algorithms can be designed to capture skewness in price movements, anticipating sharp moves in a specific direction.
  
- **Strategy Evaluation**: Evaluating the skewness of strategy returns to ensure the robustness and suitability under different [market](../m/market.md) conditions.
  
- **[Risk](../r/risk.md) Adjustments**: Adjusting position sizes based on skewness to manage tail risks effectively.

### Case Study:

Consider a trading algorithm designed to [trade](../t/trade.md) [large-cap stocks](../l/large_cap_stocks.md). Upon analyzing historical price data, the algorithm identifies periods where stock returns show significant [positive skewness](../p/positive_skewness.md). During these periods, the algorithm increases position sizes in the direction of the skew to [capitalize](../c/capitalize.md) on the expected continued upward movement. Conversely, if [negative skewness](../n/negative_skewness.md) is detected, position sizes are reduced or protective puts are purchased to [hedge](../h/hedge.md) against significant downward moves.

## Limitations of Skewness:

1. **Sample Size Sensitivity**: Skewness can be very sensitive to sample size and may provide misleading information if the sample is not representative.

2. **Outliers Impact**: Skewness is heavily influenced by outliers, which can distort the true [distribution](../d/distribution.md) characteristics.

3. **Combining Assets**: When combining several assets into a portfolio, the skewness of individual [asset](../a/asset.md) returns might not represent the skewness of the portfolio returns. Proper consideration and calculation are required.

## Tools and Software:

Skewness can be calculated using various statistical tools and software, such as:

- **Microsoft Excel**: Using the `SKEW` function.
- **R**: Using functions from the `moments` package.
- **Python**: Utilizing libraries such as Pandas (method `.skew()`) and SciPy.

## Example Calculation:

### Python:

```python
[import](../i/import.md) pandas as pd
[import](../i/import.md) numpy as np

# Sample data
returns = [0.10, 0.20, 0.15, -0.10, 0.05, -0.30, 0.25, -0.05]
returns_series = pd.Series(returns)

# Calculate skewness
skewness = returns_series.skew()
print(f'Skewness: {skewness}')
```

This code calculates the skewness of a list of returns using the Pandas library in Python. 

### R:

```R
# Sample data
returns <- c(0.10, 0.20, 0.15, -0.10, 0.05, -0.30, 0.25, -0.05)

# Calculate skewness
library(moments)
skewness <- skewness(returns)
print(paste("Skewness: ", skewness))
```

This R script calculates the skewness using the `moments` package.

## References

For more information about skewness, you may visit the corporate documentation or research papers of prominent financial firms, such as:

- [Bloomberg](https://www.bloomberg.com/)
- [Goldman Sachs](https://www.goldmansachs.com/)
- [J.P. Morgan](https://www.jpmorgan.com/)

Each of these firms provides comprehensive research and tools related to skewness and its applications in [financial markets](../f/financial_market.md).