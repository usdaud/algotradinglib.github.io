# Survivorship Analysis

Survivorship analysis is a vital concept in both academic [finance](../f/finance.md) and practical [trading strategies](../t/trading_strategies.md). It deals with the phenomenon of [survivorship bias](../s/survivorship_bias.md), which occurs when only the "survivors" of a particular process are considered in a data analysis. In the world of [finance](../f/finance.md), this typically means focusing only on companies that are currently [listed](../l/listed.md) without taking into account those that have failed, been delisted, or merged. The consequence of ignoring these entities can lead to skewed and overly optimistic dataset results, which can consequently distort [backtesting](../b/backtesting.md) results and future performance predictions of [trading strategies](../t/trading_strategies.md).

## Understanding Survivorship Bias

In the context of [financial markets](../f/financial_market.md), [survivorship bias](../s/survivorship_bias.md) typically manifests in the form of datasets that include only [stocks](../s/stock.md) currently trading and exclude those that have gone bankrupt or have been delisted. This creates an upward bias in historical performance analysis, as it disproportionately reflects companies that have been successful enough to remain [listed](../l/listed.md).

### Historical Database and Survivorship Bias

Most historical [stock market](../s/stock_market.md) databases are prone to [survivorship bias](../s/survivorship_bias.md). They often [fail](../f/fail.md) to include delisted [stocks](../s/stock.md), which can significantly alter the outcomes of backtests and the apparent efficacy of [trading strategies](../t/trading_strategies.md). For instance, assume an algorithm is backtested over a decade using a dataset that does not account for companies that went bankrupt or were delisted during that period. The returns calculated from such a dataset [will](../w/will.md) present a higher-than-true performance number as poor-performing [stocks](../s/stock.md) are systematically excluded.

### Key Implications

1. **Optimistic Performance Measures**: [Backtesting](../b/backtesting.md) a [trading strategy](../t/trading_strategy.md) on a dataset that suffers from [survivorship bias](../s/survivorship_bias.md) often leads to overly optimistic performance figures.
2. **Inaccurate [Risk](../r/risk.md) Assessment**: [Stocks](../s/stock.md) that were delisted or went bankrupt may have represented higher [risk](../r/risk.md) that is not captured in a survivorship-biased dataset.
3. **Ineffective Strategy Development**: Strategies developed on biased datasets might [fail](../f/fail.md) in real-world applications because they were optimized on skewed data.

## Methods to Mitigate Survivorship Bias

[Survivorship bias](../s/survivorship_bias.md) can be mitigated by using a variety of approaches, including:

### Inclusion of Delisted Stocks

Ensuring the dataset includes all securities, including those that have been delisted, gone bankrupt, or merged can provide a more accurate representation of historical performance. Some databases like the CRSP (Center for Research in [Security](../s/security.md) Prices) database include this information.

### Surviving Universe Analysis

Another technique is to conduct two separate analyses: one on the surviving universe and another on the entire historical universe, including delisted [stocks](../s/stock.md). Comparing these results can provide insights into the extent of [survivorship bias](../s/survivorship_bias.md).

### Adjusted Historical Data

Many vendors and financial data companies now [offer](../o/offer.md) survivorship-bias-free datasets, which adjust historical data to account for [stocks](../s/stock.md) that failed to survive. For example, the [Reuters](../r/reuters.md) and [Bloomberg](../b/bloomberg.md) datasets often include adjustments for [survivorship bias](../s/survivorship_bias.md).

## Tools and Resources

Several tools and resources are available for performing survivorship analysis and mitigating [survivorship bias](../s/survivorship_bias.md):

### StockSharp

[StockSharp](../s/stocksharp.md) is an [algorithmic trading](../a/algorithmic_trading.md) platform that provides access to both currently [listed](../l/listed.md) and historically delisted securities, allowing for more accurate [backtesting](../b/backtesting.md):

### Tiingo

[Tiingo](../t/tiingo.md) offers a survivorship-bias-free database, which allows traders and researchers to access data that includes delisted securities:

### AlgoTrader

[AlgoTrader](../a/algotrader.md) is another platform that offers tools and datasets designed to eliminate [survivorship bias](../s/survivorship_bias.md) from [backtesting](../b/backtesting.md):

## Practical Example: Backtesting a Trading Strategy

Consider an algorithmic [trader](../t/trader.md) developing a [momentum trading](../m/momentum_trading.md) strategy. If the [trader](../t/trader.md) uses a dataset that only includes [stocks](../s/stock.md) currently [listed](../l/listed.md) on the NYSE, the backtest might show that the strategy produces an [annual return](../a/annual_return.md) of 15%. However, if delisted [stocks](../s/stock.md) are included, the performance might drop to an [annual return](../a/annual_return.md) of 10%, as the dataset now reflects the inclusion of companies that went bust or were delisted. This stark difference can significantly impact the [trader](../t/trader.md)'s perception of the strategy's effectiveness and associated [risk](../r/risk.md) levels.

### Step-by-step Process

1. **Select Data Source:** Choose a historical database that is known to be survivorship-bias-free, like CRSP or use platforms such as [StockSharp](../s/stocksharp.md) and [Tiingo](../t/tiingo.md).
2. **Prepare Data:** Clean and preprocess the data to include both [listed](../l/listed.md) and delisted [stocks](../s/stock.md), ensuring that all historical price data is considered.
3. **Backtest Strategy:** Run your [trading strategy](../t/trading_strategy.md) on the cleaned dataset. Ensure you monitor key metrics like returns, [risk](../r/risk.md), and Sharpe ratios.
4. **Analyze Results:** Compare the results of your backtest against a similar test using a biased dataset. [Note](../n/note.md) the differences in [performance metrics](../p/performance_metrics.md).
5. **Adjust Strategy:** If the results varied significantly, consider modifying your strategy to better [handle](../h/handle.md) the realities of a complete [market](../m/market.md), including failures and delistings.

By meticulously [accounting](../a/accounting.md) for [survivorship bias](../s/survivorship_bias.md), algorithmic traders can develop more [robust](../r/robust.md), realistic, and ultimately more profitable [trading strategies](../t/trading_strategies.md). Survivorship analysis remains a critical step for any serious quant [trader](../t/trader.md) dedicated to understanding and mitigating biases in [market](../m/market.md) data.

This comprehensive analysis ensures the integrity of [backtesting](../b/backtesting.md) processes and fortifies the development of [trading algorithms](../t/trading_algorithms.md) against the pitfalls of overly-optimistic historical [performance metrics](../p/performance_metrics.md).
