# Perpetual Swaps

## Introduction
Perpetual swaps are a type of [derivative](../d/derivative.md) instrument that has gained significant popularity in the realm of cryptocurrency trading and [algorithmic trading](../a/algorithmic_trading.md). Unlike traditional [futures contracts](../f/futures_contracts.md), perpetual swaps do not have an expiry date, allowing traders to [hold](../h/hold.md) their positions indefinitely. They were first introduced by [BitMEX](../b/bitmex.md) and have since become a staple product on many major cryptocurrency exchanges.

## Key Features of Perpetual Swaps

### No Expiry Date
The most distinctive feature of perpetual swaps is their lack of an expiry date. Traditional [futures contracts](../f/futures_contracts.md) have a set [expiration date](../e/expiration_date.md), at which point they must be settled. Perpetual swaps, on the other hand, allow traders to keep their positions [open](../o/open.md) as long as they meet the [margin](../m/margin.md) requirements and are willing to pay or receive the funding fees.

### Funding Rate
To keep the price of the perpetual [swap](../s/swap.md) close to the [underlying asset](../u/underlying_asset.md)'s [spot price](../s/spot_price.md), exchanges employ a funding rate mechanism. The funding rate is a periodic [payment](../p/payment.md) exchanged between long and short positions. When the perpetual [swap](../s/swap.md) is trading above the [spot price](../s/spot_price.md), long positions pay the funding rate to short positions. Conversely, when the [swap](../s/swap.md) is trading below the [spot price](../s/spot_price.md), short positions pay the funding rate to long positions. This mechanism incentivizes traders to take positions that help bring the perpetual [swap](../s/swap.md) price in line with the [spot price](../s/spot_price.md).

### Leverage
Perpetual swaps often come with the option to [trade](../t/trade.md) on [margin](../m/margin.md), [offering](../o/offering.md) significant [leverage](../l/leverage.md). On platforms like [BitMEX](../b/bitmex.md), traders can [leverage](../l/leverage.md) up to 100x. High [leverage](../l/leverage.md) allows traders to amplify their potential profits, but it also increases the [risk](../r/risk.md) of significant losses, especially in a highly volatile [market](../m/market.md) like cryptocurrencies.

### Mark Price
To prevent unnecessary liquidations caused by [market manipulation](../m/market_manipulation.md) or temporary [illiquidity](../i/illiquid.md), exchanges use a "mark price" to determine the [value](../v/value.md) of positions for [margin](../m/margin.md) requirements and [liquidation](../l/liquidation.md) purposes. The mark price is usually derived from a combination of the [index](../i/index_instrument.md) price of the [underlying asset](../u/underlying_asset.md) and the funding rate, providing a fairer and more stable measure of the perpetual [swap](../s/swap.md)'s [value](../v/value.md).

## Algorithmic Trading Strategies with Perpetual Swaps

### Market Making
One of the most common [algorithmic trading](../a/algorithmic_trading.md) strategies using perpetual swaps is [market](../m/market.md) making. [Market](../m/market.md) makers place both buy and sell orders around the current [market price](../m/market_price.md), capturing the [bid-ask spread](../b/bid-ask_spread.md). The [liquidity](../l/liquidity.md) provided by [market](../m/market.md) makers helps stabilize markets and narrow the [bid-ask spread](../b/bid-ask_spread.md), making trading more efficient. Creating algorithms that can dynamically adjust to [market](../m/market.md) conditions and maintain profitable [spreads](../s/spreads.md) is key to successful [market](../m/market.md) making.

### Arbitrage
Perpetual swaps present various [arbitrage](../a/arbitrage.md) opportunities due to their unique structure. Traders can engage in cross-[exchange](../e/exchange.md) [arbitrage](../a/arbitrage.md) by exploiting price discrepancies between different platforms. Funding rate [arbitrage](../a/arbitrage.md) is also common, where traders take opposing positions in the spot and perpetual [swap](../s/swap.md) markets to capture the funding rate differences. [Algorithmic trading](../a/algorithmic_trading.md) systems are especially suited for these strategies, as they can quickly identify and act on [arbitrage](../a/arbitrage.md) opportunities.

### Trend Following
Algorithmic [trend](../t/trend.md)-following strategies can also be effective with perpetual swaps. These strategies identify and follow [market](../m/market.md) trends by analyzing historical price data and utilizing indicators such as moving averages or [momentum oscillators](../m/momentum_oscillators.md). Given the high [leverage](../l/leverage.md) available with perpetual swaps, [trend](../t/trend.md)-following algorithms can achieve substantial returns, albeit with increased [risk](../r/risk.md).

### Mean Reversion
[Mean reversion](../m/mean_reversion.md) strategies assume that prices [will](../w/will.md) revert to their historical average over time. For perpetual swaps, these strategies can involve identifying [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions and taking positions that benefit from a [return](../r/return.md) to the mean. Implementing [mean reversion](../m/mean_reversion.md) algorithms requires [robust](../r/robust.md) statistical analysis and [risk management](../r/risk_management.md) to ensure positions are adjusted appropriately as [market](../m/market.md) conditions change.

## Risks Associated with Perpetual Swaps

### Leverage and Liquidation
The use of high [leverage](../l/leverage.md) in perpetual swaps amplifies both potential gains and losses. Traders must be vigilant in managing their [margin](../m/margin.md) requirements to avoid [liquidation](../l/liquidation.md). Even minor [market](../m/market.md) fluctuations can lead to the forced closure of positions, resulting in significant losses.

### Funding Rate Fluctuations
The funding rate mechanism, while designed to keep perpetual [swap](../s/swap.md) prices aligned with the [spot market](../s/spot_market.md), can introduce additional costs for traders. Sudden spikes in the funding rate can erode profits or increase losses, especially in highly leveraged positions. Algorithmic traders must account for these fluctuations in their strategies to manage their exposure effectively.

### Market Volatility
The cryptocurrency [market](../m/market.md) is notoriously volatile, with prices capable of significant swings in short periods. [Algorithmic trading](../a/algorithmic_trading.md) strategies must be designed to [handle](../h/handle.md) this [volatility](../v/volatility.md), incorporating advanced [risk management](../r/risk_management.md) systems to protect against adverse [market](../m/market.md) movements.

### Exchange Reliability
Reliability and [security](../s/security.md) of cryptocurrency exchanges are critical considerations for perpetual swaps trading. Algorithmic traders should prioritize exchanges with [robust](../r/robust.md) trading [infrastructure](../i/infrastructure.md), transparent policies, and a track record of [security](../s/security.md) and reliability. Additionally, diversifying across [multiple](../m/multiple.md) exchanges can mitigate the [risk](../r/risk.md) of [exchange](../e/exchange.md)-specific issues.

## Prominent Platforms Offering Perpetual Swaps

### BitMEX
BitMEX is one of the pioneers in [offering](../o/offering.md) perpetual swaps and remains a leading platform in this space. [BitMEX](../b/bitmex.md) provides high [leverage](../l/leverage.md), a variety of trading pairs, and a sophisticated trading engine tailored towards professional traders and [algorithmic trading](../a/algorithmic_trading.md) strategies.

### Binance
Binance is one of the largest cryptocurrency exchanges globally, [offering](../o/offering.md) perpetual swaps on a wide [range](../r/range.md) of cryptocurrencies. [Binance](../b/binance.md)'s [robust](../r/robust.md) API, extensive [liquidity](../l/liquidity.md), and comprehensive suite of trading tools make it ideal for [algorithmic trading](../a/algorithmic_trading.md).

### Bybit
Bybit is another popular platform [offering](../o/offering.md) perpetual swaps with competitive fees and advanced trading features. [Bybit](../b/bybit.md)'s emphasis on speed and reliability, along with its high [leverage](../l/leverage.md) [options](../o/options.md), makes it a preferred choice for many algorithmic traders.

### FTX
FTX has rapidly become a favored [exchange](../e/exchange.md) for perpetual swaps, known for its innovative products and [trader](../t/trader.md)-friendly policies. FTX provides a [range](../r/range.md) of unique features, including move contracts and leveraged tokens, catering to various [algorithmic trading](../a/algorithmic_trading.md) strategies.

### Kraken
Kraken offers perpetual swaps with a focus on [security](../s/security.md) and regulatory compliance. [Kraken](../k/kraken.md)'s [robust](../r/robust.md) [trading platform](../t/trading_platform.md) and lower [leverage](../l/leverage.md) [options](../o/options.md) make it suitable for algorithmic traders who prioritize [security](../s/security.md) and [risk management](../r/risk_management.md).

## Conclusion
Perpetual swaps have revolutionized the [derivatives](../d/derivatives.md) [market](../m/market.md) in the cryptocurrency space, [offering](../o/offering.md) unique opportunities and challenges for algorithmic traders. Their flexibility, coupled with the ability to [leverage](../l/leverage.md), make them an attractive instrument for various [trading strategies](../t/trading_strategies.md). However, the inherent risks such as [leverage](../l/leverage.md), funding rate fluctuations, and [market](../m/market.md) [volatility](../v/volatility.md) necessitate sophisticated algorithmic systems and diligent [risk management](../r/risk_management.md). As the [market](../m/market.md) for perpetual swaps continues to grow, ongoing advancements in [algorithmic trading](../a/algorithmic_trading.md) technology [will](../w/will.md) likely play a crucial role in capitalizing on this dynamic [financial instrument](../f/financial_instrument.md).
