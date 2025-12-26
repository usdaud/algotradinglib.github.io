# Lookback Options

Lookback [options](../o/options.md) are a type of [exotic options](../e/exotic_options.md) in [financial markets](../f/financial_market.md) that allow the holder to "look back" over time to determine the optimal [exercise price](../e/excersise_price.md). This unique feature distinguishes lookback [options](../o/options.md) from standard [options](../o/options.md), where the [exercise price](../e/excersise_price.md) is predetermined at the start of the contract. Because of their flexibility and potential for providing significant advantages to the holder, lookback [options](../o/options.md) are considered more complex and thus more expensive than their vanilla counterparts.

### Types of Lookback Options

There are primarily two types of lookback [options](../o/options.md):
1. **Fixed Lookback [Options](../o/options.md)**: These [options](../o/options.md) allow the holder to [exercise](../e/exercise.md) the option at an optimal historical price of the [underlying asset](../u/underlying_asset.md), determined over the life of the option. For a lookback [call option](../c/call_option.md), this would be the lowest price, and for a lookback [put option](../p/put.md), it would be the highest price.
2. **Floating Lookback [Options](../o/options.md)**: These [options](../o/options.md) determine the [exercise price](../e/excersise_price.md) as the difference between the best price of the [underlying asset](../u/underlying_asset.md) over the option's life and its price at [maturity](../m/maturity.md). The lookback feature adjusts the payoff at the [exercise](../e/exercise.md) time rather than at initiation.

### Detailed Mechanics

#### Fixed Lookback Call Option
- **Purchase**: You buy a [call option](../c/call_option.md) with a lookback feature.
- **Evaluation**: Throughout the option lifespan, track the price of the [underlying asset](../u/underlying_asset.md).
- **Expiry**: Upon [maturity](../m/maturity.md), determine the lowest price achieved by the [underlying asset](../u/underlying_asset.md) during the life of the option.
- **Payoff**: The payoff [will](../w/will.md) be the current price of the [underlying asset](../u/underlying_asset.md) minus the lowest price observed, thereby ensuring the maximum potential [profit](../p/profit.md).

#### Fixed Lookback Put Option
- **Purchase**: You buy a [put option](../p/put.md) with a lookback feature.
- **Evaluation**: Throughout the option lifespan, track the price of the [underlying asset](../u/underlying_asset.md).
- **Expiry**: Upon [maturity](../m/maturity.md), determine the highest price achieved by the [underlying asset](../u/underlying_asset.md) during the life of the option.
- **Payoff**: The payoff [will](../w/will.md) be the highest price observed minus the current price of the [underlying asset](../u/underlying_asset.md), thereby ensuring the maximum potential [profit](../p/profit.md).

#### Floating Lookback Call Option
- **Purchase**: You buy a floating [call option](../c/call_option.md).
- **Evaluation**: Throughout the option lifespan, track the price of the [underlying asset](../u/underlying_asset.md).
- **Expiry**: Upon [maturity](../m/maturity.md), determine the highest price achieved.
- **Payoff**: The payoff is the difference between the highest price achieved and the price at expiration.

#### Floating Lookback Put Option
- **Purchase**: You buy a floating [put option](../p/put.md).
- **Evaluation**: Throughout the option lifespan, track the price of the [underlying asset](../u/underlying_asset.md).
- **Expiry**: Upon [maturity](../m/maturity.md), determine the lowest price achieved.
- **Payoff**: The payoff is the difference between the price at expiration and the lowest price achieved over the option's life.

### Applications of Lookback Options

Lookback [options](../o/options.md) are particularly useful in volatile markets where predicting future price movements is challenging. Their ability to optimize the [exercise price](../e/excersise_price.md) retrospectively makes them valuable for:

1. **Hedging**: Investors and companies may use lookback [options](../o/options.md) to [hedge](../h/hedge.md) against unfavorable price movements. For instance, a company expecting significant [revenue](../r/revenue.md) in the future can use lookback [options](../o/options.md) to lock in the best possible [exchange rate](../e/exchange_rate.md) for [currency](../c/currency.md) translation.
2. **[Speculation](../s/speculation.md)**: Traders can speculate on the maximum potential [profit](../p/profit.md) by taking advantage of price swings without worrying about the exact entry point.
3. **[Portfolio Management](../p/portfolio_management.md)**: Portfolio managers can use these [options](../o/options.md) to enhance [return](../r/return.md) profiles and mitigate risks associated with [market](../m/market.md) entry timing.

### Pricing of Lookback Options

Pricing lookback [options](../o/options.md) is more complex than pricing standard [options](../o/options.md) due to their path-dependent nature. Some factors influencing the pricing include:
- **[Historical Volatility](../h/historical_volatility.md)**: Higher [volatility](../v/volatility.md) increases the likelihood of favorable price points, raising the cost of lookback [options](../o/options.md).
- **Time to [Maturity](../m/maturity.md)**: Longer durations increase the window for optimal price points to occur, making lookback [options](../o/options.md) more expensive.
- **[Interest](../i/interest.md) Rates**: As with other [options](../o/options.md), prevailing [interest](../i/interest.md) rates impact the [discounting](../d/discounting.md) of future payoffs.

Pricing models often used include:
- **[Monte Carlo Simulation](../m/monte_carlo_simulation.md)**: This method involves running numerous simulations to forecast the behavior of the [underlying](../u/underlying.md) price and determine the optimal [exercise price](../e/excersise_price.md).
- **Binomial Models**: This involves constructing a price tree and evaluating possible price paths.
- **Closed-form Solutions**: For specific types of lookback [options](../o/options.md), closed-form analytical solutions, such as the Black-Scholes-based models, are also available.

### Advantages and Disadvantages

#### Advantages
- **Optimal [Return](../r/return.md)**: Enables investors to achieve the best possible returns by retroactively determining the most favorable [exercise price](../e/excersise_price.md).
- **Hedging [Efficiency](../e/efficiency.md)**: Provides [robust](../r/robust.md) hedging by catering to the best historical prices, thus minimizing exposure to adverse price movements.
- **No Need for Timing**: Ideal for investors not confident in their ability to time the [market](../m/market.md) effectively.

#### Disadvantages
- **Cost**: Higher premiums due to the favorable features and complexity of these [options](../o/options.md).
- **Complexity**: Understanding and implementing lookback [options](../o/options.md) requires a higher level of expertise and computational resources.
- **[Liquidity](../l/liquidity.md)**: Given their exotic nature, lookback [options](../o/options.md) might not be as [liquid](../l/liquid.md) as standard [options](../o/options.md), potentially leading to wider [bid](../b/bid.md)-ask [spreads](../s/spreads.md).

### Key Players and Providers

Several financial institutions and brokerage firms [offer](../o/offer.md) lookback [options](../o/options.md), either directly or via over-the-counter (OTC) mechanisms. Some of the well-known providers include:
- **Goldman Sachs**: As a global investment [bank](../b/bank.md), Goldman Sachs provides structured products, including lookback [options](../o/options.md). More
- **J.P. Morgan**: Another prominent institution [offering](../o/offering.md) various [exotic options](../e/exotic_options.md), including lookback [options](../o/options.md).
- **Barclays**: This financial group provides services in [derivatives](../d/derivatives.md) and offers customized [exotic options](../e/exotic_options.md). Their public materials offers more insights.

### Conclusion

Lookback [options](../o/options.md) represent a sophisticated [financial instrument](../f/financial_instrument.md) that offers unique advantages for hedging and speculative purposes. While their pricing and implementation are more complex, they provide significant benefits by ensuring optimal [exercise](../e/exercise.md) prices. As with any [financial instrument](../f/financial_instrument.md), a comprehensive understanding and careful analysis are crucial before deploying lookback [options](../o/options.md) in an [investment strategy](../i/investment_strategy.md).
