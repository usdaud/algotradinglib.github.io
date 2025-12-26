# Gordon Growth Model

The Gordon Growth Model, also known as the [Dividend](../d/dividend.md) [Discount](../d/discount.md) Model (DDM), is a popular method used to determine the [intrinsic value](../i/intrinsic_value.md) of a stock based on the assumption that dividends [will](../w/will.md) continue to grow at a constant rate indefinitely. This model was introduced by Myron J. Gordon and Eli Shapiro in 1956, making it one of the earliest approaches to valuing equities.

## Key Assumptions

The Gordon Growth Model relies on a few crucial assumptions:
1. **Dividends are expected to grow at a constant rate**.
2. **The growth rate (g) of dividends is less than the required [rate of return](../r/rate_of_return.md) (r)**.
3. **The required [rate of return](../r/rate_of_return.md) remains constant over time**.
4. **The [investor](../i/investor.md)'s horizon is infinite**, which simplifies the [valuation](../v/valuation.md) under the assumption of constant growth.

## Formula

The formula for the Gordon Growth Model is as follows:

\[ P_0 = \frac{D_0(1+g)}{r - g} \]

Where:
- \( P_0 \) is the current stock price
- \( D_0 \) is the most recent [dividend](../d/dividend.md) paid
- \( g \) is the constant growth rate of dividends
- \( r \) is the required [rate of return](../r/rate_of_return.md)

Alternatively, the formula can be written as:

\[ P_0 = \frac{D_1}{r - g} \]

Where \( D_1 \) is the expected [dividend](../d/dividend.md) in the next period.

## Explanation of the Components

### Current Stock Price (\( P_0 \))

This is the [present value](../p/present_value.md) of all future dividends, discounted back at the required [rate of return](../r/rate_of_return.md).

### Most Recent Dividend (\( D_0 \))

The most recent [dividend](../d/dividend.md) paid by the company can be used as a [basis](../b/basis.md) to project future dividends. This is important because dividends represent the portion of [earnings](../e/earnings.md) that companies distribute to their shareholders.

### Expected Dividend (\( D_1 \))

This is the projected [dividend](../d/dividend.md) for the next period, calculated as \( D_0 \times (1 + g) \).

### Growth Rate of Dividends (\( g \))

The growth rate in dividends is a crucial component, often estimated based on historical [dividend](../d/dividend.md) growth, [earnings](../e/earnings.md) growth, or company’s retention and [reinvestment rate](../r/reinvestment_rate.md). Analysts often refer to [financial statements](../f/financial_statements.md), [industry](../i/industry.md) [growth rates](../g/growth_rates_in_trading.md), and [economic conditions](../e/economic_conditions.md) to estimate \( g \).

### Required Rate of Return (\( r \))

The required [rate of return](../r/rate_of_return.md) is often calculated using the [Capital Asset](../c/capital_asset.md) Pricing Model (CAPM), which considers the [risk](../r/risk.md)-free rate, the stock’s [beta](../b/beta.md), and the [equity market](../e/equity_market.md) [premium](../p/premium.md).

\[ r = R_f + \[beta](../b/beta.md) ( R_m - R_f ) \]

Where:
- \( R_f \) is the [risk](../r/risk.md)-free rate
- \( \[beta](../b/beta.md) \) is the [beta](../b/beta.md) of the stock
- \( R_m \) is the [expected return](../e/expected_return.md) of the [market](../m/market.md)

## Practical Application

The Gordon Growth Model is particularly relevant for valuing companies that have stable and predictable [dividend](../d/dividend.md) policies. [Utility](../u/utility.md) companies and mature firms in stable industries are often good candidates for this model since they usually have consistent [dividend](../d/dividend.md) [growth rates](../g/growth_rates_in_trading.md).

## Strengths of the Model

1. **Simplicity**: The model is straightforward and easy to apply.
2. **Focus on Dividends**: Since dividends are a tangible [return](../r/return.md) to investors, focusing on them can provide a reliable [valuation](../v/valuation.md).
3. **Infinite Horizon**: By assuming an infinite horizon, the model simplifies the calculation by eliminating the terminal [value](../v/value.md) estimation problem found in other [valuation models](../v/valuation_models.md).

## Limitations

1. **Constant Growth Rate**: The assumption of a constant growth rate may not [hold](../h/hold.md) true in real-world scenarios where companies experience varying [growth rates](../g/growth_rates_in_trading.md).
2. **Applicability**: It's less suitable for companies that do not pay dividends or have unpredictable [dividend](../d/dividend.md) patterns.
3. **Sensitivity to Inputs**: Small changes in the growth rate (\( g \)) or required [rate of return](../r/rate_of_return.md) (\( r \)) can result in significant changes in the stock price [valuation](../v/valuation.md).

For example, if \( g \) approaches \( r \), the denominator \( r - g \) becomes very small, leading to potentially unrealistic valuations.

## Variations of the Gordon Growth Model

### Multi-Stage Dividend Discount Model

Given the limitations of a single constant growth rate, the Multi-Stage [Dividend](../d/dividend.md) [Discount](../d/discount.md) Model (DDM) incorporates different [growth rates](../g/growth_rates_in_trading.md) for different stages.
For instance:
1. **Initial High-Growth Phase**: Higher growth rate in the early years.
2. **Transition Phase**: A decreasing growth rate during the transition period.
3. **Stable Growth Phase**: A constant, lower growth rate in the long-term.

This model is more flexible and can be used for valuing companies expected to undergo various growth phases.

### H-Model

The H-Model is a specific type of multi-stage model and is defined as:

\[ P_0 = \frac{D_0(1 + g_L)}{r - g_L} + \frac{D_0H(g_S - g_L)}{r - g_L} \]

Where:
- \( g_L \) is the long-term growth rate
- \( g_S \) is the short-term growth rate
- \( H \) is the half-life period of the high-growth phase

## Case Studies

### Company A: A Mature Utility Firm

Let's consider a [utility](../u/utility.md) company that paid a [dividend](../d/dividend.md) of $2 last year (\( D_0 \)). It is expected that the dividends [will](../w/will.md) grow at a constant rate of 3% (\( g \)) annually. If an [investor](../i/investor.md)'s required [rate of return](../r/rate_of_return.md) (\( r \)) is 7%, the current stock price (\( P_0 \)) can be calculated as:

\[ D_1 = D_0 \times ( 1 + g ) = 2 \times 1.03 = 2.06 \]

\[ P_0 = \frac{2.06}{0.07 - 0.03} = \frac{2.06}{0.04} = 51.50 \]

Thus, according to the Gordon Growth Model, the [intrinsic value](../i/intrinsic_value.md) of the [utility](../u/utility.md) company's stock is $51.50.

## Advanced Considerations

### Incorporating Risk Factors

Some analysts argue that the Gordon Growth Model can be extended by incorporating additional [risk factors](../r/risk_factors_in_trading.md), particularly for companies in volatile industries. For example, using a [risk](../r/risk.md)-adjusted growth rate or a varying required [rate of return](../r/rate_of_return.md) that reflects changing [market](../m/market.md) conditions.

### Model Extensions

Moreover, there are attempts to combine the Gordon Growth Model with other [valuation approaches](../v/valuation_approaches.md) like the Discounted [Cash Flow](../c/cash_flow.md) (DCF) method or Real [Options](../o/options.md) [Valuation](../v/valuation.md), especially when dealing with firms having significant growth opportunities or high [uncertainty](../u/uncertainty_in_trading.md) in cash flows.

## Conclusion

The Gordon Growth Model remains a cornerstone in the field of [equity](../e/equity.md) [valuation](../v/valuation.md). Its simplicity and focus on dividends make it an accessible and informative tool for both novice and seasoned investors. However, its assumptions should be carefully scrutinized, and in many cases, more complex models may be required to capture the full intricacies of a company's growth prospects and [risk](../r/risk.md) profile. As financial environments evolve, so too does the application and modification of foundational models like the Gordon Growth Model.