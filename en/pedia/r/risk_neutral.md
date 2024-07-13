# Risk Neutral

In the [financial markets](../f/financial_market.md), the concept of "[Risk](../r/risk.md) [Neutral](../n/neutral.md)" or "[Risk](../r/risk.md)-[Neutral](../n/neutral.md)" plays a significant role in both theoretical and applied [finance](../f/finance.md), particularly in the [valuation](../v/valuation.md) of [derivatives](../d/derivatives.md). This concept simplifies the mathematical modeling of [asset](../a/asset.md) prices and allows for the streamlined computation of option prices using models such as the [Black-Scholes model](../b/black-scholes_model.md). A [risk](../r/risk.md)-[neutral](../n/neutral.md) measure can be considered as a probabilistic measure under which the [present value](../p/present_value.md) of all cash flows, when discounted at the [risk](../r/risk.md)-free rate, equals the current [market](../m/market.md) prices of the assets.

## Definition of Risk Neutral

"[Risk](../r/risk.md) [Neutral](../n/neutral.md)" refers to an attitude or a [market](../m/market.md) measure where the [investor](../i/investor.md) is indifferent to [risk](../r/risk.md) when making an investment decision. This means that the [investor](../i/investor.md) under a [risk](../r/risk.md)-[neutral](../n/neutral.md) perspective does not require extra compensation for taking additional [risk](../r/risk.md). Instead, they [value](../v/value.md) cash flows solely based on their expected values, discounted at the [risk](../r/risk.md)-free rate, without incorporating a [risk premium](../r/risk_premium.md).

## Risk-Neutral Measure

A [risk](../r/risk.md)-[neutral](../n/neutral.md) measure is a probability measure where the current price of any [asset](../a/asset.md) is equivalent to the expected [present value](../p/present_value.md) of future payoffs, discounted at the [risk-free rate of return](../r/risk-free_rate_of_return.md). Under this measure, all investors are assumed to be indifferent to [risk](../r/risk.md), focusing only on expected returns rather than the [variability](../v/variability.md) of those returns.

### Martingale Property

Under the [risk](../r/risk.md)-[neutral](../n/neutral.md) measure, discounted [asset](../a/asset.md) prices follow a [martingale process](../m/martingale_process.md). This means that the expected future price of the [asset](../a/asset.md), after [discounting](../d/discounting.md) by the [risk](../r/risk.md)-free rate, equals its current price. Mathematically, if \(S(t)\) is the price of an [asset](../a/asset.md) at time \(t\) and \(r\) is the [risk](../r/risk.md)-free rate, then under the [risk](../r/risk.md)-[neutral](../n/neutral.md) measure \(Q\):

\[ E_Q[S(t+1)e^{-r(t+1)} | \mathcal{F}_t] = S(t)e^{-rt} \]

This property is key in the [valuation](../v/valuation.md) of [derivative](../d/derivative.md) securities.

## Applications in Financial Models

### Black-Scholes Model

The [Black-Scholes model](../b/black-scholes_model.md), one of the most renowned models for option pricing, fundamentally relies on the concept of [risk](../r/risk.md) neutrality. When deriving the Black-Scholes formula, we assume that the [underlying asset](../u/underlying_asset.md) price follows a [geometric Brownian motion](../g/geometric_brownian_motion.md) under the [risk](../r/risk.md)-[neutral](../n/neutral.md) measure. This allows us to simplify the partial differential equation governing the [options](../o/options.md) price.

The Black-Scholes formula for a European [call option](../c/call_option.md) is given by:

\[ C = S_0 \Phi(d_1) - Ke^{-rT} \Phi(d_2) \]

Where:
- \(C\) = [Call option](../c/call_option.md) price
- \(S_0\) = Current price of the [underlying asset](../u/underlying_asset.md)
- \(K\) = [Strike price](../s/strike_price.md)
- \(r\) = [Risk](../r/risk.md)-free [interest rate](../i/interest_rate.md)
- \(T\) = Time to [maturity](../m/maturity.md)
- \(\Phi\) = [Cumulative distribution function](../c/cumulative_distribution_function_in_trading.md) of the standard [normal distribution](../n/normal_distribution_in_trading.md)
- \(d_1\) and \(d_2\) are given by:

\[ d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}} \]
\[ d_2 = d_1 - \sigma \sqrt{T} \]

### Risk-Neutral Probability Density Function

The [risk](../r/risk.md)-[neutral](../n/neutral.md) probability density function (PDF) of the [asset](../a/asset.md) price at a future date is used for the [valuation](../v/valuation.md) of various [exotic options](../e/exotic_option.md) and other complex [derivatives](../d/derivatives.md). This density function represents the [probability distribution](../p/probability_distribution.md) of possible future prices of the [asset](../a/asset.md) under the [risk](../r/risk.md)-[neutral](../n/neutral.md) measure.

### Girsanov Theorem

The Girsanov theorem is crucial in transforming the real-world measure to the [risk](../r/risk.md)-[neutral](../n/neutral.md) measure. This theorem states that under certain conditions, it is possible to change the probability measure such that the Brownian motion driving the [asset](../a/asset.md) prices under the original measure becomes a Brownian motion under the new measure, with a different drift term that reflects the [risk](../r/risk.md)-free rate instead of the original drift.

## Practical Implications for Trading and Finance

### Valuation of Derivatives

The primary implication of [risk](../r/risk.md)-[neutral](../n/neutral.md) [valuation](../v/valuation.md) is that it allows traders and analysts to price [derivatives](../d/derivatives.md) like [options](../o/options.md), [futures](../f/futures.md), and other contingent claims in a consistent and tractable manner. By using the [risk](../r/risk.md)-free rate as the [discount](../d/discount.md) [factor](../f/factor.md) and taking the [expected value](../e/expected_value.md) of future payoffs, the complexity arising from [risk](../r/risk.md) preferences is avoided.

### Hedging Strategies

[Hedging strategies](../h/hedging_strategies.md) often rely on the [risk](../r/risk.md)-[neutral](../n/neutral.md) measure to ensure that the portfolio remains self-[financing](../f/financing.md). The replication of option payoffs and the construction of hedged portfolios use the principle that under the [risk](../r/risk.md)-[neutral](../n/neutral.md) measure, the discounted prices of assets follow a [martingale process](../m/martingale_process.md).

### Financial Engineering and Structured Products

[Risk](../r/risk.md) neutrality is fundamental in the creation and [valuation](../v/valuation.md) of structured financial products. Products such as collateralized [debt](../d/debt.md) [obligations](../o/obligation.md) (CDOs), [mortgage](../m/mortgage.md)-backed securities (MBS), and other complex financial instruments are priced using the [risk](../r/risk.md)-[neutral](../n/neutral.md) approach to ensure that the discounted expected payoffs match the current [market](../m/market.md) prices.

## Challenges and Criticisms

### Real Market Dynamics

One major criticism of the [risk](../r/risk.md)-[neutral](../n/neutral.md) framework is that it often oversimplifies real [market dynamics](../m/market_dynamics.md). In reality, investors do exhibit [risk](../r/risk.md) aversion, seeking additional compensation for bearing [risk](../r/risk.md), which is not reflected in the [risk](../r/risk.md)-[neutral](../n/neutral.md) approach.

### Parameter Estimation

Estimating the necessary parameters for models like Black-Scholes under the [risk](../r/risk.md)-[neutral](../n/neutral.md) measure can be challenging. Parameters such as [volatility](../v/volatility.md) and the [risk](../r/risk.md)-free rate need to be accurately estimated, and any errors can lead to significant discrepancies in option pricing.

### Assumption of Continuous Trading

Many models that rely on [risk](../r/risk.md) neutrality assume continuous trading and no [transaction costs](../t/transaction_costs.md), which is not true in real markets. Discrete trading intervals and the existence of [transaction costs](../t/transaction_costs.md) can lead to deviations from the theoretical prices derived using [risk-neutral measures](../r/risk-neutral_measures.md).

## Conclusion

In summary, the concept of [risk](../r/risk.md) neutrality is central to modern financial theory and practice. It provides a powerful tool for valuing [derivatives](../d/derivatives.md) and other financial instruments by assuming that investors are indifferent to [risk](../r/risk.md). While it simplifies many aspects of [asset](../a/asset.md) pricing and [derivative](../d/derivative.md) [valuation](../v/valuation.md), it also comes with limitations and assumptions that may not always [hold](../h/hold.md) in real-world markets. Understanding the implications and applications of [risk](../r/risk.md) neutrality is essential for traders, financial engineers, and researchers engaged in the pricing and management of financial assets.