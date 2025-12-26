# Libor Options

Libor [options](../o/options.md), also known as London Interbank Offered Rate [options](../o/options.md), are [derivative](../d/derivative.md) instruments that derive their [value](../v/value.md) from the Libor, an [interest rate](../i/interest_rate.md) [benchmark](../b/benchmark.md) that reflects the rates at which banks lend to each other in the international [interbank market](../i/interbank_market.md). These [options](../o/options.md) represent a key segment of the financial [derivatives](../d/derivatives.md) [market](../m/market.md), and play a crucial role in [interest rate](../i/interest_rate.md) hedging, speculating, and arbitraging strategies pursued by various financial institutions.

Note: LIBOR publication ended for most tenors after 2023, and markets shifted to risk-free reference rates such as SOFR (USD), SONIA (GBP), and ESTR (EUR).

Libor is a series of [interest](../i/interest.md) rates calculated for five currencies and seven borrowing periods ranging from overnight to one year, which are published each banking day by the Intercontinental [Exchange](../e/exchange.md) (ICE). These rates serve as reference rates for various financial instruments including mortgages, loans, and [derivatives](../d/derivatives.md) exceeding trillions of dollars in [value](../v/value.md) globally.

### Pricing Mechanism in Libor Options
The [valuation](../v/valuation.md) of Libor [options](../o/options.md) is heavily influenced by the [volatility](../v/volatility.md) of the [underlying](../u/underlying.md) [Libor rate](../l/libor_rate_analysis.md). Pricing models for Libor [options](../o/options.md) are typically derived from the Black-Scholes framework adapted to [handle](../h/handle.md) [interest](../i/interest.md) rates, known as the Black model. The key inputs needed for the Black model are the current [Libor rate](../l/libor_rate_analysis.md), the [strike price](../s/strike_price.md) of the option, the time to expiry, the [risk](../r/risk.md)-free rate, and the [volatility](../v/volatility.md) of the [Libor rate](../l/libor_rate_analysis.md).

The pricing of a European [call option](../c/call_option.md) on the [Libor rate](../l/libor_rate_analysis.md) can be expressed as follows:

\[
C = P \left[ F \cdot N(d1) - X \cdot e^{-r(T-t)} \cdot N(d2) \right]
\]

Where:
- \(C\) is the price of the [call option](../c/call_option.md).
- \(P\) is the notional [principal](../p/principal.md) [value](../v/value.md).
- \(F\) is the forward [Libor rate](../l/libor_rate_analysis.md).
- \(X\) is the strike rate.
- \(T-t\) is the time to [maturity](../m/maturity.md).
- \(r\) is the [risk](../r/risk.md)-free [interest rate](../i/interest_rate.md).
- \(d1 = \frac{\ln(\frac{F}{X}) + \frac{\sigma^2}{2}(T-t)}{\sigma\sqrt{T-t}}\)
- \(d2 = d1 - \sigma\sqrt{T-t}\)
- \(N(\cdot)\) is the [cumulative distribution function](../c/cumulative_distribution_function_in_trading.md) of the standard [normal distribution](../n/normal_distribution_in_trading.md).
- \(\sigma\) is the [volatility](../v/volatility.md) of the [Libor rate](../l/libor_rate_analysis.md).

This Black model framework is also applicable for pricing Libor [put options](../p/put_options.md), with appropriate adjustments made for the payoff structure.

### Usage of Libor Options
Libor [options](../o/options.md) are used by a variety of [market](../m/market.md) participants including banks, [hedge](../h/hedge.md) funds, [insurance](../i/insurance.md) companies, and corporate treasuries for various purposes:

1. **Hedging:** Institutions use Libor [options](../o/options.md) to [hedge](../h/hedge.md) against the adverse movements in [interest](../i/interest.md) rates. For example, an institution with floating-rate liabilities may purchase Libor call [options](../o/options.md) to protect against rises in [interest](../i/interest.md) rates.

2. **[Speculation](../s/speculation.md):** Traders may employ Libor [options](../o/options.md) to speculate on future movements in [interest](../i/interest.md) rates based on their [market](../m/market.md) outlook. A [speculator](../s/speculator.md) expecting an increase in Libor rates may purchase call [options](../o/options.md) to benefit from potential rate hikes.

3. **[Arbitrage](../a/arbitrage.md):** [Market](../m/market.md) makers and [proprietary trading](../p/proprietary_trading.md) desks often engage in [arbitrage](../a/arbitrage.md) activities exploiting pricing inefficiencies between the Libor [options](../o/options.md) [market](../m/market.md) and other related markets like [futures](../f/futures.md), swaps, and [forward rate](../f/forward_rate.md) agreements.

### Regulatory and Market Landscape
Libor [options](../o/options.md) are traded on various exchanges and [over-the-counter (OTC) markets](../o/over-the-counter_markets.md). However, the credibility of Libor as a [benchmark](../b/benchmark.md) was significantly impacted by the [Libor scandal](../l/libor_scandal.md), where it was revealed that several banks colluded to manipulate the rate for [profit](../p/profit.md). This had profound repercussions, prompting global regulatory bodies to initiate a transition from Libor to alternative [risk](../r/risk.md)-free rates (RFRs) like the Secured Overnight [Financing](../f/financing.md) Rate (SOFR) in the US, the [Euro](../e/euro.md) Short-Term Rate (€STR) in Europe, and the Sterling Overnight [Index](../i/index_instrument.md) Average (SONIA) in the UK.

ICE continues to publish Libor rates despite these developments, but the transition towards alternative benchmarks is steadily advancing. [Market](../m/market.md) participants are gradually shifting their [interest rate](../i/interest_rate.md) hedging and speculative activities from Libor-based instruments to those linked with new RFR benchmarks.



### Mathematical Appendix
For those looking for a deeper mathematical understanding, the [stochastic processes](../s/stochastic_processes.md) governing the evolution of Libor rates can be modeled using various [interest rate models](../i/interest_rate_models.md), such as:

- **[Hull-White Model](../h/hull-white_model.md):** This model assumes that the short rate follows a mean-reverting process, which is particularly useful for capturing the dynamics of [interest](../i/interest.md) rates over time. Its equation is given by
\[
dr(t) = \[theta](../t/theta.md) [\mu - r(t)]dt + \sigma dW(t)
\]
where \(\[theta](../t/theta.md)\) is the reversion speed, \(\mu\) is the long-term mean rate, \(\sigma\) is the [volatility](../v/volatility.md) [factor](../f/factor.md), and \(dW(t)\) is the Wiener process.

- **Black-Derman-Toy Model:** This is a discrete-time model used to describe the evolution of [interest](../i/interest.md) rates. It accounts for varying volatilities and ensures that they are positive.

These models contribute to the accurate pricing, [risk management](../r/risk_management.md), and strategic placement of Libor [options](../o/options.md).

### Conclusion
Libor [options](../o/options.md) remain a vital part of the financial ecosystem, [offering](../o/offering.md) significant [utility](../u/utility.md) in [risk management](../r/risk_management.md) and speculative strategies even as the markets transition towards new benchmarks. With [robust](../r/robust.md) pricing frameworks and dynamic models, participants can effectively utilize these instruments to achieve their financial goals within the evolving regulatory landscape.