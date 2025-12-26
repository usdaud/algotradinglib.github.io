# Short Strangle Strategies

A [Short Strangle](../s/short_strangle.md) is an advanced [options](../o/options.md) [trading strategy](../t/trading_strategy.md) aimed at profiting from a narrow trading [range](../r/range.md) of an [underlying asset](../u/underlying_asset.md). This strategy involves selling an out-of-the-[money](../m/money.md) (OTM) [call option](../c/call_option.md) and an out-of-the-[money](../m/money.md) (OTM) [put option](../p/put.md) simultaneously. Unlike a [straddle](../s/straddle.md), which involves at-the-[money](../m/money.md) [options](../o/options.md), a [strangle](../s/strangle.md) uses [options](../o/options.md) that are further out-of-the-[money](../m/money.md), making it inherently less risky and less costly but also capping potential [profit](../p/profit.md) and loss.

#### Key Concepts

1. **Selling a [Call Option](../c/call_option.md)**: This obligates the seller to deliver the [underlying asset](../u/underlying_asset.md) at the specified [strike price](../s/strike_price.md) if the option buyer decides to [exercise](../e/exercise.md) the option.
2. **Selling a [Put Option](../p/put.md)**: This obligates the seller to buy the [underlying asset](../u/underlying_asset.md) at the specified [strike price](../s/strike_price.md) if the option buyer decides to [exercise](../e/exercise.md) the option.

By utilizing this strategy, traders aim to capture [premium](../p/premium.md) [income](../i/income.md) while betting that the [underlying asset](../u/underlying_asset.md) [will](../w/will.md) stay within a specific [range](../r/range.md) until expiration. Let's dive deeper into the components and aspects of [Short Strangle](../s/short_strangle.md) strategies.

#### Components of Short Strangle Strategy

1. **Strike Prices**: The strike prices for the call and [put options](../p/put_options.md) in a [short strangle](../s/short_strangle.md) are set outside the current trading price. For example, if Stock XYZ is trading at $100, you might sell a $110 call and a $90 put.

2. **Expiry Date**: The expiry dates for both [options](../o/options.md) are typically the same. The choice of expiry can influence the strategy's [risk](../r/risk.md) and reward profile.

3. **[Premium](../p/premium.md) [Income](../i/income.md)**: The total [premium](../p/premium.md) received is the sum of the premiums from selling both the call and the [put options](../p/put_options.md). This [premium](../p/premium.md) serves as the maximum [profit](../p/profit.md) potential if both [options](../o/options.md) expire worthless.

#### Example

Suppose Stock XYZ is currently trading at $100. You create a [Short Strangle](../s/short_strangle.md) by:

- Selling one 110 Call for $2 [premium](../p/premium.md).
- Selling one 90 Put for $2 [premium](../p/premium.md).

In this case, the total [premium](../p/premium.md) collected is $4. If the stock price remains between $90 and $110 until expiration, both [options](../o/options.md) [will](../w/will.md) expire worthless, and you keep the $4 [premium](../p/premium.md).

#### Profit and Loss Potential

- **Max [Profit](../p/profit.md)**: The maximum [profit](../p/profit.md) occurs if the [underlying asset](../u/underlying_asset.md) closes between the strike prices of the sold call and put at expiration. The maximum [profit](../p/profit.md) equals the total [premium](../p/premium.md) received when selling the [options](../o/options.md).

 Max [Profit](../p/profit.md) = [Premium](../p/premium.md) from Call + [Premium](../p/premium.md) from Put

- **Max Loss**: The potential maximum loss is theoretically unlimited on the [upside](../u/upside.md) (if the stock price soars far above the [strike price](../s/strike_price.md) of the call sold). On the downside, the loss could be substantial but limited to the [strike price](../s/strike_price.md) minus the [premium](../p/premium.md) collected, as the [underlying asset](../u/underlying_asset.md) cannot drop below zero.

 Max Loss (Upward) = Unlimited
 Max Loss (Downward) = [Strike Price](../s/strike_price.md) of Put - [Net Premium](../n/net_premium.md) Received

#### Risk Management

- **[Stop-loss Orders](../s/stop-loss_orders.md)**: To manage [risk](../r/risk.md), traders often use [stop-loss orders](../s/stop-loss_orders.md) that automatically close the position once it moves against them by a predefined amount.

- **Hedging**: Traders may [hedge](../h/hedge.md) their positions using other strategies, such as buying protection [options](../o/options.md) or diversifying their portfolio to [offset](../o/offset.md) potential losses.

#### Advanced Variants

1. **Wide [Strangle](../s/strangle.md)**: This involves setting the strike prices further outside the current trading price, which provides a more considerable safety [margin](../m/margin.md) but less [premium](../p/premium.md) [income](../i/income.md).

2. **Narrow [Strangle](../s/strangle.md)**: This involves placing the strike prices closer to the current trading price, which increases [premium](../p/premium.md) [income](../i/income.md) but also increases the likelihood the [options](../o/options.md) [will](../w/will.md) be exercised.

3. **[Iron Condor](../i/iron_condor.md)**: Combining a [short strangle](../s/short_strangle.md) with additional purchased [options](../o/options.md) can further cap potential losses and improve [risk management](../r/risk_management.md).

#### Factors to Consider

1. **Implied [Volatility](../v/volatility.md)**: High implied [volatility](../v/volatility.md) in the [underlying asset](../u/underlying_asset.md) can increase the premiums collected, but also elevates the chances of significant price movements, thus increasing [risk](../r/risk.md).

2. **[Market](../m/market.md) Conditions**: [Economic indicators](../e/economic_indicators.md), [earnings](../e/earnings.md) reports, and [geopolitical events](../g/geopolitical_events.md) can all affect [asset](../a/asset.md) price movements. It's crucial to consider short-term and long-term [market](../m/market.md) conditions when executing a [short strangle](../s/short_strangle.md) strategy.

3. **[Time Decay](../t/time_decay.md)**: [Options](../o/options.md) decay over time. The rate of this decay ([theta](../t/theta.md)) can work in favor of [short strangle](../s/short_strangle.md) strategies, as the [value](../v/value.md) of the [options](../o/options.md) sold decreases over time, all else equal.

#### Platforms for Implementation

Several trading platforms provide tools and resources to execute [Short Strangle](../s/short_strangle.md) strategies effectively. Some popular platforms include:

- **[Thinkorswim](../t/thinkorswim.md) by TD [Ameritrade](../a/ameritrade.md)**: Known for its advanced trading tools and [robust](../r/robust.md) [options](../o/options.md) analytics.


- **[Interactive Brokers](../i/interactive_brokers.md)**: Offers a wide [range](../r/range.md) of [options](../o/options.md) trading capabilities and sophisticated [order types](../o/order_types_in_trading.md).


- **Tastyworks**: Tailored for [options](../o/options.md) traders, it provides unique visualizations and ease of use.


- **[E*TRADE](../e/e_trade.md)**: Offers comprehensive tools for both novice and experienced traders.

 E*TRADE

#### Conclusion

A [Short Strangle](../s/short_strangle.md) strategy is a nuanced approach suitable for traders who believe that an [underlying asset](../u/underlying_asset.md) [will](../w/will.md) remain [range](../r/range.md)-bound over a certain period. While it offers high [premium](../p/premium.md) [income](../i/income.md) potential, it also poses significant risks, especially if the [market](../m/market.md) moves sharply in either direction. Proper [risk management](../r/risk_management.md), combined with a solid understanding of [market](../m/market.md) conditions and implied [volatility](../v/volatility.md), is crucial for successfully deploying [Short Strangle](../s/short_strangle.md) strategies. Traders should be well-versed in [options](../o/options.md) theory and practice to effectively employ this strategy.
