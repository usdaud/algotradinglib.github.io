# 90% Rule

### Introduction

[Algorithmic trading](../a/algorithmic_trading.md), also known as algo-trading, involves using computer algorithms to automate and optimize [trading strategies](../t/trading_strategies.md). These algorithms can execute trades at speeds and frequencies that human traders cannot match. One of the guiding principles for effective [algorithmic trading](../a/algorithmic_trading.md) is the "90% Rule," which emphasizes the importance of model robustness and adaptability. 

### Understanding the 90% Rule

The 90% Rule essentially states that:

- **90% of the effort in [algorithmic trading](../a/algorithmic_trading.md) should be spent on research, development, and testing.**
- **Only 10% should be on implementing and running the [trading algorithms](../t/trading_algorithms.md).**

### Research and Development

#### Data Collection

A significant portion of the 90% effort goes into data collection. High-quality data is the backbone of any successful trading algorithm. Several types of data are gathered:

- **Historical Price Data**: This includes past prices of financial instruments, which helps in understanding market trends.
- **Order Book Data**: Provides insights into market depth and liquidity.
- **News Data**: [Sentiment analysis](../s/sentiment_analysis.md) of news headlines and articles can affect market movements.
- **[Alternative Data](../a/alternative_data.md)**: This includes [non-traditional data sources](../n/non-traditional_data_sources.md) like [social media sentiment](../s/social_media_sentiment.md), satellite imagery, etc.

#### Data Cleaning and Preprocessing

Once the data is collected, the next step is to clean and preprocess it. This step ensures that the data is accurate and free of any inconsistencies. Activities include:

- **Handling Missing Values**: Null or missing values in datasets are imputed or removed.
- **Outlier Detection**: Identifies and handles anomalies in the data.
- **Normalization**: Scales the data to make it uniform.

#### Feature Engineering

Feature engineering involves creating new features based on original data that can improve the performance of [trading algorithms](../t/trading_algorithms.md). Examples include:

- **[Technical Indicators](../t/technical_indicators.md)**: Moving averages, RSI, MACD, etc.
- **Statistical Features**: Mean, variance, skewness, etc.

#### Algorithm Design

Once the data is ready, the next step is designing the trading algorithm. Key components include:

- **Strategy Selection**: Examples include [mean reversion](../m/mean_reversion.md), [trend following](../t/trend_following.md), and [arbitrage](../a/arbitrage.md).
- **[Risk Management](../r/risk_management.md)**: [Position sizing](../p/position_sizing.md), stop-loss mechanisms, and other [risk management](../r/risk_management.md) tools.
- **[Execution Algorithms](../e/execution_algorithms.md)**: Market orders, limit orders, and more sophisticated execution strategies like VWAP and TWAP.

### Backtesting

[Backtesting](../b/backtesting.md) is the process of testing the trading algorithm on historical data to evaluate its performance. This involves:

- **Creating a Simulated Environment**: Mock [trading environment](../t/trading_environment.md) replicating real-market conditions.
- **[Performance Metrics](../p/performance_metrics.md)**: Evaluating the algorithm using metrics like [Sharpe Ratio](../s/sharpe_ratio.md), Max Drawdown, etc.
- **[Overfitting Prevention](../o/overfitting_prevention.md)**: Ensuring that the model is not overly specialized to historical data.

### Optimization

Optimization involves tuning the model parameters to maximize performance:

- **[Grid Search](../g/grid_search_in_trading.md)**: Testing all possible combinations of parameters.
- **Random Search**: Random sampling of parameters.
- **[Bayesian Optimization](../b/bayesian_optimization.md)**: More sophisticated method for parameter tuning.

### Forward Testing

Forward testing, also known as paper trading or walk-forward testing, involves testing the model on out-of-sample data to validate its robustness. 

### Implementation

Once the model has been rigorously tested, it's time to implement it. This involves:

- **Setting up the Infrastructure**: Servers, databases, and connectivity to brokers.
- **Continuous Monitoring**: Real-time monitoring of algorithm performance.
- **Periodic Re-evaluation**: Regularly updating the model based on new data and market conditions.

### Companies Specializing in Algo-Trading

1. **[QuantConnect](../q/quantconnect.md)**: (https://www.[quantconnect](../q/quantconnect.md).com/)
   - [QuantConnect](../q/quantconnect.md) provides a cloud-based algorithm trading platform. It allows users to backtest, optimize, and deploy [trading algorithms](../t/trading_algorithms.md) across multiple asset classes.

2. **[AlgoTrader](../a/algotrader.md)**: (https://www.[algotrader](../a/algotrader.md).com/)
   - [AlgoTrader](../a/algotrader.md) offers [algorithmic trading](../a/algorithmic_trading.md) software for [quantitative research](../q/quantitative_research.md), trading strategy development, [backtesting](../b/backtesting.md), optimization, and execution.

3. **WorldQuant**: (https://www.worldquant.com/)
   - WorldQuant is a global quantitative investment management firm that uses mathematical and statistical methods, analysis, distinct [trading algorithms](../t/trading_algorithms.md) to manage global investment portfolios.

### Conclusion

The 90% Rule underscores the complexity and rigor involved in developing a successful trading algorithm. By focusing the vast majority of effort on research, development, and testing, traders can ensure that their algorithms are robust, adaptable, and more likely to succeed in the real world.
