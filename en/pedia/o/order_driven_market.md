# Order Driven Market

An **[order](../o/order.md) driven [market](../m/market.md)** is a type of financial [market](../m/market.md) where the price of assets, such as [stocks](../s/stock.md), bonds, currencies, or commodities, is determined by [supply](../s/supply.md) and [demand](../d/demand.md) as reflected in the orders placed by [market](../m/market.md) participants. Orders can include buy orders, sell orders, and various types of specialized orders, like limit and stop orders. Unlike [quote](../q/quote.md)-driven markets, where a [dealer](../d/dealer.md) or [market maker](../m/market_maker.md) provides the price, an [order](../o/order.md) driven [market](../m/market.md) relies entirely on the orders submitted by buyers and sellers to establish the [market price](../m/market_price.md) of an [asset](../a/asset.md).

## How Order Driven Markets Work

### Order Types
[Order](../o/order.md) driven markets operate using an electronic [order](../o/order.md) matching system where different types of orders are placed by participants. These orders generally fall into two broad categories:

1. **[Market](../m/market.md) Orders:** An [order](../o/order.md) to buy or sell immediately at the best available current price.
2. **Limit Orders:** An [order](../o/order.md) to buy or sell at a specific price or better. 
3. **Stop Orders:** Orders that become a [market order](../m/market_order.md) once a specified price threshold has been reached.
4. **[Stop-Limit Orders](../s/stop-limit_orders.md):** A two-step [order](../o/order.md) type combining the features of a [stop order](../s/stop_order.md) and a [limit order](../l/limit_order.md).

### Order Book
The heart of an [order](../o/order.md) driven [market](../m/market.md) is the [order book](../o/order_book.md), a real-time record showing the buy and sell limit orders for a particular [asset](../a/asset.md). The [order book](../o/order_book.md) organizes and prioritizes the orders based on the price and time of submission. It consists of two main parts: 

1. **[Bid](../b/bid.md) Side:** Includes all buy orders.
2. **Ask Side:** Includes all sell orders.

### Matching Engine
A central feature of [order](../o/order.md) driven markets is the matching engine, an automated system that matches buy and sell orders based on the rules pre-defined by the [exchange](../e/exchange.md). The matching process generally follows a “first-in, first-out” system, where orders are matched based on price-time priority.

### Order Execution
When a match occurs:

1. **[Market Order Execution](../m/market_order_execution.md):** Executes immediately against the best available orders on the opposite side of the [order book](../o/order_book.md).
2. **[Limit Order Execution](../l/limit_order_execution.md):** Executes either partially or fully against the current orders in the book at the specified limit price or better.
3. **[Unexecuted Orders](../u/unexecuted_orders.md):** Orders that don’t find a match immediately remain in the [order book](../o/order_book.md) until they expire or are canceled by the [trader](../t/trader.md).

### Transparency
[Order](../o/order.md) driven markets are typically very transparent:

1. **Pre-[Trade](../t/trade.md) [Transparency](../t/transparency.md):** Full [visibility](../v/visibility.md) into current orders resting in the [order book](../o/order_book.md).
2. **Post-[Trade](../t/trade.md) [Transparency](../t/transparency.md):** Immediate publication of executed trades including price and [volume](../v/volume.md) information.

## Types of Order Driven Markets

### Stock Markets
Major stock exchanges such as the New York Stock [Exchange](../e/exchange.md) (NYSE) and [NASDAQ](../n/nasdaq.md) operate primarily as [order](../o/order.md) driven markets. In these markets, participants ranging from individual investors to large institutional traders contribute buy and sell orders to a centralized system.

### Bond Markets
Certain [bond](../b/bond.md) markets, particularly those dealing with government and [municipal bonds](../m/municipal_bonds.md), also use an [order](../o/order.md) driven model where [market](../m/market.md) participants post their buy and sell orders directly.

### Commodity Markets
[Order](../o/order.md) driven systems are also used extensively in [commodity](../c/commodity.md) markets, allowing participants to [trade](../t/trade.md) contracts for commodities like oil, gold, and agricultural products.

### Cryptocurrency Markets
Cryptocurrency exchanges such as [Binance](../b/binance.md) and [Coinbase](../c/coinbase.md) operate on an [order](../o/order.md) driven [basis](../b/basis.md). These markets allow for trading of digital currencies like [Bitcoin](../b/bitcoin.md), [Ethereum](../e/ethereum_.md), and many others.

## Benefits and Challenges 

### Benefits
1. **[Price Discovery](../p/price_discovery.md):** High level of [transparency](../t/transparency.md) leads to efficient [price discovery](../p/price_discovery.md).
2. **Fair Trading:** Anonymous trading reduces chances of bias and [market manipulation](../m/market_manipulation.md).
3. **Flexibility:** Allows traders to place more specialized orders like limit and stop orders.

### Challenges
1. **[Liquidity](../l/liquidity.md):** May suffer from low [liquidity](../l/liquidity.md) during off-peak times, making it hard to execute large orders without affecting the [market price](../m/market_price.md).
2. **[Volatility](../v/volatility.md):** Higher price [volatility](../v/volatility.md) can occur due to rapid changes in [supply](../s/supply.md) and [demand](../d/demand.md).
3. **Complexity:** Requires sophisticated [trading strategies](../t/trading_strategies.md) and understanding of [order types](../o/order_types_in_trading.md) and [market](../m/market.md) mechanisms.

## Algorithms in Order Driven Markets

### Algorithmic Trading
In an [order](../o/order.md) driven [market](../m/market.md), [algorithmic trading strategies](../a/algorithmic_trading_strategies.md) are extensively used to minimize [trading costs](../t/trading_costs.md), manage risks, and optimize the [order](../o/order.md) [execution](../e/execution.md) process. These algorithms can rapidly analyze the [order book](../o/order_book.md) and execute large orders in a way that minimizes [market](../m/market.md) impact.

### Types of Trading Algorithms
1. **[Market](../m/market.md) Making:** Provides [liquidity](../l/liquidity.md) by placing both buy and sell orders around the current [market price](../m/market_price.md).
2. **[Trend Following](../t/trend_following.md):** Algorithms designed to follow and [capitalize](../c/capitalize.md) on [market](../m/market.md) trends.
3. **[Arbitrage](../a/arbitrage.md):** Exploits price discrepancies between different markets or assets.
4. **Statistical [Arbitrage](../a/arbitrage.md):** Uses statistical methods to identify and exploit [mean reversion](../m/mean_reversion.md) in [asset](../a/asset.md) prices.

### Execution Algorithms
1. **VWAP ([Volume](../v/volume.md) [Weighted Average](../w/weighted_average.md) Price):** Breaks orders into smaller chunks and executes them over a period while tracking [volume](../v/volume.md).
2. **TWAP (Time [Weighted Average](../w/weighted_average.md) Price):** Distributes orders evenly over a set time period.
3. **Implementation [Shortfall](../s/shortfall.md):** Minimizes the cost difference between the decision price and [execution](../e/execution.md) price.

## Case Studies

### New York Stock Exchange (NYSE)
The NYSE has been a prominent example of using an [order](../o/order.md) driven system. While it incorporates some elements of [quote](../q/quote.md)-driven mechanisms with its Designated [Market](../m/market.md) Makers (DMMs), the overwhelming majority of trading is driven by participant orders. 

[New York Stock Exchange](https://www.nyse.com)

### NASDAQ
[NASDAQ](../n/nasdaq.md) operates as a fully electronic [order](../o/order.md) driven [market](../m/market.md). [Market](../m/market.md) participants include a wide [range](../r/range.md) of stakeholders from individual traders to large institutional investors. The sophisticated matching engine efficiently handles a high [volume](../v/volume.md) of trades, maintaining fairness and [transparency](../t/transparency.md).

[NASDAQ](https://www.nasdaq.com)

### Binance
[Binance](../b/binance.md), one of the largest cryptocurrency exchanges, uses an [order](../o/order.md) driven system to facilitate trading across a wide [range](../r/range.md) of digital assets. The platform's sophisticated algorithms ensure efficient [order](../o/order.md) matching and [execution](../e/execution.md).

[Binance](https://www.binance.com)

## Future of Order Driven Markets

### Increased Use of AI and Machine Learning
The [incorporation](../i/incorporation.md) of AI and [machine learning](../m/machine_learning.md) technologies is expected to further refine [trading algorithms](../t/trading_algorithms.md), enhancing their predictive capacities and [execution](../e/execution.md) efficiencies.

### Regulatory Changes
Regulatory environments continue to evolve, aiming to increase [transparency](../t/transparency.md) and fairness in [order](../o/order.md) driven markets. Regulations can have significant impacts on how these markets operate.

### High-Frequency Trading (HFT)
High-frequency trading is likely to become even more prevalent, leveraging technological advancements to execute massive numbers of orders at incredibly high speeds.

### Blockchain and Decentralization
[Blockchain](../b/blockchain_in_trading.md) technology may further revolutionize [order](../o/order.md) driven markets by providing decentralized [exchange](../e/exchange.md) platforms. This could potentially increase [market](../m/market.md) [transparency](../t/transparency.md) and reduce [transaction costs](../t/transaction_costs.md).

[Order](../o/order.md) driven markets represent a complex yet efficient system for trading a multitude of financial instruments. As technology continues to evolve, so too [will](../w/will.md) the strategies and mechanisms governing these markets, promising a future filled with innovation and increased [market efficiency](../m/market_efficiency.md).