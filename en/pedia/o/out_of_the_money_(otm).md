# Out of The Money (OTM)

Out of The [Money](../m/money.md) (OTM) is a financial term particularly used in the context of [options](../o/options.md) trading. It refers to a position where an option's [strike price](../s/strike_price.md) is not favorable when compared to the current [market price](../m/market_price.md) of the [underlying asset](../u/underlying_asset.md). Essentially, an OTM option has no [intrinsic value](../i/intrinsic_value.md); its [value](../v/value.md) is purely based on [time value](../t/time_value.md) or potential future [volatility](../v/volatility.md) of the [underlying asset](../u/underlying_asset.md).

## Call Options

For call [options](../o/options.md), which give the holder the right to buy the [underlying asset](../u/underlying_asset.md), an option is considered OTM when the [strike price](../s/strike_price.md) is higher than the current [market price](../m/market_price.md) of the [asset](../a/asset.md). 

For example, let's say the current price of a stock is $50. A [call option](../c/call_option.md) with a [strike price](../s/strike_price.md) of $55 would be out of the [money](../m/money.md) because buying the stock at the [market price](../m/market_price.md) is cheaper than exercising the option at $55.

### Calculation of OTM for a Call Option

The [intrinsic value](../i/intrinsic_value.md) of a [call option](../c/call_option.md) can be calculated as follows:
\[ \text{[Intrinsic Value](../i/intrinsic_value.md)} = \max(0, \text{Current [Market Price](../m/market_price.md)} - \text{[Strike Price](../s/strike_price.md)}) \]

If the result is zero or negative, the [call option](../c/call_option.md) is out of the [money](../m/money.md). 

## Put Options

For [put options](../p/put_options.md), which give the holder the right to sell the [underlying asset](../u/underlying_asset.md), an option is considered OTM when the [strike price](../s/strike_price.md) is lower than the current [market price](../m/market_price.md) of the [asset](../a/asset.md).

For example, if the current stock price is $50, a [put option](../p/put.md) with a [strike price](../s/strike_price.md) of $45 would be out of the [money](../m/money.md) because selling the stock at the [market price](../m/market_price.md) yields a higher [return](../r/return.md) than exercising the option at $45.

### Calculation of OTM for a Put Option

The [intrinsic value](../i/intrinsic_value.md) of a [put option](../p/put.md) can be calculated as follows:
\[ \text{[Intrinsic Value](../i/intrinsic_value.md)} = \max(0, \text{[Strike Price](../s/strike_price.md)} - \text{Current [Market Price](../m/market_price.md)}) \]

If the result is zero or negative, the [put option](../p/put.md) is out of the [money](../m/money.md).

## Implications of OTM Options

Although OTM [options](../o/options.md) do not have [intrinsic value](../i/intrinsic_value.md), they can still [hold](../h/hold.md) [time value](../t/time_value.md). The [time value](../t/time_value.md) is based on the probability that an option [will](../w/will.md) move into the [money](../m/money.md) before expiration. This probability depends on factors such as [volatility](../v/volatility.md) of the [underlying asset](../u/underlying_asset.md), time to expiration, and changes in the [underlying asset](../u/underlying_asset.md)'s price.

### Time Decay

One of the critical aspects of OTM [options](../o/options.md) is the concept of [time decay](../t/time_decay.md), which is the erosion of option [value](../v/value.md) as it approaches its [expiration date](../e/expiration_date.md). The [value](../v/value.md) of an OTM option diminishes faster as the [expiration date](../e/expiration_date.md) nears because the probability of it moving into the [money](../m/money.md) decreases.

### Volatility

Higher [volatility](../v/volatility.md) can increase the [value](../v/value.md) of OTM [options](../o/options.md) because it raises the chances of the [underlying asset](../u/underlying_asset.md)'s price moving into a favorable [range](../r/range.md), thus increasing the option's potential for becoming in the [money](../m/money.md) by expiration.

## Why Traders Use OTM Options

Traders may buy OTM [options](../o/options.md) for various strategic reasons:

1. **[Speculation](../s/speculation.md)**: An OTM option can [offer](../o/offer.md) substantial [leverage](../l/leverage.md) because it is cheaper than an in-the-[money](../m/money.md) (ITM) or at-the-[money](../m/money.md) (ATM) option. If the [underlying asset](../u/underlying_asset.md)'s price moves significantly in the desired direction, the returns can be substantial.
  
2. **Hedging**: OTM [options](../o/options.md) can serve as cost-effective [insurance](../i/insurance.md) policies against significant adverse price movements in an [underlying asset](../u/underlying_asset.md) or portfolio.
  
3. **[Spreads](../s/spreads.md)**: Strategies like straddles or strangles involve buying OTM [options](../o/options.md) to benefit from large price movements regardless of the direction.

## Pricing Models

OTM [options](../o/options.md) are primarily valued using [options](../o/options.md) pricing models such as the [Black-Scholes model](../b/black-scholes_model.md) or binomial models. These models take into account factors like the current price of the [underlying asset](../u/underlying_asset.md), the [strike price](../s/strike_price.md), time to expiration, [interest](../i/interest.md) rates, dividends (if applicable), and [volatility](../v/volatility.md).

### Black-Scholes Model

The [Black-Scholes model](../b/black-scholes_model.md) is frequently used to calculate the theoretical price of an option, which can help in evaluating OTM [options](../o/options.md). The model incorporates:

- **Stock Price (S)**: The current price of the [underlying asset](../u/underlying_asset.md).
- **[Strike Price](../s/strike_price.md) (K)**: The price at which the option can be exercised.
- **Time (T)**: Time to expiration.
- **[Volatility](../v/volatility.md) (σ)**: The expected [volatility](../v/volatility.md) of the [underlying asset](../u/underlying_asset.md).
- **[Risk](../r/risk.md)-Free Rate (r)**: The [return](../r/return.md) on a [risk](../r/risk.md)-free investment over the option's life.

The Black-Scholes formula for a [call option](../c/call_option.md) is:
\[ C = S_0 N(d_1) - Ke^{-rT} N(d_2) \]

Where:
\[ d_1 = \frac{\ln{\frac{S_0}{K}} + (r + \frac{\sigma^2}{2})T}{\sigma \sqrt{T}} \]
\[ d_2 = d_1 - \sigma \sqrt{T} \]

### Binomial Model

The binomial [options](../o/options.md) pricing model provides a method for valuing [options](../o/options.md) that involves simulating different possible paths that an [underlying asset](../u/underlying_asset.md)'s price can take over the life of the option. For OTM [options](../o/options.md), this can be particularly useful in assessing the likelihood of the option moving in the [money](../m/money.md) by expiration.

## Real-world Applications

### Risk Management

OTM [options](../o/options.md) are widely used in real-world scenarios for [risk management](../r/risk_management.md). For example, a [portfolio manager](../p/portfolio_manager.md) fearing a [market](../m/market.md) downturn might buy OTM [put options](../p/put_options.md) as a [hedge](../h/hedge.md) against adverse price movements in their portfolio. 

### Corporate Finance

Corporations may use OTM [options](../o/options.md) in various strategic financial operations, such as to [hedge](../h/hedge.md) against [currency](../c/currency.md) or [commodity](../c/commodity.md) price risks.

### Algorithmic Trading

[Algorithmic trading](../a/accountability.md) systems can incorporate OTM [options](../o/options.md) in their strategies to capture specific [market](../m/market.md) inefficiencies or exploit patterns that are more profitably engaged with cheaper, high-[leverage](../l/leverage.md) instruments.

## Key Takeaways

- **Definition**: OTM [options](../o/options.md) have a [strike price](../s/strike_price.md) less favorable than the current [market price](../m/market_price.md) of the [underlying asset](../u/underlying_asset.md).
- **No [Intrinsic Value](../i/intrinsic_value.md)**: They consist solely of [time value](../t/time_value.md) as they lack [intrinsic value](../i/intrinsic_value.md).
- **[Time Decay](../t/time_decay.md) and [Volatility](../v/volatility.md)**: Their [value](../v/value.md) erodes over time and is heavily influenced by [volatility](../v/volatility.md).
- **Applications**: Used for speculative, hedging, and various strategic purposes in trading and [corporate finance](../c/corporate_finance.md).
- **[Valuation Models](../v/valuation_models.md)**: Black-Scholes and binomial models are commonly used for valuing these [options](../o/options.md).

Understanding Out of The [Money](../m/money.md) [options](../o/options.md) is crucial for traders and investors aiming to [leverage](../l/leverage.md) [options](../o/options.md) for [speculation](../s/speculation.md), hedging, or strategic [portfolio management](../p/par.md). While they come with higher risks due to their lack of [intrinsic value](../i/intrinsic_value.md), their potential for significant returns and strategic flexibility makes them an essential tool in the [financial markets](../f/financial_market.md).