# Iron Butterfly

The Iron Butterfly is a popular [options](../o/options.md) [trading strategy](../t/trading_strategy.md) that involves the use of [multiple](../m/multiple.md) [options](../o/options.md) trades to create a "wings" structure, which limits both [risk](../r/risk.md) and reward. The primary goal of this strategy is to benefit from low [volatility](../v/volatility.md) by capturing a [net premium](../n/net_premium.md), while having strictly defined [risk](../r/risk.md) parameters. Below, we explore the Iron Butterfly strategy in detail, including its construction, [profit](../p/profit.md) and loss potential, breakeven points, and practical use cases.

## Construction of an Iron Butterfly

An Iron Butterfly is constructed using four [options](../o/options.md) with the same [expiration date](../e/expiration_date.md) but three different strike prices. The strategy involves:

1. **Buying one out-of-the-[money](../m/money.md) [put option](../p/put.md) (lower [strike price](../s/strike_price.md))**
2. **Selling one at-the-[money](../m/money.md) [put option](../p/put.md) (middle [strike price](../s/strike_price.md))**
3. **Selling one at-the-[money](../m/money.md) [call option](../c/call_option.md) (middle [strike price](../s/strike_price.md))**
4. **Buying one out-of-the-[money](../m/money.md) [call option](../c/call_option.md) (higher [strike price](../s/strike_price.md))**

The middle [strike price](../s/strike_price.md), where both the put and call [options](../o/options.md) are sold, is typically the current [market price](../m/market_price.md) of the [underlying asset](../u/underlying_asset.md). The out-of-the-[money](../m/money.md) put and call [options](../o/options.md) are purchased to form the wings of the butterfly. The resulting structure appears as follows:

- Long one lower strike put
- Short one middle strike put
- Short one middle strike call
- Long one higher strike call

## Example of Iron Butterfly

Consider a stock trading at $100. Here’s how an Iron Butterfly might be constructed:

- Buy 1 put with a [strike price](../s/strike_price.md) of $95 (out-of-the-[money](../m/money.md) put)
- Sell 1 put with a [strike price](../s/strike_price.md) of $100 (at-the-[money](../m/money.md) put)
- Sell 1 call with a [strike price](../s/strike_price.md) of $100 (at-the-[money](../m/money.md) call)
- Buy 1 call with a [strike price](../s/strike_price.md) of $105 (out-of-the-[money](../m/money.md) call)

## Profit and Loss Potential

The Iron Butterfly's [profit](../p/profit.md) and loss profile are both capped. This means that there is a maximum amount you can [gain](../g/gain.md) and a maximum amount you can lose.

### Maximum Profit

The maximum [profit](../p/profit.md) is achieved when the [underlying asset](../u/underlying_asset.md) closes exactly at the middle [strike price](../s/strike_price.md) at expiration. The [profit](../p/profit.md) is calculated as:

\( \text{Max [Profit](../p/profit.md)} = \text{[Net Premium](../n/net_premium.md) Received} \)

The [Net Premium](../n/net_premium.md) Received is the total [premium](../p/premium.md) collected from selling the middle strike call and put, minus the [premium](../p/premium.md) paid for buying the out-of-the-[money](../m/money.md) call and [put options](../p/put_options.md).

### Maximum Loss

The maximum loss occurs if the [underlying asset](../u/underlying_asset.md)’s price moves significantly away from the middle [strike price](../s/strike_price.md) at expiration. The loss is calculated as:

\( \text{Max Loss} = \text{Difference in Strike Prices} - \text{[Net Premium](../n/net_premium.md) Received} \)

In our example:

- Difference in Strike Prices = $105 - $100 = $5 (or $500 per [options contract](../o/options_contract.md), considering each contract represents 100 [shares](../s/shares.md))

If the [Net Premium](../n/net_premium.md) Received was $2, the Max Loss is:

- \( \text{Max Loss} = $5 - $2 = $3 \text{ (or $300 per [options contract](../o/options_contract.md))} \)

### Breakeven Points

There are two breakeven points for an Iron Butterfly strategy. They can be calculated as follows:

- Lower [Breakeven Point](../b/breakeven_point.md) = Middle [Strike Price](../s/strike_price.md) - [Net Premium](../n/net_premium.md) Received
- Upper [Breakeven Point](../b/breakeven_point.md) = Middle [Strike Price](../s/strike_price.md) + [Net Premium](../n/net_premium.md) Received

In our example:

- Lower [Breakeven Point](../b/breakeven_point.md) = $100 - $2 = $98
- Upper [Breakeven Point](../b/breakeven_point.md) = $100 + $2 = $102

## Practical Use Cases

The Iron Butterfly is primarily used in markets where the [trader](../t/trader.md) expects low [volatility](../v/volatility.md) and believes the [underlying asset](../u/underlying_asset.md)'s price [will](../w/will.md) remain close to the current price till expiration. Here are several scenarios where the Iron Butterfly can be beneficial:

- **[Earnings](../e/earnings.md) Season**: Traders might use Iron Butterflies during [earnings](../e/earnings.md) season when they predict a company’s stock [will](../w/will.md) not experience major price shifts despite reporting [earnings](../e/earnings.md).
- **Historical Price Stability**: If an [asset](../a/asset.md) has shown a history of trading within a narrow [range](../r/range.md), an Iron Butterfly might be employed to [capitalize](../c/capitalize.md) on this lack of movement.
- **[Volatility](../v/volatility.md) Compression**: In scenarios where traders expect a decrease in implied [volatility](../v/volatility.md), selling [options](../o/options.md) (like in Iron Butterfly) can be profitable since [options](../o/options.md)' prices tend to fall with decreasing [volatility](../v/volatility.md).

## Risks and Considerations

While the Iron Butterfly offers defined [risk](../r/risk.md), several considerations must be kept in mind:

- **[Assignment](../a/assignment.md) [Risk](../r/risk.md)**: Early [assignment](../a/assignment.md) of short [options](../o/options.md) positions can occur, especially for American [options](../o/options.md). This can complicate the strategy and lead to unexpected outcomes.
- **[Liquidity](../l/liquidity.md) Concerns**: Maintaining [liquidity](../l/liquidity.md) is crucial when using an Iron Butterfly to enable easy exit before expiration if needed. Illiquid [options](../o/options.md) can result in wider [bid](../b/bid.md)-ask [spreads](../s/spreads.md) and unexpected [slippage](../s/slippage.md).
- **[Transaction Costs](../t/transaction_costs.md)**: With four legs in the strategy, [transaction costs](../t/transaction_costs.md) including commissions and fees can be significant, reducing the [net premium](../n/net_premium.md) received.

## Advanced Strategies and Modifications

Professional traders often tweak the Iron Butterfly to suit specific [market](../m/market.md) conditions or [risk tolerance](../r/risk_tolerance.md) levels. Some common modifications include:

- **[Iron Condor](../i/iron_condor.md)**: Similar to Iron Butterfly but with different middle strike prices for sold [options](../o/options.md), providing a wider [range](../r/range.md) of profitability.
- **Broken Wing Butterfly**: Adjusting strike prices to create asymmetry where one wing is further out-of-the-[money](../m/money.md) than the other, modifying [risk](../r/risk.md) and reward profiles.

## Using Technology for Iron Butterfly

Modern trading platforms and software provide tools for constructing and managing [Iron Butterfly strategies](../i/iron_butterfly_strategies.md). For instance:

- **[ThinkOrSwim](../t/thinkorswim.md) by TD [Ameritrade](../a/ameritrade.md)**: Provides tools for [options](../o/options.md) [trade](../t/trade.md) [execution](../e/execution.md), [risk analysis](../r/risk_analysis.md), and automatic alerts for managing Iron Butterfly positions.

 More information can be found at: TD Ameritrade ThinkOrSwim

- **[Interactive Brokers](../i/interactive_brokers.md)**: Offers a [robust](../r/robust.md) [options](../o/options.md) trading interface with analysis tools to implement and monitor [Iron Butterfly strategies](../i/iron_butterfly_strategies.md) effectively.

 More information can be found at: Interactive Brokers

- **[TradeStation](../t/tradestation.md)**: Known for its advanced analytical tools and strategy automation, [TradeStation](../t/tradestation.md) supports complex [options](../o/options.md) strategies including Iron Butterfly with detailed [performance analytics](../p/performance_analytics.md).

 More information can be found at: TradeStation

## Conclusion

The Iron Butterfly is a strategic approach for [options](../o/options.md) traders who anticipate minimal movement in the [underlying asset](../u/underlying_asset.md)’s price. By understanding its construction, [profit](../p/profit.md)/loss dynamics, and breakeven points, traders can implement this strategy effectively to take advantage of periods of low [volatility](../v/volatility.md) while maintaining controlled [risk](../r/risk.md) exposure. However, it requires meticulous planning, [risk](../r/risk.md) assessment, and an understanding of the [underlying](../u/underlying.md) mechanics to be used successfully.
