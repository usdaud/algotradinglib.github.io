# Trailing Stop

A trailing stop is a type of [stop-loss order](../s/stop-loss_order.md) that is designed to protect gains by enabling a [trade](../t/trade.md) to remain [open](../o/open.md) and continue to [profit](../p/profit.md) as long as the price is moving in a favorable direction. The trailing stop price moves with the [market price](../m/market_price.md) as it moves in a favorable direction, but it "trails" behind it by a specified percentage or dollar amount. Should the price change direction by a specified amount, the trailing [stop order](../s/stop_order.md) [will](../w/will.md) be executed, and the position [will](../w/will.md) be closed.

## Key Features

1. **Dynamic Adjustments**: Unlike a static [stop-loss order](../s/stop-loss_order.md), which is set at a specific price that doesn't change, a trailing stop adjusts as the price moves in favor of the position. This dynamic nature allows traders to [lock in profits](../l/lock_in_profits.md) while still giving the [trade](../t/trade.md) room to grow.

2. **Self-Discipline**: Trailing stops enforce a level of discipline by preventing emotional decision-making. Traders often struggle to know when to let profits run and when to cut losses. A trailing stop removes this [uncertainty](../u/uncertainty_in_trading.md) by adhering to a pre-defined strategy.

3. **Customizable Parameters**: Traders can define the trailing amount, setting it to a specific dollar [value](../v/value.md) or percentage. This customization allows the strategy to be tailored to different types of assets and [market](../m/market.md) conditions.

## Types of Trailing Stops

### Fixed Trailing Stops
A fixed trailing stop is set to trail the [market price](../m/market_price.md) by a fixed dollar amount or percentage. For instance, if you set a fixed trailing stop at $2 for a long position, the stop price [will](../w/will.md) always be $2 below the highest price achieved since entering the [trade](../t/trade.md).

### Volatility-Based Trailing Stops
Some traders prefer to set trailing stops based on [volatility](../v/volatility.md) measures such as the [Average True Range](../a/average_true_range_(atr).md) (ATR). This approach adjusts the trailing stop distance based on the current level of [market](../m/market.md) [volatility](../v/volatility.md), making it more adaptive to [market](../m/market.md) conditions.

### Technical Indicator-Based Trailing Stops
Another method is to base the trailing stop on [technical indicators](../t/technical_indicator.md), such as moving averages or [Bollinger Bands](../b/bollinger_band.md). This method lets traders [leverage](../l/leverage.md) complex algorithms to recalibrate the stop-loss levels dynamically.

## Calculating Trailing Stops

### Percentage Method
If your trailing stop is based on a percentage, the calculation [will](../w/will.md) dynamically change as prices increase. For example, if you buy a stock at $100 and set a 5% trailing stop, the [stop-loss order](../s/stop-loss_order.md) [will](../w/will.md) initially be placed at $95. If the stock price increases to $110, the trailing stop [will](../w/will.md) move up to $104.50.

### Dollar Method
Alternatively, if you use a dollar amount, the trailing stop calculation is more straightforward but less adaptive. If the stock price increases by $10, your trailing stop [will](../w/will.md) always remain $10 below the current highest price.

## Implementation in Trading Platforms

Most trading platforms provide features to set trailing stops. Let's take a look at how to set trailing stops on some popular trading platforms:

### MetaTrader 4/5
To set a trailing stop in MetaTrader, right-click on your [open position](../o/open_position.md) and select 'Trailing Stop,' then choose a predefined [value](../v/value.md) or set a custom one.

### Interactive Brokers
[Interactive Brokers](../i/interactive_brokers.md) offers a comprehensive guide to setting trailing stops.

### Thinkorswim by TD Ameritrade
Users of the Thinkorswim [trading platform](../t/trading_platform.md) can set trailing stops from the [order](../o/order.md) entry screen. Detailed instructions can be found here.

## Benefits of Using Trailing Stops

1. **[Profit](../p/profit.md) Protection**: As the [market price](../m/market_price.md) increases, the trailing stop rises, thereby protecting a portion of the gains.

2. **Automation**: Trailing stops automate exit decisions, reducing the need for constant monitoring.

3. **Discipline**: Trailing stops can enforce a [trading strategy](../t/trading_strategy.md) by preventing emotional decision-making.

4. **Versatility**: They can be applied to any [asset class](../a/asset_class.md) including [stocks](../s/stock.md), forex, commodities, and cryptocurrencies.

## Limitations and Risks

1. **Unexpected [Market](../m/market.md) Closure**: Trailing stops might not execute if the [market](../m/market.md) closes unexpectedly, leaving positions unprotected.

2. **[Slippage](../s/slippage.md)**: In fast-moving markets, there may be a gap between the stop price and the actual price at which the [order](../o/order.md) is executed, known as [slippage](../s/slippage.md).

3. **Over-tight Stops**: Setting the trailing distance too tight may result in premature stop-outs, especially in volatile markets.

4. **[Noise](../n/noise.md) and Whipsaws**: In highly volatile markets, trailing stops may trigger due to short-term price fluctuations ([market](../m/market.md) [noise](../n/noise.md)) rather than a substantial change in [trend](../t/trend.md) direction.

## Best Practices

1. **Appropriate Distance**: Choosing an appropriate trailing distance (percentage or dollar amount) is crucial. Too tight a distance can result in frequent stop-outs, while too wide a distance may not effectively limit losses.

2. **[Market](../m/market.md) Analysis**: Before setting a trailing stop, perform a [market](../m/market.md) analysis to understand the [asset](../a/asset.md)'s [volatility](../v/volatility.md) and trading patterns.

3. **Regular Reviews**: Periodically review your trailing stop strategy and adjust based on [market](../m/market.md) conditions.

4. **Integration with Overall Strategy**: Ensure that the use of trailing stops aligns with your overall [trading strategy](../t/trading_strategy.md) and [risk management](../r/risk_management.md) framework.

## Advanced Strategies

### Combining With Other Orders
Combining trailing stops with other types of orders can create more sophisticated [trading strategies](../t/trading_strategies.md). For instance, you can use a trailing stop along with a [limit order](../l/limit_order.md) to [lock in profits](../l/lock_in_profits.md) once a certain [price level](../p/price_level.md) is reached.

### Algorithmic Trading
In [algorithmic trading](../a/algorithmic_trading.md), trailing stops can be coded into [automated trading systems](../a/automated_trading_systems.md) to execute exit strategies without human intervention. These algorithms can be backtested and optimized to ensure they perform well under different [market](../m/market.md) conditions.

### Multi-Trailing Stops
An advanced tactic involves using [multiple](../m/multiple.md) trailing stops at different levels. For instance, setting one tight trailing stop to secure immediate gains and another wider one to capture larger trends can achieve a balance between protecting profits and allowing for growth.

## Conclusion

Trailing stops are a powerful tool for traders looking to protect profits while giving their trades room to grow. By understanding how to calculate, implement, and utilize trailing stops, traders can enhance their [trading strategies](../t/trading_strategies.md), manage [risk](../r/risk.md) more effectively, and navigate complex [market](../m/market.md) environments with greater confidence. However, it is crucial to continually adapt and review trailing stop settings to ensure they align with prevailing [market](../m/market.md) conditions and individual trading goals.