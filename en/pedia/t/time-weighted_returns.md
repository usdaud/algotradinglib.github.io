# Time-Weighted Returns

In the realm of investment performance evaluation, the Time-Weighted Return (TWR), also known as the [geometric mean](../g/geometric_mean_in_trading.md) return, is a vital metric. This method of return calculation eliminates the effects of cash inflows and outflows, providing a fair assessment of an investment manager's performance over multiple periods. The TWR is especially relevant in the context of performance measurement and comparison, where contributions and withdrawals can unduly influence the results.

#### Definition and Importance

Time-[Weighted Returns](../w/weighted_returns_in_trading.md) are used to evaluate the rate of return earned by an investment portfolio regardless of the effects of additional investments or withdrawals. This characteristic makes it a crucial tool for comparing the performance of investment funds, mutual funds, and any managed investment portfolios. The TWR is particularly beneficial when the timing and amount of cash flows are outside the control of the portfolio manager.

#### Calculation Method

The calculation of Time-[Weighted Returns](../w/weighted_returns_in_trading.md) involves a multi-step process:

1. **Segmentation into Sub-Periods**: The overall investment period is divided into sub-periods based on the timing of cash flows. Each sub-period represents the time between any two consecutive cash flows or the start and the end of the investment period.

2. **Determining Sub-Period Returns**: For each sub-period, the return is calculated as follows:
   \[
   R_i = \frac{(V_i - V_{i-1} - C_i)}{V_{i-1}}
   \]
   where:
   - \( R_i \) is the return for sub-period \( i \)
   - \( V_i \) is the portfolio value at the end of sub-period \( i \)
   - \( V_{i-1} \) is the portfolio value at the beginning of sub-period \( i \)
   - \( C_i \) is the net cash flow during sub-period \( i \)

3. **Compounding Sub-Period Returns**: After calculating the returns for each sub-period, these returns are compounded to derive the overall Time-Weighted Return using the formula:
   \[
   TWR = (1 + R_1) \times (1 + R_2) \times \ldots \times (1 + R_n) - 1
   \]
   Here, \( R_1, R_2, \ldots, R_n \) are the sub-period returns, and \( n \) is the number of sub-periods.

#### Example Calculation

Consider a portfolio with the following values and cash flows:

- Portfolio value at T0 (beginning): $100,000
- Portfolio value at T1: $105,000 (no cash flow)
- Portfolio value at T2: $110,000 (after withdrawing $5,000)
- Portfolio value at T3: $120,000 (no cash flow)
- Portfolio value at T4 (end): $130,000 (after investing an additional $10,000)

Steps:

1. Segmenting into sub-periods:
   - Period 1: T0 to T1
   - Period 2: T1 to T2
   - Period 3: T2 to T3
   - Period 4: T3 to T4

2. Calculating sub-period returns:
   \[
   R_1 = \frac{(105,000 - 100,000)}{100,000} = 0.05 \, \text{(5%)}
   \]
   \[
   R_2 = \frac{(110,000 - 105,000 + 5,000)}{105,000} = 0.0952 \, \text{(9.52%)}
   \]
   \[
   R_3 = \frac{(120,000 - 110,000)}{110,000} = 0.0909 \, \text{(9.09%)}
   \]
   \[
   R_4 = \frac{(130,000 - 120,000 - 10,000)}{120,000} = 0 \, \text{(0%)}
   \]

3. Compounding returns:
   \[
   TWR = (1 + 0.05) \times (1 + 0.0952) \times (1 + 0.0909) \times (1 + 0) - 1
   \]
   \[
   TWR = 1.05 \times 1.0952 \times 1.0909 \times 1 - 1
   \]
   \[
   TWR = 1.2562 - 1 = 0.2562 \, \text{(25.62%)}
   \]

Hence, the Time-Weighted Return for this portfolio over the entire period is 25.62%.

#### Advantages and Disadvantages

**Advantages:**
- **Eliminates Cash Flow Effects**: TWR provides a pure measure of the portfolio’s performance by neutralizing the impact of cash flows.
- **Consistency in Comparison**: Enables fair comparison across different portfolios and managers.
- **Preferred by Industry**: Often recommended by industry standards and guidelines such as the Global Investment Performance Standards (GIPS).

**Disadvantages:**
- **Complex Calculation**: The necessity for detailed transaction records and segmentation can make the calculation cumbersome.
- **May Not Reflect Investor Experience**: Ignores the actual timing and impact of cash flows from the investor's perspective.

#### Applications in the Industry

Time-[Weighted Returns](../w/weighted_returns_in_trading.md) are widely used by mutual funds, hedge funds, and investment managers to report performance. Regulatory bodies and performance reporting standards also prefer TWR for its consistency and comparability. Examples of entities using TWR include:

- **Vanguard**: Vanguard, a major player in the mutual fund industry, reports TWR for its wide array of funds, allowing investors to gauge performance objectively. [Vanguard Performance Reporting](https://investor.vanguard.com/performance)
- **Fidelity**: Fidelity Investment uses TWR to provide comparative [performance metrics](../p/performance_metrics.md) across their offerings, ensuring that investors can make informed decisions. [Fidelity Performance Data](https://www.fidelity.com/mutual-funds/investment-options/performance)
- **[Morningstar](../m/morningstar.md)**: [Morningstar](../m/morningstar.md), a leading investment research firm, incorporates TWR in its fund analysis and ratings, enhancing the comparability and reliability of its data. [Morningstar Methodology](https://www.morningstar.com/learn/glossary/time-weighted-rate-of-return)

Overall, Time-[Weighted Returns](../w/weighted_returns_in_trading.md) are indispensable in the financial industry for providing unbiased [performance metrics](../p/performance_metrics.md). It remains a cornerstone in performance evaluation, ensuring transparency and fairness in the reporting of investment returns.
