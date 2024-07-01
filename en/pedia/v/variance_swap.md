# Variance Swap

A variance swap is a type of derivative financial instrument that allows investors to trade future realized (or actual) volatility against current implied volatility. Unlike traditional options, which can also be used to speculate on or hedge against volatility, variance swaps provide a pure exposure to volatility by isolating and betting directly on the realized variance of an asset's returns over a specified period.

## Key Concepts and Terminology

### 1. **Realized Variance and Volatility**
- **Realized Variance:** The actual variance of a financial instrument's returns over a given period. It is calculated as the average of the squared returns, typically annualized.
- **[Realized Volatility](../r/realized_volatility.md):** Often more intuitive for market participants, [realized volatility](../r/realized_volatility.md) is the square root of the realized variance. It is typically expressed in annualized terms and reflects the degree of variation in an asset's returns over time.

### 2. **Implied Volatility**
- Implied volatility is an estimate of the future volatility of an asset's return as implied by the price of its options. It represents the market's forecast of a likely movement in the asset's price and is an essential input in the pricing of options.

### 3. **Variance Swap Structure**
- **Strike Price (Kvar):** The fixed volatility level agreed upon by both parties in the swap contract.
- **Variance Notional (Nvar):** The amount used to determine the payoff. It can be seen as a scaling factor, which determines the financial size of the swap.
- **Settlement:** At maturity, the variance swap is settled in cash. The payoff to the long party (buyer) is calculated by comparing the realized variance to the strike price and scaling it by the variance notional.

### 4. **Payoff Structure**
The payoff for a variance swap at maturity can be expressed mathematically as:

\[
\text{Payoff} = N_{var} \times (\text{Realized Variance} - K_{var})
\]

or, more formally,

\[
\text{Payoff} = N_{var} \times \left( \frac{252}{n} \sum_{i=1}^{n} \left( \ln \frac{S_i}{S_{i-1}} \right)^2 - K_{var} \right)
\]

where:
- \( S_i \) denotes the asset price at day \( i \),
- \( n \) is the total number of trading days over the swap period,
- 252 is the typical number of trading days in a year used to annualize the variance.

## Applications of Variance Swaps

Variance swaps are versatile tools employed by various market participants for different purposes:

### 1. **Hedging**
Investors use variance swaps to hedge against unexpected spikes in volatility. For example, portfolio managers might use variance swaps to protect their portfolios from adverse price movements due to sudden increases in market volatility.

### 2. **Speculation**
Traders can speculate on changes in market volatility by taking a position in variance swaps. If a trader anticipates an increase in volatility, they might buy a variance swap, benefitting from the subsequent realized variance exceeding the strike price.

### 3. **Arbitrage**
Arbitrageurs can exploit mispricings between variance swaps and other volatility instruments such as options. By constructing complex strategies, they can lock in risk-free profits from discrepancies in the pricing of realized and implied volatility.

## Pricing and Valuation
The pricing of variance swaps hinges on the relationship between implied and [realized volatility](../r/realized_volatility.md). The value at the inception of the swap (when no volatility has been realized yet) is typically zero, meaning the strike price is set so that the expected payoff is zero for both parties. However, ongoing valuation of an existing variance swap involves:

### 1. **Replication via Options**
A variance swap can be synthetically replicated using a portfolio of options. This portfolio typically consists of a strip of European-style calls and puts across various strikes. The key is to hold a delta-neutral (insensitive to small price changes) position that captures the changes in variance.

### 2. **Numerical Methods**
When analytical solutions are impractical, numerical techniques such as Monte Carlo simulations or [finite difference methods](../f/finite_difference_methods.md) may be employed to estimate the fair value of a variance swap.

## Variance Swaps vs. Volatility Swaps
While the terms might be used interchangeably, variance swaps and volatility swaps have distinct differences:

- **Variance Swaps:** The payoff depends on the squared returns, making it sensitive to extreme price movements (large deviations contribute more to the realized variance).
- **Volatility Swaps:** The payoff depends on the [realized volatility](../r/realized_volatility.md) (the square root of variance), offering a more direct hedge against volatility and typically more intuitive for traders.

## Examples of Market Use

### 1. **Equity Markets**
In equity markets, variance swaps are often used to trade the volatility of stock indices like the S&P 500 or Euro Stoxx 50.

### 2. **Commodity Markets**
Commodity traders utilize variance swaps to hedge against or speculate on volatility in markets like crude oil or gold.

### 3. **Foreign Exchange (Forex) Markets**
Variance swaps in forex markets cater to volatility trading in currency pairs, providing a mechanism to hedge against or speculate on the volatility of currency exchanges.

## Risk Management
While variance swaps offer unique advantages for volatility trading, they also carry distinct risks:

### 1. **Model Risk**
Pricing and hedging variance swaps require sophisticated models. Inaccuracies in these models can result in significant financial losses.

### 2. **Liquidity Risk**
The variance swap market can be less liquid compared to traditional options markets. Thin trading volumes can lead to substantial bid-ask spreads and slippage.

### 3. **Counterparty Risk**
As with any derivative contract, there is the risk that one party may default. Market participants must assess the creditworthiness of counterparties and potentially use collateral arrangements to mitigate this risk.

## Variance Swap Markets and Providers

Several financial institutions and trading firms offer variance swap products to their clients. Notable players in this space include:

### 1. **Goldman Sachs**
Goldman Sachs provides variance swaps as part of its suite of equity [derivatives](../d/derivatives.md) and structured products. The firm leverages its market-making and [risk management](../r/risk_management.md) expertise to facilitate these trades.
[Goldman Sachs Equity Derivatives](https://www.goldmansachs.com/what-we-do/securities/equity-derivatives/)

### 2. **J.P. Morgan**
J.P. Morgan offers customized variance swap solutions, allowing clients to align their volatility expectations with structured products tailored to specific market views.
[J.P. Morgan Equities & Equity Derivatives](https://www.jpmorgan.com/global/markets/equity-derivatives)

### 3. **Morgan Stanley**
Morgan Stanley's equity derivative operations include variance swaps, providing clients with strategic volatility exposure and hedging tools.
[Morgan Stanley Equity Derivatives](https://www.morganstanley.com/im/en-us/capital-securities-strategies/equity/index.html)

### 4. **Barclays**
Barclays facilitates variance swaps through its equity [derivatives](../d/derivatives.md) platform, enabling seamless execution and innovative volatility [trading strategies](../t/trading_strategies.md).
[Barclays Markets & Research - Equity Derivatives](https://www.cib.barclays/markets/equity-derivatives/)

In conclusion, variance swaps represent a sophisticated tool for trading and managing [volatility risk](../v/volatility_risk.md). They offer market participants a direct and efficient way to gain exposure to or hedge against changes in realized variance, distinct from traditional option-based strategies. As with any financial instrument, a thorough understanding of their features, applications, and risks is essential for effective utilization.