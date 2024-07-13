# Vanilla Option

A vanilla option, often simply referred to as a [plain vanilla](../p/plain_vanilla.md) option, is a standardized financial [derivative](../d/derivative.md) that gives the holder the right, but not the obligation, to buy or sell an [underlying asset](../u/underlying_asset.md) at a predetermined price (known as the [strike price](../s/strike_price.md)) within a specific time frame (before the [expiration date](../e/expiration_date.md)). These [options](../o/options.md) are called "vanilla" because they are the most basic and common type of [options contract](../o/options_contract.md), in contrast to more complex and [exotic options](../e/exotic_option.md).

Vanilla [options](../o/options.md) can be divided into two main types:

1. **[Call Option](../c/call_option.md)**: This gives the holder the right to buy the [underlying asset](../u/underlying_asset.md) at the [strike price](../s/strike_price.md).
2. **[Put Option](../p/put.md)**: This gives the holder the right to sell the [underlying asset](../u/underlying_asset.md) at the [strike price](../s/strike_price.md).

## Key Components of a Vanilla Option

### Underlying Asset
The [underlying asset](../u/underlying_asset.md) is the [financial instrument](../f/financial_instrument.md) on which the option is based. This can be [stocks](../s/stock.md), bonds, commodities, currencies, indices, or even [interest](../i/interest.md) rates.

### Strike Price (Exercise Price)
The [strike price](../s/strike_price.md) is the specified price at which the [underlying asset](../u/underlying_asset.md) can be bought ([call option](../c/call_option.md)) or sold ([put option](../p/put.md)) by the option holder. This is agreed upon when the option contract is created and remains fixed throughout the life of the option.

### Expiration Date
The [expiration date](../e/expiration_date.md) is the last day on which the option can be exercised. After this date, the option becomes worthless.

### Premium
The [premium](../p/premium.md) is the price paid by the option buyer to the option seller for the rights conveyed by the option. This is determined by various factors including the current price of the [underlying asset](../u/underlying_asset.md), the [strike price](../s/strike_price.md), time to expiration, and [market](../m/market.md) [volatility](../v/volatility.md).

## Pricing Vanilla Options

Vanilla [options](../o/options.md) are typically priced using models such as the [Black-Scholes Model](../b/black-scholes_model.md), which takes into account several variables:

1. **Current Price of the [Underlying Asset](../u/underlying_asset.md)**: The [market price](../m/market_price.md) of the [asset](../a/asset.md).
2. **[Strike Price](../s/strike_price.md)**: The price at which the [asset](../a/asset.md) can be bought or sold.
3. **Time to Expiration**: The time remaining until the option expires.
4. **[Volatility](../v/volatility.md)**: The extent to which the [underlying asset](../u/underlying_asset.md) price is expected to fluctuate.
5. **[Risk](../r/risk.md)-Free [Interest Rate](../i/interest_rate.md)**: The [return](../r/return.md) on a [risk](../r/risk.md)-free investment, typically government bonds.
6. **Dividends**: Payments made by a company to its shareholders, relevant mainly for [options](../o/options.md) on individual [stocks](../s/stock.md).

## Basic Strategies Involving Vanilla Options

### 1. **Long Call**
- **Objective**: [Profit](../p/profit.md) from an increase in the [underlying asset](../u/underlying_asset.md)'s price.
- **[Risk](../r/risk.md)**: Limited to the [premium](../p/premium.md) paid.
- **Reward**: Potentially unlimited.

### 2. **Short Call**
- **Objective**: [Profit](../p/profit.md) from a decrease in the [underlying asset](../u/underlying_asset.md)'s price.
- **[Risk](../r/risk.md)**: Potentially unlimited as the [asset](../a/asset.md)'s price can theoretically rise indefinitely.
- **Reward**: Limited to the [premium](../p/premium.md) received.

### 3. **Long Put**
- **Objective**: [Profit](../p/profit.md) from a decrease in the [underlying asset](../u/underlying_asset.md)'s price.
- **[Risk](../r/risk.md)**: Limited to the [premium](../p/premium.md) paid.
- **Reward**: Limited to the [strike price](../s/strike_price.md) minus the [premium](../p/premium.md) paid (if the [asset](../a/asset.md) price falls to zero).

### 4. **Short Put**
- **Objective**: [Profit](../p/profit.md) from an increase or stabilization in the [underlying asset](../u/underlying_asset.md)'s price.
- **[Risk](../r/risk.md)**: Significant but limited to the [strike price](../s/strike_price.md) minus the [premium](../p/premium.md) received.
- **Reward**: Limited to the [premium](../p/premium.md) received.

## Greeks in Vanilla Options

The "[Greeks](../g/greeks.md)" are measures used to assess the risks and potential returns of [options](../o/options.md). They provide insights into how sensitive an option's price is to various factors. The primary [Greeks](../g/greeks.md) for vanilla [options](../o/options.md) include:

- **[Delta](../d/delta.md)**: Measures the sensitivity of the option's price to changes in the price of the [underlying asset](../u/underlying_asset.md). For a call, [delta](../d/delta.md) is positive; for a put, [delta](../d/delta.md) is negative.
- **[Gamma](../g/gamma.md)**: Measures the rate of change of [delta](../d/delta.md) over time or per unit movement in the [underlying asset](../u/underlying_asset.md)'s price.
- **[Theta](../t/theta.md)**: Measures the sensitivity of the option's price to the passage of time. It reflects the [time decay](../t/time_decay.md) of the option.
- **[Vega](../v/vega.md)**: Measures the sensitivity of the option's price to changes in the [volatility](../v/volatility.md) of the [underlying asset](../u/underlying_asset.md).
- **[Rho](../r/rho.md)**: Measures the sensitivity of the option's price to changes in the [risk](../r/risk.md)-free [interest rate](../i/interest_rate.md).

## Example of a Vanilla Option Trade

### Scenario: Buying a Call Option

- **[Underlying Asset](../u/underlying_asset.md)**: Stock XYZ
- **Current Price**: $100
- **[Strike Price](../s/strike_price.md)**: $105
- **[Expiration Date](../e/expiration_date.md)**: 3 months from today
- **[Premium](../p/premium.md)**: $2 per option

### Trade Actions and Outcomes

1. **Initiate the [Trade](../t/trade.md)**
   - You buy one [call option](../c/call_option.md) contract for Stock XYZ.
   - Total cost is $2 ([premium](../p/premium.md)) * 100 (number of [shares](../s/shares.md) per contract) = $200.

2. **Possible Outcomes at Expiration**
   - **Stock Price Rises to $115**:
     - You [exercise](../e/exercise.md) the option, buying 100 [shares](../s/shares.md) at $105 each.
     - Total cost = $10,500 (for 100 [shares](../s/shares.md)) + $200 ([premium](../p/premium.md)).
     - [Market value](../m/market_value.md) of [shares](../s/shares.md) = $11,500 (100 [shares](../s/shares.md) * $115).
     - [Profit](../p/profit.md) = $11,500 - $10,500 - $200 = $800.
   
   - **Stock Price Remains at $100**:
     - The option expires worthless.
     - Loss is the [premium](../p/premium.md) paid = $200.
   
   - **Stock Price Falls to $95**:
     - The option expires worthless.
     - Loss is the [premium](../p/premium.md) paid = $200.

### Scenario: Writing a Put Option

- **[Underlying Asset](../u/underlying_asset.md)**: Stock ABC
- **Current Price**: $50
- **[Strike Price](../s/strike_price.md)**: $45
- **[Expiration Date](../e/expiration_date.md)**: 2 months from today
- **[Premium](../p/premium.md)**: $1.50 per option

### Trade Actions and Outcomes

1. **Initiate the [Trade](../t/trade.md)**
   - You sell one [put option](../p/put.md) contract for Stock ABC.
   - Total [credit](../c/credit.md) received is $1.50 ([premium](../p/premium.md)) * 100 (number of [shares](../s/shares.md) per contract) = $150.

2. **Possible Outcomes at Expiration**
   - **Stock Price Falls to $40**:
     - The buyer exercises the option, and you must buy 100 [shares](../s/shares.md) at $45 each.
     - Total cost = $4,500 (for 100 [shares](../s/shares.md)).
     - [Market value](../m/market_value.md) of [shares](../s/shares.md) = $4,000 (100 [shares](../s/shares.md) * $40).
     - Loss = $500 - $150 ([premium](../p/premium.md) received) = $350.
   
   - **Stock Price Remains at $50**:
     - The option expires worthless.
     - [Gain](../g/gain.md) is the [premium](../p/premium.md) received = $150.
   
   - **Stock Price Rises to $55**:
     - The option expires worthless.
     - [Gain](../g/gain.md) is the [premium](../p/premium.md) received = $150.

## Platforms and Tools for Trading Vanilla Options

Various platforms provide tools and services for trading vanilla [options](../o/options.md). Here are a few notable ones:

- **[Interactive Brokers](../i/interactive_brokers.md) (IBKR)**:
  [Interactive Brokers](https://www.interactivebrokers.com)
  
  Offers a comprehensive platform for [options](../o/options.md) trading with advanced tools, low commissions, and extensive [market](../m/market.md) access.
  
- **TD [Ameritrade](../a/ameritrade.md)**:
  [TD Ameritrade](https://www.tdameritrade.com)
  
  Provides the thinkorswim [trading platform](../t/trading_platform.md), known for its analytical tools and educational resources.
  
- **[E*TRADE](../e/e_trade.md)**:
  [E*TRADE](https://www.etrade.com)
  
  User-friendly platform with [robust](../r/robust.md) features for [options](../o/options.md) trading, research tools, and dedicated support.
  
- **[Robinhood](../r/robinhood.md)**:
  [Robinhood](https://www.robinhood.com)
  
  Offers [commission](../c/commission.md)-free trading, including [options](../o/options.md), suitable for beginners and casual traders.

## Conclusion

Vanilla [options](../o/options.md) serve as a fundamental building block in the world of [options](../o/options.md) trading. Their straightforward and standardized nature makes them accessible to traders of varying experience levels. By understanding the key components, pricing mechanisms, strategies, and risks associated with vanilla [options](../o/options.md), traders can [leverage](../l/leverage.md) these instruments to achieve diverse financial objectives, from hedging against [risk](../r/risk.md) to speculating on [market](../m/market.md) movements.

For those looking to dive deeper into [options](../o/options.md) trading, it is recommended to explore educational resources, utilize [simulation](../s/simulation_in_trading.md) tools offered by trading platforms, and perhaps even consult with financial advisors to develop a well-rounded understanding and strategy tailored to individual financial goals and [risk tolerance](../r/risk_tolerance.md).