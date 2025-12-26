# Short Put Spread

A [Short Put](../s/short_put.md) Spread, also known as a [bull put spread](../b/bull_put_spread.md), is an [options](../o/options.md) [trading strategy](../t/trading_strategy.md) primarily used in the realm of [algorithmic trading](../a/algorithmic_trading.md) (or "algo trading"). This strategy involves two [put options](../p/put_options.md) - one short and one long - that are of the same [underlying asset](../u/underlying_asset.md) and have the same [expiration date](../e/expiration_date.md), but different strike prices. The primary goal of the strategy is to [capitalize](../c/capitalize.md) on a rise in the price of the [underlying asset](../u/underlying_asset.md) while limiting potential losses.

## Components of a Short Put Spread

- **Short [Put Option](../p/put.md)**: This is the [put option](../p/put.md) that the [trader](../t/trader.md) sells or writes. The [strike price](../s/strike_price.md) of this option is usually higher than the current price of the [underlying asset](../u/underlying_asset.md).

- **Long [Put Option](../p/put.md)**: This is the [put option](../p/put.md) that the [trader](../t/trader.md) buys. The [strike price](../s/strike_price.md) of this option is lower than the [strike price](../s/strike_price.md) of the short [put option](../p/put.md), providing protection against significant downward moves in the [underlying asset](../u/underlying_asset.md)'s price.

## Mechanics of the Strategy

1. **Selling the Higher Strike [Put Option](../p/put.md) (Short [Leg](../l/leg.md))**: When you sell a [put option](../p/put.md), you receive a [premium](../p/premium.md). This [premium](../p/premium.md) is your maximum [profit](../p/profit.md) in the [short put](../s/short_put.md) spread strategy.

2. **Buying the Lower Strike [Put Option](../p/put.md) (Long [Leg](../l/leg.md))**: When you buy a [put option](../p/put.md), you pay a [premium](../p/premium.md). The purpose of buying a put with a lower [strike price](../s/strike_price.md) is to limit your potential losses if the [underlying asset](../u/underlying_asset.md)'s price drops significantly.

## Calculation of Profit and Loss

- **Maximum [Profit](../p/profit.md)**: The maximum [profit](../p/profit.md) for a [short put](../s/short_put.md) spread is the [net premium](../n/net_premium.md) received from selling the higher strike put and buying the lower strike put. This occurs if the [underlying asset](../u/underlying_asset.md)'s price stays above the higher [strike price](../s/strike_price.md) until expiration.

- **Maximum Loss**: The maximum loss is limited to the difference between the two strike prices minus the [net premium](../n/net_premium.md) received. This occurs if the [underlying asset](../u/underlying_asset.md)'s price drops below the lower [strike price](../s/strike_price.md).

- **[Breakeven Point](../b/breakeven_point.md)**: The [breakeven point](../b/breakeven_point.md) for the [short put](../s/short_put.md) spread is calculated as the higher [strike price](../s/strike_price.md) minus the [net premium](../n/net_premium.md) received.

## Example

Let's consider a stock currently trading at $100. A [trader](../t/trader.md) employs a [short put](../s/short_put.md) spread strategy as follows:
- Sell a 105-strike [put option](../p/put.md) for a [premium](../p/premium.md) of $8.
- Buy a 95-strike [put option](../p/put.md) for a [premium](../p/premium.md) of $3.

**[Net Premium](../n/net_premium.md) Received**: $8 ([credit](../c/credit.md) from selling the 105-strike put) - $3 ([debit](../d/debit.md) from buying the 95-strike put) = $5.

- **Maximum [Profit](../p/profit.md)**: $5 (the [net premium](../n/net_premium.md) received).
- **Maximum Loss**: (105 - 95) - $5 = $5.
- **[Breakeven Point](../b/breakeven_point.md)**: 105 - $5 = $100.

## Advantages

1. **Limited [Risk](../r/risk.md)**: Unlike merely writing a naked [put option](../p/put.md), the long [put option](../p/put.md) part of the spread provides a [hedge](../h/hedge.md) that limits the [trader](../t/trader.md)'s [downside risk](../d/downside_risk.md).

2. **Lower [Capital](../c/capital.md) Requirement**: A [short put](../s/short_put.md) spread typically requires less [capital](../c/capital.md) than outright long puts or short puts due to its limited maximum loss.

3. **[Profit](../p/profit.md) from [Time Decay](../t/time_decay.md)**: Selling the higher strike put allows the [trader](../t/trader.md) to benefit from [time decay](../t/time_decay.md) ([theta](../t/theta.md)), as [options](../o/options.md) typically lose [value](../v/value.md) as they approach expiration.

4. **Flexibility and Customization**: Traders can select strike prices and expiration dates tailored to their [market](../m/market.md) outlook and [risk tolerance](../r/risk_tolerance.md).

## Disadvantages

1. **Limited [Profit](../p/profit.md) Potential**: The maximum [profit](../p/profit.md) is limited to the [net premium](../n/net_premium.md) received, which can be relatively small compared to other strategies such as writing naked puts.

2. **Complexity**: Although not as complex as some multi-[leg](../l/leg.md) [options](../o/options.md) strategies, a [short put](../s/short_put.md) spread still requires a good understanding of [options](../o/options.md) pricing and [market](../m/market.md) behavior.

3. **[Execution](../e/execution.md) Challenges**: Executing the [trade](../t/trade.md) at the desired prices can be challenging, particularly in volatile markets or with illiquid [options](../o/options.md).

## Real-World Applications

### Institutions and Algo Trading

Investment firms and [hedge](../h/hedge.md) funds often employ [algorithmic trading](../a/algorithmic_trading.md) strategies that include [short put](../s/short_put.md) [spreads](../s/spreads.md). Algorithms can be programmed to identify favorable [market](../m/market.md) conditions for implementing the strategy, execute trades, manage [risk](../r/risk.md), and even exit positions when certain criteria are met.

For example, an algo trading [firm](../f/firm.md) like Two Sigma might develop an algorithm that scans the [options](../o/options.md) [market](../m/market.md) for opportunities to implement [short put](../s/short_put.md) [spreads](../s/spreads.md) based on statistical patterns and historical data.

### Retail Traders

Retail traders can use online brokerage platforms to implement short [put spread strategies](../p/put_spread_strategies.md). Platforms such as Thinkorswim by TD Ameritrade provide tools for analyzing, executing, and managing these trades.

## Tools and Platforms

- **[Market Scanners](../m/market_scanners.md)**: [Software tools](../s/software_tools_for_trading.md) that scan the [market](../m/market.md) for [options](../o/options.md) with favorable conditions for [short put](../s/short_put.md) [spreads](../s/spreads.md). Examples include OptionsPlay and Finviz.

- **Trading Platforms**: Comprehensive platforms like [Thinkorswim](../t/thinkorswim.md) and [Interactive Brokers](../i/interactive_brokers.md)' [Trader](../t/trader.md) Workstation (TWS) [offer](../o/offer.md) [robust](../r/robust.md) functionality for executing and managing [short put](../s/short_put.md) [spreads](../s/spreads.md).

- **[Risk Management](../r/risk_management.md) Tools**: Tools like portfolio [margin](../m/margin.md) calculators and [risk](../r/risk.md) analytics tools can help manage the risks associated with [short put](../s/short_put.md) [spreads](../s/spreads.md).

## Conclusion

The [Short Put](../s/short_put.md) Spread is a versatile [options](../o/options.md) strategy that can fit into a broader [algorithmic trading](../a/algorithmic_trading.md) system. It offers a balance between [risk](../r/risk.md) and reward, making it appealing for both institutional and retail traders. With the right tools and an understanding of [market dynamics](../m/market_dynamics.md), this strategy can be a valuable component of an [options](../o/options.md) trading arsenal.
