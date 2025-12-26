# Long Condor Spread

A Long Condor Spread is an advanced [trading strategy](../t/trading_strategy.md) primarily used in [options](../o/options.md) trading. It involves the use of four different strike prices, all with the same [expiration date](../e/expiration_date.md), to form a [profit](../p/profit.md)/loss profile that looks like the wings of a condor bird. This strategy is generally employed by traders when they expect low [volatility](../v/volatility.md) in the price of the [underlying asset](../u/underlying_asset.md) and are seeking to [capitalize](../c/capitalize.md) on that outlook. Let's dive deeply into each aspect of the Long Condor Spread.

## Components of Long Condor Spread

The Long Condor Spread can be established using either call or [put options](../p/put_options.md), and it involves the following components:

1. **Buying one in-the-[money](../m/money.md) (ITM) option**: An option with a [strike price](../s/strike_price.md) lower (for calls) or higher (for puts) than the current [underlying asset](../u/underlying_asset.md) price.
2. **Selling one at-the-[money](../m/money.md) (ATM) option**: An option with a [strike price](../s/strike_price.md) close to the current [underlying asset](../u/underlying_asset.md) price.
3. **Selling one near-the-[money](../m/money.md) (NTM) option**: An option with a [strike price](../s/strike_price.md) slightly higher (for calls) or slightly lower (for puts) than the ATM option.
4. **Buying one out-of-the-[money](../m/money.md) (OTM) option**: An option with a [strike price](../s/strike_price.md) higher (for calls) or lower (for puts) than the NTM option.

Let's illustrate this with an example of a Long Call Condor Spread.

### Example: Long Call Condor Spread

Imagine a stock trades at $100. A [trader](../t/trader.md) sets up a Long Call Condor Spread using the following [options](../o/options.md):

- **Buy 1 ITM Call** at $90
- **Sell 1 ATM Call** at $100
- **Sell 1 NTM Call** at $110
- **Buy 1 OTM Call** at $120

In a similar vein, we can establish a [Long Put](../l/long_put.md) Condor Spread with corresponding strike prices, but the structure involves puts instead of calls.

### Long Condor Spread Profit/Loss (P/L) Profile

The P/L profile of a Long Condor Spread is mainly determined by the net [debit](../d/debit.md) incurred by the position. You benefit if the [underlying asset](../u/underlying_asset.md) remains within a specified trading [range](../r/range.md) until the [options](../o/options.md) expire. Let's break down the P/L scenarios:

- **Maximum [Profit](../p/profit.md)**: This is achieved when the [underlying asset](../u/underlying_asset.md)'s price is between the two short strikes (NTM and ATM) at expiration. The maximum [profit](../p/profit.md) is the difference between the strike prices of the short calls (NTM and ATM) minus the net [debit](../d/debit.md) paid for the position.
- **Maximum Loss**: This occurs if the [underlying asset](../u/underlying_asset.md)'s price either soars above or plummets below the long strikes (ITM and OTM) at expiration. The maximum loss is the net [debit](../d/debit.md) paid to enter the [trade](../t/trade.md).
- **Breakeven Points**: The breakeven points are calculated by adding and subtracting the net [debit](../d/debit.md) from the lower long strike and the upper long strike, respectively.

### Example: Profit/Loss Calculation

Assuming the stock in our earlier example remains at $105 at expiration, let's calculate the [profit](../p/profit.md)/loss:

- **Long $90 Call**: [Profit](../p/profit.md) is $105 - $90 = $15
- **Short $100 Call**: Loss is $105 - $100 = $5
- **Short $110 Call**: Expires worthless (no [profit](../p/profit.md) or loss)
- **Long $120 Call**: Expires worthless (no [profit](../p/profit.md) or loss)

Net P/L per condor spread would be $15 ([profit](../p/profit.md)) - $5 (loss) = $10

Minus the initial net [debit](../d/debit.md) paid, the [trader](../t/trader.md)'s overall [profit](../p/profit.md) could be calculated from this figure.

## Specialty and Rationale Behind Using Long Condor Spread

The rationale behind using a Long Condor Spread lies in exploiting [market](../m/market.md) conditions where an [underlying asset](../u/underlying_asset.md) is expected to show low [volatility](../v/volatility.md). This strategy is preferred by traders because:

1. **[Risk Management](../r/risk_management.md)**: It carries a defined [risk](../r/risk.md) and reward profile, making it easier for traders to manage their [risk](../r/risk.md) exposure.
2. **Reduced Cost**: In comparison to other strategies requiring [multiple](../m/multiple.md) trades, the Long Condor Spread involves fewer [transaction costs](../t/transaction_costs.md).

Additionally, since the exposure beyond the wings is limited to the net [debit](../d/debit.md) paid, the strategy provides a level of safety against unpredictable [market](../m/market.md) movements.

## Practical Considerations with Long Condor Spread

### Market Conditions

A Long Condor Spread is most effective when the [market](../m/market.md) expects minimal price movement. This can be in markets where prices are forecasted to be stagnant due to lack of catalysts, low trading volumes, or after major corporate events like [earnings](../e/earnings.md) reports.

### Implied Volatility

Implied [volatility](../v/volatility.md) has a vital role in setting up a Long Condor Spread. Traders should ideally look to execute this strategy when the implied [volatility](../v/volatility.md) is higher than expected future [volatility](../v/volatility.md), potentially allowing entry at more favorable pricing.

### Transaction Costs

As with any multi-[leg](../l/leg.md) [options](../o/options.md) strategy, [transaction costs](../t/transaction_costs.md) can significantly affect the overall profitability of the [trade](../t/trade.md). Modern trading platforms and brokers, such as Interactive Brokers or TradeStation, [offer](../o/offer.md) tools and lower [commission](../c/commission.md) rates to manage [spreads](../s/spreads.md) efficiently.

## Examples of Usage in the Real Trading World

High [market](../m/market.md) participants like [hedge](../h/hedge.md) funds and [proprietary trading](../p/proprietary_trading.md) desks use variations of condor [spreads](../s/spreads.md) to manage their exposure and [capitalize](../c/capitalize.md) on their specific [market](../m/market.md) outlook. Tools like those provided by ThinkOrSwim by TD Ameritrade [offer](../o/offer.md) traders the ability to analyze and implement complex spread strategies, including Long Condor [Spreads](../s/spreads.md).

## Adjusting the Long Condor Spread

Traders can adjust Long Condor [Spreads](../s/spreads.md) based on [market](../m/market.md) conditions:

1. **Rolling**: This involves closing the current position and opening a new one with different strike prices or expiration dates.
2. **Closing Early**: If the [market](../m/market.md) behaves contrary to the [trader](../t/trader.md)'s initial expectations, they might opt to close the position early to mitigate losses.
3. **Legging into the Spread**: Traders can also choose to enter each [leg](../l/leg.md) of the condor spread at different times to get better overall [execution](../e/execution.md) prices.

## Conclusion

The Long Condor Spread is a sophisticated [options](../o/options.md) strategy [offering](../o/offering.md) defined [risk](../r/risk.md) and potential for profitability in low [volatility](../v/volatility.md) environments. It is essential for traders to have a solid understanding of [options](../o/options.md) [market dynamics](../m/market_dynamics.md) and to use the appropriate tools and platforms to execute this strategy successfully. With careful setup and management, the Long Condor Spread can be an effective addition to a [trader](../t/trader.md)'s toolbox.
