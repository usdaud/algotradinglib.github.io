# ISO Currency Code

ISO [currency](../c/currency.md) codes, also known as ISO 4217 codes, are a set of internationally recognized three-letter codes that denote different currencies used around the world. These codes are maintained by the International Organization for Standardization (ISO) and are crucial for various financial and commercial activities. In the realm of algo trading, ISO [currency](../c/currency.md) codes play a significant role, particularly when dealing with forex trading, multi-[currency](../c/currency.md) portfolios, and international financial transactions.

## Understanding ISO 4217

ISO 4217 is the international standard for [currency](../c/currency.md) codes. Each [currency](../c/currency.md) is assigned a unique three-letter code, typically comprising two letters from the ISO 3166-1 alpha-2 country code and an additional letter identifying the [currency](../c/currency.md) (e.g., USD for United States Dollar). Besides the alphabetic code, ISO 4217 also assigns numeric codes to each [currency](../c/currency.md) for computational ease.

### Components of ISO 4217 Codes

1. **Alphabetic Code**:
 - A three-letter code that uniquely identifies a [currency](../c/currency.md).
 - For example, GBP (Great Britain Pound), EUR ([Euro](../e/euro.md)), JPY (Japanese Yen).

2. **Numeric Code**:
 - A three-digit number that can be used in automated systems and electronic communication.
 - For instance, the numeric code for USD is 840, for EUR it is 978, and for JPY it is 392.

3. **Minor Unit**:
 - Represents the subdivision of the [currency](../c/currency.md), often used to indicate cents or pence.
 - For example, 1 USD = 100 cents, 1 GBP = 100 pence.

## Importance in Algo Trading

Algo trading involves executing trades using automated systems based on pre-defined algorithms. Given the global nature of [financial markets](../f/financial_market.md), it is necessary to [handle](../h/handle.md) [multiple](../m/multiple.md) currencies accurately and efficiently. ISO [currency](../c/currency.md) codes facilitate this by providing a standardized method to identify and process different currencies.

### Key Areas of Application

1. **Forex Trading**:
 - Forex ([foreign exchange](../f/foreign_exchange.md)) trading is a primary area where ISO [currency](../c/currency.md) codes are essential.
 - [Trading algorithms](../t/trading_algorithms.md) that deal with [currency](../c/currency.md) pairs (e.g., EUR/USD, GBP/JPY) rely heavily on these codes to execute trades accurately.

2. **Multi-[Currency](../c/currency.md) Portfolios**:
 - Investors often [hold](../h/hold.md) portfolios consisting of assets denominated in various currencies.
 - ISO [currency](../c/currency.md) codes allow for seamless management and reporting of these assets.

3. **International Transactions**:
 - Companies and financial institutions engage in cross-border transactions requiring precise [currency](../c/currency.md) identification.
 - Algorithms used to optimize these transactions depend on ISO [currency](../c/currency.md) codes for accurate conversion and processing.

## Practical Implementation

In practice, these codes are used in different ways depending on the algorithm’s complexity and purpose. Here are some examples:

### Automated Trading Systems

[Automated trading systems](../a/automated_trading_systems.md) use ISO [currency](../c/currency.md) codes to identify and [trade](../t/trade.md) different [currency](../c/currency.md) pairs. For instance, a simple trading algorithm might look like this:

```python
def trade_forex(currency_pair):
    if currency_pair == "EURUSD":
        # Execute buy or sell [trade](../t/trade.md)
        pass
    elif currency_pair == "GBPJPY":
        # Execute buy or sell [trade](../t/trade.md)
        pass
    # Additional [currency](../c/currency.md) pairs can be added here

trade_forex("EURUSD")
```

Here, the ISO codes EUR and USD are used to identify the [Euro](../e/euro.md) and US Dollar, while EURUSD represents the [currency](../c/currency.md) pair.

### Risk Management

[Risk management](../r/risk_management.md) algorithms also use ISO codes to assess the exposure to different currencies. The following pseudocode demonstrates a basic [risk management](../r/risk_management.md) strategy:

```python
def assess_risk(portfolio):
    currency_exposure = {
        "USD": 0,
        "EUR": 0,
        "JPY": 0
    }
    
    for [asset](../a/asset.md) in portfolio:
        currency_exposure[asset.[currency](../c/currency.md)] += [asset](../a/asset.md).[value](../v/value.md)
    
    for [currency](../c/currency.md), exposure in currency_exposure.items():
        if exposure > threshold:
            print(f"High exposure to {[currency](../c/currency.md)}: {exposure}")

portfolio = [
    {"[currency](../c/currency.md)": "USD", "[value](../v/value.md)": 100000},
    {"[currency](../c/currency.md)": "EUR", "[value](../v/value.md)": 50000},
    {"[currency](../c/currency.md)": "JPY", "[value](../v/value.md)": 3000000}
]

assess_risk(portfolio)
```

This code uses ISO codes to track and print the exposure to different currencies in a portfolio.

## Major ISO Currency Codes

### List of Commonly Used Codes

#### US Dollar (USD)
- **Code**: USD
- **Country**: United States
- **Numeric Code**: 840
- **Minor Unit**: 2 (cents)

#### Euro (EUR)
- **Code**: EUR
- **Countries**: [Eurozone](../e/eurozone.md) countries
- **Numeric Code**: 978
- **Minor Unit**: 2 (cents)

#### Japanese Yen (JPY)
- **Code**: JPY
- **Country**: Japan
- **Numeric Code**: 392
- **Minor Unit**: 0 (no subdivision used)

#### British Pound (GBP)
- **Code**: GBP
- **Country**: United Kingdom
- **Numeric Code**: 826
- **Minor Unit**: 2 (pence)

#### Swiss Franc (CHF)
- **Code**: CHF
- **Country**: Switzerland
- **Numeric Code**: 756
- **Minor Unit**: 2 (rappen)

### Comprehensive List

A comprehensive list of ISO 4217 codes can be found on the public materials of the International Organization for Standardization:

- ISO 4217 Currency Codes

This list includes all active and historical currencies, their alphabetic and numeric codes, and minor units.

## ISO Currency Codes in Financial Software

Financial software and trading platforms frequently incorporate ISO [currency](../c/currency.md) codes in their systems. For instance:

### Bloomberg Terminal

The [Bloomberg Terminal](../b/bloomberg_terminal.md) uses ISO codes extensively to present data and execute commands. Traders can look up [exchange](../e/exchange.md) rates, historical data, and execute trades based on these codes.

### MetaTrader

MetaTrader, a popular [trading platform](../t/trading_platform.md), uses ISO [currency](../c/currency.md) codes to identify [currency](../c/currency.md) pairs in forex trading. Scripts and expert advisors (EAs) on MetaTrader use these codes to automate [trading strategies](../t/trading_strategies.md).

### SAP Financial Systems

SAP, a leading enterprise resource planning (ERP) system, uses ISO [currency](../c/currency.md) codes for all its financial transactions. This ensures consistency and accuracy in multi-[currency](../c/currency.md) transactions and reporting.

## Conclusion

ISO [currency](../c/currency.md) codes are fundamental in global [financial markets](../f/financial_market.md). Their standardization enables efficient and accurate processing of transactions involving different currencies. In algo trading, these codes are indispensable for executing forex trades, managing multi-[currency](../c/currency.md) portfolios, and facilitating international [trade](../t/trade.md). As the financial world continues to globalize, the importance of ISO 4217 codes [will](../w/will.md) only grow, ensuring seamless and reliable [currency](../c/currency.md) identification across various platforms and systems.