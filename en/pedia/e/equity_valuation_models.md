# Equity Valuation Models

[Equity](../e/equity.md) [valuation](../v/valuation.md) is the process of determining the fair [market value](../m/market_value.md) of a company's [equity](../e/equity.md), and it is a cornerstone of [investment analysis](../i/investment_analysis.md) and strategy. This [valuation](../v/valuation.md) is essential for various stakeholders, including individual investors, institutional investors, and corporate managers. The goal of [equity](../e/equity.md) [valuation](../v/valuation.md) is to derive the [intrinsic value](../i/intrinsic_value.md) of a stock, which can then be compared to its current [market price](../m/market_price.md) to identify investment opportunities.

[Equity](../e/equity.md) [valuation models](../v/valuation_models.md) can be broadly classified into two categories: absolute [valuation models](../v/valuation_models.md) and relative [valuation models](../v/valuation_models.md). Absolute [valuation models](../v/valuation_models.md) are used to find the [intrinsic value](../i/intrinsic_value.md) of an [asset](../a/asset.md) based on its fundamentals, such as dividends, [earnings](../e/earnings.md), and [growth rates](../g/growth_rates_in_trading.md). Relative [valuation models](../v/valuation_models.md), on the other hand, estimate the [value](../v/value.md) of an [asset](../a/asset.md) by comparing it to the [valuation](../v/valuation.md) of other similar assets.

## Absolute Valuation Models

Absolute [valuation models](../v/valuation_models.md) are grounded in the theory that the [intrinsic value](../i/intrinsic_value.md) of a stock is derived from the fundamentals of the issuing company. The two most common absolute [valuation](../v/valuation.md) methods are the [Dividend](../d/dividend.md) [Discount](../d/discount.md) Model (DDM) and the Discounted [Cash Flow](../c/cash_flow.md) (DCF) model.

### Dividend Discount Model (DDM)

The [Dividend](../d/dividend.md) [Discount](../d/discount.md) Model (DDM) is based on the premise that the [value](../v/value.md) of a stock is the [present value](../p/present_value.md) of all future dividends. It assumes that dividends are the primary [return](../r/return.md) for shareholders and forecasts these dividends over an extended period.

There are several variations of the DDM, including the [Gordon Growth Model](../g/gordon_growth_model.md) (GGM), which assumes a constant growth rate in dividends, and the Multi-stage DDM, which assumes that [dividend](../d/dividend.md) [growth rates](../g/growth_rates_in_trading.md) [will](../w/will.md) change over time.

```markdown
#### Gordon Growth Model (GGM)

The [Gordon Growth Model](../g/gordon_growth_model.md) (GGM), named after Myron J. Gordon, is a simple and widely used version of DDM. It assumes that dividends [will](../w/will.md) grow at a constant rate in [perpetuity](../p/perpetuity.md). The formula for GGM is:

\[ P_0 = \frac{D_0 (1 + g)}{r - g} \]

where:
- \( P_0 \) = Current stock price
- \( D_0 \) = Most recent [dividend](../d/dividend.md) [payment](../p/payment.md)
- \( g \) = Growth rate of dividends
- \( r \) = Required [rate of return](../r/rate_of_return.md)

This model is best suited for companies with stable and predictable [dividend](../d/dividend.md) [growth rates](../g/growth_rates_in_trading.md).

#### Multi-stage Dividend Discount Model

The Multi-stage [Dividend](../d/dividend.md) [Discount](../d/discount.md) Model accounts for different growth phases that a company might experience. It segments the future into [multiple](../m/multiple.md) periods, each with a different growth rate. A common approach is the Two-stage DDM, which involves an initial high-growth period followed by a stable-growth period.

The [valuation](../v/valuation.md) in a two-stage model can be represented as:

\[ P_0 = \sum_{t=1}^{T} \frac{D_t}{(1 + r)^t} + \frac{P_T}{(1 + r)^T} \]

where:
- \( D_t \) = [Dividend](../d/dividend.md) at time \( t \)
- \( T \) = Terminal year, or the point at which growth stabilizes
- \( P_T \) = Terminal stock price, calculated by applying the GGM to dividends from year \( T \) onward
- \( r \) = Required [rate of return](../r/rate_of_return.md)
```

### Discounted Cash Flow (DCF) Model

The Discounted [Cash Flow](../c/cash_flow.md) (DCF) model values a company based on the [present value](../p/present_value.md) of its expected future cash flows. DCF analysis is a powerful tool because it incorporates all aspects of a company’s [financial structure](../f/financial_structure.md)—revenues, expenses, [taxes](../t/taxes.md), and [capital](../c/capital.md) investments.

The DCF model typically involves the following steps:

1. **Estimation of Free Cash Flows** - [Forecasting](../f/forecasting.md) free cash flows (FCFs) for a certain period, usually 5-10 years.
2. **Determining the Terminal [Value](../v/value.md)** - Calculating the [value](../v/value.md) of the [business](../b/business.md) beyond the forecast period, known as the terminal [value](../v/value.md).
3. **[Discounting](../d/discounting.md) Cash Flows** - [Discounting](../d/discounting.md) the FCFs and terminal [value](../v/value.md) to the [present value](../p/present_value.md) using a [discount rate](../d/discount_rate.md) (typically the [weighted average](../w/weighted_average.md) [cost of capital](../c/cost_of_capital.md) or WACC).

The formula for the DCF model is:

\[ [Value](../v/value.md) = \sum_{t=1}^{n} \frac{FCF_t}{(1 + WACC)^t} + \frac{TV}{(1 + WACC)^n} \]

where:
- \( FCF_t \) = Free [cash flow](../c/cash_flow.md) at time \( t \)
- \( WACC \) = [Weighted average](../w/weighted_average.md) [cost of capital](../c/cost_of_capital.md)
- \( TV \) = Terminal [value](../v/value.md)
- \( n \) = Forecast period in years

#### Free Cash Flow (FCF)

Free [Cash Flow](../c/cash_flow.md) represents the cash generated by the company after [accounting](../a/accounting.md) for [capital](../c/capital.md) expenditures required to maintain or expand the [asset](../a/asset.md) base. It is a crucial metric because it indicates the amount of cash available to investors (both [equity](../e/equity.md) and [debt](../d/debt.md) holders). The formula is:

\[ FCF = EBIT \times (1 - Tax Rate) + [Depreciation](../d/depreciation.md) \& Amortization - Change in Working [Capital](../c/capital.md) - [Capital](../c/capital.md) Expenditures \]

#### Terminal Value (TV)

The Terminal [Value](../v/value.md) captures the [value](../v/value.md) of the company beyond the forecast period. There are several methods to calculate terminal [value](../v/value.md), but the two most common are the [Perpetuity](../p/perpetuity.md) Growth Model and the Exit [Multiple](../m/multiple.md) Method.

**[Perpetuity](../p/perpetuity.md) Growth Model**:
\[ TV = \frac{FCF_{n+1}}{WACC - g} \]

where:
- \( FCF_{n+1} \) = Free [cash flow](../c/cash_flow.md) in the first year beyond the forecast period
- \( WACC \) = [Weighted average](../w/weighted_average.md) [cost of capital](../c/cost_of_capital.md)
- \( g \) = Growth rate in [perpetuity](../p/perpetuity.md)

**Exit [Multiple](../m/multiple.md) Method**:
This method involves applying a [multiple](../m/multiple.md) to a financial metric (like EBITDA) at the end of the forecast period.
\[ TV = EBITDA_n \times Exit \, [Multiple](../m/multiple.md) \]

where:
- \( EBITDA_n \) = EBITDA in the final year of the forecast period
- \( Exit \, [Multiple](../m/multiple.md) \) = [Multiple](../m/multiple.md) based on comparable company analysis

## Relative Valuation Models

Relative [valuation models](../v/valuation_models.md), also known as multiples-based [valuation](../v/valuation.md) methods, compare the company's [valuation](../v/valuation.md) with those of peer companies in the same [industry](../i/industry.md). Common multiples include Price-to-[Earnings](../e/earnings.md) (P/E), Price-to-Book (P/B), and Enterprise [Value](../v/value.md)-to-EBITDA (EV/EBITDA).

### Price-to-Earnings (P/E) Ratio

The P/E ratio compares a company's current share price to its per-share [earnings](../e/earnings.md), providing insight into how the [market](../m/market.md) values a company's [earnings](../e/earnings.md).

\[ P/E \, Ratio = \frac{Market \, Value \, per \, Share}{[Earnings](../e/earnings.md) \, per \, Share (EPS)} \]

A high P/E ratio may indicate that the stock is [overvalued](../o/overvalued.md), or investors expect high [growth rates](../g/growth_rates_in_trading.md) in the future. Conversely, a low P/E ratio might imply undervaluation or expectations of slower growth.

### Price-to-Book (P/B) Ratio

The P/B ratio compares a company's [market value](../m/market_value.md) to its [book value](../b/book_value.md), [offering](../o/offering.md) a sense of whether the stock is valued appropriately relative to its assets.

\[ P/B \, Ratio = \frac{[Market](../m/market.md) \, [Value](../v/value.md) \, per \, Share}{Book \, [Value](../v/value.md) \, per \, Share} \]

A P/B ratio greater than 1 suggests that the company is valued more than its [book value](../b/book_value.md), which could be due to [market](../m/market.md) perception of its growth potential or intangible assets.

### Enterprise Value-to-EBITDA (EV/EBITDA) Ratio

The EV/EBITDA ratio examines a company's [valuation](../v/valuation.md) by comparing its enterprise [value](../v/value.md) (EV) to its [earnings](../e/earnings.md) before [interest](../i/interest.md), [taxes](../t/taxes.md), [depreciation](../d/depreciation.md), and amortization (EBITDA), providing a more comprehensive [valuation](../v/valuation.md) by including [debt](../d/debt.md) and cash.

\[ EV/EBITDA = \frac{Enterprise \, [Value](../v/value.md)}{EBITDA} \]

The formula for Enterprise [Value](../v/value.md) is:
\[ Enterprise \, Value = [Market](../m/market.md) \, Cap + Total \, [Debt](../d/debt.md) - Cash \]

A low EV/EBITDA ratio may suggest that the company is [undervalued](../u/undervalued.md), while a high ratio can indicate overvaluation.

## Advanced Valuation Techniques

While the basic absolute and relative models are used widely due to their simplicity and clarity, advanced techniques incorporate more complex aspects of [business](../b/business.md) operations and [market](../m/market.md) conditions. Some of these advanced methods include:

### Economic Value Added (EVA)

[Economic Value](../e/economic_value.md) Added (EVA) is a measure of a company's [financial performance](../f/financial_performance.md) based on residual [wealth](../w/wealth.md), calculated by deducting the [cost of capital](../c/cost_of_capital.md) from the company's [operating profit](../o/operating_profit.md).

\[ EVA = NOPAT - ([Capital](../c/capital.md) \times WACC) \]

where:
- \( NOPAT \) = Net [operating profit](../o/operating_profit.md) after [taxes](../t/taxes.md)
- \( [Capital](../c/capital.md) \) = Total [capital](../c/capital.md) invested in the company
- \( WACC \) = [Weighted average](../w/weighted_average.md) [cost of capital](../c/cost_of_capital.md)

EVA helps in assessing whether a company generates [value](../v/value.md) over and above its [cost of capital](../c/cost_of_capital.md), which is useful for evaluating managerial performance and investment decisions.

### Real Options Valuation

Real [options](../o/options.md) provide a framework for valuing investment opportunities that accounts for the flexibility managers have in making investment decisions in response to unexpected [market](../m/market.md) developments. This approach treats investment opportunities as "[options](../o/options.md)" that can be exercised or deferred in the future.

Valuing real [options](../o/options.md) typically involves using financial [option pricing models](../o/option_pricing_models.md) like the [Black-Scholes model](../b/black-scholes_model.md) or binomial models.

### Residual Income Model

The [Residual Income](../r/residual_income.md) Model (RIM) values a company based on the [income](../i/income.md) generated above a required [rate of return](../r/rate_of_return.md). Unlike DCF, RIM focuses on the excess returns a company generates, making it particularly useful for companies that do not pay dividends.

\[ Value = Book \, Value + \sum_{t=1}^n \frac{Residual \, [Income](../i/income.md) \, t}{(1 + r)^t} \]

where:
- [Residual Income](../r/residual_income.md) = Net [Income](../i/income.md) - ([Equity](../e/equity.md) [Capital](../c/capital.md) \times [Cost of Equity](../c/cost_of_equity.md))
- \( r \) = [Cost of Equity](../c/cost_of_equity.md)

### Sum-of-the-Parts (SOTP) Valuation

Sum-of-the-Parts (SOTP) [valuation](../v/valuation.md) involves valuing each [business](../b/business.md) unit or segment of a [diversified company](../d/diversified_company.md) separately and then summing these values to arrive at the total enterprise [value](../v/value.md). This method is particularly useful for conglomerates with [multiple](../m/multiple.md) unrelated [business](../b/business.md) segments.

## Conclusion

[Equity](../e/equity.md) [valuation](../v/valuation.md) is a multifaceted field necessitating a deep understanding of [finance](../f/finance.md), [accounting](../a/accounting.md), and [market dynamics](../m/market_dynamics.md). Whether using absolute models like DDM and DCF, relative models like P/E and EV/EBITDA, or advanced techniques like EVA and real [options](../o/options.md) [valuation](../v/valuation.md), the goal remains to determine the [intrinsic value](../i/intrinsic_value.md) of a stock to make informed investment decisions.

For further reading and resources on [equity](../e/equity.md) [valuation models](../v/valuation_models.md), consider visiting:

1. [Morningstar](https://www.morningstar.com/)
2. [Damodaran Online](http://pages.stern.nyu.edu/~adamodar/)
3. [Bloomberg](https://www.bloomberg.com/)
4. [McKinsey & Company](https://www.mckinsey.com/)
