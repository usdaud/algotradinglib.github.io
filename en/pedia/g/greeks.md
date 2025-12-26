# Greeks

In the world of financial trading and [derivatives](../d/derivatives.md), especially in [options](../o/options.md) trading, the term "Greeks" refers to a set of [risk measures](../r/risk_measures.md) that describe how the price of an option or [derivatives](../d/derivatives.md) contract is expected to change as the [underlying](../u/underlying.md) conditions change. These measures are vital for traders and [risk](../r/risk.md) managers in their strategies to [hedge](../h/hedge.md) and [profit](../p/profit.md) from the movements in the [market](../m/market.md). Below is an extensive explanation of the main types of Greeks, how they are used, and their significance.

## Delta (Δ)

[Delta](../d/delta.md) represents the rate of change of the option's price with respect to changes in the price of the [underlying asset](../u/underlying_asset.md). In other words, it is the sensitivity of the option price to the price of the [underlying asset](../u/underlying_asset.md).

- **[Call Option](../c/call_option.md)**: The [delta](../d/delta.md) of a [call option](../c/call_option.md) ranges from 0 to 1. As the price of the [underlying asset](../u/underlying_asset.md) increases, the [value](../v/value.md) of the [call option](../c/call_option.md) tends to increase, so the [delta](../d/delta.md) [will](../w/will.md) generally be positive.
- **[Put Option](../p/put.md)**: The [delta](../d/delta.md) of a [put option](../p/put.md) ranges from -1 to 0. As the price of the [underlying asset](../u/underlying_asset.md) decreases, the [value](../v/value.md) of the [put option](../p/put.md) tends to increase, so the [delta](../d/delta.md) [will](../w/will.md) generally be negative.

The [delta](../d/delta.md) of an option can be used to approximate the probability that the option [will](../w/will.md) expire in-the-[money](../m/money.md).

### Usage Example
If an option has a [delta](../d/delta.md) of 0.5, and the price of the [underlying](../u/underlying.md) stock goes up by $1, the price of the option is expected to increase by approximately $0.50.

## Gamma (Γ)

[Gamma](../g/gamma.md) measures the rate of change in [delta](../d/delta.md) with respect to changes in the price of the [underlying asset](../u/underlying_asset.md). Essentially, it is the second [derivative](../d/derivative.md) of the option's price with respect to the [underlying asset](../u/underlying_asset.md)'s price.

[Gamma](../g/gamma.md) is higher when the option is at-the-[money](../m/money.md) and lower when it is in-the-[money](../m/money.md) or out-of-the-[money](../m/money.md). [Gamma](../g/gamma.md) can help traders understand the stability of [delta](../d/delta.md) and can indicate when adjustments might be needed in a [delta](../d/delta.md)-hedged portfolio.

### Usage Example
If an option has a [gamma](../g/gamma.md) of 0.05, and the price of the [underlying](../u/underlying.md) stock goes up by $1, then the [delta](../d/delta.md) of the option [will](../w/will.md) change by 0.05. For instance, if the original [delta](../d/delta.md) is 0.5, it [will](../w/will.md) become 0.55.

## Theta (Θ)

[Theta](../t/theta.md) measures the rate of decline in the [value](../v/value.md) of an option due to the passage of time, also known as [time decay](../t/time_decay.md). For [options](../o/options.md), [time decay](../t/time_decay.md) is significant because [options](../o/options.md) expire; as expiration approaches, the [time value](../t/time_value.md) of the option tends to decrease.

[Theta](../t/theta.md) is generally negative for both call and [put options](../p/put_options.md). This is particularly important for short-option positions, where [time decay](../t/time_decay.md) can be beneficial.

### Usage Example
If an option has a [theta](../t/theta.md) of -0.05, the price of the option is expected to decrease by $0.05 each day, assuming other factors remain constant.

## Vega (ν)

[Vega](../v/vega.md) measures the sensitivity of the option's price to changes in the [volatility](../v/volatility.md) of the [underlying asset](../u/underlying_asset.md). Higher [volatility](../v/volatility.md) increases the potential for profitable movements in the [underlying asset](../u/underlying_asset.md)'s price, thereby increasing the price of the option.

[Vega](../v/vega.md) is the same for both call and [put options](../p/put_options.md) and increases as the option becomes more at-the-[money](../m/money.md).

### Usage Example
If an option has a [vega](../v/vega.md) of 0.10, and the [volatility](../v/volatility.md) of the [underlying](../u/underlying.md) stock increases by 1%, the price of the option is expected to increase by $0.10.

## Rho (ρ)

[Rho](../r/rho.md) measures the sensitivity of the option's price to changes in the [interest rate](../i/interest_rate.md). This Greek is less commonly discussed because [interest](../i/interest.md) rates do not fluctuate as frequently as other factors, but it can still be significant, especially for longer-term [options](../o/options.md).

- **[Call Option](../c/call_option.md)**: [Rho](../r/rho.md) is typically positive; as [interest](../i/interest.md) rates rise, the price of a [call option](../c/call_option.md) is expected to increase.
- **[Put Option](../p/put.md)**: [Rho](../r/rho.md) is typically negative; as [interest](../i/interest.md) rates rise, the price of a [put option](../p/put.md) is expected to decrease.

### Usage Example
If an option has a [rho](../r/rho.md) of 0.05, and the [interest rate](../i/interest_rate.md) increases by 1%, the price of the option is expected to increase by $0.05.

## Charm (δΔ/δt)

Charm, also referred to as [delta](../d/delta.md) decay, measures the rate of change of [delta](../d/delta.md) over the passage of time. This Greek is particularly important for understanding how [delta](../d/delta.md) and, consequently, the [hedge ratio](../h/hedge_ratio.md), changes as time passes.

### Usage Example
If an option's charm is -0.02 and [delta](../d/delta.md) is 0.5, in one day, absent other influences (like changes in the price of the [underlying](../u/underlying.md)), the [delta](../d/delta.md) would change to 0.48.

## Vanna (δΔ/δσ)

Vanna measures the sensitivity of [delta](../d/delta.md) with respect to changes in the [volatility](../v/volatility.md) of the [underlying asset](../u/underlying_asset.md). Vanna becomes significant when both [delta](../d/delta.md) and [volatility](../v/volatility.md) shift.

### Usage Example
If an option's vanna is 0.03 and [volatility](../v/volatility.md) increases by 1%, the [delta](../d/delta.md) would increase by 0.03.

## Vomma (δVega/δσ)

[Vomma](../v/vomma.md) measures the sensitivity of [vega](../v/vega.md) to changes in [volatility](../v/volatility.md). This Greek is most useful when trading [options](../o/options.md) in highly volatile markets where [volatility](../v/volatility.md) can spike unexpectedly.

### Usage Example
If an option's [vomma](../v/vomma.md) is 0.04 and [volatility](../v/volatility.md) increases by 1%, the [vega](../v/vega.md) would increase by 0.04.

## Lambda (λ)

[Lambda](../l/lambda.md) measures the [percentage change](../p/percentage_change.md) in the option's price per [percentage change](../p/percentage_change.md) in the price of the [underlying asset](../u/underlying_asset.md). This is sometimes referred to as the [leverage](../l/leverage.md) of the option.

### Usage Example
If an option has a [lambda](../l/lambda.md) of 1.5, and the price of the [underlying](../u/underlying.md) stock increases by 2%, the price of the option is expected to increase by 3%.

## Practical Applications of Greeks

### Hedging

One of the primary uses of Greeks is in hedging. For example, if you are long an option, you might short some of the [underlying](../u/underlying.md) to reduce the price [risk](../r/risk.md) ([delta hedging](../d/delta_hedging.md)). The Greeks help in determining the quantities needed.

### Risk Management

[Risk](../r/risk.md) managers use Greeks to understand and mitigate risks in an [options](../o/options.md) portfolio. For example, a [portfolio manager](../p/portfolio_manager.md) might look at the aggregate [gamma](../g/gamma.md) of a portfolio to understand how volatile their [delta](../d/delta.md) is.

### Strategy Formulation

Traders use Greeks to form profitable strategies under different [market](../m/market.md) conditions. For instance, if a [trader](../t/trader.md) expects high [volatility](../v/volatility.md), they might look for [options](../o/options.md) with high [vega](../v/vega.md).

### Automated Trading

For firms that engage in [algorithmic trading](../a/algorithmic_trading.md), Greeks can be programmed into [trading algorithms](../t/trading_algorithms.md) to dynamically adjust positions based on changes in the [market](../m/market.md), ensuring that portfolios remain hedged in real-time.

## Key Considerations

- **Interdependence**: The Greeks are not independent; changing one Greek often changes others.
- **Non-linearity**: Especially with large moves or near expiration, the relations described by Greeks can become non-linear and require more sophisticated modeling.
- **Approximation**: Greeks provide approximations and not exact measures, actual outcomes may differ slightly.

## Conclusion

Understanding the Greeks is fundamental for anyone involved in trading or managing [options](../o/options.md) and [derivative](../d/derivative.md) portfolios. They provide vital insights into how an option's price [will](../w/will.md) change with movements in the [market](../m/market.md) and help traders make more informed decisions. Whether for hedging, [risk management](../r/risk_management.md), or strategy formulation, Greeks are indispensable tools in the [financial markets](../f/financial_market.md).