# Limit Order

A limit [order](../o/order.md) is a type of [order](../o/order.md) to buy or sell a [security](../s/security.md) at a specific price or better. It is a fundamental concept in trading and [financial markets](../f/financial_market.md), serving as a cornerstone for various [trading strategies](../t/trading_strategies.md), including [algorithmic trading](../a/algorithmic_trading.md) and high-frequency trading. Understanding the mechanics, advantages, and limitations of limit orders is crucial for traders and investors who aim to execute trades under specific conditions to maximize profitability and manage [risk](../r/risk.md).

## Definition and Purpose

A limit [order](../o/order.md) specifies that a [trade](../t/trade.md) should be executed only at the limit price or a more favorable one. For a [buy limit order](../b/buy_limit_order.md), the [order](../o/order.md) [will](../w/will.md) be executed only at the limit price or lower. Conversely, for a sell limit [order](../o/order.md), the [trade](../t/trade.md) [will](../w/will.md) be executed only at the limit price or higher. This mechanism allows traders and investors to control the entry and exit points of their trades, thereby preventing unfavorable prices from affecting their positions.

## Types of Limit Orders

### Buy Limit Order

A [buy limit order](../b/buy_limit_order.md) instructs the [broker](../b/broker.md) to purchase a particular number of [shares](../s/shares.md) or other securities only if the price reaches the specified limit or a lower [value](../v/value.md). This type of [order](../o/order.md) is particularly useful when traders expect the price to drop to a certain level before it rebounds.

#### Example

If an [investor](../i/investor.md) wants to buy [shares](../s/shares.md) of Company XYZ, currently trading at $50, but believes the price [will](../w/will.md) drop to $45, they might place a [buy limit order](../b/buy_limit_order.md) at $45. The [order](../o/order.md) [will](../w/will.md) only be executed if the share price falls to $45 or below.

### Sell Limit Order

A sell limit [order](../o/order.md) instructs the [broker](../b/broker.md) to sell a particular number of [shares](../s/shares.md) or other securities only if the price reaches the specified limit or a higher [value](../v/value.md). This helps secure profits when the [trader](../t/trader.md) believes the [security](../s/security.md) [will](../w/will.md) reach a target price before potentially declining.

#### Example

If an [investor](../i/investor.md) holds [shares](../s/shares.md) of Company XYZ, currently trading at $50, and wants to sell when the price reaches $55, they would place a sell limit [order](../o/order.md) at $55. The [order](../o/order.md) [will](../w/will.md) only be executed if the share price reaches $55 or higher.

## How Limit Orders Work

Limit orders are placed through brokerage platforms. Once placed, the [order](../o/order.md) enters the [order book](../o/order_book.md) of the [exchange](../e/exchange.md) where it waits for the [market](../m/market.md) to meet the specified price. When the [market price](../m/market_price.md) reaches the limit price, the [trade](../t/trade.md) is executed. However, if the [market price](../m/market_price.md) never hits the limit price, the [order](../o/order.md) remains unexecuted.

### Order Execution Priority

Orders in the [order book](../o/order_book.md) are executed based on price and time priority. Among [multiple](../m/multiple.md) limit orders at the same [price level](../p/price_level.md), those placed earlier are executed first. This is known as the "first come, first served" principle.

### Partial Fills

Limit orders can be partially filled if the quantity available at the limit price is less than the [order](../o/order.md) quantity. For instance, if an [investor](../i/investor.md) places a sell limit [order](../o/order.md) for 200 [shares](../s/shares.md) at $55, but only 150 [shares](../s/shares.md) find a buyer at that price, the remaining 50 [shares](../s/shares.md) [will](../w/will.md) stay in the [order book](../o/order_book.md) until the limit price is reached again.

## Advantages of Limit Orders

### Price Control

Limit orders provide significant control over the [execution](../e/execution.md) price, helping traders avoid unfavorable [market](../m/market.md) conditions. This is especially useful in markets with high [volatility](../v/volatility.md) where prices can change rapidly.

### Risk Management

By setting specific entry and exit points, investors can better manage [risk](../r/risk.md). For example, setting a sell limit [order](../o/order.md) at a target price allows traders to [lock in profits](../l/lock_in_profits.md) without constantly monitoring the [market](../m/market.md).

### Precision

Limit orders enable traders to execute trades at precise price levels, which can be critical for executing complex [trading strategies](../t/trading_strategies.md) that depend on specific price points.

### Avoids Market Impact

Since limit orders are executed at specified prices, they can help avoid the [market](../m/market.md) impact that large [market](../m/market.md) orders might cause. This is particularly relevant for institutional investors and high-frequency traders.

## Limitations of Limit Orders

### Non-Guaranteed Execution

One of the main drawbacks of limit orders is that they are not guaranteed to be executed. If the [market price](../m/market_price.md) never reaches the specified limit price, the [order](../o/order.md) remains unfilled, potentially resulting in missed trading opportunities.

### Timing Risk

Limit orders are subject to timing [risk](../r/risk.md), as the specified [price level](../p/price_level.md) may not be reached within the desired timeframe. This can be a disadvantage in fast-moving markets where prices can quickly move away from the limit price.

### Partial Fills

As mentioned, limit orders can be partially filled, which may not align with the [trader](../t/trader.md)'s intentions. This can complicate [trade](../t/trade.md) management and make it difficult to achieve the desired position size.

### Market Volatility

In highly volatile markets, limit orders can sometimes be bypassed by rapid price movements, causing the [order](../o/order.md) to remain unfilled while the [market](../m/market.md) moves in the opposite direction.

## Use Cases in Algorithmic Trading

Limit orders are a staple in [algorithmic trading strategies](../a/algorithmic_trading_strategies.md) due to their ability to provide price certainty and minimize [slippage](../s/slippage.md). [Algorithmic trading](../a/algorithmic_trading.md) systems, also known as [trading algorithms](../t/trading_algorithms.md) or "algos," use limit orders to execute trades based on predefined criteria and conditions.

### Market-Making Algorithms

[Market](../m/market.md)-makers use limit orders to provide [liquidity](../l/liquidity.md) to the [market](../m/market.md) by continuously placing both buy and sell limit orders. They [profit](../p/profit.md) from the [bid-ask spread](../b/bid-ask_spread.md) and rely on the precision and control that limit orders [offer](../o/offer.md).

### Statistical Arbitrage

Statistical [arbitrage](../a/arbitrage.md) strategies involve placing limit orders to exploit price discrepancies between correlated securities. By executing trades at specific price points, these strategies can capture small price differentials with high frequency.

### Trend-Following Algorithms

[Trend](../t/trend.md)-following algorithms may use limit orders to enter and exit positions at [key support and resistance levels](../k/key_support_and_resistance_levels.md). By setting limit orders near these levels, traders can [capitalize](../c/capitalize.md) on anticipated price movements.

## Real-World Examples

### Example 1: Individual Investor

An individual [investor](../i/investor.md), Jane, wants to buy [shares](../s/shares.md) of ABC Corp., which is currently trading at $100. She believes the stock [will](../w/will.md) drop to $95 before rising again. Jane places a [buy limit order](../b/buy_limit_order.md) at $95 for 100 [shares](../s/shares.md). If the stock price drops to $95 or lower, her [order](../o/order.md) [will](../w/will.md) be executed at $95 or a better price.

### Example 2: Institutional Investor

An [institutional investor](../i/institutional_investor.md), a mutual [fund manager](../f/fund_manager.md), wants to sell a large position in DEF Corp., currently trading at $200. To avoid driving the price down with a large [market order](../m/market_order.md), the manager places a series of sell limit orders at various price points above $200. As the [market price](../m/market_price.md) reaches these levels, portions of the position are sold without significantly impacting the [market price](../m/market_price.md).

## Conclusion

Limit orders are a powerful tool for traders and investors, providing control, precision, and [risk management](../r/risk_management.md) in executing trades. While they [offer](../o/offer.md) numerous advantages, such as price control and reduced [market](../m/market.md) impact, they also come with limitations like non-guaranteed [execution](../e/execution.md) and timing [risk](../r/risk.md). By understanding the mechanics and applications of limit orders, traders can make informed decisions and implement effective [trading strategies](../t/trading_strategies.md). In the realm of [algorithmic trading](../a/algorithmic_trading.md), limit orders are indispensable, enabling sophisticated algorithms to execute trades with precision and [efficiency](../e/efficiency.md).