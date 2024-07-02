# Survivorship Analysis

Survivorship analysis is a vital concept in both academic finance and practical [trading strategies](../t/trading_strategies.md). It deals with the phenomenon of [survivorship bias](../s/survivorship_bias.md), which occurs when only the "survivors" of a particular process are considered in a data analysis. In the world of finance, this typically means focusing only on companies that are currently listed without taking into account those that have failed, been delisted, or merged. The consequence of ignoring these entities can lead to skewed and overly optimistic dataset results, which can consequently distort [backtesting](../b/backtesting.md) results and future performance predictions of [trading strategies](../t/trading_strategies.md).

## Understanding Survivorship Bias

In the context of financial markets, [survivorship bias](../s/survivorship_bias.md) typically manifests in the form of datasets that include only stocks currently trading and exclude those that have gone bankrupt or have been delisted. This creates an upward bias in historical performance analysis, as it disproportionately reflects companies that have been successful enough to remain listed.

### Historical Database and Survivorship Bias

Most historical stock market databases are prone to [survivorship bias](../s/survivorship_bias.md). They often fail to include delisted stocks, which can significantly alter the outcomes of backtests and the apparent efficacy of [trading strategies](../t/trading_strategies.md). For instance, assume an algorithm is backtested over a decade using a dataset that does not account for companies that went bankrupt or were delisted during that period. The returns calculated from such a dataset will present a higher-than-true performance number as poor-performing stocks are systematically excluded.

### Key Implications

1. **Optimistic Performance Measures**: [Backtesting](../b/backtesting.md) a trading strategy on a dataset that suffers from [survivorship bias](../s/survivorship_bias.md) often leads to overly optimistic performance figures.
2. **Inaccurate Risk Assessment**: Stocks that were delisted or went bankrupt may have represented higher risk that is not captured in a survivorship-biased dataset.
3. **Ineffective Strategy Development**: Strategies developed on biased datasets might fail in real-world applications because they were optimized on skewed data.

## Methods to Mitigate Survivorship Bias

[Survivorship bias](../s/survivorship_bias.md) can be mitigated by using a variety of approaches, including:

### Inclusion of Delisted Stocks

Ensuring the dataset includes all securities, including those that have been delisted, gone bankrupt, or merged can provide a more accurate representation of historical performance. Some databases like the CRSP (Center for Research in Security Prices) database include this information.

### Surviving Universe Analysis

Another technique is to conduct two separate analyses: one on the surviving universe and another on the entire historical universe, including delisted stocks. Comparing these results can provide insights into the extent of [survivorship bias](../s/survivorship_bias.md).

### Adjusted Historical Data

Many vendors and financial data companies now offer survivorship-bias-free datasets, which adjust historical data to account for stocks that failed to survive. For example, the Reuters and Bloomberg datasets often include adjustments for [survivorship bias](../s/survivorship_bias.md).

## Tools and Resources

Several tools and resources are available for performing survivorship analysis and mitigating [survivorship bias](../s/survivorship_bias.md):

### QuantConnect

QuantConnect is an [algorithmic trading](../a/algorithmic_trading.md) platform that provides access to both currently listed and historically delisted securities, allowing for more accurate [backtesting](../b/backtesting.md):
[QuantConnect](https://www.quantconnect.com/)

### Tiingo

Tiingo offers a survivorship-bias-free database, which allows traders and researchers to access data that includes delisted securities:
[Tiingo](https://www.tiingo.com/)

### AlgoTrader

AlgoTrader is another platform that offers tools and datasets designed to eliminate [survivorship bias](../s/survivorship_bias.md) from [backtesting](../b/backtesting.md):
[AlgoTrader](https://www.algotrader.com/)

## Practical Example: Backtesting a Trading Strategy

Consider an algorithmic trader developing a [momentum trading](../m/momentum_trading.md) strategy. If the trader uses a dataset that only includes stocks currently listed on the NYSE, the backtest might show that the strategy produces an annual return of 15%. However, if delisted stocks are included, the performance might drop to an annual return of 10%, as the dataset now reflects the inclusion of companies that went bust or were delisted. This stark difference can significantly impact the trader's perception of the strategy's effectiveness and associated risk levels.

### Step-by-step Process

1. **Select Data Source:** Choose a historical database that is known to be survivorship-bias-free, like CRSP or use platforms such as QuantConnect and Tiingo.
2. **Prepare Data:** Clean and preprocess the data to include both listed and delisted stocks, ensuring that all historical price data is considered.
3. **Backtest Strategy:** Run your trading strategy on the cleaned dataset. Ensure you monitor key metrics like returns, risk, and Sharpe ratios.
4. **Analyze Results:** Compare the results of your backtest against a similar test using a biased dataset. Note the differences in [performance metrics](../p/performance_metrics.md).
5. **Adjust Strategy:** If the results varied significantly, consider modifying your strategy to better handle the realities of a complete market, including failures and delistings.

By meticulously accounting for [survivorship bias](../s/survivorship_bias.md), algorithmic traders can develop more robust, realistic, and ultimately more profitable [trading strategies](../t/trading_strategies.md). Survivorship analysis remains a critical step for any serious quant trader dedicated to understanding and mitigating biases in market data.

This comprehensive analysis ensures the integrity of [backtesting](../b/backtesting.md) processes and fortifies the development of [trading algorithms](../t/trading_algorithms.md) against the pitfalls of overly-optimistic historical [performance metrics](../p/performance_metrics.md).
