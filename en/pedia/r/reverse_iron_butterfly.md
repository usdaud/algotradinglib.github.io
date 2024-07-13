# Reverse Iron Butterfly

The Reverse [Iron Butterfly](../i/iron_butterfly.md), also known as the reverse iron fly, is an advanced [trading strategy](../t/trading_strategy.md) used in [options](../o/options.md) markets. Unlike its counterpart, the [Iron Butterfly](../i/iron_butterfly.md), which profits from low [volatility](../v/volatility.md) and a stable [underlying asset](../u/underlying_asset.md) price, the Reverse [Iron Butterfly](../i/iron_butterfly.md) is designed to [profit](../p/profit.md) from significant price movements, thus favoring high [volatility](../v/volatility.md) scenarios. Here's a detailed overview of the Reverse [Iron Butterfly](../i/iron_butterfly.md), including its structure, advantages, risks, and practical considerations for traders.

## Structure of the Reverse Iron Butterfly

### Components

The Reverse [Iron Butterfly](../i/iron_butterfly.md) is composed of four [options](../o/options.md) contracts:
1. **Long [Call Option](../c/call_option.md) (Lower Strike)**  
   A [call option](../c/call_option.md) with the lowest [strike price](../s/strike_price.md).
2. **[Short Call Option](../s/short_call_option.md) (Middle Strike)**  
   A [call option](../c/call_option.md) with a middle [strike price](../s/strike_price.md), typically at-the-[money](../m/money.md).
3. **Short [Put Option](../p/put.md) (Middle Strike)**  
   A [put option](../p/put.md) with the same middle [strike price](../s/strike_price.md) as the [short call](../s/short_call.md).
4. **Long [Put Option](../p/put.md) (Higher Strike)**  
   A [put option](../p/put.md) with the highest [strike price](../s/strike_price.md).

### Formation

1. **Buy 1 Lower Strike [Call Option](../c/call_option.md)** (Long Call)
2. **Sell 1 Middle Strike [Call Option](../c/call_option.md)** ([Short Call](../s/short_call.md))
3. **Sell 1 Middle Strike [Put Option](../p/put.md)** ([Short Put](../s/short_put.md))
4. **Buy 1 Higher Strike [Put Option](../p/put.md)** ([Long Put](../l/long_put.md))

### Example

Let's assume the [underlying asset](../u/underlying_asset.md) is trading at $100. A Reverse [Iron Butterfly](../i/iron_butterfly.md) might be constructed as follows:

1. **Buy 1 Call at $90**
2. **Sell 1 Call at $100**
3. **Sell 1 Put at $100**
4. **Buy 1 Put at $110**

This setup creates a net [debit](../d/debit.md) position, where the [trader](../t/trader.md) incurs a cost upfront. The maximum loss is limited to the initial [debit](../d/debit.md), while the maximum [profit](../p/profit.md) potential is substantial, depending on the extent of the [underlying asset](../u/underlying_asset.md)'s price movement.

## Profit and Loss Scenarios

### Maximum Profit

The maximum [profit](../p/profit.md) of the Reverse [Iron Butterfly](../i/iron_butterfly.md) occurs when the price of the [underlying asset](../u/underlying_asset.md) moves significantly away from the middle [strike price](../s/strike_price.md) (either upward or downward). In our example, the highest profits are achieved if the [underlying asset](../u/underlying_asset.md)'s price moves far below $90 or above $110.

### Maximum Loss

The maximum loss is restricted to the [net premium](../n/net_premium.md) paid to enter the position. This loss occurs when the [underlying asset](../u/underlying_asset.md)'s price is exactly at the middle [strike price](../s/strike_price.md) at expiration. In our example, this would be at $100.

### Breakeven Points

There are two breakeven points for the Reverse [Iron Butterfly](../i/iron_butterfly.md):
1. **Lower [Breakeven Point](../b/breakeven_point.md):**  
   Lower Strike + [Net Premium](../n/net_premium.md) Paid
2. **Upper [Breakeven Point](../b/breakeven_point.md):**  
   Higher Strike - [Net Premium](../n/net_premium.md) Paid

## Greeks of the Reverse Iron Butterfly

Understanding the Greek parameters is essential for gauging the [risk](../r/risk.md) and reward dynamics:
- **[Delta](../d/delta.md):** Near zero at inception, with potential to fluctuate as the [underlying](../u/underlying.md) price moves.
- **[Gamma](../g/gamma.md):** Initially low, but grows as the [underlying](../u/underlying.md) price approaches the breakeven points.
- **[Vega](../v/vega.md):** Positive, indicating that the position gains with rising [volatility](../v/volatility.md).
- **[Theta](../t/theta.md):** Negative, as [time decay](../t/time_decay.md) works against the net long position.
- **[Rho](../r/rho.md):** Impacted by [interest](../i/interest.md) rates, but generally considered minor compared to other [Greeks](../g/greeks.md).

## Advantages of the Reverse Iron Butterfly

### High Profit Potential

The strategy offers substantial [profit](../p/profit.md) potential from large price movements in either direction. This is suitable for traders who anticipate increased [volatility](../v/volatility.md) in the [underlying asset](../u/underlying_asset.md).

### Limited Risk

The maximum loss is confined to the initial [debit](../d/debit.md) paid, providing a clear and defined [risk](../r/risk.md) parameter.

### Beneficial in Volatile Markets

Given its positive [Vega](../v/vega.md), the Reverse [Iron Butterfly](../i/iron_butterfly.md) gains from rising [volatility](../v/volatility.md), making it ideal during times of [market](../m/market.md) [uncertainty](../u/uncertainty_in_trading.md) or anticipated significant price swings.

## Risks and Considerations

### Time Decay

Negative [Theta](../t/theta.md) means that [time decay](../t/time_decay.md) [will](../w/will.md) erode the position’s [value](../v/value.md) if the [underlying asset](../u/underlying_asset.md)’s price does not move significantly. Traders must be mindful of the expiration timeline.

### Execution Complexity

Executing four contracts can be complex and may involve higher fees. [Slippage](../s/slippage.md) and [bid](../b/bid.md)-ask [spreads](../s/spreads.md) can also impact the overall profitability.

### Market Movements

If the [underlying asset](../u/underlying_asset.md) remains around the middle [strike price](../s/strike_price.md), the [trader](../t/trader.md) [will](../w/will.md) face the maximum loss, making it crucial to have accurate predictions about [volatility](../v/volatility.md) and price movements.

## Practical Application

### When to Use

The Reverse [Iron Butterfly](../i/iron_butterfly.md) is most effective in markets where significant price movement is expected, either due to [earnings announcements](../e/earnings_announcements.md), economic data releases, or [geopolitical events](../g/geopolitical_events.md) that could lead to high [volatility](../v/volatility.md).

### Example: Earnings Season

During [earnings](../e/earnings.md) season, companies often experience substantial price swings following [earnings announcements](../e/earnings_announcements.md). Implementing a Reverse [Iron Butterfly](../i/iron_butterfly.md) around such events can help [capitalize](../c/capitalize.md) on these movements.

## Conclusion

The Reverse [Iron Butterfly](../i/iron_butterfly.md) is a powerful strategy for traders equipped with a solid understanding of [options](../o/options.md) and [market dynamics](../m/market_dynamics.md). While it offers limited [risk](../r/risk.md) and the potential for high rewards, it requires precise [execution](../e/execution.md) and a keen eye on [market](../m/market.md) conditions. It is most beneficial in volatile markets and requires a disciplined approach to manage risks associated with [time decay](../t/time_decay.md) and [market](../m/market.md) movements. 

For further exploration and advanced tools for [options](../o/options.md) strategies, the following firms provide comprehensive resources:
- [Thinkorswim by TD Ameritrade](https://www.tdameritrade.com/tools-and-platforms/thinkorswim/features.page)
- [Interactive Brokers](https://www.interactivebrokers.com/en/index.php?f=4985)

These platforms [offer](../o/offer.md) [robust](../r/robust.md) [options](../o/options.md) trading tools, educational resources, and analytics to help traders effectively implement strategies like the Reverse [Iron Butterfly](../i/iron_butterfly.md).