# Duration

Duration is a vital concept in [finance](../f/finance.md) and [investing](../i/investing.md), particularly in the context of bonds and other fixed-[income](../i/income.md) securities. It provides a measure of the sensitivity of a [bond](../b/bond.md)'s price to changes in [interest](../i/interest.md) rates and is essential for managing the [interest rate risk](../i/interest_rate_risk.md) of [bond](../b/bond.md) portfolios. There are several types of duration, each [offering](../o/offering.md) distinct insights into different aspects of [interest rate risk](../i/interest_rate_risk.md).

## Macaulay Duration

### Definition
[Macaulay Duration](../m/macaulay_duration.md) is a [weighted average](../w/weighted_average.md) time until cash flows are received, and it is measured in years. It was developed by Frederick Macaulay in 1938 and is often used as a theoretical foundation for other types of duration.

### Formula
The [Macaulay Duration](../m/macaulay_duration.md) \(D_M\) is calculated using the formula:

\[ D_M = \frac{ \sum_{t=1}^{T} \frac{C_t \cdot t}{(1+y)^t} }{ P } \]

Where:
- \( C_t \) = [Cash flow](../c/cash_flow.md) at time \( t \)
- \( y \) = [Yield to maturity](../y/yield_to_maturity.md)
- \( T \) = Total number of payments
- \( P \) = Current [bond](../b/bond.md) price

### Interpretation
[Macaulay Duration](../m/macaulay_duration.md) represents the [weighted average](../w/weighted_average.md) time until a [bondholder](../b/bondholder.md) receives the [bond](../b/bond.md)'s cash flows. Bonds with longer Macaulay Durations are more sensitive to changes in [interest](../i/interest.md) rates.

## Modified Duration

### Definition
[Modified Duration](../m/modified_duration.md) adjusts the [Macaulay Duration](../m/macaulay_duration.md) to account for changes in [yield](../y/yield.md), providing a direct measure of the [price sensitivity](../p/price_sensitivity.md) of a [bond](../b/bond.md) to [interest rate](../i/interest_rate.md) changes.

### Formula
The [Modified Duration](../m/modified_duration.md) \(D_{mod}\) is derived from the [Macaulay Duration](../m/macaulay_duration.md):

\[ D_{mod} = \frac{D_M}{1 + \frac{y}{n}} \]

Where:
- \( n \) = Number of [compounding](../c/compounding.md) periods per year

### Interpretation
[Modified Duration](../m/modified_duration.md) measures the [percentage change](../p/percentage_change.md) in a [bond](../b/bond.md)'s price for a 1% change in [yield](../y/yield.md). It is used by [bond](../b/bond.md) investors to manage [interest rate risk](../i/interest_rate_risk.md) and is directly comparable across different bonds.

## Effective Duration

### Definition
[Effective Duration](../e/effective_duration.md) accounts for changes in cash flows due to embedded [options](../o/options.md) in bonds, such as call or [put options](../p/put_options.md). It provides a better measure of [interest rate sensitivity](../i/interest_rate_sensitivity.md) for bonds with complex features.

### Formula
[Effective Duration](../e/effective_duration.md) \(D_{eff}\) is computed using the following formula:

\[ D_{eff} = \frac{P_{-} - P_{+}}{2 \cdot P_0 \cdot \[Delta](../d/delta.md) y} \]

Where:
- \( P_{-} \) = [Bond](../b/bond.md) price if yields decrease by \( \[Delta](../d/delta.md) y \)
- \( P_{+} \) = [Bond](../b/bond.md) price if yields increase by \( \[Delta](../d/delta.md) y \)
- \( P_0 \) = Current [bond](../b/bond.md) price
- \( \[Delta](../d/delta.md) y \) = Change in [yield](../y/yield.md)

### Interpretation
[Effective Duration](../e/effective_duration.md) is crucial for bonds with embedded [options](../o/options.md), as it accounts for changes in cash flows resulting from [interest rate](../i/interest_rate.md) movements. It offers a more accurate measure of [interest rate risk](../i/interest_rate_risk.md) for these securities.

## Duration in Portfolio Management

### Importance
Duration is a critical tool for portfolio managers to balance [risk](../r/risk.md) and [return](../r/return.md). It helps in constructing portfolios that are [robust](../r/robust.md) to [interest rate](../i/interest_rate.md) changes, aligning the [investment horizon](../i/investment_horizon.md) with the [liability](../l/liability.md) structure, and understanding the impact of [interest rate](../i/interest_rate.md) changes on the entire portfolio.

### Portfolio Duration
[Portfolio Duration](../p/portfolio_duration.md) is a [weighted average](../w/weighted_average.md) duration of all bonds in the portfolio, [weighted](../w/weighted.md) by [market value](../m/market_value.md). It is calculated as:

\[ D_{portfolio} = \sum_{i=1}^{N} w_i \cdot D_i \]

Where:
- \( w_i \) = Proportion of the portfolio invested in [bond](../b/bond.md) \( i \)
- \( D_i \) = Duration of [bond](../b/bond.md) \( i \)
- \( N \) = Total number of bonds in the portfolio

[Portfolio Duration](../p/portfolio_duration.md) helps in understanding the [interest rate risk](../i/interest_rate_risk.md) at the portfolio level and is used for strategic [asset allocation](../a/asset_allocation.md), immunization strategies, and [risk management](../r/risk_management.md).

## Duration and Interest Rate Risk

### Interest Rate Sensitivity
Duration directly quantifies how much a [bond](../b/bond.md)'s price [will](../w/will.md) change with a change in [interest](../i/interest.md) rates. Longer-duration bonds are more sensitive to [interest rate](../i/interest_rate.md) changes, implying higher [interest rate risk](../i/interest_rate_risk.md).

### Convexity
While duration provides a linear approximation of [price sensitivity](../p/price_sensitivity.md), [convexity](../c/convexity.md) accounts for the curvature in the price-[yield](../y/yield.md) relationship. Combined with duration, [convexity](../c/convexity.md) offers a more accurate prediction of [bond](../b/bond.md) price changes for larger shifts in [interest](../i/interest.md) rates.

\[ C = \frac{1}{P} \sum_{t=1}^{T} \frac{C_t \cdot t(t+1)}{(1+y)^{t+2}} \]

Where:
- \( C \) = [Convexity](../c/convexity.md)
- Other variables are as previously defined

Higher [convexity](../c/convexity.md) indicates that a [bond](../b/bond.md)'s price [will](../w/will.md) increase more when yields fall, and decrease less when yields rise, compared to a [bond](../b/bond.md) with lower [convexity](../c/convexity.md).

## Applying Duration in Real Life

### Duration Matching
Duration matching is an [investment strategy](../i/investment_strategy.md) where the duration of assets is aligned with the duration of liabilities to immunize the portfolio from [interest rate](../i/interest_rate.md) changes. This is particularly relevant for pension funds, [insurance](../i/insurance.md) companies, and other entities with fixed future liabilities.

### Barbell and Bullet Strategies
- **[Barbell Strategy](../b/barbell_strategy.md):** Invests in short-term and long-term bonds to balance [interest rate risk](../i/interest_rate_risk.md) and [liquidity](../l/liquidity.md) needs.
- **Bullet Strategy:** Concentrates investments in bonds with durations that match the [investment horizon](../i/investment_horizon.md).

These strategies use duration to manage the [trade](../t/trade.md)-off between [interest rate risk](../i/interest_rate_risk.md), [yield](../y/yield.md), and [liquidity](../l/liquidity.md).

## Example: PIMCO's Use of Duration
PIMCO, a global [investment management](../i/investment_management.md) [firm](../f/firm.md), utilizes duration as a core element of its [bond](../b/bond.md) investment strategies. Detailed information on their approach to managing duration and [interest rate risk](../i/interest_rate_risk.md) can be found through its online channels: PIMCO - Managing Interest Rate Risk.

## Conclusion

Duration is an essential metric for understanding and managing the [interest rate risk](../i/interest_rate_risk.md) of bonds and fixed-[income](../i/income.md) portfolios. By quantifying the sensitivity of [bond](../b/bond.md) prices to changes in [interest](../i/interest.md) rates, duration enables investors to make informed decisions and construct resilient portfolios. Familiarity with various types of duration, such as [Macaulay Duration](../m/macaulay_duration.md), [Modified Duration](../m/modified_duration.md), and [Effective Duration](../e/effective_duration.md), and their application in [portfolio management](../p/par.md) strategies like duration matching and [barbell](../b/barbell.md) strategies, is crucial for successful fixed-[income](../i/income.md) [investing](../i/investing.md).