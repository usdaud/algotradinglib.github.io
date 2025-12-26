# Fama and French Three Factor Model

The Fama and French Three [Factor](../f/factor.md) Model is an influential theory in the field of [financial economics](../f/financial_economics.md), specifically in the realm of [asset](../a/asset.md) pricing. Developed by Eugene Fama and Kenneth French in the early 1990s, the model extends the [Capital Asset](../c/capital_asset.md) Pricing Model (CAPM) by adding two additional factors to better explain the variations in stock returns. These factors are Size (SMB, Small Minus Big) and [Value](../v/value.md) (HML, High Minus Low). The Fama and French model has since become a cornerstone in both academic research and practical financial management.

## Background

### Capital Asset Pricing Model (CAPM)

Before delving into the specifics of the Fama and French Three [Factor](../f/factor.md) Model, it's important to briefly touch on its predecessor, the [Capital Asset](../c/capital_asset.md) Pricing Model (CAPM). Developed in the early 1960s by William Sharpe, John Lintner, and Jan Mossin, the CAPM is a single-[factor](../f/factor.md) model that describes the relationship between [systematic risk](../s/systematic_risk.md) and [expected return](../e/expected_return.md) for assets. The formula for the CAPM is:

\[ E(R_i) = R_f + \beta_i (E(R_m) - R_f) \]

- \( E(R_i) \): [Expected return](../e/expected_return.md) of the investment
- \( R_f \): [Risk](../r/risk.md)-free rate
- \( \beta_i \): [Beta coefficient](../b/beta_coefficient.md) of the investment
- \( E(R_m) \): [Expected return](../e/expected_return.md) of the [market](../m/market.md)

While the CAPM has been widely used, it has its limitations. Empirical evidence showed that it could not fully explain stock returns due to the exclusion of other significant factors influencing [asset](../a/asset.md) prices.

### Introduction to the Fama and French Three Factor Model

Eugene Fama and Kenneth French introduced their model in a seminal 1992 paper titled "The Cross-Section of Expected Stock Returns." The primary departure from CAPM is the inclusion of two additional factors—Size (SMB) and [Value](../v/value.md) (HML)—alongside the [market risk](../m/market_risk.md) [factor](../f/factor.md) (the [excess return](../e/excess_return.md) on the [market](../m/market.md), or \( R_m - R_f \)). Their extended model is expressed as:

\[ E(R_i) = R_f + \beta_i (E(R_m) - R_f) + \text{SMB}_i \times \text{SMB} + \text{HML}_i \times \text{HML} \]

- \( \text{SMB} \): Small Minus Big, a [factor](../f/factor.md) representing the outperformance of small-cap [stocks](../s/stock.md) over [large-cap stocks](../l/large_cap_stocks.md)
- \( HML \): High Minus Low, a [factor](../f/factor.md) representing the outperformance of [value](../v/value.md) [stocks](../s/stock.md) (high [book-to-market ratio](../b/book-to-market_ratio.md)) over [growth stocks](../g/growth_stocks.md) (low [book-to-market ratio](../b/book-to-market_ratio.md))

## Components of the Model

### Market Risk Premium (MRP)

The [Market Risk Premium](../m/market_risk_premium.md) (MRP) reflects the difference between the [expected return](../e/expected_return.md) of the [market](../m/market.md) and the [risk](../r/risk.md)-free rate. It accounts for the general [market risk](../m/market_risk.md) that [stocks](../s/stock.md) are exposed to. In the Fama and French Three [Factor](../f/factor.md) Model, this is represented by:

\[ \beta_i (E(R_m) - R_f) \]

The [market risk](../m/market_risk.md) component remains consistent with the CAPM, emphasizing that this [factor](../f/factor.md) alone is not sufficient to explain the complexities of [asset](../a/asset.md) returns fully.

### Size (SMB - Small Minus Big)

The Size [factor](../f/factor.md) captures the additional [risk](../r/risk.md) and [return](../r/return.md) characteristics associated with small-[capitalization](../c/capitalization.md) [stocks](../s/stock.md). Empirical evidence indicates that small-cap [stocks](../s/stock.md) tend to [outperform](../o/outperform.md) [large-cap stocks](../l/large_cap_stocks.md) over the long term. This difference is attributed to various factors, such as higher growth potential and greater [financial risk](../f/financial_risk.md) faced by smaller firms. The SMB [factor](../f/factor.md) is calculated as follows:

\[ \text{SMB} = \frac{1}{3} (R_{small, value} + R_{small, [neutral](../n/neutral.md)} + R_{small, growth} - R_{big, [value](../v/value.md)} - R_{big, [neutral](../n/neutral.md)} - R_{big, growth}) \]

Where:
- \( R_{small, [value](../v/value.md)} \): [Return](../r/return.md) on small-cap [value](../v/value.md) [stocks](../s/stock.md)
- \( R_{small, [neutral](../n/neutral.md)} \): [Return](../r/return.md) on small-cap [neutral](../n/neutral.md) [stocks](../s/stock.md)
- \( R_{small, growth} \): [Return](../r/return.md) on small-cap [growth stocks](../g/growth_stocks.md)
- \( R_{big, [value](../v/value.md)} \): [Return](../r/return.md) on large-cap [value](../v/value.md) [stocks](../s/stock.md)
- \( R_{big, [neutral](../n/neutral.md)} \): [Return](../r/return.md) on large-cap [neutral](../n/neutral.md) [stocks](../s/stock.md)
- \( R_{big, growth} \): [Return](../r/return.md) on large-cap [growth stocks](../g/growth_stocks.md)

### Value (HML - High Minus Low)

The [Value factor](../v/value_factor.md) represents the difference in returns between [value](../v/value.md) [stocks](../s/stock.md) and [growth stocks](../g/growth_stocks.md). [Value](../v/value.md) [stocks](../s/stock.md) are characterized by high book-to-[market](../m/market.md) ratios, meaning they have a relatively low [market](../m/market.md) [valuation](../v/valuation.md) compared to their [book value](../b/book_value.md). Conversely, [growth stocks](../g/growth_stocks.md) have low book-to-[market](../m/market.md) ratios and are generally considered to have higher future growth potential. The HML [factor](../f/factor.md) is computed as follows:

\[ \text{HML} = \frac{1}{2} (R_{small, [value](../v/value.md)} + R_{big, [value](../v/value.md)} - R_{small, growth} - R_{big, growth}) \]

Where:
- \( R_{small, [value](../v/value.md)} \): [Return](../r/return.md) on small-cap [value](../v/value.md) [stocks](../s/stock.md)
- \( R_{big, [value](../v/value.md)} \): [Return](../r/return.md) on large-cap [value](../v/value.md) [stocks](../s/stock.md)
- \( R_{small, growth} \): [Return](../r/return.md) on small-cap [growth stocks](../g/growth_stocks.md)
- \( R_{big, growth} \): [Return](../r/return.md) on large-cap [growth stocks](../g/growth_stocks.md)

## Empirical Validation

### Initial Evidence

Fama and French initially validated their model using data from the New York Stock [Exchange](../e/exchange.md) (NYSE), American Stock [Exchange](../e/exchange.md) (AMEX), and [NASDAQ](../n/nasdaq.md) for the period from 1963 to 1990. They found that their three-[factor](../f/factor.md) model significantly improved the explanation of stock returns compared to CAPM. The model's inclusion of the SMB and HML factors addressed the anomalies evident with a single-[factor](../f/factor.md) CAPM, such as the higher average returns of small-cap [stocks](../s/stock.md) and [value](../v/value.md) [stocks](../s/stock.md).

### Broad Acceptance

Over the years, numerous studies have corroborated the efficacy of the Fama and French Three [Factor](../f/factor.md) Model across different periods and diverse markets. Some of the most significant supporting evidence comes from:

- **International Markets**: The model has been validated in international [equity](../e/equity.md) markets, proving its applicability beyond the U.S. equities.
- **Different Time Periods**: Research covering various time periods continues to support the findings that small-cap and [value](../v/value.md) [stocks](../s/stock.md) tend to [outperform](../o/outperform.md) their large-cap and growth counterparts.

### Criticisms and Limitations

Despite its broad acceptance, the Fama and French Three [Factor](../f/factor.md) Model is not without its criticisms. Some of the key limitations include:

- **Model Complexity**: Adding more factors increases the complexity of the model which can make it less intuitive for practitioners.
- **[Factor](../f/factor.md) Stability**: There is ongoing debate about whether SMB and HML remain stable over time or are susceptible to changes in [market](../m/market.md) conditions and [investor](../i/investor.md) behavior.
- **Other Anomalies**: Even with three factors, the model does not capture all anomalies (such as [momentum](../m/momentum.md)).

## Real-World Applications

### Investment Management

Many investment firms and [fund](../f/fund.md) managers have adopted the Fama and French Three [Factor](../f/factor.md) Model to inform their [asset allocation](../a/asset_allocation.md), [risk management](../r/risk_management.md), and performance evaluation practices. The model is particularly popular in the realm of [factor investing](../f/factor_investing.md), where investors construct portfolios based on exposure to various [risk factors](../r/risk_factors_in_trading.md).

### Hedge Funds

[Hedge](../h/hedge.md) funds, including quantitative and [algorithmic trading](../a/accountability.md) firms, often use the three-[factor](../f/factor.md) model as a component of more complex models to predict [asset](../a/asset.md) prices and identify [arbitrage opportunities](../a/arbitrage_opportunities.md). By incorporating SMB and HML, these entities refine their strategies to [gain](../g/gain.md) an edge in the [market](../m/market.md).

### Financial Education

The model is a staple in [finance](../f/finance.md) curricula at universities around the world. It serves as a bridge between the simpler CAPM and more intricate [asset pricing models](../a/asset_pricing_models.md), providing students with a deeper understanding of the multi-dimensional nature of [risk](../r/risk.md) and [return](../r/return.md).

## Extensions of the Model

### Fama and French Five Factor Model

In 2015, Fama and French expanded their model into a five-[factor](../f/factor.md) framework by adding two more factors: profitability and investment. The five-[factor](../f/factor.md) model aims to account for even more dimensions of stock returns. The additional factors are:

- **[Robust](../r/robust.md) Minus Weak (RMW)**: Represents the returns of [stocks](../s/stock.md) with [robust](../r/robust.md) profitability minus those with weak profitability.
- **Conservative Minus Aggressive (CMA)**: Represents the returns of [stocks](../s/stock.md) with conservative investment policies minus those with aggressive investment policies.

### Other Multi-Factor Models

Numerous other [multi-factor models](../m/multi-factor_models.md) have been developed in the [finance](../f/finance.md) literature, taking inspiration from Fama and French to incorporate additional factors like [momentum](../m/momentum.md), [liquidity](../l/liquidity.md), and others. These models aim to [offer](../o/offer.md) even more refined explanations for [asset](../a/asset.md) returns.

## Conclusion

The Fama and French Three [Factor](../f/factor.md) Model has had a profound impact on the field of [asset](../a/asset.md) pricing, [offering](../o/offering.md) significant improvements over the [Capital Asset](../c/capital_asset.md) Pricing Model (CAPM). By introducing the Size (SMB) and [Value](../v/value.md) (HML) factors, Fama and French provided a more comprehensive framework for understanding stock returns. Despite its limitations, the model remains a cornerstone in [financial economics](../f/financial_economics.md) and continues to be widely used in both academic research and practical financial management.

For further reading and to explore more about the contributions of Eugene Fama and Kenneth French, you can visit their respective academic and professional profiles:

- Eugene F. Fama at University of Chicago
- Kenneth R. French at Dartmouth College