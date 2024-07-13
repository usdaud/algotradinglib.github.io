# Risk-Weighted Return

[Risk](../r/risk.md)-[Weighted](../w/weighted.md) [Return](../r/return.md) is a financial metric that adjusts the returns of an investment by the amount of [risk](../r/risk.md) taken to achieve those returns. This metric helps investors understand the [efficiency](../e/efficiency.md) of their [investment strategy](../i/investment_strategy.md) by comparing the returns to the potential risks involved. It is particularly important in the context of [algorithmic trading](../a/algorithmic_trading.md) (often referred to as "algo-trading" or "automated trading"), where complex [trading strategies](../t/trading_strategies.md) are executed using computers and [quantitative models](../q/quantitative_models.md).

## Key Concepts

### Risk-Weighted Return

At its core, [Risk](../r/risk.md)-[Weighted](../w/weighted.md) [Return](../r/return.md) considers the variance or [volatility](../v/volatility.md) of returns and adjusts the [performance metrics](../p/performance_metrics.md) accordingly. Higher [volatility](../v/volatility.md) implies higher [risk](../r/risk.md); hence, a high [return](../r/return.md) with high [uncertainty](../u/uncertainty_in_trading.md) may not be as attractive as a lower but stable [return](../r/return.md).

### Importance in Algo-Trading

In the realm of algo-trading, the use of sophisticated algorithms for making trading decisions involves substantial [risk](../r/risk.md), primarily because these are based on historical data and models which may not always predict future movements accurately. [Risk](../r/risk.md)-[Weighted](../w/weighted.md) [Return](../r/return.md) helps in choosing algorithms and strategies that provide optimal performance with controlled [risk](../r/risk.md).

### Common Metrics

Several specific ratios and measurements assess [Risk](../r/risk.md)-[Weighted Returns](../w/weighted_returns_in_trading.md), each with its own method of factoring in [risk](../r/risk.md):

1. **[Sharpe Ratio](../s/sharpe_ratio.md)**
2. **[Sortino Ratio](../s/sortino_ratio.md)**
3. **[Treynor Ratio](../t/treynor_ratio.md)**
4. **[Information Ratio](../i/information_ratio.md)**

## Sharpe Ratio

Developed by Nobel Laureate [William F. Sharpe](../w/william_f._sharpe.md), the [Sharpe Ratio](../s/sharpe_ratio.md) is one of the most widely used measures of [risk](../r/risk.md)-[weighted](../w/weighted.md) performance. It is calculated by dividing the difference between the portfolio [return](../r/return.md) and the [risk](../r/risk.md)-free rate by the [standard deviation](../s/standard_deviation.md) of the portfolio returns.

### Calculation

\[ Sharpe\ Ratio = \frac{E(R) - R_f}{\sigma} \]

- \( E(R) \) = [Expected return](../e/expected_return.md) of the portfolio
- \( R_f \) = [Risk](../r/risk.md)-free rate
- \( \sigma \) = [Standard deviation](../s/standard_deviation.md) of the portfolio returns

### Interpretation

A higher [Sharpe Ratio](../s/sharpe_ratio.md) indicates better [risk-adjusted return](../r/risk-adjusted_return.md). A negative [Sharpe Ratio](../s/sharpe_ratio.md) suggests that a [risk](../r/risk.md)-free investment would perform better than the observed strategy.

## Sortino Ratio

The [Sortino Ratio](../s/sortino_ratio.md) is similar to the [Sharpe Ratio](../s/sharpe_ratio.md) but differentiates between harmful [volatility](../v/volatility.md) ([downside risk](../d/downside_risk.md)) and total [volatility](../v/volatility.md). It uses the [standard deviation](../s/standard_deviation.md) of the negative [asset](../a/asset.md) returns ([downside deviation](../d/downside_deviation.md)) rather than the [standard deviation](../s/standard_deviation.md) of all returns.

### Calculation

\[ Sortino\ Ratio = \frac{E(R) - R_f}{DD} \]

- \( E(R) \) = [Expected return](../e/expected_return.md) of the portfolio
- \( R_f \) = [Risk](../r/risk.md)-free rate
- \( DD \) = [Downside deviation](../d/downside_deviation.md)

### Interpretation

The [Sortino Ratio](../s/sortino_ratio.md) provides a more accurate measure of an investment’s [risk-adjusted return](../r/risk-adjusted_return.md) by focusing on the [downside risk](../d/downside_risk.md), making it particularly useful for evaluating investments expected to have significant downside [volatility](../v/volatility.md).

## Treynor Ratio

Named after Jack L. Treynor, the [Treynor Ratio](../t/treynor_ratio.md) measures returns earned in excess of those that could have been earned on a [risk](../r/risk.md)-free investment per each unit of [market risk](../m/market_risk.md). Unlike the [Sharpe Ratio](../s/sharpe_ratio.md), which uses [standard deviation](../s/standard_deviation.md) as the [risk](../r/risk.md) measure, the [Treynor Ratio](../t/treynor_ratio.md) uses [beta](../b/beta.md).

### Calculation

\[ Treynor\ Ratio = \frac{E(R) - R_f}{\[beta](../b/beta.md)} \]

- \( E(R) \) = [Expected return](../e/expected_return.md) of the portfolio
- \( R_f \) = [Risk](../r/risk.md)-free rate
- \( \[beta](../b/beta.md) \) = [Beta](../b/beta.md) of the portfolio

### Interpretation

A higher [Treynor Ratio](../t/treynor_ratio.md) indicates that the investment has provided a higher [return](../r/return.md) per unit of [market risk](../m/market_risk.md).

## Information Ratio

The [Information Ratio](../i/information_ratio.md) measures portfolio returns beyond the returns of a [benchmark](../b/benchmark.md), usually an [index](../i/index.md), compared to the [volatility](../v/volatility.md) of those returns.

### Calculation

\[ Information\ Ratio = \frac{E(R_p - R_b)}{\sigma} \]

- \( E(R_p) \) = [Expected return](../e/expected_return.md) of the portfolio
- \( E(R_b) \) = [Expected return](../e/expected_return.md) of the [benchmark](../b/benchmark.md)
- \( \sigma \) = [Standard deviation](../s/standard_deviation.md) of the difference in returns

### Interpretation

A higher [Information Ratio](../i/information_ratio.md) suggests that the [portfolio manager](../p/portfolio_manager.md) has a higher level of skill, as they are able to generate excess returns with higher consistency.

## Companies Utilizing Risk-Weighted Return in Algo-Trading

### Two Sigma Investments [Link](https://www.twosigma.com/)

Two Sigma uses machine learning, distributed computing, and other sophisticated technologies to find connections in global markets. They heavily rely on [risk](../r/risk.md)-[weighted](../w/weighted.md) [return](../r/return.md) metrics to optimize their [trading strategies](../t/trading_strategies.md).

### Renaissance Technologies [Link](https://www.rentec.com/)

Renaissance Technologies, known for their Medallion [Fund](../f/fund.md), employs complex [mathematical models](../m/mathematical_models_in_trading.md) and algorithms to exploit [market](../m/market.md) inefficiencies, continually adjusting for [risk](../r/risk.md)-to-[return](../r/return.md) ratios to maintain their competitive edge.

### AQR Capital Management [Link](https://www.aqr.com/)

AQR [Capital](../c/capital.md) Management leverages [quantitative analysis](../q/quantitative_analysis.md) to manage [risk](../r/risk.md) and optimize returns. They utilize [risk](../r/risk.md)-[weighted](../w/weighted.md) [return](../r/return.md) metrics extensively in their multi-strategy investment approach.

### Citadel [Link](https://www.citadel.com/)

Citadel applies rigorous research and technology-driven strategies to manage a broad [range](../r/range.md) of [asset](../a/asset.md) classes and investment strategies. These strategies often incorporate [risk](../r/risk.md)-[weighted returns](../w/weighted_returns_in_trading.md) to ensure alignment with investment objectives.

## Application in Portfolio Management

[Risk](../r/risk.md)-[weighted](../w/weighted.md) [return](../r/return.md) metrics are crucial in [portfolio optimization](../p/portfolio_optimization.md), helping investors choose a mix of assets that [offer](../o/offer.md) the best [return](../r/return.md) for the level of [risk](../r/risk.md) they are willing to take.

### Example

Consider a [portfolio manager](../p/portfolio_manager.md) evaluating two investment opportunities: 

1. **Investment A** has an [expected return](../e/expected_return.md) of 10% with a [standard deviation](../s/standard_deviation.md) of 15%.
2. **Investment B** has an [expected return](../e/expected_return.md) of 8% with a [standard deviation](../s/standard_deviation.md) of 8%.

If the [risk](../r/risk.md)-free rate is 2%, the Sharpe Ratios would be:

- \( Sharpe\ Ratio_A = \frac{10\% - 2\%}{15\%} = 0.53 \)
- \( Sharpe\ Ratio_B = \frac{8\% - 2\%}{8\%} = 0.75 \)

Though Investment A offers higher returns, Investment B is more attractive on a [risk](../r/risk.md)-adjusted [basis](../b/basis.md).

## Conclusion

[Risk](../r/risk.md)-[weighted](../w/weighted.md) [return](../r/return.md) is an invaluable concept in the world of investments, particularly in algo-trading. It allows for a more nuanced view of performance, considering not just the returns but also the risks taken to achieve them. By employing metrics like Sharpe, Sortino, and Treynor Ratios, investors and [fund](../f/fund.md) managers can make more informed decisions, optimizing their strategies to balance potential rewards with corresponding risks.
