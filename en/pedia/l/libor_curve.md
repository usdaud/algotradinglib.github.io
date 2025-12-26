# LIBOR Curve

The London Interbank Offered Rate (LIBOR) curve is an essential element in the world of [finance](../f/finance.md) and trading, acting as a [benchmark](../b/benchmark.md) [interest rate](../i/interest_rate.md) for various financial instruments. Understanding the intricacies of the LIBOR curve is crucial for traders, financial analysts, and anyone involved in [interest rate](../i/interest_rate.md)-based financial products. In this comprehensive discussion, we [will](../w/will.md) unpack what the LIBOR curve is, its significance, components, construction, and usage in different financial contexts.

Note: LIBOR publication ended for most tenors after 2023, and markets shifted to risk-free reference rates such as SOFR (USD), SONIA (GBP), and ESTR (EUR).

## What is LIBOR?

LIBOR stands for the London Interbank Offered Rate. It is the average rate at which major global banks borrow from one another in the international [interbank market](../i/interbank_market.md). Traditionally, LIBOR has been calculated in five currencies: the US Dollar (USD), the [Euro](../e/euro.md) (EUR), the British Pound Sterling (GBP), the Japanese Yen (JPY), and the Swiss Franc (CHF), and for seven different maturities: overnight, one week, and one month, two months, three months, six months, and one year.

## Importance of LIBOR

1. **[Benchmark](../b/benchmark.md) Rate**: LIBOR is used as a [benchmark](../b/benchmark.md) rate for a wide [range](../r/range.md) of financial products including bonds, loans, [derivatives](../d/derivatives.md), and mortgages. It essentially reflects the cost of borrowing unsecured funds in the [interbank market](../i/interbank_market.md).

2. **[Risk](../r/risk.md) Assessment**: It helps financial institutions assess the [risk](../r/risk.md) and [liquidity](../l/liquidity.md) in the banking sector. Higher LIBOR rates can indicate rising [risk](../r/risk.md) in the banking system, while lower rates suggest more confidence among banks.

3. **[Interest Rate](../i/interest_rate.md) Determination**: LIBOR is used to determine [interest](../i/interest.md) rates on various financial products. For example, many floating-rate notes and adjustable-rate mortgages use the [LIBOR rate](../l/libor_rate_analysis.md) as a reference point.

## LIBOR Curve Structure

The LIBOR curve is a graphical representation showing the yields ([interest](../i/interest.md) rates) of LIBOR-based financial instruments across different maturities. The curve is often plotted with the [interest rate](../i/interest_rate.md) on the Y-axis and time to [maturity](../m/maturity.md) on the X-axis.

### Components of the LIBOR Curve

1. **Spot Rates**: These are the rates for immediate settlement. Spot LIBOR rates are published daily by the Intercontinental [Exchange](../e/exchange.md) (ICE) or its predecessor British Bankers Association (BBA).

2. **Forward Rates**: These refer to the future rates implied by current spot rates. Forward rates can be derived using [mathematical models](../m/mathematical_models_in_trading.md) and are a key component for constructing the LIBOR curve.

3. **[Discount](../d/discount.md) Factors**: These are used to calculate the [present value](../p/present_value.md) of future cash flows. [Discount](../d/discount.md) factors can be extracted from the LIBOR curve.

## Construction of the LIBOR Curve

Constructing the LIBOR curve involves a series of steps:

1. **Data Collection**: Collect the current LIBOR rates for different maturities. These rates are usually published daily.

2. **Bootstrapping Method**: This is a process used to derive zero-coupon [yield](../y/yield.md) curves from the [market](../m/market.md) prices of a set of coupon-bearing products, primarily swaps.

3. **Linear [Interpolation](../i/interpolation.md)**: To fill any [gaps](../g/gap.md) between the maturities for which the LIBOR rates are available, linear [interpolation](../i/interpolation.md) is used.

4. **Spline Modelling**: More sophisticated methods such as spline modelling can be used to create a smooth curve. Common splines include cubic splines and B-splines.

## Applications of the LIBOR Curve

### Interest Rate Swaps

LIBOR is fundamental in the pricing and [valuation](../v/valuation.md) of [interest rate swaps](../i/interest_rate_swaps.md). In a typical [interest rate swap](../i/interest_rate_swap.md), one [counterparty](../c/counterparty.md) pays a fixed rate while the other pays a floating rate, which is often pegged to LIBOR.

### Credit Default Swaps

The LIBOR curve also plays a crucial role in [credit default swaps](../c/credit_default_swaps.md) (CDS). These are [financial derivatives](../f/financial_derivatives.md) that function as a type of [insurance](../i/insurance.md) against the [default](../d/default.md) of a borrower.

### Mortgage Loans

Many adjustable-rate [mortgage](../m/mortgage.md) (ARM) products are indexed to LIBOR. Therefore, any movement in the [LIBOR rate](../l/libor_rate_analysis.md) directly impacts the payments on such mortgages.

### Futures and Options

Traders use the LIBOR curve to price various [futures](../f/futures.md) and [options](../o/options.md). For instance, [Eurodollar](../e/eurodollar.md) [futures](../f/futures.md) are directly linked to LIBOR rates.

## Limitations and Criticisms

Despite its widespread use, LIBOR has faced criticisms and challenges:

1. **Manipulation Scandals**: There have been instances where banks were found manipulating LIBOR rates for their own financial benefit. This has led to significant fines and calls for reform.

2. **Transition to New Benchmarks**: Due to the scandals and the [risk](../r/risk.md) of manipulation, [financial markets](../f/financial_market.md) are transitioning to new [benchmark](../b/benchmark.md) rates. In the U.S., for example, the Secured Overnight [Financing](../f/financing.md) Rate (SOFR) is being promoted as an alternative to LIBOR.

## Conclusion

The LIBOR curve remains a cornerstone in [financial markets](../f/financial_market.md), influencing a myriad of financial instruments and contracts. While it has faced its share of controversies, understanding the LIBOR curve is indispensable for anyone involved in [finance](../f/finance.md). As the [market](../m/market.md) transitions to new benchmarks, the [underlying](../u/underlying.md) principles and techniques for analyzing [interest](../i/interest.md) rates [will](../w/will.md) remain crucial.


This comprehensive overview captures the essence and importance of the LIBOR curve, providing the foundational knowledge required to navigate its complexities in the financial world.