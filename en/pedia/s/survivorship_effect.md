# Survivorship Effect

[Survivorship bias](../s/survivorship_bias.md) is a critical phenomenon to understand in the context of [algorithmic trading](../a/algorithmic_trading.md) and financial research. It occurs when analyses are skewed by focusing on entities that survived a certain process while disregarding those that did not. This becomes particularly relevant when dealing with historical data, [backtesting](../b/backtesting.md) [trading strategies](../t/trading_strategies.md), or conducting empirical financial research. 

## Understanding Survivorship Bias

[Survivorship bias](../s/survivorship_bias.md) can lead to overly optimistic conclusions because failed entities are excluded from analysis. For example, when assessing the performance of [stocks](../s/stock.md), funds, or companies, only the successful ones are typically sampled, creating a false [impression](../i/impression.md) of overall performance. This bias can significantly distort the perception of [risk](../r/risk.md) and [return](../r/return.md).

In [algorithmic trading](../a/algorithmic_trading.md), [survivorship bias](../s/survivorship_bias.md) can affect the validity of [backtesting](../b/backtesting.md) results. The inherent flaw here is that backtests conducted on historical data without [accounting](../a/accounting.md) for companies that went bankrupt, were delisted, or ceased operations can present misleading efficacy of [trading strategies](../t/trading_strategies.md).

## Causes of Survivorship Effect

1. **Non-Inclusion of Failed Firms:** Researchers and traders often have access only to data on firms that are currently active or that have merged successfully, ignoring those that have failed.
   
2. **Data Availability:** Commercial databases sometimes only maintain records of surviving entities to reduce data storage needs, leading to an incomplete dataset.
   
3. **Historical Revisions:** Inclusion of only the most recent data for companies, funds, etc., may exclude cases that existed in the past but are no longer present due to failures.

## Consequences of Survivorship Bias in Trading

1. **Misleading Accuracy of [Trading Models](../t/trading_models.md):** Algorithms based on datasets that exclude failed entities may show inaccurate success ratios and predictive power.
   
2. **Overall [Market](../m/market.md) Performance:** Analyzing only surviving companies can create a distorted view of overall [market](../m/market.md) health and dynamics.
   
3. **[Risk](../r/risk.md) Underestimation:** By not [accounting](../a/accounting.md) for companies that have failed, historical data may appear less risky than it truly was.
   
4. **Strategy [Optimization](../o/optimization.md):** It can lead to an over-[optimization](../o/optimization.md) of [trading strategies](../t/trading_strategies.md), falsely elevating the expected returns based on incomplete datasets.

## Overcoming Survivorship Bias

1. **Complete Dataset Utilization:** Ensure that any historical data encompasses both active and inactive entities.
   
2. **Access Specialized Databases:** Use specialized financial databases that include delisted [stocks](../s/stock.md) and companies, such as those from [CRSP](http://www.crsp.org/).

3. **Comprehensive [Backtesting](../b/backtesting.md):** Include price data of [stocks](../s/stock.md) or companies that failed or merged when [backtesting](../b/backtesting.md) [trading strategies](../t/trading_strategies.md).
   
4. **Data Providers:** Collaborate with reputable data providers like [Bloomberg](../b/bloomberg.md), which [offer](../o/offer.md) comprehensive datasets including delisted securities, to mitigate [survivorship bias](../s/survivorship_bias.md) ([Bloomberg Terminal](https://www.bloomberg.com/professional/solution/bloomberg-terminal/)).

## Real-World Example

A prominent example demonstrating [survivorship bias](../s/survivorship_bias.md) occurs in [mutual fund](../m/mutual_fund.md) performance analysis. Analyzing only funds that exist currently substantially overestimates their historical performance, ignoring the considerable percentage that did not survive.

An empirical study by Elton, Gruber, and Blake (1996) illustrated that nearly 50% of funds started during a specific period did not survive and [accounting](../a/accounting.md) for these non-surviving funds significantly reduced the average observed [return](../r/return.md).

## Case Study

### Long-Term Capital Management (LTCM)

LTCM was a [hedge fund](../h/hedge_fund.md) that collapsed in 1998. Ignoring such failures can give a misleading [impression](../i/impression.md) of [market](../m/market.md) stability and the efficacy of [trading strategies](../t/trading_strategies.md) being applied during that period. Including data from LTCM shows the inherent risks and can provide a more holistic view of financial strategies' impacts.

## Research Implications

In academic and practical research, [accounting](../a/accounting.md) for [survivorship bias](../s/survivorship_bias.md) is crucial for ensuring the validity of conclusions. Researchers must deliberately include data on all entities, regardless of their survival status, to avoid biased results. This is particularly important in constructing financial models and strategies that withstand real-world [market](../m/market.md) conditions.

1. **Benchmarks:** Consider using benchmarks that include both active and inactive securities.
   
2. **[Risk Management](../r/risk_management.md):** Include historical losses from failed companies to better capture true [market risk](../m/market_risk.md).

3. **Statistical Adjustments:** Statistical methods such as survival analysis can help adjust for the bias introduced by excluding non-surviving entities.

In summary, recognizing and mitigating [survivorship bias](../s/survivorship_bias.md) is essential for accurate analysis and [backtesting](../b/backtesting.md) in [algorithmic trading](../a/algorithmic_trading.md). By incorporating data from both surviving and non-surviving entities, analysts can draw more reliable and realistic inferences about [market](../m/market.md) behavior, strategy performance, and [risk management](../r/risk_management.md).
