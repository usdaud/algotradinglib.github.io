# Fill Or Kill (FOK)

Fill Or [Kill](../k/kill.md) (FOK) is a specific type of [order](../o/order.md) used in [financial markets](../f/financial_market.md), particularly for trading [stocks](../s/stock.md), [options](../o/options.md), and other securities. This term is essential to understand if you are delving into [algorithmic trading](../a/accountability.md) (algotrading), where speed and precision can significantly influence trading outcomes. 

## Definition and Purpose

FOK is an [order](../o/order.md) that instructs the [broker](../b/broker.md) or trading system to execute a [transaction](../t/transaction.md) immediately and in its entirety or not at all. If the entire [order](../o/order.md) cannot be filled at once, it is canceled (killed) without any partial [execution](../e/execution.md). The primary objective of a Fill Or [Kill](../k/kill.md) [order](../o/order.md) is to ensure that no partial transactions occur which could potentially disrupt the [trader](../t/trader.md)'s strategy or lead to less favorable [execution](../e/execution.md) prices.

### Key Attributes
- **Immediate [Execution](../e/execution.md)**: The [order](../o/order.md) is executed as soon as it reaches the [market](../m/market.md).
- **All or Nothing**: There is no room for partial fills; the entire [order](../o/order.md) must be completed or canceled.
- **Time-Sensitive**: This type of [order](../o/order.md) does not sit in the [order book](../o/order_book.md) waiting for a match.

### Example

Consider a [trader](../t/trader.md) who places a FOK [order](../o/order.md) to buy 1000 [shares](../s/shares.md) of company XYZ at a maximum price of $10 per share. If 1000 [shares](../s/shares.md) are available at $10 or less, the [order](../o/order.md) [will](../w/will.md) be executed in its entirety instantly. However, if only 900 [shares](../s/shares.md) are available or if the [shares](../s/shares.md) are priced higher than $10, the [order](../o/order.md) [will](../w/will.md) be canceled immediately.

## Importance in Algorithmic Trading

### Speed and Efficiency

In [algorithmic trading](../a/accountability.md), speed is crucial. Algorithms are designed to make decisions and execute trades in fractions of a second. FOK orders are beneficial in such environments as they provide a binary outcome instantaneously—either the [trade](../t/trade.md) is executed in full or not at all. This is particularly useful for high-frequency trading (HFT) strategies that require precision and speed to [capitalize](../c/capitalize.md) on [market](../m/market.md) opportunities.

### Avoiding Slippage

[Slippage](../s/slippage.md) refers to the difference between the expected price of a [trade](../t/trade.md) and the actual price at which the [trade](../t/trade.md) is executed. FOK orders help in minimizing [slippage](../s/slippage.md) by ensuring that the [order](../o/order.md) is either completely filled at the desired price or canceled. This is critical when trading large volumes where partial fills at varying prices could lead to significant deviations from the targeted [execution](../e/execution.md) price.

### Risk Management

FOK orders can also be a part of [risk management](../r/risk_management.md) strategies. By ensuring that a [trade](../t/trade.md) is executed only if the entire [volume](../v/volume.md) can be matched, traders can avoid the risks associated with incomplete or partial fills. This is especially important in volatile markets where prices can fluctuate rapidly.

### Market Impact

Using FOK orders can mitigate the [market](../m/market.md) impact of large trades. For example, if a large buy [order](../o/order.md) is partially filled, it may push up the price, making subsequent fills more expensive. A FOK [order](../o/order.md) either executes in full at the initial price or not at all, thus preventing any adverse impact on the [market price](../m/market_price.md).

## How FOK Orders Work

### Placement

When placing a FOK [order](../o/order.md), a [trader](../t/trader.md) or algorithm specifies the number of [shares](../s/shares.md), the price (if a [limit order](../l/limit_order.md)), and the FOK instruction. This informs the brokerage platform or trading system that the [order](../o/order.md) must be executed immediately in full or canceled.

### Execution

Upon receiving the FOK [order](../o/order.md), the trading system checks the [liquidity](../l/liquidity.md) available in the [market](../m/market.md):
- If the full [order](../o/order.md) can be filled at the specified price or better, it is executed instantly.
- If the full [order](../o/order.md) cannot be filled, it is canceled immediately without any partial executions.

### Example in Different Markets

1. **[Stock Market](../s/stock_market.md)**: In a [liquid market](../l/liquid_market.md) like the New York Stock [Exchange](../e/exchange.md) (NYSE), a FOK [order](../o/order.md) for 1000 [shares](../s/shares.md) of a [blue-chip stock](../b/blue-chip_stock.md) is likely to be executed quickly if the price conditions are reasonable. However, in a less [liquid market](../l/liquid_market.md), the [order](../o/order.md) might not be filled at all due to insufficient available [shares](../s/shares.md) at the desired price.
 
2. **[Options](../o/options.md) [Market](../m/market.md)**: In the [options](../o/options.md) [market](../m/market.md), FOK orders can be used to ensure the [acquisition](../a/acquisition.md) of a specific number of contracts. Given the complexity and lower [liquidity](../l/liquidity.md) of [options](../o/options.md) compared to [stocks](../s/stock.md), FOK orders ensure precise [execution](../e/execution.md) without partial fills.

3. **[Futures Market](../f/futures_market.md)**: In [futures](../f/futures.md) trading, FOK orders are particularly useful for large institutional traders who need to enter or exit positions swiftly to avoid [slippage](../s/slippage.md) and [market](../m/market.md) impact.

## Advantages of FOK Orders

### Certainty and Clarity

FOK orders provide certainty to traders. You know instantly whether your [order](../o/order.md) is executed or not, facilitating better decision-making and strategy adjustments.

### Efficiency in High-Frequency Trading

In high-frequency trading, the [efficiency](../e/efficiency.md) of FOK orders is unmatched. They allow algorithms to attempt trades and, if not successful, move on to the next opportunity without dwelling on partial executions.

### Reduced Administrative Overhead

Partially filled orders can lead to [multiple](../m/multiple.md) transactions that need to be managed. FOK orders reduce this administrative burden by ensuring orders are fully completed or canceled.

### Ideal for Large Orders

For institutions or traders dealing with large orders, FOK ensures that the intended [volume](../v/volume.md) is traded at the desired price, avoiding the complexities and risks associated with partial fills.

## Disadvantages of FOK Orders

### Missed Opportunities

One of the primary downsides of FOK orders is the potential for missed trading opportunities. In illiquid markets or during volatile trading conditions, finding counterparties for large orders at a fixed price can be challenging, leading to frequent cancellations.

### Not Suitable for All Scenarios

FOK orders are not ideal for every trading scenario. For traders willing to accept partial fills, other [order types](../o/order_types_in_trading.md) like Immediate or Cancel (IOC) might be more appropriate.

### Higher Complexity

Using FOK orders adds complexity to [trading strategies](../t/trading_strategies.md), particularly for novice traders or those unfamiliar with advanced [order types](../o/order_types_in_trading.md).

### Potential for Increased Costs

In some markets, the frequent cancellation of FOK orders could incur higher [transaction costs](../t/transaction_costs.md), depending on the [fee](../f/fee.md) structure of the trading venue or [broker](../b/broker.md).

## Alternative Order Types

### Immediate or Cancel (IOC)

An IOC [order](../o/order.md) is similar to a FOK [order](../o/order.md) but allows for partial [execution](../e/execution.md). If any part of the [order](../o/order.md) can be filled immediately, it [will](../w/will.md) be, and the remaining portion [will](../w/will.md) be canceled. This provides a middle ground between FOK, which requires full [execution](../e/execution.md), and other more flexible [order types](../o/order_types_in_trading.md).

### Good Till Cancelled (GTC)

A GTC [order](../o/order.md) remains active until it is either filled or explicitly canceled by the [trader](../t/trader.md). Unlike FOK orders, GTC orders do not have an immediacy requirement and can remain [open](../o/open.md) in the [order book](../o/order_book.md) for an extended period.

### Day Orders

Day orders are active only for the trading day on which they are placed. If they are not filled by the end of the [trading session](../t/trading_session.md), they are automatically canceled. These are generally more flexible than FOK orders in terms of [execution](../e/execution.md).

## Implementing FOK in Algorithmic Trading

### Software and Tools

For algorithmic traders, implementing FOK orders requires [robust](../r/robust.md) software and [trading systems](../t/trading_systems.md) capable of processing complex [order types](../o/order_types_in_trading.md). Trading platforms like MetaTrader, [TradeStation](../t/tradestation.md), and others [offer](../o/offer.md) the capability to place FOK orders either through their graphical user interface or via programmatic access using APIs.

### Coding FOK Logic

When coding FOK logic into an algorithm, the primary steps involve:
- Checking [market](../m/market.md) [liquidity](../l/liquidity.md) in real-time.
- Placing the FOK [order](../o/order.md) if [liquidity](../l/liquidity.md) conditions are met.
- Canceling the [order](../o/order.md) immediately if it cannot be filled in full.

Here is a simplified pseudo-code example:

```python
def place_fok_order(order_volume, target_price):
    current_price = get_current_market_price()
    available_volume = get_market_liquidity_at_price(target_price)
    
    if available_volume >= order_volume and current_price <= target_price:
        execute_order(order_volume, target_price)
        [return](../r/return.md) "[Order](../o/order.md) Filled"
    else:
        [return](../r/return.md) "[Order](../o/order.md) Canceled"

# Example usage
result = place_fok_order(1000, 10)
print(result)  # Output [will](../w/will.md) either be "[Order](../o/order.md) Filled" or "[Order](../o/order.md) Canceled"
```

### Integrating with Trading APIs

Most [algorithmic trading strategies](../a/algorithmic_trading_strategies.md) are executed through trading APIs provided by brokerage firms. For example, [Interactive Brokers](../i/interactive_brokers.md) offers an API that supports advanced [order types](../o/order_types_in_trading.md) including FOK. Traders need to ensure that their code interfaces correctly with the API and handles the necessary [trade](../t/trade.md) lifecycle events.

For more information on [Interactive Brokers](../i/interactive_brokers.md)' API, visit their official site: [Interactive Brokers API](https://www.interactivebrokers.com/en/index.php?f=5041).

### Performance Considerations

The effectiveness of FOK orders in algo trading hinges on several performance factors:
- **Latency**: The time taken to place and confirm the [order](../o/order.md) must be minimal.
- **[Market](../m/market.md) Data Accuracy**: Real-time data must be precise to ensure that the algorithm makes informed decisions.
- **System Resilience**: The trading system must [handle](../h/handle.md) rapid [order](../o/order.md) placements and cancellations without crashing or significant delays.

## Real-World Applications

### High-Frequency Trading Firms

High-frequency trading firms, such as Virtu Financial and Tower Research [Capital](../c/capital.md), use FOK orders to manage the precision and speed required for their [trading strategies](../t/trading_strategies.md). These companies rely on the instantaneous nature of FOK orders to execute large volumes without affecting [market](../m/market.md) prices.

### Institutional Investors

Institutional investors, managing large portfolios, often use FOK orders when they need to re-balance portfolios or enter/exit significant positions quickly. This minimizes the impact on the [market price](../m/market_price.md) and ensures that their [trading strategies](../t/trading_strategies.md) remain intact.

### Retail Traders

While FOK orders are more common among professional and institutional traders, retail traders can also utilize them, especially in volatile markets or when trading low-[liquidity](../l/liquidity.md) [stocks](../s/stock.md). Platforms like Thinkorswim and [Interactive Brokers](../i/interactive_brokers.md) provide retail traders with access to FOK orders.

## Conclusion

Fill Or [Kill](../k/kill.md) (FOK) orders play an integral role in modern trading, particularly within the realm of [algorithmic trading](../a/accountability.md). Their ability to provide immediate, complete, and decisive [execution](../e/execution.md) makes them a valuable tool for managing large trades and minimizing [market](../m/market.md) impact. However, they are not without disadvantages, such as the potential for missed opportunities and increased complexity. By understanding the mechanics, advantages, and use cases of FOK orders, traders and algorithms can better navigate the complex landscape of [financial markets](../f/financial_market.md) and execute their strategies with greater precision and confidence.