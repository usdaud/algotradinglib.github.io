# Butterfly Options Strategies

Butterfly Options Strategies are a set of advanced options trading strategies that involve multiple legs (contracts) aimed at exploiting different market scenarios, typically with limited risk and controlled profit potential. The primary allure of these strategies is their capacity to allow traders to profit from a range of market conditions—whether the market is moving up, down, or staying neutral. In this guide, we will dive deep into the various types of butterfly options strategies, their construction, suitability, and practical applications.

### Types of Butterfly Options Strategies

1. **Long Call [Butterfly Spread](../b/butterfly_spread.md)**
2. **Long Put [Butterfly Spread](../b/butterfly_spread.md)**
3. **Iron [Butterfly Spread](../b/butterfly_spread.md)**
4. **[Iron Condor](../i/iron_condor.md) Spread**

### 1. Long Call Butterfly Spread

#### Definition
A Long Call [Butterfly Spread](../b/butterfly_spread.md) is a neutral options strategy combining bull and bear spreads with the same expiration date. It involves buying one call option at a lower strike price, selling two call options at a middle strike price, and buying one call option at a higher strike price.

#### Construction
- **Buy 1 ITM (In-The-Money) Call Option (Strike Price X)**
- **Sell 2 ATM (At-The-Money) Call Options (Strike Price Y)**
- **Buy 1 OTM (Out-The-Money) Call Option (Strike Price Z)**

Here, the strike prices follow the relation: \( X < Y < Z \).

#### Example
If a stock is trading at $100, you could:
- Buy 1 call option at $90 strike price
- Sell 2 call options at $100 strike price
- Buy 1 call option at $110 strike price

#### Payoff
The maximum profit is attained when the stock price at expiration is equal to the middle strike price (Y). The maximum loss is limited to the initial net debit (the cost to enter the trade).

#### Suitability
This strategy is ideal in a low-volatility environment where the trader expects the stock to stay around the middle strike price at expiration. 

### 2. Long Put Butterfly Spread

#### Definition
A Long Put [Butterfly Spread](../b/butterfly_spread.md) is a neutral strategy consisting of three different [put options](../p/put_options.md) with the same expiration but different strike prices. It involves buying one put option at a higher strike price, selling two puts at a middle strike price, and buying one put option at a lower strike price.

#### Construction
- **Buy 1 ITM Put Option (Strike Price Z)**
- **Sell 2 ATM [Put Options](../p/put_options.md) (Strike Price Y)**
- **Buy 1 OTM Put Option (Strike Price X)**

Here, the strike prices follow the relation: \( X < Y < Z \).

#### Example
If a stock is trading at $100, you could:
- Buy 1 put option at $110 strike price
- Sell 2 [put options](../p/put_options.md) at $100 strike price
- Buy 1 put option at $90 strike price

#### Payoff
Similar to the Long Call [Butterfly Spread](../b/butterfly_spread.md), the maximum profit is achieved when the stock price is at the middle strike price (Y). The maximum loss is limited to the initial cost to enter the trade.

#### Suitability
This strategy is also best used in a low-volatility environment where the trader expects the stock price to hover around the middle strike price.

### 3. Iron Butterfly Spread

#### Definition
An Iron [Butterfly Spread](../b/butterfly_spread.md) is a limited risk, limited profit options strategy that offers benefits in sideways markets. It combines a [bear call spread](../b/bear_call_spread.md) and a [bull put spread](../b/bull_put_spread.md) with the same expiry.

#### Construction
- **Sell 1 ATM Call Option (Strike Price Y)**
- **Buy 1 OTM Call Option (Strike Price Z)**
- **Sell 1 ATM Put Option (Strike Price Y)**
- **Buy 1 OTM Put Option (Strike Price X)**

Here, the strike prices are: \( X < Y < Z \).

#### Example
If a stock is trading at $100, you could:
- Sell 1 call option at $100 strike price
- Buy 1 call option at $110 strike price
- Sell 1 put option at $100 strike price
- Buy 1 put option at $90 strike price

#### Payoff
The maximum profit is realized when the stock price at expiration is equal to the middle strike price (Y). The maximum loss is limited to the difference between the lower and middle strike prices minus the net credit received.

#### Suitability
The [Iron Butterfly](../i/iron_butterfly.md) is ideal when the trader expects minimal price movement in the stock. It is also popular for its limited risk and limited reward structure.

### 4. Iron Condor Spread

#### Definition
An [Iron Condor](../i/iron_condor.md) Spread is a non-directional options strategy that has a higher probability of making a smaller, limited profit when the underlying stock price trades in a narrow range. It is a combination of a [bear call spread](../b/bear_call_spread.md) and a [bull put spread](../b/bull_put_spread.md) with different expiry dates compared to the [Iron Butterfly](../i/iron_butterfly.md).

#### Construction
- **Sell 1 OTM Call Option (Strike Price Z)**
- **Buy 1 Higher OTM Call Option (Strike Price W)**
- **Sell 1 OTM Put Option (Strike Price Y)**
- **Buy 1 Lower OTM Put Option (Strike Price X)**

Here, the strike prices follow the relation: \( X < Y < Z < W \).

#### Example
If a stock is trading at $100, you could:
- Sell 1 call option at $110 strike price
- Buy 1 call option at $120 strike price
- Sell 1 put option at $90 strike price
- Buy 1 put option at $80 strike price

#### Payoff
The maximum profit is achieved when the stock price remains between the inner strike prices (Y and Z) at expiry. The maximum loss is limited to the difference between the strike prices minus the net credit received.

#### Suitability
The [Iron Condor](../i/iron_condor.md) is preferable in a low volatility environment where the trader expects the stock to remain within a specific range. It is well-liked due to its high probability of earning a limited profit and the bounded risk.

### Practical Applications

Butterfly Options Strategies are widely used by traders and hedge funds to manage risk and maximize profits. For instance, the hedge fund **Two Sigma Investments** (https://www.twosigma.com/) employs advanced quantitative strategies that may include varied [options trading strategies](../o/options_trading_strategies.md) such as butterflies to optimize their portfolios.

### Conclusion
Butterfly Options Strategies offer a palette of low-risk, high-control trading techniques suitable for different market outlooks. While they appear complex, understanding their construction, risks, and payoffs can provide traders with powerful tools to enhance their [trading strategies](../t/trading_strategies.md) in both volatile and non-volatile markets. Careful planning and execution are key to leveraging these strategies optimally.