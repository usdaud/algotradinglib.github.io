# Options Put-Call Parity

[Options](../o/options.md) trading is a sophisticated financial domain that plays a critical role in the landscape of modern [finance](../f/finance.md). One of the foundational principles within [options](../o/options.md) trading is the concept of [put-call parity](../p/put-call_parity.md). This principle is crucial for traders and investors to understand as it presents an essential relationship between the prices of put and call [options](../o/options.md). In this detailed discussion, we [will](../w/will.md) delve into the mechanics of [put-call parity](../p/put-call_parity.md), its mathematical formulation, assumptions, implications, and real-world applications.

#### Basics of Options

Before diving into [put-call parity](../p/put-call_parity.md), it is essential to grasp the basics of [options](../o/options.md). [Options](../o/options.md) are financial [derivatives](../d/derivatives.md) that give the holder the right, but not the obligation, to buy (call [options](../o/options.md)) or sell ([put options](../p/put_options.md)) an [underlying asset](../u/underlying_asset.md) at a predetermined price ([strike price](../s/strike_price.md)) on or before a specified date ([expiration date](../e/expiration_date.md)).

##### Call Options

- **Definition**: A [call option](../c/call_option.md) gives the holder the right to buy the [underlying asset](../u/underlying_asset.md) at the [strike price](../s/strike_price.md).
- **Buyer’s Perspective**: The buyer of a [call option](../c/call_option.md) expects the [asset](../a/asset.md)’s price to rise.
- **Seller’s Perspective**: The seller ([writer](../w/writer.md)) of the [call option](../c/call_option.md) expects the [asset](../a/asset.md)’s price to stay below the [strike price](../s/strike_price.md).

##### Put Options

- **Definition**: A [put option](../p/put.md) gives the holder the right to sell the [underlying asset](../u/underlying_asset.md) at the [strike price](../s/strike_price.md).
- **Buyer’s Perspective**: The buyer of a [put option](../p/put.md) expects the [asset](../a/asset.md)’s price to fall.
- **Seller’s Perspective**: The seller ([writer](../w/writer.md)) of the [put option](../p/put.md) expects the [asset](../a/asset.md)’s price to stay above the [strike price](../s/strike_price.md).

#### What Is Put-Call Parity?

[Put-call parity](../p/put-call_parity.md) is a financial principle that defines the relationship between the prices of European put and call [options](../o/options.md) with the same [underlying asset](../u/underlying_asset.md), [strike price](../s/strike_price.md), and [expiration date](../e/expiration_date.md). It is based on [arbitrage](../a/arbitrage.md)-free pricing and ensures that no [arbitrage](../a/arbitrage.md) opportunity exists in a balanced [market](../m/market.md).

#### Mathematical Formulation

The [put-call parity](../p/put-call_parity.md) relationship can be expressed mathematically as follows:

\[ C - P = S - K e^{-r(T-t)} \]

Where:
- \( C \) = Price of the European [call option](../c/call_option.md)
- \( P \) = Price of the European [put option](../p/put.md)
- \( S \) = Current price of the [underlying asset](../u/underlying_asset.md)
- \( K \) = [Strike price](../s/strike_price.md) of the [options](../o/options.md)
- \( r \) = [Risk](../r/risk.md)-free [interest rate](../i/interest_rate.md)
- \( T \) = [Expiration date](../e/expiration_date.md) of the [options](../o/options.md)
- \( t \) = Current time

This equation states that the difference between the price of a [call option](../c/call_option.md) and a [put option](../p/put.md) (with the same [strike price](../s/strike_price.md) and [expiration date](../e/expiration_date.md)) is equal to the current price of the [underlying asset](../u/underlying_asset.md) minus the [present value](../p/present_value.md) of the [strike price](../s/strike_price.md) discounted at the [risk](../r/risk.md)-free rate.

#### Assumptions Behind Put-Call Parity

For [put-call parity](../p/put-call_parity.md) to [hold](../h/hold.md), several key assumptions must be satisfied:

1. **European-style [Options](../o/options.md)**: The [options](../o/options.md) must be European-style, meaning they can only be exercised at expiration.
2. **Same [Strike Price](../s/strike_price.md) and [Expiration Date](../e/expiration_date.md)**: The put and call [options](../o/options.md) must have the same [strike price](../s/strike_price.md) and [expiration date](../e/expiration_date.md).
3. **[Arbitrage](../a/arbitrage.md) Opportunities**: Markets are assumed to be free from [arbitrage](../a/arbitrage.md) opportunities.
4. **[Interest](../i/interest.md) Rates**: The [risk](../r/risk.md)-free [interest rate](../i/interest_rate.md) is known and constant over the option’s life.
5. **No Dividends**: The [underlying asset](../u/underlying_asset.md) does not pay dividends during the option’s life.

#### Implications of Put-Call Parity

[Put-call parity](../p/put-call_parity.md) has several critical implications for [options](../o/options.md) trading and [financial markets](../f/financial_market.md):

##### Arbitrage Opportunities

If [put-call parity](../p/put-call_parity.md) is violated, arbitrageurs can exploit the price discrepancy to make a [risk](../r/risk.md)-free [profit](../p/profit.md). [Arbitrage](../a/arbitrage.md) mechanisms involve buying [undervalued](../u/undervalued.md) assets and selling [overvalued](../o/overvalued.md) ones, thus ensuring that prices eventually align with the [put-call parity](../p/put-call_parity.md) relationship.

##### Pricing Consistency

[Put-call parity](../p/put-call_parity.md) helps maintain consistency in the pricing of put and call [options](../o/options.md). If the prices deviate from the [parity](../p/parity.md) relationship, traders can employ various [arbitrage](../a/arbitrage.md) strategies to bring them back in line, thus ensuring the integrity of the [options](../o/options.md) [market](../m/market.md).

#### Real-World Applications

[Put-call parity](../p/put-call_parity.md) is not just a theoretical concept but has practical applications in the real world. Some of the notable applications include:

##### Hedging Strategies

Traders and investors use [put-call parity](../p/put-call_parity.md) to construct synthetic positions. For instance, a synthetically created long call can be achieved by holding a [long put](../l/long_put.md), the [underlying asset](../u/underlying_asset.md), and borrowing at the [risk](../r/risk.md)-free rate. Similarly, synthetic put positions can be established using call [options](../o/options.md) and the [underlying asset](../u/underlying_asset.md).

##### Options Pricing Models

[Put-call parity](../p/put-call_parity.md) serves as a foundational block in the development of more complex [options](../o/options.md) pricing models, notably the [Black-Scholes model](../b/black-scholes_model.md). Understanding [put-call parity](../p/put-call_parity.md) helps in comprehending how different parameters affect option prices.

##### Risk Management

Financial institutions and large trading desks use [put-call parity](../p/put-call_parity.md) to manage [risk](../r/risk.md). By understanding this relationship, traders can devise strategies to [hedge](../h/hedge.md) against potential losses arising from adverse price movements in the [underlying asset](../u/underlying_asset.md).

#### Example Calculation of Put-Call Parity

Let’s consider a practical example to illustrate how [put-call parity](../p/put-call_parity.md) works. Assume the following details:
- Current stock price (\( S \)): $100
- [Strike price](../s/strike_price.md) (\( K \)): $105
- [Risk](../r/risk.md)-free rate (\( r \)): 5% annually
- Time to expiration (\( T-t \)): 1 year
- Price of the European [call option](../c/call_option.md) (\( C \)): $10

Using the [put-call parity](../p/put-call_parity.md) formula:

\[ C - P = S - K e^{-r(T-t)} \]

\[ 10 - P = 100 - 105 e^{-0.05 \cdot 1} \]

Calculate the [present value](../p/present_value.md) of the [strike price](../s/strike_price.md):

\[ 105 e^{-0.05} ≈ 105 e^{-0.05} ≈ 105 \cdot 0.9512 ≈ 99.88 \]

[Substitute](../s/substitute.md) back into the equation:

\[ 10 - P = 100 - 99.88 \]

\[ 10 - P = 0.12 \]

\[ P = 10 - 0.12 \]

\[ P = 9.88 \]

Thus, the price of the European [put option](../p/put.md) should be $9.88 to satisfy the [put-call parity](../p/put-call_parity.md) relationship.

#### Conclusion

[Put-call parity](../p/put-call_parity.md) is a cornerstone principle in [options](../o/options.md) trading, providing a clear and consistent relationship between the prices of put and call [options](../o/options.md) with corresponding strike prices and expiration dates. It emerges from the foundational economic principle of no [arbitrage](../a/arbitrage.md) and plays a pivotal role in ensuring the integrity and [efficiency](../e/efficiency.md) of [financial markets](../f/financial_market.md). Understanding [put-call parity](../p/put-call_parity.md) enables traders and investors to [leverage](../l/leverage.md) [arbitrage](../a/arbitrage.md) opportunities, devise [hedging strategies](../h/hedging_strategies.md), and build a deeper appreciation of [options](../o/options.md) pricing mechanisms. By grasping the nuances of [put-call parity](../p/put-call_parity.md), [market](../m/market.md) participants can enhance their trading acumen and [risk management](../r/risk_management.md) capabilities in the complex world of [options](../o/options.md) trading.
