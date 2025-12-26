# Commission

In the realm of [financial markets](../f/financial_market.md), commissions play a critical role, especially in the context of [algorithmic trading](../a/accountability.md). A commission is essentially a [fee](../f/fee.md) charged by a [broker](../b/broker.md) or [investment advisor](../i/investment_advisor.md) for facilitating transactions such as buying and selling securities. These fees can profoundly impact [trading strategies](../t/trading_strategies.md), especially those that involve a high frequency of trades.

### Types of Commissions in Trading
1. **Fixed Commissions**: These are predefined fees charged on each [trade](../t/trade.md) irrespective of the [trade](../t/trade.md)'s [volume](../v/volume.md) or [value](../v/value.md). Since they are flat, they can make it easier to predict costs over time.

2. **Percentage-based Commissions**: Unlike fixed commissions, these fees are calculated as a percentage of the [transaction](../t/transaction.md)'s [value](../v/value.md). This means that larger transactions [will](../w/will.md) incur larger fees.

3. **Tiered Commissions**: Some brokers [offer](../o/offer.md) tiered pricing models where the commission rates decrease as the trading [volume](../v/volume.md) or activity increases. This approach is designed to attract high-frequency traders by [offering](../o/offering.md) them lower fees as their trading activity scales up.

4. **Per-share Commissions**: This model charges traders based on the number of [shares](../s/shares.md) traded rather than the total [value](../v/value.md) of the [trade](../t/trade.md). This can be particularly appealing for high-frequency [trading strategies](../t/trading_strategies.md) involving large quantities of [low-priced stocks](../l/low-priced_stocks.md).

### Impact of Commission on Trading Strategies

[Algorithmic trading](../a/accountability.md) relies heavily on executing orders at speeds and frequencies that human traders cannot match. Understanding the impact of commissions is vital because these fees can erode the profitability of [trading strategies](../t/trading_strategies.md) if not managed properly.

1. **[Scalping](../s/scalping.md)**: This high-frequency [trading strategy](../t/trading_strategy.md) involves making numerous small profits from brief price movements. Due to the high frequency of trades, commission costs can quickly add up, drastically affecting profitability.

2. **[Market](../m/market.md) Making**: Here, the [trader](../t/trader.md) provides [liquidity](../l/liquidity.md) to the [market](../m/market.md) by placing both buy and sell orders and earns a spread (the difference between buying and selling prices). Even though [market](../m/market.md) makers often receive rebates, commissions can still impact the net gains, especially if the spread is tight.

3. **[Mean Reversion](../m/mean_reversion.md)**: This strategy involves buying low and selling high based on the assumption that [asset](../a/asset.md) prices [will](../w/will.md) revert to their historical averages. The frequency and size of trades can influence the overall commission costs, impacting the strategy's effectiveness.

### Examples of Brokerages and Their Commission Structures

#### Interactive Brokers
[Interactive Brokers](../i/interactive_brokers.md) is renowned for its low-cost commission structure, particularly appealing to high-frequency traders.

Link: Interactive Brokers

#### Charles Schwab
[Charles Schwab](../c/charles_schwab.md) offers a [range](../r/range.md) of commission-free trading on various products, making it an attractive option for different types of traders.

Link: Charles Schwab

#### E*TRADE
[E*TRADE](../e/e_trade.md) offers a mix of commission-free trading [options](../o/options.md) and tiered commission structures.

Link: E*TRADE

### Calculating the Impact of Commissions on Profitability

To effectively manage the costs associated with [algorithmic trading](../a/accountability.md), it’s vital to incorporate commission calculations into your [trading algorithms](../t/trading_algorithms.md). Here’s a simplified example of how you might [factor](../f/factor.md) commissions into a [trading strategy](../t/trading_strategy.md):

```python
def calculate_net_profit([profit](../p/profit.md), total_shares_traded, commission_per_share):
    total_commission = total_shares_traded * commission_per_share
    net_profit = [profit](../p/profit.md) - total_commission
    [return](../r/return.md) net_profit

# Example parameters
[profit](../p/profit.md) = 5000
total_shares_traded = 2000
commission_per_share = 0.01

net_profit = calculate_net_profit([profit](../p/profit.md), total_shares_traded, commission_per_share)
print(f"Net [Profit](../p/profit.md): ${net_profit}")
# Output: Net Profit: $4800.00
```

### Conclusion

Understanding commissions is a fundamental aspect of successful [algorithmic trading](../a/accountability.md). Every strategy, whether it involves high-frequency trades or [long-term investments](../l/long-term_investments.md), needs to account for these costs to ensure the profitability of the trades. With a deep understanding of various commission structures and their impacts, traders can make more informed decisions to maximize their returns.