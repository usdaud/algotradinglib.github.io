# Fibonacci Numbers and Lines

## Introduction

Fibonacci numbers and lines are mathematical tools used extensively in various fields, including [algorithmic trading](../a/accountability.md). Named after the Italian mathematician Leonardo of Pisa, known as Fibonacci, these numbers and lines are derived from a sequence identified in his 1202 book, "Liber Abaci". This sequence and its associated ratios have applications ranging from nature to [financial markets](../f/financial_market.md), where they are employed to predict potential support, resistance levels, and [price action](../p/price_action.md).

## Fibonacci Sequence

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The sequence is represented as:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Mathematically, it is expressed as:
\[ F(n) = F(n-1) + F(n-2) \]

for \( n \geq 2 \) with initial conditions:
\[ F(0) = 0, F(1) = 1 \]

These numbers exhibit unique properties, and ratios derived from this sequence form the [basis](../b/basis.md) of [Fibonacci retracement](../f/fibonacci_retracement.md) and extension levels used in trading.

## Fibonacci Ratios

Derived from the Fibonacci sequence are ratios, often referred to as [Fibonacci retracement](../f/fibonacci_retracement.md) levels, that are used to identify potential [reversal](../r/reversal.md) levels in [financial markets](../f/financial_market.md). The primary ratios are:
- 23.6%
- 38.2%
- 50% (not a Fibonacci ratio but commonly used)
- 61.8%
- 78.6%

These ratios, except for 50%, are connected either directly or indirectly to the golden ratio (\(\phi\)), approximately equal to 1.618. This golden ratio is extensively observed in natural patterns and [market](../m/market.md) movements.

## Application in Algorithmic Trading

In [algorithmic trading](../a/accountability.md), [Fibonacci retracement](../f/fibonacci_retracement.md) and extension levels are utilized to develop [trading strategies](../t/trading_strategies.md) incorporated into [automated trading systems](../a/automated_trading_systems.md). These tools help in identifying key levels for entering and exiting trades based on predicted [support and resistance](../s/support_and_resistance.md) levels.

### Fibonacci Retracement

[Fibonacci retracement](../f/fibonacci_retracement.md) is a method for determining potential [support and resistance](../s/support_and_resistance.md) levels by measuring the distance between a major high and low point on a chart. Traders typically use the following steps:
1. Identify a significant high and low point.
2. Calculate and plot the [retracement](../r/retracement.md) levels using the Fibonacci ratios.

These levels indicate where price corrections may potentially reverse. Algorithmic traders use these levels as part of their entry or exit signals.

### Fibonacci Extension

Unlike [retracement](../r/retracement.md) levels, Fibonacci extension levels are used to identify potential future price targets once the [price action](../p/price_action.md) has resumed its original [trend](../t/trend.md) after a [retracement](../r/retracement.md). Common extension levels include 100%, 161.8%, and 261.8%.

Algorithmic strategies incorporating these levels might set [profit](../p/profit.md) targets at these extensions, activating automated selling or buying actions.

### Practical Example

For instance, in a [downtrend](../d/downtrend.md), if the price of an [asset](../a/asset.md) starts to retrace upwards:
1. Identify the high and low of the recent significant move down.
2. Apply the [Fibonacci retracement](../f/fibonacci_retracement.md) tool from the high to the low.
3. Monitor the [asset](../a/asset.md)'s behavior around the 23.6%, 38.2%, 50%, and 61.8% [retracement](../r/retracement.md) levels.

## Incorporation into Trading Algorithms

[Trading algorithms](../t/trading_algorithms.md) incorporating Fibonacci analysis might:
- Identify shifts in [trend](../t/trend.md) direction by detecting price bounces or breaks from Fibonacci levels.
- Combine [multiple](../m/multiple.md) indicators such as moving averages, RSI ([Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md)), or MACD (Moving Average Convergence [Divergence](../d/divergence.md)) with Fibonacci levels to refine signals.
- Automate entry and exit points based on [Fibonacci retracement](../f/fibonacci_retracement.md) and extension levels.

## Example of Algorithmic Implementation

Here is a simplified pseudo-code example demonstrating how [Fibonacci retracement](../f/fibonacci_retracement.md) might be incorporated into an [algorithmic trading](../a/accountability.md) strategy:

```python
def calculate_fibonacci_levels(high, low):
    difference = high - low
    fibonacci_levels = [high - difference * level for level in [0.236, 0.382, 0.5, 0.618, 0.786]]
    [return](../r/return.md) fibonacci_levels

def trading_strategy(current_price, high, low):
    fibonacci_levels = calculate_fibonacci_levels(high, low)
    
    for level in fibonacci_levels:
        if current_price <= level:
            trigger_buy_signal()
            break
        elif current_price >= high:
            trigger_sell_signal()
            break

# Assume these prices are fetched from historical data
high_price = 100
low_price = 80
current_market_price = 90

trading_strategy(current_market_price, high_price, low_price)
```

## Real-World Usage

Several companies and trading platforms [offer](../o/offer.md) tools and API access for incorporating Fibonacci analysis into [trading algorithms](../t/trading_algorithms.md). Examples include:

- **MetaTrader 4/5** by MetaQuotes:
  MetaTrader platforms [offer](../o/offer.md) built-in tools for applying [Fibonacci retracement](../f/fibonacci_retracement.md) and extension levels to charts. This can be used directly or incorporated into Expert Advisors (EAs) for [algorithmic trading](../a/accountability.md).
  [MetaTrader](https://www.metatrader4.com/)

- **[TradingView](../t/tradingview.md)**:
  [TradingView](../t/tradingview.md) provides in-depth charting tools and scripting languages such as Pine Script, which allows traders to implement and backtest their strategies using Fibonacci levels.
  [TradingView](https://www.tradingview.com/)

- **[QuantConnect](../q/quantconnect.md)**:
  [QuantConnect](../q/quantconnect.md) provides [algorithmic trading infrastructure](../a/algorithmic_trading_infrastructure.md) and supports the development of strategies using languages like Python and C#. It offers the ability to implement custom Fibonacci-based indicators.
  [QuantConnect](https://www.quantconnect.com/)

## Conclusion

Fibonacci numbers and lines are essential tools in [algorithmic trading](../a/accountability.md). Understanding how to calculate and utilize these levels can enhance [trading strategies](../t/trading_strategies.md) by predicting potential [support and resistance](../s/support_and_resistance.md) levels. Whether used independently or combined with other analytical tools, Fibonacci analysis provides a [robust](../r/robust.md) framework for algorithmic traders looking to optimize their [automated trading systems](../a/automated_trading_systems.md).