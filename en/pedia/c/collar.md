# Collar

## Overview
A collar, also known as a [hedge](../h/hedge.md) wrapper, is an [options](../o/options.md) [trading strategy](../t/trading_strategy.md) that involves holding the [underlying security](../u/underlying_security.md) while simultaneously buying an out-of-the-[money](../m/money.md) [put option](../p/put.md) and selling an out-of-the-[money](../m/money.md) [call option](../c/call_option.md). This strategy is designed to provide downside protection while giving up some [upside potential](../u/upside_potential_in_trading.md) in [exchange](../e/exchange.md). Collars are commonly used to [hedge](../h/hedge.md) against volatile [market](../m/market.md) conditions and to [lock in profits](../l/lock_in_profits.md).

## Components of a Collar
1. **[Underlying Security](../u/underlying_security.md)**: This is the [asset](../a/asset.md) (such as stock or [commodity](../c/commodity.md)) that the [trader](../t/trader.md) owns and wishes to [hedge](../h/hedge.md).
2. **[Put Option](../p/put.md)**: An [options contract](../o/options_contract.md) that gives the holder the right, but not the obligation, to sell the [underlying security](../u/underlying_security.md) at a specified [strike price](../s/strike_price.md) before the contract expires. In a collar strategy, a [put option](../p/put.md) is bought to provide downside protection.
3. **[Call Option](../c/call_option.md)**: An [options contract](../o/options_contract.md) that gives the holder the right, but not the obligation, to buy the [underlying security](../u/underlying_security.md) at a specified [strike price](../s/strike_price.md) before the contract expires. In a collar strategy, a [call option](../c/call_option.md) is sold to partially [finance](../f/finance.md) the purchase of the [put option](../p/put.md).

## Construction of a Collar
To construct a collar:
1. **[Hold](../h/hold.md) the [Underlying Security](../u/underlying_security.md)**: Typically, this is done if the [trader](../t/trader.md) already owns the stock or [security](../s/security.md).
2. **Buy a [Put Option](../p/put.md)**: Purchase a [put option](../p/put.md) at a [strike price](../s/strike_price.md) below the current [market price](../m/market_price.md) of the [underlying security](../u/underlying_security.md). This provides protection against a decline in the [security](../s/security.md)'s price.
3. **Sell a [Call Option](../c/call_option.md)**: Sell a [call option](../c/call_option.md) at a [strike price](../s/strike_price.md) above the current [market price](../m/market_price.md) of the [underlying security](../u/underlying_security.md). This generates [premium](../p/premium.md) [income](../i/income.md) that can [offset](../o/offset.md) the cost of purchasing the [put option](../p/put.md).

## Example of a Collar
Suppose an [investor](../i/investor.md) owns 100 [shares](../s/shares.md) of ABC Corp, currently trading at $50 per share. The [investor](../i/investor.md) fears the stock might drop but also wants to participate if the stock rises. They could implement a collar:
- **Buy a [put option](../p/put.md)** with a [strike price](../s/strike_price.md) of $45 (out-of-the-[money](../m/money.md)) expiring in three months.
- **Sell a [call option](../c/call_option.md)** with a [strike price](../s/strike_price.md) of $55 (out-of-the-[money](../m/money.md)) expiring in three months.

This strategy ensures that the [investor](../i/investor.md) can sell the stock at $45 if it drops below this level, thus limiting [downside risk](../d/downside_risk.md). However, the [gain](../g/gain.md) is capped at $55 because if the stock rises above this level, the [call option](../c/call_option.md) [will](../w/will.md) likely be exercised.

## Payoff Diagram
The payoff of a collar strategy can be visualized in a payoff diagram, which plots [profit](../p/profit.md) and loss against the price of the [underlying security](../u/underlying_security.md) at expiration:

- **Below $45**: The [put option](../p/put.md) offsets losses by allowing the [investor](../i/investor.md) to sell the [shares](../s/shares.md) at $45.
- **Between $45 and $55**: The [investor](../i/investor.md) enjoys any gains in the [underlying security](../u/underlying_security.md) as the [options](../o/options.md) expire worthless.
- **Above $55**: Gains are capped as the [call option](../c/call_option.md) gets exercised, and the [underlying](../u/underlying.md) [shares](../s/shares.md) are sold at $55.

## Advantages of Collar Strategy
1. **Downside Protection**: Provides a safety net against significant losses in the [underlying security](../u/underlying_security.md).
2. **Reduced Cost**: The [premium](../p/premium.md) received from selling the [call option](../c/call_option.md) partially offsets the cost of buying the [put option](../p/put.md).
3. **Flexibility**: Allows the [investor](../i/investor.md) to participate in some [upside potential](../u/upside_potential_in_trading.md) while limiting [downside risk](../d/downside_risk.md).

## Disadvantages of Collar Strategy
1. **Limited [Upside](../u/upside.md)**: Gains are capped by the [strike price](../s/strike_price.md) of the sold [call option](../c/call_option.md).
2. **Complexity**: Requires knowledge of [options](../o/options.md) trading and careful management of positions.
3. **Cost of Implementation**: While partially [offset](../o/offset.md) by the call [premium](../p/premium.md), buying [put options](../p/put_options.md) can be expensive, particularly in high [volatility](../v/volatility.md) markets.

## Practical Applications in Algorithmic Trading
[Algorithmic trading](../a/accountability.md) systems can utilize collars for [risk management](../r/risk_management.md) and [profit](../p/profit.md)-locking strategies. These systems can be programmed to automatically implement collars based on pre-defined rules, such as:

- **[Volatility Analysis](../v/volatility_analysis.md)**: Deploying collars when a certain level of [market](../m/market.md) [volatility](../v/volatility.md) is detected.
- **[Profit](../p/profit.md) Booking**: Establishing collars after achieving a target [profit](../p/profit.md) level in an [underlying security](../u/underlying_security.md).

### Example of Algorithmic Collar Execution
Suppose an algorithm is designed to:
1. Monitor a portfolio of [stocks](../s/stock.md).
2. Identify [stocks](../s/stock.md) that have reached a specific [profit](../p/profit.md) threshold.
3. Automatically create collars on these [stocks](../s/stock.md) to lock in gains.

Consider the portfolio includes 1,000 [shares](../s/shares.md) of XYZ Corp, purchased at $100 each. The stock rises to $150, and the algorithm decides to implement a collar:
- **Buy a [put option](../p/put.md)** with a [strike price](../s/strike_price.md) of $140 (out-of-the-[money](../m/money.md)).
- **Sell a [call option](../c/call_option.md)** with a [strike price](../s/strike_price.md) of $160 (out-of-the-[money](../m/money.md)).

By doing this, the algorithm ensures that:
- If the stock price drops below $140, losses are limited.
- Gains are capped at $160 if the stock price rises beyond this level.

## Companies Offering Collar Trade Execution
Several financial institutions and trading platforms [offer](../o/offer.md) tools and services to execute collar strategies. Notably:

- **[Interactive Brokers](../i/interactive_brokers.md)**: Provides a [robust](../r/robust.md) platform for [options](../o/options.md) trading, including the ability to create and manage collar strategies. More information can be found on their [website](https://www.interactivebrokers.com).
- **TD [Ameritrade](../a/ameritrade.md)**: Offers advanced [options](../o/options.md) trading tools suitable for implementing collar strategies. Details are available on their [website](https://www.tdameritrade.com).
- **[E*TRADE](../e/e_trade.md)**: Allows traders to design and execute [options](../o/options.md) strategies, including collars. [Check](../c/check.md) their [website](https://us.etrade.com) for more.

## Conclusion
The collar strategy is a valuable tool in a [trader](../t/trader.md)'s arsenal for managing [risk](../r/risk.md) and protecting gains, especially in volatile markets. By utilizing [algorithmic trading](../a/accountability.md) systems, the [execution](../e/execution.md) of collars can be automated, ensuring consistent application of the strategy without the need for constant monitoring.