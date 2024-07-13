# Long Iron Butterfly

## Introduction

The Long [Iron Butterfly](../i/iron_butterfly.md) strategy is an advanced [options](../o/options.md) [trading strategy](../t/trading_strategy.md) that combines elements of both the [Iron Condor](../i/iron_condor.md) and the [Butterfly Spread](../b/butterfly_spread.md). It is designed to [profit](../p/profit.md) from low [volatility](../v/volatility.md) in the [underlying asset](../u/underlying_asset.md), allowing traders to [capitalize](../c/capitalize.md) on price containment within a specific [range](../r/range.md). The strategy involves the simultaneous buying and selling of four [options](../o/options.md) of the same [underlying asset](../u/underlying_asset.md) with three different strike prices. By understanding the mechanics of the Long [Iron Butterfly](../i/iron_butterfly.md), traders can better appreciate its benefits and risks.

## Basics of Options Trading

Before delving into the Long [Iron Butterfly](../i/iron_butterfly.md), it's crucial to have a foundational understanding of [options](../o/options.md) trading. [Options](../o/options.md) are financial [derivatives](../d/derivatives.md) that provide the buyer the right, but not the obligation, to buy or sell an [underlying asset](../u/underlying_asset.md) at a predetermined [strike price](../s/strike_price.md) before or at the expiry date. There are two primary types of [options](../o/options.md):

1. **Call [Options](../o/options.md)**: These give the holder the right to buy the [underlying asset](../u/underlying_asset.md).
2. **[Put Options](../p/put_options.md)**: These give the holder the right to sell the [underlying asset](../u/underlying_asset.md).

## Structure of the Long Iron Butterfly

The Long [Iron Butterfly](../i/iron_butterfly.md) consists of four [options](../o/options.md) contracts:
1. Long one lower strike put (buy a [put option](../p/put.md) at [strike price](../s/strike_price.md) A).
2. Short two middle strike calls and puts (write both a call and a [put option](../p/put.md) at [strike price](../s/strike_price.md) B).
3. Long one higher strike call (buy a [call option](../c/call_option.md) at [strike price](../s/strike_price.md) C).

The general structure follows the format: [Long Put](../l/long_put.md) @ Strike A, [Short Put](../s/short_put.md) and Call @ Strike B, Long Call @ Strike C, where Strike A < Strike B < Strike C.

### Setting Up the Trade

1. **Select the [Underlying Asset](../u/underlying_asset.md)**: Choose a stock or [index](../i/index_instrument.md) that you expect to have low [volatility](../v/volatility.md).
2. **Identify the Strike Prices and Expiration Dates**: Strike prices should be equidistant, and the [expiration date](../e/expiration_date.md) should allow sufficient time for the strategy to play out.
3. **Execute the Contracts**: Buy one put at the lower [strike price](../s/strike_price.md), sell one put and one call at the middle [strike price](../s/strike_price.md), and buy one call at the higher [strike price](../s/strike_price.md).

### Example Setup

Suppose a stock is trading at $100. A [trader](../t/trader.md) could set up a Long [Iron Butterfly](../i/iron_butterfly.md) as follows:

- Buy 1 $95 put (lower strike put)
- Sell 1 $100 put (middle strike put)
- Sell 1 $100 call (middle strike call)
- Buy 1 $105 call (higher strike call)

## Payoff Diagram

The payoff diagram of a Long [Iron Butterfly](../i/iron_butterfly.md) resembles a 'V' shape, inverted due to being "long." This profile indicates that maximum [profit](../p/profit.md) occurs if the [underlying asset](../u/underlying_asset.md)'s price remains near the middle [strike price](../s/strike_price.md) (Strike B) at expiration, while maximum loss occurs if the price deviates significantly from the middle [strike price](../s/strike_price.md).

### Maximum Profit

The maximum [profit](../p/profit.md) is achieved when the [underlying asset](../u/underlying_asset.md)'s price is exactly at the middle [strike price](../s/strike_price.md) (Strike B) at expiration. The [profit](../p/profit.md) is calculated as:

\[ \text{Max Profit} = \text{[Net Premium](../n/net_premium.md) Received} \]

### Maximum Loss

The maximum loss occurs if the [underlying asset](../u/underlying_asset.md)'s price falls below the lower [strike price](../s/strike_price.md) (Strike A) or rises above the higher [strike price](../s/strike_price.md) (Strike C). The loss is calculated as:

\[ \text{Max Loss} = \text{Strike Width} - \text{[Net Premium](../n/net_premium.md) Received} \]

Where Strike Width = Strike C - Strike A

## Advantages of the Long Iron Butterfly

1. **[Profit](../p/profit.md) from Low [Volatility](../v/volatility.md)**: The strategy is optimal when the [underlying asset](../u/underlying_asset.md)'s price remains within a narrow [range](../r/range.md).
2. **Limited [Risk](../r/risk.md)**: Both maximum loss and maximum [gain](../g/gain.md) are predefined, allowing for effective [risk management](../r/risk_management.md).
3. **Cost [Efficiency](../e/efficiency.md)**: Compared to buying a stock outright, the Long [Iron Butterfly](../i/iron_butterfly.md) requires a lower initial investment.

## Disadvantages of the Long Iron Butterfly

1. **Limited [Profit](../p/profit.md) Potential**: While the [risk](../r/risk.md) is limited, so is the [profit](../p/profit.md) potential, which is confined to the [net premium](../n/net_premium.md) received.
2. **Complex [Execution](../e/execution.md)**: Involves [multiple](../m/multiple.md) legs which can be confusing for beginners and usually incurs higher [transaction costs](../t/transaction_costs.md).
3. **Sensitivity to Small Price Movements**: The strategy can suffer if the [underlying asset](../u/underlying_asset.md)'s price makes minor unexpected movements.

## Risk Management

Effective [risk management](../r/risk_management.md) is critical in [options](../o/options.md) trading, and the Long [Iron Butterfly](../i/iron_butterfly.md) is no exception. Consider the following tips:

1. **Monitor [Volatility](../v/volatility.md)**: Keep an eye on implied [volatility](../v/volatility.md), as fluctuations can significantly affect strategy performance.
2. **Set [Stop-Loss Orders](../s/stop-loss_orders.md)**: Predefine exit points to minimize losses if the [market](../m/market.md) moves unfavorably.
3. **Adjust Positions**: If the [market](../m/market.md) environment changes, consider closing the position early or adjusting one or more legs to better align with the new conditions.

## Comparing Long Iron Butterfly with Other Strategies

### Butterfly Spread

- **Similarity**: Both involve a combination of calls and puts and aim to benefit from low [volatility](../v/volatility.md).
- **Difference**: The [Butterfly Spread](../b/butterfly_spread.md) uses only calls or only puts, while the Long [Iron Butterfly](../i/iron_butterfly.md) uses both.

### Iron Condor

- **Similarity**: Both involve buying and selling calls and puts at different strike prices.
- **Difference**: [Iron Condor](../i/iron_condor.md) requires four different strike prices and is typically not as sensitive to the [underlying asset](../u/underlying_asset.md) price as the Long [Iron Butterfly](../i/iron_butterfly.md).

## Example Companies Using the Strategy

### Goldman Sachs
Goldman Sachs, a leading global [investment banking](../i/investment_banking.md) [firm](../f/firm.md), utilizes various [options](../o/options.md) strategies, including the Long [Iron Butterfly](../i/iron_butterfly.md), for [portfolio management](../p/portfolio_management.md) and hedging purposes. More about their [trading strategies](../t/trading_strategies.md) can be found on their [official website](https://www.goldmansachs.com).

### Interactive Brokers
[Interactive Brokers](../i/interactive_brokers.md) provides comprehensive tools and platforms for traders to execute complex [options](../o/options.md) strategies like the Long [Iron Butterfly](../i/iron_butterfly.md). Their trading insights and resources cater to both retail and institutional investors. For more information, visit [Interactive Brokers](https://www.interactivebrokers.com).

## Conclusion

The Long [Iron Butterfly](../i/iron_butterfly.md) is an advanced [options](../o/options.md) [trading strategy](../t/trading_strategy.md) that can effectively [leverage](../l/leverage.md) low [volatility](../v/volatility.md) in the [underlying asset](../u/underlying_asset.md). By understanding its structure, mechanics, advantages, and risks, traders can make more informed decisions and better manage their portfolios. Whether used by professional trading firms like Goldman Sachs or facilitated through platforms like [Interactive Brokers](../i/interactive_brokers.md), the Long [Iron Butterfly](../i/iron_butterfly.md) remains a valuable tool in the [options](../o/options.md) trading arsenal.
