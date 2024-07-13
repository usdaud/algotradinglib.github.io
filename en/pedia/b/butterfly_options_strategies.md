# Butterfly Options Strategies

Butterfly [Options](../o/options.md) Strategies are a set of advanced [options trading strategies](../o/options_trading_strategies.md) that involve [multiple](../m/multiple.md) legs (contracts) aimed at exploiting different [market](../m/market.md) scenarios, typically with limited [risk](../r/risk.md) and controlled [profit](../p/profit.md) potential. The primary allure of these strategies is their capacity to allow traders to [profit](../p/profit.md) from a [range](../r/range.md) of [market](../m/market.md) conditions—whether the [market](../m/market.md) is moving up, down, or staying [neutral](../n/neutral.md). In this guide, we [will](../w/will.md) dive deep into the various types of butterfly [options](../o/options.md) strategies, their construction, suitability, and practical applications.

### Types of Butterfly Options Strategies

1. **Long Call [Butterfly Spread](../b/butterfly_spread.md)**
2. **[Long Put](../l/long_put.md) [Butterfly Spread](../b/butterfly_spread.md)**
3. **Iron [Butterfly Spread](../b/butterfly_spread.md)**
4. **[Iron Condor](../i/iron_condor.md) Spread**

### 1. Long Call Butterfly Spread

#### Definition
A Long Call [Butterfly Spread](../b/butterfly_spread.md) is a [neutral](../n/neutral.md) [options](../o/options.md) strategy combining [bull](../b/bull.md) and bear [spreads](../s/spreads.md) with the same [expiration date](../e/expiration_date.md). It involves buying one [call option](../c/call_option.md) at a lower [strike price](../s/strike_price.md), selling two call [options](../o/options.md) at a middle [strike price](../s/strike_price.md), and buying one [call option](../c/call_option.md) at a higher [strike price](../s/strike_price.md).

#### Construction
- **Buy 1 ITM (In-The-[Money](../m/money.md)) [Call Option](../c/call_option.md) ([Strike Price](../s/strike_price.md) X)**
- **Sell 2 ATM (At-The-[Money](../m/money.md)) Call [Options](../o/options.md) ([Strike Price](../s/strike_price.md) Y)**
- **Buy 1 OTM (Out-The-[Money](../m/money.md)) [Call Option](../c/call_option.md) ([Strike Price](../s/strike_price.md) Z)**

Here, the strike prices follow the relation: \( X < Y < Z \).

#### Example
If a stock is trading at $100, you could:
- Buy 1 [call option](../c/call_option.md) at $90 [strike price](../s/strike_price.md)
- Sell 2 call [options](../o/options.md) at $100 [strike price](../s/strike_price.md)
- Buy 1 [call option](../c/call_option.md) at $110 [strike price](../s/strike_price.md)

#### Payoff
The maximum [profit](../p/profit.md) is attained when the stock price at expiration is equal to the middle [strike price](../s/strike_price.md) (Y). The maximum loss is limited to the initial net [debit](../d/debit.md) (the cost to enter the [trade](../t/trade.md)).

#### Suitability
This strategy is ideal in a low-[volatility](../v/volatility.md) environment where the [trader](../t/trader.md) expects the stock to stay around the middle [strike price](../s/strike_price.md) at expiration. 

### 2. Long Put Butterfly Spread

#### Definition
A [Long Put](../l/long_put.md) [Butterfly Spread](../b/butterfly_spread.md) is a [neutral](../n/neutral.md) strategy consisting of three different [put options](../p/put_options.md) with the same expiration but different strike prices. It involves buying one [put option](../p/put.md) at a higher [strike price](../s/strike_price.md), selling two puts at a middle [strike price](../s/strike_price.md), and buying one [put option](../p/put.md) at a lower [strike price](../s/strike_price.md).

#### Construction
- **Buy 1 ITM [Put Option](../p/put.md) ([Strike Price](../s/strike_price.md) Z)**
- **Sell 2 ATM [Put Options](../p/put_options.md) ([Strike Price](../s/strike_price.md) Y)**
- **Buy 1 OTM [Put Option](../p/put.md) ([Strike Price](../s/strike_price.md) X)**

Here, the strike prices follow the relation: \( X < Y < Z \).

#### Example
If a stock is trading at $100, you could:
- Buy 1 [put option](../p/put.md) at $110 [strike price](../s/strike_price.md)
- Sell 2 [put options](../p/put_options.md) at $100 [strike price](../s/strike_price.md)
- Buy 1 [put option](../p/put.md) at $90 [strike price](../s/strike_price.md)

#### Payoff
Similar to the Long Call [Butterfly Spread](../b/butterfly_spread.md), the maximum [profit](../p/profit.md) is achieved when the stock price is at the middle [strike price](../s/strike_price.md) (Y). The maximum loss is limited to the initial cost to enter the [trade](../t/trade.md).

#### Suitability
This strategy is also best used in a low-[volatility](../v/volatility.md) environment where the [trader](../t/trader.md) expects the stock price to hover around the middle [strike price](../s/strike_price.md).

### 3. Iron Butterfly Spread

#### Definition
An Iron [Butterfly Spread](../b/butterfly_spread.md) is a limited [risk](../r/risk.md), limited [profit](../p/profit.md) [options](../o/options.md) strategy that offers benefits in sideways markets. It combines a [bear call spread](../b/bear_call_spread.md) and a [bull put spread](../b/bull_put_spread.md) with the same expiry.

#### Construction
- **Sell 1 ATM [Call Option](../c/call_option.md) ([Strike Price](../s/strike_price.md) Y)**
- **Buy 1 OTM [Call Option](../c/call_option.md) ([Strike Price](../s/strike_price.md) Z)**
- **Sell 1 ATM [Put Option](../p/put.md) ([Strike Price](../s/strike_price.md) Y)**
- **Buy 1 OTM [Put Option](../p/put.md) ([Strike Price](../s/strike_price.md) X)**

Here, the strike prices are: \( X < Y < Z \).

#### Example
If a stock is trading at $100, you could:
- Sell 1 [call option](../c/call_option.md) at $100 [strike price](../s/strike_price.md)
- Buy 1 [call option](../c/call_option.md) at $110 [strike price](../s/strike_price.md)
- Sell 1 [put option](../p/put.md) at $100 [strike price](../s/strike_price.md)
- Buy 1 [put option](../p/put.md) at $90 [strike price](../s/strike_price.md)

#### Payoff
The maximum [profit](../p/profit.md) is realized when the stock price at expiration is equal to the middle [strike price](../s/strike_price.md) (Y). The maximum loss is limited to the difference between the lower and middle strike prices minus the net [credit](../c/credit.md) received.

#### Suitability
The [Iron Butterfly](../i/iron_butterfly.md) is ideal when the [trader](../t/trader.md) expects minimal price movement in the stock. It is also popular for its limited [risk](../r/risk.md) and limited reward structure.

### 4. Iron Condor Spread

#### Definition
An [Iron Condor](../i/iron_condor.md) Spread is a non-directional [options](../o/options.md) strategy that has a higher probability of making a smaller, limited [profit](../p/profit.md) when the [underlying](../u/underlying.md) stock price trades in a narrow [range](../r/range.md). It is a combination of a [bear call spread](../b/bear_call_spread.md) and a [bull put spread](../b/bull_put_spread.md) with different expiry dates compared to the [Iron Butterfly](../i/iron_butterfly.md).

#### Construction
- **Sell 1 OTM [Call Option](../c/call_option.md) ([Strike Price](../s/strike_price.md) Z)**
- **Buy 1 Higher OTM [Call Option](../c/call_option.md) ([Strike Price](../s/strike_price.md) W)**
- **Sell 1 OTM [Put Option](../p/put.md) ([Strike Price](../s/strike_price.md) Y)**
- **Buy 1 Lower OTM [Put Option](../p/put.md) ([Strike Price](../s/strike_price.md) X)**

Here, the strike prices follow the relation: \( X < Y < Z < W \).

#### Example
If a stock is trading at $100, you could:
- Sell 1 [call option](../c/call_option.md) at $110 [strike price](../s/strike_price.md)
- Buy 1 [call option](../c/call_option.md) at $120 [strike price](../s/strike_price.md)
- Sell 1 [put option](../p/put.md) at $90 [strike price](../s/strike_price.md)
- Buy 1 [put option](../p/put.md) at $80 [strike price](../s/strike_price.md)

#### Payoff
The maximum [profit](../p/profit.md) is achieved when the stock price remains between the inner strike prices (Y and Z) at expiry. The maximum loss is limited to the difference between the strike prices minus the net [credit](../c/credit.md) received.

#### Suitability
The [Iron Condor](../i/iron_condor.md) is preferable in a low [volatility](../v/volatility.md) environment where the [trader](../t/trader.md) expects the stock to remain within a specific [range](../r/range.md). It is well-liked due to its high probability of earning a limited [profit](../p/profit.md) and the bounded [risk](../r/risk.md).

### Practical Applications

Butterfly [Options](../o/options.md) Strategies are widely used by traders and [hedge](../h/hedge.md) funds to manage [risk](../r/risk.md) and maximize profits. For instance, the [hedge fund](../h/hedge_fund.md) **Two Sigma Investments** (https://www.twosigma.com/) employs advanced [quantitative strategies](../q/quantitative_strategies_in_trading.md) that may include varied [options trading strategies](../o/options_trading_strategies.md) such as butterflies to optimize their portfolios.

### Conclusion
Butterfly [Options](../o/options.md) Strategies [offer](../o/offer.md) a palette of low-[risk](../r/risk.md), high-control trading techniques suitable for different [market](../m/market.md) outlooks. While they appear complex, understanding their construction, risks, and payoffs can provide traders with powerful tools to enhance their [trading strategies](../t/trading_strategies.md) in both volatile and non-volatile markets. Careful planning and [execution](../e/execution.md) are key to leveraging these strategies optimally.