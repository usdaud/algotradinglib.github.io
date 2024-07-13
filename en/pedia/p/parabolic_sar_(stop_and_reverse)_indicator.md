# Parabolic SAR (Stop and Reverse) Indicator

The [Parabolic SAR](../p/parabolic_sar.md) (Stop and Reverse) is a [technical analysis](../t/technical_analysis.md) [indicator](../i/indicator.md) developed by J. Welles Wilder, a mechanical engineer turned [technical analyst](../t/technical_analyst.md). The [indicator](../i/indicator.md) is principally used to determine potential reversals in the direction of price movement in [financial markets](../f/financial_market.md). Its primary use is in the realm of [trend following](../t/trend_following.md) and [trend](../t/trend.md) identification.

## Mechanics of Parabolic SAR

The [Parabolic SAR](../p/parabolic_sar.md) is plotted on the price chart itself rather than in a separate pane. It appears as a series of dots placed either above or below the price bars. These dots serve as [trailing stop](../t/trailing_stop.md) loss points and also help to signal potential [trend](../t/trend.md) reversals.

### Calculation

The [Parabolic SAR](../p/parabolic_sar.md) is calculated using the following formula:

\[ SAR_{n+1} = SAR_n + \[alpha](../a/alpha.md) ( EP - SAR_n ) \]

Where:
- \( SAR_{n+1} \) = the SAR [value](../v/value.md) for the next period.
- \( SAR_n \) = the current period's SAR [value](../v/value.md).
- \( EP \) = Extreme Point, the highest high (for long positions) or the lowest low (for short positions) reached during the current [trend](../t/trend.md).
- \( \[alpha](../a/alpha.md) \) = Acceleration [Factor](../f/factor.md), which typically starts at 0.02 and increases by 0.02 up to a maximum of 0.20 each time a new high or low is reached during the [trend](../t/trend.md).

### Reversal

A [reversal](../r/reversal.md) occurs when the price closes below the SAR [value](../v/value.md) (in an [uptrend](../u/uptrend.md)) or above it (in a [downtrend](../d/downtrend.md)). When this happens, the SAR switches sides.

## Parameters and Customization

The [default](../d/default.md) Acceleration [Factor](../f/factor.md) (\(\[alpha](../a/alpha.md)\)) starts at 0.02 and ends at a maximum of 0.20. However, these values can be customized to suit different trading styles:

- **Lower \(\[alpha](../a/alpha.md)\) Values:** [Yield](../y/yield.md) fewer signals and are suitable for long-term trading.
- **Higher \(\[alpha](../a/alpha.md)\) Values:** [Yield](../y/yield.md) more signals and are suitable for [short-term trading](../s/short-term_trading.md).

## Usage in Trading

### Trend Identification

The primary use of the [Parabolic SAR](../p/parabolic_sar.md) is identifying the direction of the [trend](../t/trend.md). When the dots are below the price, it signals an [uptrend](../u/uptrend.md). Conversely, when the dots are above the price, it signals a [downtrend](../d/downtrend.md).

### Entry and Exit Points

- **Entry Points:** Traders might enter a long position when the dots move below the price, and a short position when the dots move above the price.
- **Exit Points:** Traders might use the dots as [trailing stop](../t/trailing_stop.md)-loss points to [lock in profits](../l/lock_in_profits.md). When the price crosses the SAR, it may signal an exit point.

### Combination with Other Indicators

The [Parabolic SAR](../p/parabolic_sar.md) is often used in combination with other [technical indicators](../t/technical_indicator.md) to improve the reliability of [trading signals](../t/trading_signals.md). For example, combining the SAR with moving averages or the [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI) can provide additional layers of confirmation.

## Advantages and Limitations

### Advantages

- **Simplicity:** The [Parabolic SAR](../p/parabolic_sar.md) is easy to understand and straightforward to plot.
- **Clear Signals:** It provides clear signals for [trend](../t/trend.md) reversals, which can be valuable for creating stop-loss and take-[profit](../p/profit.md) strategies.

### Limitations

- **Whipsaws:** In sideways or choppy markets, the [indicator](../i/indicator.md) can generate [false signals](../f/false_signals_in_trading.md) or whipsaws.
- **Lag:** Since it is a [trend](../t/trend.md)-following [indicator](../i/indicator.md), it may lag and produce signals after a substantial portion of the move has already occurred.

## Implementation in Algorithmic Trading

Algorithmic traders often incorporate the [Parabolic SAR](../p/parabolic_sar.md) into [automated trading systems](../a/automated_trading_systems.md) due to its clear and straightforward rules. Here’s a simple Python code snippet using the popular TA-Lib library to compute the [Parabolic SAR](../p/parabolic_sar.md):

```python
[import](../i/import.md) talib
[import](../i/import.md) pandas as pd

# Sample DataFrame
data = {
    'high': [104, 105, 106, 107, 108],
    'low': [100, 101, 102, 103, 104],
    'close': [102, 103, 104, 105, 106]
}
df = pd.DataFrame(data)

# Compute Parabolic SAR
df['SAR'] = talib.SAR(df['high'], df['low'], acceleration=0.02, maximum=0.20)

print(df)
```

## Final Thoughts

The [Parabolic SAR](../p/parabolic_sar.md) remains a popular tool among traders for identifying trends and potential reversals. While it may not be foolproof, its simplicity and [efficiency](../e/efficiency.md) make it a valuable component of any [trader](../t/trader.md)'s [technical analysis](../t/technical_analysis.md) toolkit, especially when used in conjunction with other indicators and analysis techniques.

For more detailed information on the [Parabolic SAR](../p/parabolic_sar.md), you can refer to resources provided by [TradingView](https://www.tradingview.com) and [Investopedia](https://www.investopedia.com).