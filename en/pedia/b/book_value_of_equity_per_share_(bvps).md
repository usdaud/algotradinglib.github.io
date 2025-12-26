# Book Value of Equity Per Share (BVPS)

## Introduction

[Book Value](../b/book_value.md) of [Equity](../e/equity.md) Per Share (BVPS) is a key financial metric that investors use to gauge the inherent [value](../v/value.md) of a company's stock. Essentially, BVPS measures the amount of [equity](../e/equity.md) available to common shareholders divided by the number of outstanding [shares](../s/shares.md). It represents the minimum [value](../v/value.md) of a company's [equity](../e/equity.md) and serves as a useful comparison with the [market value](../m/market_value.md) of the stock. Let's delve deeper into the intricacy of this metric, its calculation, significance, and the role it plays in algotrading strategies.

## What is Book Value of Equity Per Share (BVPS)?

BVPS is calculated by dividing the total [book value](../b/book_value.md) of [equity](../e/equity.md) by the number of outstanding [shares](../s/shares.md). The [book value](../b/book_value.md) of [equity](../e/equity.md), often referred to as 'shareholders' [equity](../e/equity.md),' is the net [asset](../a/asset.md) [value](../v/value.md) of a company abstracted from its liabilities. In simple terms:

\[ BVPS = \frac{Total \, Shareholders' \, [Equity](../e/equity.md) - Preferred \, [Equity](../e/equity.md)}{Number \, of \, Outstanding \, [Shares](../s/shares.md)} \]

## Importance of BVPS

BVPS holds significance for several reasons:

1. **[Valuation](../v/valuation.md) [Benchmark](../b/benchmark.md)**: It provides a [baseline](../b/baseline.md) measure for valuing a company's stock. If the BVPS is higher than the current [market price](../m/market_price.md) per share, the stock may be [undervalued](../u/undervalued.md), and vice versa.
2. **[Financial Health](../f/financial_health.md) [Indicator](../i/indicator.md)**: It offers insight into a company’s [financial health](../f/financial_health.md), indicating how much [capital](../c/capital.md) shareholders would theoretically receive if the company were liquidated.
3. **Investment Screening**: BVPS is often used in screening [stocks](../s/stock.md) for [value](../v/value.md)-[investing](../i/investing.md) strategies, particularly in [algorithmic trading](../a/accountability.md) models.

## Calculating BVPS

To calculate BVPS, follow these steps:

1. **Determine Total Shareholders' [Equity](../e/equity.md)**: Look at the company's [balance sheet](../b/balance_sheet.md) to find the total shareholders' [equity](../e/equity.md). This is also known as [book value](../b/book_value.md), which is the company's total assets minus its [total liabilities](../t/total_liabilities.md).
2. **Subtract Preferred [Equity](../e/equity.md)**: In cases where the company has issued [preferred stock](../p/preferred_stock.md), this amount needs to be subtracted from the total shareholders' [equity](../e/equity.md) since BVPS focuses on common stockholders.
3. **Identify Outstanding [Shares](../s/shares.md)**: Find the number of outstanding [shares](../s/shares.md), which is usually available in the [financial statements](../f/financial_statements.md) or company filings.
4. **Apply the Formula**: Divide the adjusted [equity](../e/equity.md) by the number of outstanding [shares](../s/shares.md) to get the BVPS.

Example:

Assume Company X has:
- Total Shareholders' [Equity](../e/equity.md): $500 million
- Preferred [Equity](../e/equity.md): $50 million
- Outstanding [Shares](../s/shares.md): 20 million

\[ BVPS = \frac{500M - 50M}{20M} = \frac{450M}{20M} = $22.5 \]

## Factors Affecting BVPS

Several factors can influence BVPS, including:

- **[Asset](../a/asset.md) [Depreciation](../d/depreciation.md)**: Decreases the [book value](../b/book_value.md) of assets, and, consequently, the BVPS, as [asset](../a/asset.md) values diminish over time.
- **Liabilities**: Increases in liabilities reduce shareholders' [equity](../e/equity.md), potentially lowering BVPS.
- **[Share Buybacks](../s/share_buybacks.md)**: Reducing the number of outstanding [shares](../s/shares.md) increases BVPS.
- **[Retained Earnings](../r/retained_earnings.md)**: Profitable companies often add [retained earnings](../r/retained_earnings.md) to shareholders' [equity](../e/equity.md), raising the BVPS.
- **[Revaluation](../r/revaluation.md) of Assets**: Changes in [asset valuation](../a/asset_valuation.md), such as [real estate](../r/real_estate.md) or equipment, impact the total assets and thus the BVPS.

## BVPS vs. Market Value

It's crucial to compare BVPS with [Market Value](../m/market_value.md) per Share (MVPS):

- **[Market Value](../m/market_value.md) Per Share (MVPS)**: This is the price at which a stock is trading on the [open market](../o/open_market.md). It reflects the [market](../m/market.md)'s perception of the company's growth potential, risks, and overall [value](../v/value.md).
- **[Book Value](../b/book_value.md) of [Equity](../e/equity.md) Per Share (BVPS)**: Represents the net [asset](../a/asset.md) [value](../v/value.md) allocated to each share, providing a more conservative and stable measure compared to MVPS.

## Application in Algotrading

In algotrading, BVPS can be part of various [trading strategies](../t/trading_strategies.md):

1. **[Value Investing](../v/value_investing.md) Algorithms**: Incorporate BVPS to identify [undervalued](../u/undervalued.md) [stocks](../s/stock.md) with strong [intrinsic value](../i/intrinsic_value.md), triggering buy orders when MVPS is significantly below BVPS.
2. **[Mean Reversion](../m/mean_reversion.md) Strategies**: Utilize the difference between BVPS and MVPS to anticipate price corrections, capitalizing on the assumption that [market](../m/market.md) prices [will](../w/will.md) revert to their [intrinsic value](../i/intrinsic_value.md).
3. **[Fundamental Analysis](../f/fundamental_analysis.md) Integration**: Combine BVPS with other fundamental indicators like P/E ratio, [Return](../r/return.md) on [Equity](../e/equity.md) (ROE), and [Debt](../d/debt.md)/[Equity](../e/equity.md) ratio to enhance model accuracy.
4. **Pair Trading**: Use BVPS to select fundamentally strong [stocks](../s/stock.md) when establishing [market](../m/market.md)-[neutral](../n/neutral.md) pair trades, matching a long position in [undervalued](../u/undervalued.md) [stocks](../s/stock.md) with a short position in [overvalued](../o/overvalued.md) counterparts.

## Real-World Example: IBM

Let's consider IBM (International [Business](../b/business.md) Machines [Corporation](../c/corporation.md))

As of IBM's latest financial [disclosure](../d/disclosure.md), assume the following:
- Total Shareholders' [Equity](../e/equity.md): $20 billion
- Preferred [Equity](../e/equity.md): $0 (IBM has no preferred [shares](../s/shares.md))
- Outstanding [Shares](../s/shares.md): 850 million [shares](../s/shares.md)

\[ BVPS = \frac{20B}{850M} = $23.53 \]

Suppose IBM's [market price](../m/market_price.md) per share is $150. Here, MBPS ($150) is significantly higher than BVPS ($23.53), suggesting that the [market](../m/market.md) values IBM based on its anticipated future [earnings](../e/earnings.md), technological advancements, [goodwill](../g/goodwill.md), and [brand equity](../b/brand_equity.md). Algotrading systems might use this data point to calibrate their [valuation models](../v/valuation_models.md) or identify anomalies.

## Limitations of BVPS

While BVPS is insightful, it has limitations:

- **[Historical Cost](../h/historical_cost.md) Bias**: Assets are recorded at [historical cost](../h/historical_cost.md), potentially underestimating or overestimating their current [market value](../m/market_value.md).
- **Non-[Tangible Assets](../t/tangible_asset.md)**: It excludes intangible assets like intellectual property, brand [value](../v/value.md), or [goodwill](../g/goodwill.md), which might be significant for tech or service-oriented companies.
- **[Industry](../i/industry.md) [Variability](../v/variability.md)**: BVPS can vary widely across industries, making cross-[industry](../i/industry.md) comparisons less meaningful.

## Advanced Concepts and Metrics

Advanced investors and algotrading models might also consider related metrics:

- **Tangible [Book Value](../b/book_value.md) Per Share (TBVPS)**: Excludes intangible assets from the calculation. Useful for industries where intangible assets play a minor role.
- **Growth of BVPS**: Historical [growth rates](../g/growth_rates_in_trading.md) of BVPS can [offer](../o/offer.md) insights into a company's long-term [asset](../a/asset.md) growth and management effectiveness.

Example: Advanced BVPS Calculation
Let's assume a tech company with significant intangible assets:

- Total Shareholders' [Equity](../e/equity.md): $800 million
- Intangible Assets: $200 million
- Preferred [Equity](../e/equity.md): $0
- Outstanding [Shares](../s/shares.md): 40 million

\[ TBVPS = \frac{800M - 200M}{40M} = \frac{600M}{40M} = $15 \]

By excluding intangibles, the TBVPS of $15 offers a more conservative view of the company's [value](../v/value.md).

## Conclusion

[Book Value](../b/book_value.md) of [Equity](../e/equity.md) Per Share (BVPS) is a foundational metric for understanding a company's [intrinsic value](../i/intrinsic_value.md) from a fundamental perspective. For algotrading, BVPS provides a quantifiable measure to develop and refine [trading algorithms](../t/trading_algorithms.md). By integrating BVPS with other financial metrics and leveraging it within various [trading strategies](../t/trading_strategies.md), investors and traders can [gain](../g/gain.md) deeper insights and make more informed decisions. Whether used as a standalone metric or part of a comprehensive [valuation](../v/valuation.md) model, BVPS remains a vital tool in the [financial analysis](../f/financial_analysis.md) toolkit.