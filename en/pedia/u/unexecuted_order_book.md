# Unexecuted Order Book

An unexecuted [order book](../o/order_book.md), also known as a [limit order book](../l/limit_order_book.md) or simply an [order book](../o/order_book.md), is a ledger or electronic list maintained by an [exchange](../e/exchange.md) or trading venue that details orders that traders have placed to buy or sell securities or assets at specified prices. These orders have not yet been executed, meaning they haven't been matched with a corresponding buy or sell [order](../o/order.md) at the desired price. The unexecuted [order book](../o/order_book.md) plays a fundamental role in [financial markets](../f/financial_market.md), providing [visibility](../v/visibility.md) into the [supply](../s/supply.md) and [demand](../d/demand.md) for a given [security](../s/security.md) or [asset](../a/asset.md).

### Structure of the Unexecuted Order Book

A typical unexecuted [order book](../o/order_book.md) is organized by price levels. Each [price level](../p/price_level.md) displays:

- **[Order](../o/order.md) Size**: The quantity of the [asset](../a/asset.md) or [security](../s/security.md) that traders are willing to buy or sell at that particular price.
- **[Order](../o/order.md) Time**: The timestamp indicating when the [order](../o/order.md) was placed. This becomes important for the prioritization of orders, especially when [multiple](../m/multiple.md) orders exist at the same [price level](../p/price_level.md).

The structure of the [order book](../o/order_book.md) involves two main sides:

1. **[Bid](../b/bid.md) Side**: This side of the [order book](../o/order_book.md) contains all the buy orders, with traders placing these orders aiming to purchase the [asset](../a/asset.md) at or below a certain price.
2. **Ask Side**: This side of the [order book](../o/order_book.md) contains all the sell orders, where traders seek to sell the [asset](../a/asset.md) at or above their specified price.

The best [bid](../b/bid.md) (the highest price a [trader](../t/trader.md) is willing to pay) and the best ask (the lowest price at which a [trader](../t/trader.md) is willing to sell) are known as the top of the book. The difference between these two prices is called the [bid-ask spread](../b/bid-ask_spread.md). A tighter spread usually indicates higher [liquidity](../l/liquidity.md), meaning that it's easier to execute trades without significantly impacting the [asset](../a/asset.md)'s price.

### Order Types

Within the unexecuted [order book](../o/order_book.md), various types of orders may be present:

- **Limit Orders**: Orders to buy or sell a [security](../s/security.md) at a specific price or better. These do not get executed immediately as they are waiting for the [market](../m/market.md) to reach the specified price.
- **Stop Orders**: Orders that become active [market](../m/market.md) orders once a certain [price level](../p/price_level.md) is reached. These are typically used to limit losses or protect profits.
- **Iceberg Orders**: Large orders that are split into smaller, more manageable chunks to prevent revealing the full [order](../o/order.md) size to the [market](../m/market.md). Only a portion of the [order](../o/order.md) is visible on the [order book](../o/order_book.md), with the remaining portion becoming visible as the pieces get executed.

### Importance in Algorithmic Trading

For algorithmic traders, the unexecuted [order book](../o/order_book.md) is a crucial source of information. It provides insights into the [market](../m/market.md)’s depth and [liquidity](../l/liquidity.md), allowing algorithms to make informed decisions based on the [visible supply](../v/visible_supply.md) and [demand](../d/demand.md). High-frequency trading (HFT) strategies, in particular, rely heavily on the information contained in the [order book](../o/order_book.md) to execute trades rapidly and [capitalize](../c/capitalize.md) on minute price differences.

### Data Analytics and Visualization

Modern trading platforms and algorithms employ sophisticated [data analytics](../d/data_analytics.md) and visualization techniques to interpret the [order book](../o/order_book.md). Key metrics and tools include:

- **[Heatmaps](../h/heatmaps_in_trading.md)**: Visual representations showing concentrations of buy and sell orders at various price levels.
- **[Order Flow Analysis](../o/order_flow_analysis.md)**: Monitoring the stream of incoming orders to predict price movements and [market](../m/market.md) trends.
- **[Market](../m/market.md) Impact Models**: Estimating the potential impact of executing large orders on the [asset](../a/asset.md)’s price, which is critical for minimizing [slippage](../s/slippage.md) in large trades.

### Market Data Providers

Several companies specialize in providing [real-time market data](../r/real-time_market_data.md), including unexecuted [order book](../o/order_book.md) data. Examples include:

- **Refinitiv (formerly Thomson [Reuters](../r/reuters.md))**: [Refinitiv](https://www.refinitiv.com)
- **[Bloomberg](../b/bloomberg.md)**: [Bloomberg](https://www.bloomberg.com)
- **[CQG](../c/cqg.md)**: [CQG](https://www.cqg.com)
- **[Nasdaq](../n/nasdaq.md) [Market](../m/market.md) Data**: [Nasdaq](https://www.nasdaq.com/market-activity/data).

### Role of Market Makers

[Market](../m/market.md) makers play a pivotal role in an unexecuted [order book](../o/order_book.md). They provide [liquidity](../l/liquidity.md) by consistently placing buy and sell limit orders. Their activities help narrow the [bid-ask spread](../b/bid-ask_spread.md) and increase the [market](../m/market.md)'s overall [efficiency](../e/efficiency.md). [Market](../m/market.md) makers [profit](../p/profit.md) from the [bid-ask spread](../b/bid-ask_spread.md) by buying at lower prices and selling at higher prices.

### Challenges and Considerations

- **[Order Book](../o/order_book.md) [Spoofing](../s/spoofing.md)**: A manipulative technique where fake orders are placed to create a false sense of [supply](../s/supply.md) or [demand](../d/demand.md), only to be canceled before they can be executed. Regulatory bodies have become more vigilant in detecting and penalizing such practices.
- **Latency**: The speed at which [order book](../o/order_book.md) data is updated can vary, and even minor delays (latency) can have significant implications for traders relying on real-time data.
- **Data Overload**: The sheer [volume](../v/volume.md) of data can be overwhelming, hence the importance of effective filtering and processing systems.

### Conclusion

The unexecuted [order book](../o/order_book.md) is an essential component of modern trading, [offering](../o/offering.md) critical insights into [market dynamics](../m/market_dynamics.md). It serves as the foundation for various [trading strategies](../t/trading_strategies.md) and is integral for maintaining [market](../m/market.md) [liquidity](../l/liquidity.md) and [efficiency](../e/efficiency.md). As technology and [market](../m/market.md) structures evolve, the role and complexity of the unexecuted [order book](../o/order_book.md) are likely to grow, necessitating ongoing adaptations in both trading practices and regulatory oversight.
