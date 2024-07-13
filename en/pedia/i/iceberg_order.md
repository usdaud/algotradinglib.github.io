# Iceberg Order

An iceberg [order](../o/order.md) is a type of [algorithmic trading](../a/accountability.md) [order](../o/order.md) that is large in size but divided into smaller limit orders. These smaller orders, known as "child" orders, are only visible to the [market](../m/market.md) once the [order](../o/order.md) before them has been executed. The primary purpose of iceberg orders is to conceal the actual size of the [order](../o/order.md) to minimize [market](../m/market.md) impact and to prevent other traders from exploiting the information about the large [order](../o/order.md) size, which could lead to unfavorable price movements. This technique derives its name from an iceberg because, much like the physical iceberg, only a small portion of the entire [order](../o/order.md) is visible above the surface at any given time.

## Components of Iceberg Orders

### Visible Quantity

The visible quantity is the portion of the iceberg [order](../o/order.md) that is displayed to the [market](../m/market.md). It’s the "tip of the iceberg" that other traders can see. Once this visible portion is executed, another portion of the [order](../o/order.md), of the same size or a different size depending on the strategy, is placed in the [market](../m/market.md).

### Hidden Quantity

The hidden quantity is the remainder of the iceberg [order](../o/order.md) that is not visible to the [market](../m/market.md). It stays hidden until the visible portion has been filled. When exchanged, the next segment of the hidden [order](../o/order.md) becomes visible.

### Execution Strategy

The [execution](../e/execution.md) strategy can vary but generally involves replenishing the visible part of the [order](../o/order.md) automatically. Some advanced algorithms may adjust the size of the visible [order](../o/order.md) dynamically in response to [market](../m/market.md) conditions.

## Uses of Iceberg Orders

### Minimizing Market Impact

By breaking a large [order](../o/order.md) into smaller visible orders, iceberg orders help to minimize the [market](../m/market.md) impact. This prevents large price movements that can occur if the [market](../m/market.md) is aware of a large pending [order](../o/order.md).

### Reducing Information Leakage

Traders often do not want their trading intentions to be known, especially in the case of large trades. Iceberg orders help to maintain secrecy regarding the full size of the [order](../o/order.md), reducing the [risk](../r/risk.md) of adversaries taking advantage of this information.

### Improving Execution Price

In volatile markets, large orders can cause significant price [slippage](../s/slippage.md). By using iceberg orders, traders can achieve a better average [execution](../e/execution.md) price for their trades.

## Implementation of Iceberg Orders

### Trading Platforms

Many trading platforms and [brokerage services](../b/brokerage_services.md) [offer](../o/offer.md) iceberg orders as a part of their advanced trading features. Some well-known trading platforms that support iceberg orders include:

- **[Interactive Brokers](../i/interactive_brokers.md)**: [Interactive Brokers Iceberg Orders](https://www.interactivebrokers.com/en/index.php?f=614)

### Algorithmic Trading Systems

[Algorithmic trading](../a/accountability.md) systems developed by financial institutions and [hedge](../h/hedge.md) funds often include the capability to execute iceberg orders as part of their suite of strategies for optimal [trade](../t/trade.md) [execution](../e/execution.md).

## Advantages and Disadvantages

### Advantages

- **Minimized [Market](../m/market.md) Impact**: Iceberg orders reduce the impact of large trades on [market](../m/market.md) prices.
  
- **Secrecy**: They help in keeping trading intentions secret from competitors.
  
- **Better Price [Execution](../e/execution.md)**: Smaller [order](../o/order.md) sizes reduce the chances of significant price movement, achieving a better average price.

### Disadvantages

- **Partial Fills**: There is a [risk](../r/risk.md) that only part of the iceberg [order](../o/order.md) might be executed, particularly if the [market](../m/market.md) moves away from the [order](../o/order.md) price.
  
- **Higher [Transaction Costs](../t/transaction_costs.md)**: Repeatedly placing smaller orders can lead to higher cumulative [transaction costs](../t/transaction_costs.md), including fees and [spreads](../s/spreads.md).

- **Technical Complexity**: Effective use of iceberg orders often requires sophisticated [trading systems](../t/trading_systems.md) and technology, which can be resource-intensive to build and maintain.

## Use Case Examples

### Institutional Investors

Large [asset management](../a/asset_management.md) firms or pension funds often [trade](../t/trade.md) large quantities of [stocks](../s/stock.md) or other assets. Using iceberg orders, these institutions can execute large trades without spooking the [market](../m/market.md) or attracting attention from other traders.

### High-Frequency Traders

High-frequency trading (HFT) firms use iceberg orders to manage their massive [trade](../t/trade.md) volumes while reducing information [leakage](../l/leakage.md) and adverse price movements.

### Market Makers

[Market](../m/market.md) makers maintain [liquidity](../l/liquidity.md) by buying and selling securities. Iceberg orders allow them to manage their [inventory](../i/inventory.md) discreetly and [hedge](../h/hedge.md) risks without revealing the true size of their positions.

## Risks and Considerations

### Detection Algorithms

Advanced traders use sophisticated algorithms to detect hidden orders in the [market](../m/market.md). If an iceberg [order](../o/order.md) is detected, it could result in adverse [market](../m/market.md) impacts similar to those the iceberg [order](../o/order.md) is designed to avoid.

### Regulatory Scrutiny

In some jurisdictions, the use of iceberg orders may attract regulatory scrutiny. Traders must ensure compliance with local trading regulations when using iceberg orders.

### Latency

The effectiveness of an iceberg [order](../o/order.md) can be impacted by latency, which is the delay between when an [order](../o/order.md) is placed and when it is executed. High latency can result in [slippage](../s/slippage.md) and incomplete fills.

## Conclusion

Iceberg orders are a sophisticated tool in the arsenal of algorithmic traders, designed to minimize [market](../m/market.md) impact and conceal true trading intentions. By breaking large orders into smaller, more manageable chunks, iceberg orders help traders achieve better [execution](../e/execution.md) prices and reduce the [risk](../r/risk.md) of adverse price movements. However, they come with their own set of challenges, including partial fills, higher [transaction costs](../t/transaction_costs.md), and the need for advanced algorithms to remain effective in the [market](../m/market.md). As technology advances and markets become more efficient, iceberg orders [will](../w/will.md) continue to play a crucial role in modern [trading strategies](../t/trading_strategies.md).