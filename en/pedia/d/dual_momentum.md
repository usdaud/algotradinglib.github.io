# Dual Momentum

Dual [Momentum](../m/momentum.md) is an [investment strategy](../i/investment_strategy.md) popularized by Gary Antonacci, involving two types of [momentum](../m/momentum.md): absolute [momentum](../m/momentum.md) and relative [momentum](../m/momentum.md). The strategy aims to identify superior investments by looking at the performance of assets over a specified time period and making buy/sell decisions based on comparative and absolute returns. This approach attempts to capture the benefits of both [trend](../t/trend.md)-following (absolute [momentum](../m/momentum.md)) and [value investing](../v/value_investing.md) (relative [momentum](../m/momentum.md)) strategies.

## The Basics of Momentum

[Momentum](../m/momentum.md) in [finance](../f/finance.md) refers to the tendency for assets that have performed well in the past to continue performing well in the future. Conversely, assets that have performed poorly are likely to continue underperforming. [Momentum](../m/momentum.md) is generally divided into two types:

1. **Absolute [Momentum](../m/momentum.md):** This measures the performance of an [asset](../a/asset.md) relative to its own past performance. For example, if a stock has shown positive returns over the past year, it has positive absolute [momentum](../m/momentum.md).
   
2. **Relative [Momentum](../m/momentum.md):** This measures the performance of an [asset](../a/asset.md) relative to other assets. For example, if a stock has outperformed other [stocks](../s/stock.md) over the same period, it has positive relative [momentum](../m/momentum.md).

Dual [Momentum](../m/momentum.md) integrates these two concepts to create a [robust](../r/robust.md) [trading strategy](../t/trading_strategy.md).

## Absolute Momentum

Absolute [momentum](../m/momentum.md) is also known as time-series [momentum](../m/momentum.md). It focuses on an [asset](../a/asset.md)'s price behavior over a particular time window. Gary Antonacci recommended a 12-month look-back period for calculating absolute [momentum](../m/momentum.md). The procedure is straightforward: 

- Calculate the [asset](../a/asset.md)'s returns over the past 12 months.
- If the returns are positive, the [asset](../a/asset.md) has positive absolute [momentum](../m/momentum.md); otherwise, it has negative absolute [momentum](../m/momentum.md).

Absolute [momentum](../m/momentum.md) helps avoid investments in down-trending assets and drives the strategy to favor assets with upward price trends. 

## Relative Momentum

Relative [momentum](../m/momentum.md) evaluates the performance of an [asset](../a/asset.md) in relation to a group of other assets. This approach allows investors to pick securities that are expected to [outperform](../o/outperform.md) their peers. For instance, if you're comparing [multiple](../m/multiple.md) [stocks](../s/stock.md), relative [momentum](../m/momentum.md) would help you identify which [stocks](../s/stock.md) are doing better relative to the others. 

The calculation typically involves:

- Comparing the 12-month performance of each [asset](../a/asset.md) in a specified universe.
- Ranking the assets based on their performance.

In the simplest form, you might always choose to invest in the top-performing assets in the group while avoiding or shorting the underperformers.

## Combining Absolute and Relative Momentum

Dual [Momentum](../m/momentum.md) strategy involves a two-step process to identify optimal investments. Here's a generalized framework:

1. **Step 1: Apply Relative [Momentum](../m/momentum.md) Screening**
   - Identify a set of potential assets (e.g., [stocks](../s/stock.md), bonds, commodities).
   - Calculate the past 12-month returns for each [asset](../a/asset.md).
   - Rank the assets based on their returns.
   - Select the top-performing assets.

2. **Step 2: Apply Absolute [Momentum](../m/momentum.md) Verification**
   - For each selected [asset](../a/asset.md) from Step 1, evaluate its absolute [momentum](../m/momentum.md).
   - Measure its 12-month [return](../r/return.md).
   - If the [return](../r/return.md) is positive, the [asset](../a/asset.md) is selected for investment. If not, it is excluded or another [asset](../a/asset.md) meeting these criteria is chosen.

### Example: Global Equity and Bond Portfolio

Let's illustrate Dual [Momentum](../m/momentum.md) with an example:

1. **[Asset](../a/asset.md) Universe:** Consider a simple universe comprising [global equities](../g/global_equities.md) and bonds.
2. **Relative [Momentum](../m/momentum.md) Screening:** Rank the [global equities](../g/global_equities.md) and bonds based on their 12-month returns.
3. **Absolute [Momentum](../m/momentum.md) Verification:** From the top-ranked [asset](../a/asset.md)(s), [check](../c/check.md) if their 12-month [return](../r/return.md) is positive.
   - If positive, invest in those assets.
   - If negative, move to the next ranked [asset](../a/asset.md) or allocate funds differently (e.g., to cash or Treasury bills).

This combination creates a diversified portfolio that aims to capture high-[return](../r/return.md) opportunities while mitigating [risk](../r/risk.md) by avoiding down-trending assets.

## Practical Implementation and Tools

### Software and Platforms

1. **[AlgoTrader](../a/algotrader.md):** [AlgoTrader](../a/algotrader.md) is a comprehensive [trading platform](../t/trading_platform.md) that can assist in implementing Dual [Momentum](../m/momentum.md) strategies. It offers tools for [backtesting](../b/backtesting.md), strategy development, and live trading. [Visit AlgoTrader](https://www.algotrader.com/)
   
2. **Python Libraries:** Utilizing Python libraries like pandas and numpy can help build custom Dual [Momentum](../m/momentum.md) models. Tools like Jupyter Notebooks provide an interactive environment to visualize and tweak the strategy.

3. **Online Brokers:** Many online brokerage platforms, such as [Interactive Brokers](../i/interactive_brokers.md), [offer](../o/offer.md) APIs for automated trading. Integrating these with Dual [Momentum](../m/momentum.md) strategies can streamline the investment process. [Visit Interactive Brokers](https://www.interactivebrokers.com/)

4. **[QuantConnect](../q/quantconnect.md):** [QuantConnect](../q/quantconnect.md) is a cloud-based [algorithmic trading](../a/algorithmic_trading.md) platform allowing users to design, backtest, and deploy [trading strategies](../t/trading_strategies.md), including Dual [Momentum](../m/momentum.md). [Visit QuantConnect](https://www.quantconnect.com/)

### Strategy Execution

1. **[Backtesting](../b/backtesting.md):** Before deploying a Dual [Momentum](../m/momentum.md) strategy, rigorous [backtesting](../b/backtesting.md) is crucial. This involves running the strategy through historical data to evaluate its performance. Ensure to include [transaction costs](../t/transaction_costs.md) and [slippage](../s/slippage.md) in these analyses.

2. **Live Trading:** After successful [backtesting](../b/backtesting.md), the move to live trading should be gradual. Start with a small fraction of the portfolio to monitor real-world performance.

3. **Periodic Review:** Continuously review the strategy's performance. Markets evolve, and strategies may need recalibration over time.

## Advantages and Disadvantages

### Advantages

1. **[Risk Management](../r/risk_management.md):** By combining absolute and relative [momentum](../m/momentum.md), the strategy can help avoid prolonged downtrending assets, thus managing [risk](../r/risk.md) better than simpler strategies.
   
2. **[Diversification](../d/diversification.md):** The method encourages [investing](../i/investing.md) across a diverse set of assets, potentially smoothing out [volatility](../v/volatility.md).

3. **Systematic Approach:** Dual [Momentum](../m/momentum.md) is rule-based, reducing emotional biases in investment decisions.

### Disadvantages

1. **Data-intensive:** Requires access to historical price data and regular updates, making it resource-intensive.
   
2. **Complexity:** More complex than single-[momentum](../m/momentum.md) strategies, making it harder for newcomers to implement effectively.

3. **[Market](../m/market.md) Conditions:** Performance can vary based on [market](../m/market.md) conditions. In extremely volatile or trending markets, the strategy might not perform as expected.

## Real-world Performance

Empirical studies and real-world implementations have shown that Dual [Momentum](../m/momentum.md) strategies can [outperform](../o/outperform.md) conventional buy-and-[hold](../h/hold.md) strategies over long periods. Gary Antonacci's book, "Dual [Momentum Investing](../m/momentum_investing.md)", provides ample evidence and case studies demonstrating the efficacy of the method. However, as with all strategies, past performance is not indicative of future results.

## Conclusion

Dual [Momentum investing](../m/momentum_investing.md) offers a balanced approach to capitalizing on the inherent trends and relative strengths of different assets. By integrating both absolute and relative [momentum](../m/momentum.md), investors can systematically enhance returns while managing [risk](../r/risk.md). Though not without challenges, the strategy's evidence-based framework and systematic nature make it a compelling choice for both individual and institutional investors. For those willing to invest the necessary time and resources, Dual [Momentum](../m/momentum.md) can be a potent addition to the investment toolkit.
