# Negative Gamma Strategies

## Introduction

In the realm of [options](../o/options.md) trading, [gamma](../g/gamma.md) is a crucial [risk](../r/risk.md) metric that measures the rate of change of [delta](../d/delta.md) in an option relative to changes in the price of the [underlying asset](../u/underlying_asset.md). [Delta](../d/delta.md) represents the sensitivity of the option's price to movements in the price of the [underlying asset](../u/underlying_asset.md). [Gamma](../g/gamma.md), therefore, provides insight into the [convexity](../c/convexity.md) or curvature of the option's payoff profile.

Negative [gamma](../g/gamma.md) refers to a situation where the [gamma](../g/gamma.md) of an [options](../o/options.md) position is negative, meaning that the position loses [delta](../d/delta.md) faster than it gains it when the price of the [underlying asset](../u/underlying_asset.md) moves. This characteristic can lead to greater risks in volatile markets but can also be harnessed by sophisticated traders through targeted strategies known as negative [gamma](../g/gamma.md) strategies.

## Understanding Gamma

### Definition of Gamma

[Gamma](../g/gamma.md) (Γ) is the second [derivative](../d/derivative.md) of an option's price with respect to the price of the [underlying asset](../u/underlying_asset.md). Mathematically:

\[ \[Gamma](../g/gamma.md) = \frac{\partial^2 V}{\partial S^2} \]

where \( V \) is the price of the option, and \( S \) is the price of the [underlying asset](../u/underlying_asset.md).

### Interpretation of Gamma

- **Positive [Gamma](../g/gamma.md)**: Implies that as the [underlying asset](../u/underlying_asset.md)'s price increases, the [delta](../d/delta.md) of the option increases. Conversely, as the [underlying asset](../u/underlying_asset.md)'s price decreases, the [delta](../d/delta.md) of the option decreases.
- **Negative [Gamma](../g/gamma.md)**: Implies that as the [underlying asset](../u/underlying_asset.md)'s price increases, the [delta](../d/delta.md) of the option decreases. Conversely, as the [underlying asset](../u/underlying_asset.md)'s price decreases, the [delta](../d/delta.md) of the option increases.

Positive [gamma](../g/gamma.md) is typically found in long [options](../o/options.md) positions (both calls and puts), whereas negative [gamma](../g/gamma.md) is associated with short [options](../o/options.md) positions.

## Negative Gamma Strategies

Negative [gamma](../g/gamma.md) strategies [capitalize](../c/capitalize.md) on the unique attributes of negative [gamma](../g/gamma.md) positions, typically through [options](../o/options.md) writing (selling) strategies. These strategies are designed to benefit from periods of low [volatility](../v/volatility.md), where the [underlying asset](../u/underlying_asset.md)’s price remains relatively stable.

### Types of Negative Gamma Strategies

1. **[Short Straddle](../s/short_straddle.md)**

A [short straddle](../s/short_straddle.md) involves selling both a [call option](../c/call_option.md) and a [put option](../p/put.md) with the same [strike price](../s/strike_price.md) and [expiration date](../e/expiration_date.md). This strategy profits from minimal movement in the [underlying asset](../u/underlying_asset.md)'s price, as the premiums collected from selling the [options](../o/options.md) [will](../w/will.md) exceed any losses if the price remains stable.

 - **[Risk](../r/risk.md)/Reward Profile**: While the potential [profit](../p/profit.md) is limited to the premiums received, the [risk](../r/risk.md) can be substantial if the [underlying](../u/underlying.md) price moves significantly in either direction.
 - **Example**: Selling a call and [put option](../p/put.md) on XYZ stock, both with a [strike price](../s/strike_price.md) of $100 and expiration in one month, aiming to [profit](../p/profit.md) from low [volatility](../v/volatility.md) in XYZ’s stock price.

2. **[Short Strangle](../s/short_strangle.md)**

A [short strangle](../s/short_strangle.md) involves selling an out-of-the-[money](../m/money.md) call and an out-of-the-[money](../m/money.md) put with different strike prices but the same [expiration date](../e/expiration_date.md). This strategy also benefits from low [volatility](../v/volatility.md), but it provides a larger [range](../r/range.md) within which the [underlying asset](../u/underlying_asset.md)’s price can move without causing a loss.

 - **[Risk](../r/risk.md)/Reward Profile**: Similar to a [short straddle](../s/short_straddle.md), but with a potentially wider [profit](../p/profit.md) [range](../r/range.md) and correspondingly lower premiums collected compared to a [straddle](../s/straddle.md).
 - **Example**: Selling a [call option](../c/call_option.md) on XYZ stock with a [strike price](../s/strike_price.md) of $110 and a [put option](../p/put.md) with a [strike price](../s/strike_price.md) of $90, both expiring in one month.

3. **[Iron Condor](../i/iron_condor.md)**

An [iron condor](../i/iron_condor.md) involves selling an out-of-the-[money](../m/money.md) call and an out-of-the-[money](../m/money.md) put while simultaneously buying a further out-of-the-[money](../m/money.md) call and a further out-of-the-[money](../m/money.md) put. This creates a position with limited [risk](../r/risk.md) and limited [profit](../p/profit.md) potential, benefiting from low [volatility](../v/volatility.md) in the [underlying asset](../u/underlying_asset.md)’s price.

 - **[Risk](../r/risk.md)/Reward Profile**: The maximum [profit](../p/profit.md) is achieved if the [underlying](../u/underlying.md) price remains between the two strike prices of the sold [options](../o/options.md), with the maximum loss limited to the difference between the strike prices of the sold and bought [options](../o/options.md) minus the [net premium](../n/net_premium.md) received.
 - **Example**: Selling a [call option](../c/call_option.md) on XYZ stock with a [strike price](../s/strike_price.md) of $105 and a [put option](../p/put.md) with a [strike price](../s/strike_price.md) of $95, while buying a [call option](../c/call_option.md) with a [strike price](../s/strike_price.md) of $110 and a put with a [strike price](../s/strike_price.md) of $90, all expiring in one month.

4. **[Short Call](../s/short_call.md) or Put Spread**

A [short call spread](../s/short_call_spread.md) involves selling a [call option](../c/call_option.md) and buying another [call option](../c/call_option.md) with a higher [strike price](../s/strike_price.md) and the same [expiration date](../e/expiration_date.md). Similarly, a [short put spread](../s/short_put_spread.md) involves selling a [put option](../p/put.md) and buying another [put option](../p/put.md) with a lower [strike price](../s/strike_price.md).

 - **[Risk](../r/risk.md)/Reward Profile**: These [spreads](../s/spreads.md) limit both the potential [profit](../p/profit.md) and potential loss, making them a more controlled negative [gamma](../g/gamma.md) strategy compared to outright short [options](../o/options.md) positions.
 - **Example**: Selling a [call option](../c/call_option.md) on XYZ stock with a [strike price](../s/strike_price.md) of $100 and buying a [call option](../c/call_option.md) with a [strike price](../s/strike_price.md) of $105, both expiring in one month.

### Managing Risk in Negative Gamma Strategies

Negative [gamma](../g/gamma.md) strategies inherently involve significant risks, particularly in volatile [market](../m/market.md) conditions. Effective [risk management](../r/risk_management.md) techniques include:

- **[Diversification](../d/diversification.md)**: Holding a broad [range](../r/range.md) of positions across different assets and strike prices to mitigate the impact of adverse price movements.
- **[Dynamic Hedging](../d/dynamic_hedging.md)**: Actively adjusting the [delta](../d/delta.md) of the portfolio to maintain a desired exposure level. This involves buying or selling the [underlying asset](../u/underlying_asset.md) to counterbalance changes in [delta](../d/delta.md) resulting from movements in the [asset](../a/asset.md)’s price.
- **Using [Stop-Loss Orders](../s/stop-loss_orders.md)**: Placing [stop-loss orders](../s/stop-loss_orders.md) to automatically close out positions at predefined loss levels.
- **Limiting Position Size**: Ensuring that individual positions do not constitute a disproportionate share of the overall portfolio, thereby reducing the impact of any single adverse price move.

## Real-World Applications

### Market Makers

[Market](../m/market.md) makers, such as Virtu Financial [ and Citadel Securities [ frequently employ negative gamma strategies. Their role in providing [liquidity](../l/liquidity.md) involves continuously quoting buy and sell prices, necessitating the writing of [options](../o/options.md) and maintaining [delta](../d/delta.md)-[neutral](../n/neutral.md) portfolios through active hedging.

### Hedge Funds

[Hedge](../h/hedge.md) funds specializing in [volatility](../v/volatility.md) [arbitrage](../a/arbitrage.md), like those managed by AQR [Capital](../c/capital.md) Management [ and options-focused funds, often utilize negative gamma strategies to exploit differences between implied and realized volatility. These funds deploy sophisticated algorithms and risk management frameworks to capture premiums from writing options while controlling [gamma exposure](../g/gamma_exposure.md).

### Proprietary Trading Firms

[Proprietary trading](../p/proprietary_trading.md) firms, such as Jane Street [ and DRW [ leverage their advanced trading systems and large capital bases to implement negative gamma strategies effectively. These firms utilize high-frequency trading algorithms to dynamically hedge their [gamma exposure](../g/gamma_exposure.md) in real-time.

## Advanced Considerations

### Volatility Skew

Understanding [volatility skew](../v/volatility_skew.md), the pattern of varying implied [volatility](../v/volatility.md) across different strike prices, is crucial for successfully implementing negative [gamma](../g/gamma.md) strategies. Traders must consider how [skewness](../s/skewness.md) affects option pricing and adjust their strategies to account for higher or lower premiums at different strikes.

### Impact of Dividends and Corporate Actions

Dividends and other corporate actions can significantly influence the behavior of [options](../o/options.md) and the [underlying asset](../u/underlying_asset.md)'s price. Traders must adjust their negative [gamma](../g/gamma.md) strategies to account for these events, ensuring that the impact on [delta](../d/delta.md) and [gamma](../g/gamma.md) is appropriately hedged.

### Utilization of Exotic Options

[Exotic options](../e/exotic_options.md), such as binary [options](../o/options.md) or barrier [options](../o/options.md), can be incorporated into negative [gamma](../g/gamma.md) strategies to create more complex payoff profiles. These [options](../o/options.md) provide additional flexibility in managing [gamma exposure](../g/gamma_exposure.md) and tailoring [risk](../r/risk.md)-reward characteristics to specific [market](../m/market.md) conditions.

## Conclusion

Negative [gamma](../g/gamma.md) strategies [offer](../o/offer.md) sophisticated traders opportunities to [profit](../p/profit.md) from periods of low [volatility](../v/volatility.md) by writing [options](../o/options.md) and managing their [delta](../d/delta.md) exposure dynamically. While these strategies carry substantial [risk](../r/risk.md), especially in volatile markets, diligent [risk management](../r/risk_management.md) and an in-depth understanding of [gamma](../g/gamma.md) behavior can lead to consistent profits. Advanced applications by [market](../m/market.md) makers, [hedge](../h/hedge.md) funds, and [proprietary trading](../p/proprietary_trading.md) firms highlight the versatility and potential of negative [gamma](../g/gamma.md) strategies in various trading environments.
