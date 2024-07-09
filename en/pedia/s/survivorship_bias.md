# Survivorship Bias

Survivorship Bias is a logical error that concentrates on the people or things that "survived" some process and inadvertently overlooks those that did not because of their lack of visibility. This bias can skew various types of analyses and conclusions. The term is widely discussed in the context of finance, especially in [algorithmic trading](../a/algorithmic_trading.md) and investment strategies. Let's delve deeper into its definition, implications, and its significant role in the realm of [algorithmic trading](../a/algorithmic_trading.md).

#### Definition and Explanation

Survivorship Bias occurs when an analysis only takes into account the entities that have successfully completed a process, disregarding those that have failed. This selective visibility can lead to an overestimation of the performance or characteristics of a certain group.

Consider a simple historical example from World War II: when analyzing bullet holes in returning fighter planes to improve armor, the logical conclusion might be to reinforce the areas most hit. However, Abraham Wald, a statistician, showed that the bullet holes visible on returning planes were on areas that were not critical, as planes hit in critical areas did not return. By understanding this bias, the reinforcement was applied to unhit critical areas, improving overall survival.

#### Implications in Algorithmic Trading

[Algorithmic trading](../a/algorithmic_trading.md) (also known as algo-trading) refers to using computer algorithms to manage [trading strategies](../t/trading_strategies.md), usually at high speed and high frequency. Survivorship Bias in this context can be particularly misleading when analyzing historical data to develop [trading strategies](../t/trading_strategies.md).

##### 1. Historical Performance Overestimation
When testing an [algorithmic trading](../a/algorithmic_trading.md) strategy, if historical data only includes surviving stocks (stocks that have not been delisted or gone bankrupt), the backtest results will likely overestimate the performance. This is because the dataset disregards the stocks that performed poorly and were removed from indices or went bankrupt.

##### 2. Misleading Risk Assessments
Survivorship Bias can also distort risk assessments. If one only looks at data from firms that survived a financial crisis, the [risk models](../r/risk_models_in_trading.md) built from such data might underestimate the true risks involved. Real-world trading incorporates firms that failed—failing to include these in the analysis means ignoring the "tail risks" that can lead to significant losses.

##### 3. Robustness to Market Conditions
Strategies developed without considering survivorship bias may appear robust in backtests but could perform poorly under actual market conditions. This is because the backtested data might not represent true market conditions, having excluded a swath of failing companies that would otherwise impact the strategy's robustness.

#### How to Mitigate Survivorship Bias

Several techniques can be employed to mitigate Survivorship Bias in [algorithmic trading](../a/algorithmic_trading.md):
1. **Comprehensive Data Sets:** Use databases that include delisted as well as active stocks. Some financial data providers offer complete datasets that track all stocks, including those that have failed or been delisted (e.g., CRSP U.S. Stock Databases).

2. **Survivorship Bias-Free Indices:** Opt for indices specifically constructed to avoid survivorship bias. These indices track both living and dead entities, providing a more realistic picture of historical performance.

3. **[Sector Analysis](../s/sector_analysis.md):** When [backtesting](../b/backtesting.md), consider sector-specific survivorship. Sectors have different failure rates and characteristics, and incorporating this into analysis can provide more accurate historical data.

#### Real-World Examples

##### Case Study: Long-Term Capital Management
Long-Term Capital Management (LTCM) is a famous hedge fund that collapsed in 1998. Despite having Nobel laureates on its board and sophisticated [trading algorithms](../t/trading_algorithms.md), LTCM failed due to a combination of high leverage and underestimated risk. Analysis that only focuses on surviving hedge funds might neglect the lessons from LTCM's failure, underestimating the real risks in similar strategies.

##### Example: Actively Managed Mutual Funds
Consider actively managed mutual funds. When analyzing their historical performance, excluding the funds that were closed or merged due to poor performance leads to an overestimated performance track record for surviving funds. As a result, potential investors might be misled about the true performance potential of these funds.

#### Conclusion

Survivorship Bias plays a critical role in skewing perceptions and outcomes, particularly in [algorithmic trading](../a/algorithmic_trading.md) and financial analyses. By recognizing and mitigating survivorship bias, investors and analysts can develop more accurate models and strategies that offer a true representation of market conditions and risks. Practical steps include using comprehensive databases, opting for bias-free indices, and incorporating sector-specific analyses into the models.

Understanding and addressing survivorship bias allow for better investment decisions, leading to more robust and realistic [trading strategies](../t/trading_strategies.md). Whether you are a seasoned trader or a novice in [algorithmic trading](../a/algorithmic_trading.md), being aware of this bias is pivotal to ensuring the integrity and effectiveness of your analytical insights and trading practices.
