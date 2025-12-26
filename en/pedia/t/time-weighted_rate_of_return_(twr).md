# Time-Weighted Rate of Return (TWR)

The Time-[Weighted](../w/weighted.md) [Rate of Return](../r/rate_of_return.md) (TWR) is a method of measuring the compound rate of growth in a portfolio. It neutralizes the impact of external funds flow such as deposits and withdrawals, making it an excellent choice for evaluating the performance of investment managers. TWR is especially relevant when there are [multiple](../m/multiple.md) cash flows in and out of the portfolio over a period of time and is designed to give a clear picture of the manager's performance independent of the [investor](../i/investor.md)'s actions.

## Key Components

### Definition
The TWR is calculated by dividing the portfolio period into sub-periods that correspond to the times when there are external cash flows. Each sub-period calculates the [rate of return](../r/rate_of_return.md), and these rates are then geometrically linked to produce the annualized [return](../r/return.md).

### Formula
The formula to compute TWR can be summarized as:

\[ TWR = \prod_{t=1}^{n} (1 + R_t)^{w_t} - 1 \]

where:
- \( R_t \) is the [return](../r/return.md) for each sub-period, computed as:
\[ R_t = \frac{V_t - V_{t-1} - CF_t }{V_{t-1} + CF_t} \]
- \( V_t \) is the [value](../v/value.md) of the portfolio at the end of the sub-period.
- \( V_{t-1} \) is the [value](../v/value.md) of the portfolio at the beginning of the sub-period.
- \( CF_t \) is the [cash flow](../c/cash_flow.md) at the beginning of the sub-period.
- \( w_t \) is the weight of each sub-period.

## Calculation Steps

1. **Segment the Period**: Split the total period into individual sub-periods based on external cash flows.
2. **Compute the Sub-period Returns**: For each sub-period, calculate the [return](../r/return.md) considering the portfolio [value](../v/value.md) before and after the [cash flow](../c/cash_flow.md).
3. **Geometrically Chain the Returns**: Multiply each of these sub-period returns together in a geometric series.
4. **[Annualize](../a/annualize.md) the [Return](../r/return.md)**: If the total period is longer than a year, [annualize](../a/annualize.md) the [return](../r/return.md) by taking the compound result to the power of the inverse of the number of years.

## Example Calculation

Consider an investment portfolio that experiences the following changes over a year:

| Date | Portfolio [Value](../v/value.md) | External [Cash Flow](../c/cash_flow.md) |
|------------|-----------------|--------------------|
| Jan 1, 2021| $100,000 | $0 |
| Apr 1, 2021| $120,000 | +$10,000 |
| Jul 1, 2021| $115,000 | -$5,000 |
| Oct 1, 2021| $130,000 | +$20,000 |
| Dec 31, 2021|$140,000 | $0 |

The calculation would proceed as follows:

1. **Calculate Sub-period Returns**:
 - [Return](../r/return.md) for Q1:
 \[
 R_1 = \frac{120,000 - 100,000}{100,000} = 0.20
 \]
 - [Return](../r/return.md) for Q2:
 \[
 R_2 = \frac{115,000 - (120,000 + 10,000)}{130,000} = -0.1154
 \]
 - [Return](../r/return.md) for Q3:
 \[
 R_3 = \frac{130,000 - 115,000 + 5,000}{110,000} = 0.1364
 \]
 - [Return](../r/return.md) for Q4:
 \[
 R_4 = \frac{140,000 - (130,000 + 20,000)}{150,000} = 0.0667
 \]

2. **Geometrically Link Returns**:
 \[
 TWR = (1 + R_1) \times (1 + R_2) \times (1 + R_3) \times (1 + R_4) - 1
 \]

 Simplifying this:
 \[
 TWR = (1 + 0.20) \times (1 - 0.1154) \times (1 + 0.1364) \times (1 + 0.0667) - 1
 \]
 \[
 TWR = 1.20 \times 0.8846 \times 1.1364 \times 1.0667 - 1 \approx 0.2854
 \]

3. **[Annualize](../a/annualize.md) the [Return](../r/return.md) (if necessary)**:
 Since the period is one year, the TWR for the year is 28.54%.

## Advantages
1. **Neutralizes Cash Flows**: TWR removes the impact of external cash flows, making it a fair assessment of the [portfolio manager](../p/portfolio_manager.md)'s performance.
2. **Standardized Measure**: Financial [industry](../i/industry.md) standards often require TWR because it precisely isolates the manager's investment acumen.
3. **Comparability**: Allows for a direct comparison between different portfolios or against a [benchmark](../b/benchmark.md) without the influence of [investor](../i/investor.md) contributions or withdrawals.

## Disadvantages
1. **Complexity**: The calculation of TWR is more complex compared to other methods like the [Money-Weighted Rate of Return](../m/money-weighted_rate_of_return.md) (MWR).
2. **Sub-period Performance**: May not adequately reflect performance over very small sub-periods, where very large cash flows occur.

## Applications

### Performance Measurement
Investment firms and portfolio managers often use TWR to report their performance. By standardizing the measure as TWR, they ensure that their reported returns are comparable across different portfolios and time periods, regardless of [investor](../i/investor.md)-specific cash flows.

### Benchmarking
TWR allows comparison against benchmarks such as indices. Since benchmarks do not have cash flows, comparing the TWR of a portfolio against a [market index](../m/market_index.md) provides a clear view of the manager’s relative performance.

### Regulatory Requirement
In many jurisdictions, financial regulators mandate the use of TWR for performance reporting, ensuring [transparency](../t/transparency.md) and fairness in assessing investment results.

### Popular Tools and Software
Several financial software packages and tools provide TWR calculation capabilities, including:

- **[Morningstar](../m/morningstar.md) Direct**: Provides comprehensive performance measurement and analysis tools, including TWR.
- **[Bloomberg Terminal](../b/bloomberg_terminal.md)**: Offers detailed analytics, including TWR calculations.
- **[FactSet](../f/factset.md)**: Known for its extensive data and performance measurement abilities.
- **Addepar**: A [wealth management](../w/wealth_management.md) platform that includes TWR among its suite of performance measurement tools.

For more details on these solutions, you can visit their respective websites:
- Morningstar Direct
- Bloomberg Terminal
- FactSet
- Addepar

Understanding and correctly applying the Time-[Weighted](../w/weighted.md) [Rate of Return](../r/rate_of_return.md) (TWR) is essential for investment professionals who are tasked with evaluating [portfolio performance](../p/portfolio_performance.md) accurately and fairly. Given its ability to mitigate the effects of [cash flow](../c/cash_flow.md) timing, TWR stands out as the preferred choice in [portfolio performance](../p/portfolio_performance.md) measurement in the sphere of [finance](../f/finance.md) and investments.