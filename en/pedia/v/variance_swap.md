# Variance Swap

A variance [swap](../s/swap.md) is a type of [derivative](../d/derivative.md) [financial instrument](../f/financial_instrument.md) that allows investors to [trade](../t/trade.md) future realized (or actual) [volatility](../v/volatility.md) against current implied [volatility](../v/volatility.md). Unlike traditional [options](../o/options.md), which can also be used to speculate on or [hedge](../h/hedge.md) against [volatility](../v/volatility.md), variance swaps provide a pure exposure to [volatility](../v/volatility.md) by isolating and betting directly on the realized variance of an [asset](../a/asset.md)'s returns over a specified period.

## Key Concepts and Terminology

### 1. **Realized Variance and Volatility**
- **Realized Variance:** The actual variance of a [financial instrument](../f/financial_instrument.md)'s returns over a given period. It is calculated as the average of the squared returns, typically annualized.
- **[Realized Volatility](../r/realized_volatility.md):** Often more intuitive for [market](../m/market.md) participants, [realized volatility](../r/realized_volatility.md) is the square root of the realized variance. It is typically expressed in annualized terms and reflects the degree of variation in an [asset](../a/asset.md)'s returns over time.

### 2. **Implied Volatility**
- Implied [volatility](../v/volatility.md) is an estimate of the future [volatility](../v/volatility.md) of an [asset](../a/asset.md)'s [return](../r/return.md) as implied by the price of its [options](../o/options.md). It represents the [market](../m/market.md)'s forecast of a likely movement in the [asset](../a/asset.md)'s price and is an essential input in the pricing of [options](../o/options.md).

### 3. **Variance Swap Structure**
- **[Strike Price](../s/strike_price.md) (Kvar):** The fixed [volatility](../v/volatility.md) level agreed upon by both parties in the [swap](../s/swap.md) contract.
- **Variance Notional (Nvar):** The amount used to determine the payoff. It can be seen as a scaling [factor](../f/factor.md), which determines the financial size of the [swap](../s/swap.md).
- **Settlement:** At [maturity](../m/maturity.md), the variance [swap](../s/swap.md) is settled in cash. The payoff to the long party (buyer) is calculated by comparing the realized variance to the [strike price](../s/strike_price.md) and scaling it by the variance notional.

### 4. **Payoff Structure**
The payoff for a variance [swap](../s/swap.md) at [maturity](../m/maturity.md) can be expressed mathematically as:

\[
\text{Payoff} = N_{var} \times (\text{Realized Variance} - K_{var})
\]

or, more formally,

\[
\text{Payoff} = N_{var} \times \left( \frac{252}{n} \sum_{i=1}^{n} \left( \ln \frac{S_i}{S_{i-1}} \right)^2 - K_{var} \right)
\]

where:
- \( S_i \) denotes the [asset](../a/asset.md) price at day \( i \),
- \( n \) is the total number of trading days over the [swap](../s/swap.md) period,
- 252 is the typical number of trading days in a year used to [annualize](../a/annualize.md) the variance.

## Applications of Variance Swaps

Variance swaps are versatile tools employed by various [market](../m/market.md) participants for different purposes:

### 1. **Hedging**
Investors use variance swaps to [hedge](../h/hedge.md) against unexpected spikes in [volatility](../v/volatility.md). For example, portfolio managers might use variance swaps to protect their portfolios from adverse price movements due to sudden increases in [market](../m/market.md) [volatility](../v/volatility.md).

### 2. **Speculation**
Traders can speculate on changes in [market](../m/market.md) [volatility](../v/volatility.md) by taking a position in variance swaps. If a [trader](../t/trader.md) anticipates an increase in [volatility](../v/volatility.md), they might buy a variance [swap](../s/swap.md), benefitting from the subsequent realized variance exceeding the [strike price](../s/strike_price.md).

### 3. **Arbitrage**
Arbitrageurs can exploit mispricings between variance swaps and other [volatility](../v/volatility.md) instruments such as [options](../o/options.md). By constructing complex strategies, they can lock in [risk](../r/risk.md)-free profits from discrepancies in the pricing of realized and implied [volatility](../v/volatility.md).

## Pricing and Valuation
The pricing of variance swaps hinges on the relationship between implied and [realized volatility](../r/realized_volatility.md). The [value](../v/value.md) at the inception of the [swap](../s/swap.md) (when no [volatility](../v/volatility.md) has been realized yet) is typically zero, meaning the [strike price](../s/strike_price.md) is set so that the expected payoff is zero for both parties. However, ongoing [valuation](../v/valuation.md) of an existing variance [swap](../s/swap.md) involves:

### 1. **Replication via Options**
A variance [swap](../s/swap.md) can be synthetically replicated using a portfolio of [options](../o/options.md). This portfolio typically consists of a strip of European-style calls and puts across various strikes. The key is to [hold](../h/hold.md) a [delta](../d/delta.md)-[neutral](../n/neutral.md) (insensitive to small price changes) position that captures the changes in variance.

### 2. **Numerical Methods**
When analytical solutions are impractical, numerical techniques such as Monte Carlo simulations or [finite difference methods](../f/finite_difference_methods.md) may be employed to estimate the [fair value](../f/fair_value.md) of a variance [swap](../s/swap.md).

## Variance Swaps vs. Volatility Swaps
While the terms might be used interchangeably, variance swaps and [volatility](../v/volatility.md) swaps have distinct differences:

- **Variance Swaps:** The payoff depends on the squared returns, making it sensitive to extreme price movements (large deviations contribute more to the realized variance).
- **[Volatility](../v/volatility.md) Swaps:** The payoff depends on the [realized volatility](../r/realized_volatility.md) (the square root of variance), [offering](../o/offering.md) a more direct [hedge](../h/hedge.md) against [volatility](../v/volatility.md) and typically more intuitive for traders.

## Examples of Market Use

### 1. **Equity Markets**
In [equity](../e/equity.md) markets, variance swaps are often used to [trade](../t/trade.md) the [volatility](../v/volatility.md) of stock indices like the S&P 500 or [Euro](../e/euro.md) Stoxx 50.

### 2. **Commodity Markets**
[Commodity](../c/commodity.md) traders utilize variance swaps to [hedge](../h/hedge.md) against or speculate on [volatility](../v/volatility.md) in markets like [crude oil](../c/crude_oil.md) or gold.

### 3. **Foreign Exchange (Forex) Markets**
Variance swaps in forex markets cater to [volatility](../v/volatility.md) trading in [currency](../c/currency.md) pairs, providing a mechanism to [hedge](../h/hedge.md) against or speculate on the [volatility](../v/volatility.md) of [currency](../c/currency.md) exchanges.

## Risk Management
While variance swaps [offer](../o/offer.md) unique advantages for [volatility](../v/volatility.md) trading, they also carry distinct risks:

### 1. **Model Risk**
Pricing and hedging variance swaps require sophisticated models. Inaccuracies in these models can result in significant financial losses.

### 2. **Liquidity Risk**
The variance [swap](../s/swap.md) [market](../m/market.md) can be less [liquid](../l/liquid.md) compared to traditional [options](../o/options.md) markets. Thin trading volumes can lead to substantial [bid](../b/bid.md)-ask [spreads](../s/spreads.md) and [slippage](../s/slippage.md).

### 3. **Counterparty Risk**
As with any [derivative](../d/derivative.md) contract, there is the [risk](../r/risk.md) that one party may [default](../d/default.md). [Market](../m/market.md) participants must assess the [creditworthiness](../c/creditworthiness.md) of counterparties and potentially use [collateral](../c/collateral.md) arrangements to mitigate this [risk](../r/risk.md).

## Variance Swap Markets and Providers

Several financial institutions and trading firms [offer](../o/offer.md) variance [swap](../s/swap.md) products to their clients. Notable players in this space include:

### 1. **Goldman Sachs**
Goldman Sachs provides variance swaps as part of its suite of [equity](../e/equity.md) [derivatives](../d/derivatives.md) and structured products. The [firm](../f/firm.md) leverages its [market](../m/market.md)-making and [risk management](../r/risk_management.md) expertise to facilitate these trades.
[Goldman Sachs Equity Derivatives](https://www.goldmansachs.com/what-we-do/securities/equity-derivatives/)

### 2. **J.P. Morgan**
J.P. Morgan offers customized variance [swap](../s/swap.md) solutions, allowing clients to align their [volatility](../v/volatility.md) expectations with structured products tailored to specific [market](../m/market.md) views.
[J.P. Morgan Equities & Equity Derivatives](https://www.jpmorgan.com/global/markets/equity-derivatives)

### 3. **Morgan Stanley**
Morgan Stanley's [equity derivative](../e/equity_derivative.md) operations include variance swaps, providing clients with strategic [volatility](../v/volatility.md) exposure and hedging tools.
[Morgan Stanley Equity Derivatives](https://www.morganstanley.com/im/en-us/capital-securities-strategies/equity/index.html)

### 4. **Barclays**
Barclays facilitates variance swaps through its [equity](../e/equity.md) [derivatives](../d/derivatives.md) platform, enabling seamless [execution](../e/execution.md) and innovative [volatility](../v/volatility.md) [trading strategies](../t/trading_strategies.md).
[Barclays Markets & Research - Equity Derivatives](https://www.cib.barclays/markets/equity-derivatives/)

In conclusion, variance swaps represent a sophisticated tool for trading and managing [volatility risk](../v/volatility_risk.md). They [offer](../o/offer.md) [market](../m/market.md) participants a direct and efficient way to [gain](../g/gain.md) exposure to or [hedge](../h/hedge.md) against changes in realized variance, distinct from traditional option-based strategies. As with any [financial instrument](../f/financial_instrument.md), a thorough understanding of their features, applications, and risks is essential for effective utilization.