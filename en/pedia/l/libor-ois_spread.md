# Libor-OIS Spread

The LIBOR-OIS spread is a critical financial metric that reflects the difference between the London Interbank Offered Rate (LIBOR) and the Overnight Indexed [Swap](../s/swap.md) (OIS) rate. This spread serves as an [indicator](../i/indicator.md) of banking sector health and [liquidity](../l/liquidity.md) conditions in the [financial markets](../f/financial_market.md). Understanding the LIBOR-OIS spread involves delving into both components of the spread, their significance, and their applications in algo trading.

## What is LIBOR?

The London Interbank Offered Rate (LIBOR) is one of the world's most important [benchmark](../b/benchmark.md) [interest](../i/interest.md) rates. It represents the average rate at which major global banks are willing to lend to one another on an unsecured [basis](../b/basis.md) for a specific period ranging from overnight to twelve months. LIBOR is calculated for five currencies (USD, EUR, GBP, JPY, CHF) and for seven borrowing periods (overnight, 1 week, and 1, 2, 3, 6, 12 months).

LIBOR has traditionally been a key [reference rate](../r/reference_rate.md) for a large [volume](../v/volume.md) of financial products, including [derivatives](../d/derivatives.md), mortgages, and corporate loans. However, it has faced scrutiny and reform, especially following the [interest rate](../i/interest_rate.md) rigging scandal in 2012. The Financial Conduct Authority (FCA) has been working to phase out LIBOR with alternative reference rates like SOFR (Secured Overnight [Financing](../f/financing.md) Rate).

Learn more about LIBOR from [ICE Benchmark Administration](https://www.theice.com/iba/libor).

## What is OIS?

The Overnight Indexed [Swap](../s/swap.md) (OIS) is an [interest rate swap](../i/interest_rate_swap.md) agreement where one party agrees to pay a [fixed interest rate](../f/fixed_interest_rate.md) in [exchange](../e/exchange.md) for receiving a floating rate pegged to an overnight [index](../i/index_instrument.md), such as the [Federal Funds Rate](../f/federal_funds_rate.md) in the United States or EONIA ([Euro](../e/euro.md) Overnight [Index](../i/index_instrument.md) Average) in the [Eurozone](../e/eurozone.md). OIS rates are considered low-[risk](../r/risk.md) because they are based on the overnight repo rate, which is typically low and stable.

OIS contracts are particularly useful for [hedging interest rate risk](../h/hedging_interest_rate_risk.md) and for [monetary policy](../m/monetary_policy.md) signaling. They also serve as a [liquidity](../l/liquidity.md) [indicator](../i/indicator.md) and a [proxy](../p/proxy.md) for the true [risk](../r/risk.md)-free rate.

## Understanding the Libor-OIS Spread

The LIBOR-OIS spread is the difference between the [LIBOR rate](../l/libor_rate_analysis.md) and the OIS rate for the same [maturity](../m/maturity.md). It serves as a gauge of perceived [credit risk](../c/credit_risk.md) and [liquidity](../l/liquidity.md) in the [interbank market](../i/interbank_market.md). A widening spread indicates rising [credit risk](../c/credit_risk.md) or reduced [liquidity](../l/liquidity.md), while a narrowing spread suggests improving conditions.

### Historical Context

The LIBOR-OIS spread gained prominence during the 2008 [financial crisis](../f/financial_crisis.md). Typically, the spread remains within the [range](../r/range.md) of a few [basis](../b/basis.md) points. However, during the crisis, it spiked dramatically as fears over [counterparty risk](../c/counterparty_risk.md) and [liquidity](../l/liquidity.md) shortages soared. For instance, the spread widened to over 300 [basis](../b/basis.md) points in October 2008, illustrating the extreme stress in the banking system.

### Calculation

The LIBOR-OIS spread is straightforward to calculate. Suppose the 3-month USD LIBOR is at 0.50%, and the 3-month USD OIS rate is at 0.15%. The LIBOR-OIS spread is:

```
LIBOR-OIS Spread = [LIBOR Rate](../l/libor_rate_analysis.md) - OIS Rate
                 = 0.50% - 0.15%
                 = 0.35% or 35 [basis](../b/basis.md) points
```

### Economic Significance

#### Indicator of Bank Health

The spread is closely watched by financial analysts, economists, and central banks as it reflects the [risk](../r/risk.md) perception and [liquidity](../l/liquidity.md) in the banking sector. A high spread signals that banks perceive a higher [risk](../r/risk.md) of lending to each other, indicating potential distress or lack of confidence in the [financial system](../f/financial_system.md).

#### Policy Implications

Central banks may intervene when the LIBOR-OIS spread widens significantly. For instance, during the 2008 crisis, the Federal Reserve and other central banks provided [liquidity](../l/liquidity.md) injections to stabilize the banking system.

## Applications in Algo Trading

In the realm of algo trading, the LIBOR-OIS spread can be utilized for developing [trading strategies](../t/trading_strategies.md) and [risk management](../r/risk_management.md) mechanisms. Here are a few ways in which it is applied:

### Market Sentiment Analysis

Algo [trading systems](../t/trading_systems.md) can monitor the LIBOR-OIS spread as a part of their [sentiment analysis](../s/sentiment_analysis.md) toolset. A sudden increase in the spread can indicate rising [risk](../r/risk.md) and prompt algorithms to adjust their positions accordingly.

### Arbitrage and Spread Trading

Traders can design algorithms to exploit discrepancies between LIBOR and OIS rates. For example, if the spread widens beyond historical norms, it might indicate a trading opportunity either through direct [arbitrage](../a/arbitrage.md) or by taking positions in related financial instruments.

### Risk Management

Algo trading platforms can use changes in the LIBOR-OIS spread to dynamically adjust their [risk models](../r/risk_models_in_trading.md). A widening spread can prompt models to become more [risk-averse](../r/risk-averse.md), shedding risky assets and increasing [holdings](../h/holdings.md) in safer instruments.

### Portfolio Hedging

For portfolios containing [interest rate](../i/interest_rate.md)-sensitive instruments, tracking the spread can be crucial. Algorithms can be programmed to adjust hedges based on movements in the LIBOR-OIS spread, thus optimizing [risk](../r/risk.md)-adjusted returns.

### Liquidity Forecasting

Changes in the LIBOR-OIS spread provide insights into [market](../m/market.md) [liquidity](../l/liquidity.md). Algo [trading systems](../t/trading_systems.md) can incorporate these insights to predict and prepare for potential [liquidity](../l/liquidity.md) squeezes, ensuring that they maintain effective [execution](../e/execution.md) rates.

## Conclusion

The LIBOR-OIS spread is a pivotal metric within the [financial markets](../f/financial_market.md), reflecting both [credit risk](../c/credit_risk.md) and [liquidity](../l/liquidity.md) in the banking sector. For algo trading, it serves as a vital [indicator](../i/indicator.md) for [market sentiment](../m/market_sentiment.md), [risk management](../r/risk_management.md), and strategic decision-making. As LIBOR transitions to other [benchmark](../b/benchmark.md) rates, understanding [spreads](../s/spreads.md) like the LIBOR-OIS [will](../w/will.md) continue to be essential for [robust](../r/robust.md) [financial analysis](../f/financial_analysis.md) and [algorithmic trading](../a/algorithmic_trading.md) strategies.
