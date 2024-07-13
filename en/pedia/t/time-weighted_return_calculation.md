# Time-Weighted Return Calculation

Time-[Weighted](../w/weighted.md) [Return](../r/return.md) (TWR) is a method of calculating investment performance that eliminates the effects of external cash flows. Among investors, [asset](../a/asset.md) managers, and financial advisors, TWR is widely acknowledged as a [robust](../r/robust.md) performance measurement method. Unlike other [return](../r/return.md) calculation methods that can be skewed by deposits and withdrawals, TWR focuses solely on the performance of the investment itself.

## Basic Concepts

### Time-Weighted Return vs. Money-Weighted Return
- **Time-[Weighted](../w/weighted.md) [Return](../r/return.md) (TWR)**: Measures the compound rate of growth of $1 over a specified period; it divides the performance periods by each time cash flows in or out.
- **[Money](../m/money.md)-[Weighted](../w/weighted.md) [Return](../r/return.md) (MWR)**: This is equivalent to the Internal [Rate of Return](../r/rate_of_return.md) (IRR); it takes into account the size and timing of cash flows.

### Key Terms
- **[Cash Flow](../c/cash_flow.md)**: Refers to deposits or withdrawals from an investment account.
- **Performance Periods**: Segments created every time there is a [cash flow](../c/cash_flow.md).
- **Sub-period Returns**: Returns computed for each performance period.

## Why Use TWR?

### Elimination of Timing Effects
One of the biggest advantages of TWR is its ability to remove the distorting impact of cash inflows and outflows. This feature makes it an ideal measure for evaluating the performance of investment managers who do not have control over the timing and size of client cash flows.

### Applicability to Performance Measurement
- **[Fund](../f/fund.md) Managers**: Often used by mutual funds and other investment vehicles to present performance that is true to the manager's decisions.
- **Benchmarking**: Offers a comparable metric when comparing against indices or other benchmarks.
  
## Methodology

### Step-by-Step Calculation
Understanding the calculation of TWR involves several steps:

1. **Segment the Investment Periods**
   - Divide the total investment period into smaller periods, each ending when a [cash flow](../c/cash_flow.md) occurs.
   
2. **Calculate Sub-period Returns**
   - For each sub-period, calculate the [return](../r/return.md) using the formula:
     \[
     R_i = \frac{E_i - B_i}{B_i}
     \]
     where \( R_i \) is the [return](../r/return.md) of the i-th sub-period, \( E_i \) is the ending [value](../v/value.md) of the sub-period, and \( B_i \) is the beginning [value](../v/value.md).

3. **Compound the Sub-period Returns**
   - Chain-link the sub-period returns to get the overall [return](../r/return.md):
     \[
     TWR = \prod_{i=1}^{n} (1 + R_i) - 1
     \]
     where \( n \) is the number of sub-periods.
  
## Practical Application

### Example
Suppose an [investor](../i/investor.md) starts with $10,000. During the year, they make additional investments and withdrawals at different times. Here’s a scenario:

- January 1: Initial investment of $10,000.
- April 1: The portfolio [value](../v/value.md) is $10,500, and the [investor](../i/investor.md) adds $5,000.
- July 1: The portfolio [value](../v/value.md) is $16,000, and the [investor](../i/investor.md) withdraws $6,000.
- October 1: The portfolio [value](../v/value.md) is $10,200.

To calculate TWR:

1. **First Sub-period (Jan 1 - Apr 1)**:
   \[ 
   R_1 = \frac{10,500 - 10,000}{10,000} = 0.05 
   \]

2. **Second Sub-period (Apr 1 - Jul 1)**:
   \[ 
   R_2 = \frac{16,000 - 15,500}{15,500} \approx 0.03226 
   \]

3. **Third Sub-period (Jul 1 - Oct 1)**:
   \[ 
   R_3 = \frac{10,200 - 10,000}{10,000} = 0.02 
   \]

4. **Chain Linking**:
   \[
   TWR = (1+R_1) \times (1+R_2) \times (1+R_3) - 1
   \]
   \[
   TWR = (1+0.05) \times (1+0.03226) \times (1+0.02) - 1
   \]
   \[
   TWR \approx 1.05 \times 1.03226 \times 1.02 - 1 \approx 0.1055 \text{ or } 10.55\%
   \]

### Adjusting for Compounding
The simplified example above is straightforward. In practice, the methodology often involves more frequent computations and may include daily cash flows, necessitating the use of financial software.

## Software Tools for TWR Calculation

### Examples of Software Tools
- **[Morningstar](../m/morningstar.md) Direct**: A platform [offering](../o/offering.md) a variety of performance measurement tools and analytics. ([Morningstar Direct Website](https://www.morningstar.com/products/direct))
- **[Bloomberg](../b/bloomberg.md) Terminal**: Provides [robust](../r/robust.md) financial analytics, including performance measurement. ([Bloomberg Terminal](https://www.bloomberg.com/professional/solution/bloomberg-terminal/))
- **Portfolio123**: Focuses on quantitative stock [market research](../m/market_research.md) and [portfolio management](../p/portfolio_management.md). ([Portfolio123 Website](https://www.portfolio123.com/))
  
## Challenges and Limitations

### Cash Flow Frequency
TWR calculations can become cumbersome with frequent cash flows. The need for accurate division of performance periods and [compounding](../c/compounding.md) returns for each period can be computationally intensive.

### Assumptions
It assumes intermediate cash flows are reinvested at the same rate. Variances in [market](../m/market.md) conditions and timing can affect the actual [reinvestment rate](../r/reinvestment_rate.md), introducing minor inaccuracies.

## Conclusion

Time-[Weighted](../w/weighted.md) [Return](../r/return.md) is a powerful tool for eliminating the bias introduced by external cash flows, making it vital for assessing genuine investment performance. Despite its computational complexity, TWR is indispensable for [fund](../f/fund.md) managers, investors, and advisors aiming for accurate [performance attribution](../p/performance_attribution.md).

By focusing on [market](../m/market.md) returns over a specific period, TWR delivers a true reflection of investment skill and strategy effectiveness, beneficial for a multitude of financial applications.
