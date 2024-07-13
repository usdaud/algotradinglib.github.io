# Compound Annual Growth Rate (CAGR)

### Introduction
The Compound Annual Growth Rate (CAGR) is a metric that is used to measure the mean annual growth rate of an investment over a specified time period longer than one year. CAGR is a useful measure because it represents one of the most accurate ways to calculate and determine returns for anything that can rise or fall in [value](../v/value.md) over time. Unlike average annual returns, CAGR represents one rate that, if compounded over a period of years, would [yield](../y/yield.md) the investment's ending [value](../v/value.md).

### Formula and Calculation
The formula for CAGR is:

\[ \text{CAGR} = \left( \frac{EV}{BV} \right)^{\frac{1}{n}} - 1 \]

Where:
- \( EV \) = Ending [Value](../v/value.md)
- \( BV \) = Beginning [Value](../v/value.md)
- \( n \) = Number of years

Let's break it down with an example:

1. Suppose you have an investment that was worth $1,000 at the beginning and $2,000 after 5 years.
2. The formula would be applied as follows:

\[ \text{CAGR} = \left( \frac{2000}{1000} \right)^{\frac{1}{5}} - 1 \]
\[ \text{CAGR} = (2)^{0.2} - 1 \]
\[ \text{CAGR} \approx 0.1487 \text{ or } 14.87\% \]

Thus, the investment has grown at an annual compound growth rate of approximately 14.87%.

### Importance in Algorthmic Trading
In [algorithmic trading](../a/algorithmic_trading.md), CAGR is essential for the following reasons:

1. **Performance Measurement:** It provides a single annualized rate that shows the consistent growth of an investment portfolio over time, even if the growth happened at an irregular rate year over year.
  
2. **Portfolio Comparison:** Traders can use CAGR to compare the performance of different portfolios or investment strategies over the same period because it normalizes the [growth rates](../g/growth_rates_in_trading.md).
  
3. **[Risk](../r/risk.md) Evaluation:** By comparing CAGR with the [volatility](../v/volatility.md) of the investment (measured in terms of the [standard deviation](../s/standard_deviation.md) of returns), traders can evaluate the [risk](../r/risk.md)-adjusted performance of a strategy. 

### Practical Applications

#### Portfolio "A" vs. Portfolio "B"
Consider two portfolios over a 3-year period:

- Portfolio "A" grows from $10,000 to $13,000.
- Portfolio "B" fluctuates wildly but grows from $10,000 to $12,500.

To decide which portfolio performed better in terms of steady growth, we calculate the respective CAGRs:

**Portfolio "A":**

\[ \text{CAGR} = \left( \frac{13000}{10000} \right)^{\frac{1}{3}} - 1 \]
\[ \text{CAGR} = (1.3)^{0.3333} - 1 \]
\[ \text{CAGR} \approx 0.0914 \text{ or } 9.14\% \]

**Portfolio "B":**

\[ \text{CAGR} = \left( \frac{12500}{10000} \right)^{\frac{1}{3}} - 1 \]
\[ \text{CAGR} = (1.25)^{0.3333} - 1 \]
\[ \text{CAGR} \approx 0.0764 \text{ or } 7.64\% \]

Even though Portfolio "B" had significant upticks and downticks, Portfolio "A" demonstrated more consistent growth as indicated by a higher CAGR.

### Comparison to Other Metrics

#### Average Annual Return
Unlike the average [annual return](../a/annual_return.md), CAGR smoothes out the effects of [volatility](../v/volatility.md). For instance, an [asset](../a/asset.md) that gains 100% in one year and loses 50% the next year has an average [annual return](../a/annual_return.md) of 25% over those two years. However, its CAGR illustrates a different reality:

\[ \text{CAGR} = \left( \frac{1.50}{1.00} \right)^{\frac{1}{2}} - 1 \]
\[ \text{CAGR} = (1.50)^{0.5} - 1 \]
\[ \text{CAGR} \approx 0.225 \text{ or } 22.5\% \]

#### Total Return
[Total return](../t/total_return.md) refers to the total [gain](../g/gain.md) or loss on an investment, including dividends, [interest](../i/interest.md), and [capital](../c/capital.md) gains. Unlike CAGR, it does not [annualize](../a/annualize.md) the returns, making CAGR a preferable metric for comparing investments of different lengths.

### Real-World Usage

#### Investors
Private and institutional investors use CAGR to gauge the performance of investments like [stocks](../s/stock.md), bonds, and mutual funds. Websites like [Morningstar](https://www.morningstar.com) often use CAGR when showcasing the historical performance of investment funds.

#### Financial Analysts
Analysts use CAGR in their financial models to predict future [earnings](../e/earnings.md) and to evaluate the historical performance of a company. This can be seen in Analyst reports from companies like [Goldman Sachs](https://www.goldmansachs.com).

#### Businesses
Businesses use CAGR to monitor and report the growth of key [performance indicators](../p/performance_indicators.md) (KPIs) such as [revenue](../r/revenue.md), profits, and user base. Companies like [Amazon](https://www.amazon.com) display such data in their annual reports to showcase performance growth over time.

### Limitations of CAGR
Despite its usefulness, CAGR has some limitations:

1. **Does Not Reflect [Volatility](../v/volatility.md):** CAGR smoothes returns to show an average rate of growth, thereby masking the [volatility](../v/volatility.md) an investment might experience from year to year.

2. **Past Performance:** It’s backward-looking and may not necessarily predict future performance.

3. **Single Metric:** It should not be used in isolation but rather combined with other metrics like [standard deviation](../s/standard_deviation.md), [Sharpe ratio](../s/sharpe_ratio.md), and maximum [drawdown](../d/drawdown.md) to get a comprehensive view.

### Conclusion
CAGR provides a clear and straightforward metric for comparing the annual [growth rates](../g/growth_rates_in_trading.md) of investments over time. It's a critical tool for traders, investors, analysts, and businesses to measure and compare performance accurately. Its main advantage is its ability to normalize the [growth rates](../g/growth_rates_in_trading.md) of different investments, providing a 'smoother' perspective on performance. However, users should be aware of its limitations and use it in conjunction with other metrics for a well-rounded analysis.