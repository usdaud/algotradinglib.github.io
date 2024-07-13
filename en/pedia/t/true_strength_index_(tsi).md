# True Strength Index (TSI)

The True Strength [Index](../i/index.md) (TSI) is a [momentum](../m/momentum.md) [oscillator](../o/oscillator.md) developed by William Blau. It measures the strength of a [financial instrument](../f/financial_instrument.md) by using double smoothing to minimize long-term trends and provide a clearer indication of price changes and potential shifts in [market](../m/market.md) [momentum](../m/momentum.md).

## Understanding the True Strength Index

The TSI takes into account the price difference between successive bars, often referred to as the price change or [delta](../d/delta.md), and smooths it using a pair of exponential moving averages (EMAs). This double EMA smoothing approach helps filter out the [noise](../n/noise.md) and identify more significant trends or shifts in [momentum](../m/momentum.md). The TSI oscillates between positive and negative values and can be interpreted in ways similar to other [momentum oscillators](../m/momentum_oscillators.md) like the [Relative Strength](../r/relative_strength.md) [Index](../i/index.md) (RSI).

## Formula

The TSI is calculated with the following formula:

1. **Price Change (`[delta](../d/delta.md)`)**:
    \( \[Delta](../d/delta.md) = \text{Close} - \text{Close}_{prev} \)

2. **Smoothed Price Change (`[Delta](../d/delta.md)`)**:
    \( \text{Smoothed} \[Delta](../d/delta.md) = EMA(EMA(\[Delta](../d/delta.md), r), s) \)

3. **Absolute Price Change (`absDelta`)**:
    \( abs\[Delta](../d/delta.md) = |\[Delta](../d/delta.md)| \)

4. **Smoothed Absolute Price Change (`absDelta`)**:
    \( \text{Smoothed} abs\[Delta](../d/delta.md) = EMA(EMA(abs\[Delta](../d/delta.md), r), s) \)

5. **True Strength [Index](../i/index.md)**:
    \( TSI = \frac{Smoothed \[Delta](../d/delta.md)}{Smoothed abs\[Delta](../d/delta.md)} \times 100 \)

Where:
- `EMA` is the Exponential Moving Average
- `r` and `s` are the periods for the first and second EMA smoothings, respectively

## Interpretation

### Overbought and Oversold Conditions

- **[Overbought](../o/overbought.md)**: A TSI [value](../v/value.md) above a certain high threshold (commonly 25) may indicate that the [asset](../a/asset.md) is in an [overbought](../o/overbought.md) condition and could be due for a potential price [correction](../c/correction.md).
- **[Oversold](../o/oversold.md)**: Conversely, a TSI [value](../v/value.md) below a low threshold (commonly -25) could suggest that the [asset](../a/asset.md) is [oversold](../o/oversold.md) and might be poised for a rebound.

### Crossovers and Signal Lines

- **Signal Line**: Often, a smoothed version of the TSI (usually with a shorter EMA period) is used as a signal line to generate buy or sell signals. When the TSI crosses above the signal line, it may be a bullish signal, implying it's a good time to buy. When the TSI crosses below the signal line, it could be a bearish signal, suggesting a potential sell time.
- **Zero Line Crosses**: A cross above zero might indicate bullish [momentum](../m/momentum.md), while a drop below zero could signal bearish [momentum](../m/momentum.md).

### Divergences

Divergences between the TSI and the price of the [underlying asset](../u/underlying_asset.md) can also provide valuable [trading signals](../t/trading_signals.md):
- **[Bullish Divergence](../b/bullish_divergence.md)**: When the price makes a lower low, but the TSI makes a higher low, it can be an indication of weakening downward [momentum](../m/momentum.md) and potential [reversal](../r/reversal.md) to the [upside](../u/upside.md).
- **[Bearish Divergence](../b/bearish_divergence.md)**: When the price sets a higher high, but the TSI forms a lower high, it could signal a weakening [uptrend](../u/uptrend.md) and potential [reversal](../r/reversal.md) to the downside.

## Advantages of TSI

1. **Reduces [Noise](../n/noise.md)**: The double smoothing process helps reduce [noise](../n/noise.md) from short-term price fluctuations, making the TSI a clearer [indicator](../i/indicator.md) of [momentum](../m/momentum.md) shifts.
2. **Identification of Bullish & Bearish Markets**: The TSI's ability to track both price direction and [momentum](../m/momentum.md) allows traders to identify bullish or bearish markets more effectively.
3. **Useful for Various Timeframes**: TSI can be applied across [multiple](../m/multiple.md) timeframes, making it a versatile tool for both short-term and long-term traders.

## Implementation and Usage

### In Trading Platforms

Many trading platforms like MetaTrader, thinkorswim (by TD [Ameritrade](../a/ameritrade.md)), and [TradingView](../t/tradingview.md) support TSI as a built-in [indicator](../i/indicator.md). Traders can easily add TSI to their charts and modify parameters (`r` and `s`) to suit their specific [trading strategies](../t/trading_strategies.md) and the particular [asset](../a/asset.md) they are analyzing.

### Optimization

Parameter [optimization](../o/optimization.md) is a common practice among traders using TSI. Adjusting the periods for the EMAs (`r` and `s`) can help fine-tune the [indicator](../i/indicator.md) to match the [volatility](../v/volatility.md) and behavioral characteristics of different financial instruments.

## Example Calculation

Let's assume `r = 25` and `s = 13`. Here is a step-by-step process to calculate the TSI:

1. **Price Changes**: Compute the daily price changes by subtracting the previous day's close from today's close.
2. **Smoothing**: Apply a 25-period EMA to the series of price changes, followed by a 13-period EMA to the resulting series.
3. **Absolute Price Changes**: Take the absolute [value](../v/value.md) of the daily price changes.
4. **Smoothing Absolute Changes**: Apply the same EMA smoothings (25-period followed by 13-period) to the absolute price changes.
5. **TSI Calculation**: Divide the double-smoothed price change by the double-smoothed absolute price change and multiply by 100 to obtain the TSI [value](../v/value.md).

## Application in Algorithmic Trading

The TSI can play a significant role in [algorithmic trading](../a/accountability.md) due to its responsiveness and accuracy in detecting [momentum](../m/momentum.md) shifts. Here's an example of how TSI can be integrated into an [algorithmic trading](../a/accountability.md) strategy:

### Strategy Outline

1. **Data Preprocessing**: Collect historical price data for the [financial instrument](../f/financial_instrument.md).
2. **TSI Calculation**: Calculate the TSI values based on chosen `r` and `s` periods.
3. **Signal Generation**:
    - **Buy Signal**: Trigger a buy [trade](../t/trade.md) when the TSI crosses above the signal line or rises above zero.
    - **Sell Signal**: Trigger a sell [trade](../t/trade.md) when the TSI crosses below the signal line or falls below zero.
4. **[Backtesting](../b/backtesting.md)**: Validate the strategy by running it against historical data to assess performance (profitability, [drawdown](../d/drawdown.md), win-rate, etc.).
5. **[Optimization](../o/optimization.md)**: Adjust parameters (`r` and `s`) and thresholds to optimize performance.
6. **Implementation**: Deploy the strategy in a live [trading environment](../t/trading_environment.md) with [risk management](../r/risk_management.md) settings.

### Libraries and Frameworks

Various libraries and frameworks in languages such as Python and R can be leveraged to implement TSI-based strategies:

- **Python**:
    - `pandas` for data manipulation
    - `numpy` for numerical calculations
    - `ta-lib` or `pandas_ta` for [technical indicators](../t/technical_indicator.md), including TSI
    - `[backtrader](../b/backtrader.md)` for [backtesting](../b/backtesting.md)
- **R**:
    - `quantmod` for data retrieval
    - `TTR` for [technical analysis](../t/technical_analysis.md) functions, including TSI
    - `PerformanceAnalytics` for [performance metrics](../p/performance_metrics.md)

## Example in Python

Below is a simple example of computing TSI using Python and the `ta-lib` library:

```python
[import](../i/import.md) pandas as pd
[import](../i/import.md) talib

# Sample data: replace with actual price data
data = {
    'Close': [10, 11, 12, 11, 13, 14, 13, 14, 15, 14, 16]
}
df = pd.DataFrame(data)

# Compute TSI
df['TSI'] = talib.TSI(df['Close'], timeperiod1=25, timeperiod2=13)

print(df)
```

## Practical Example: Using TSI in TradingView

[TradingView](../t/tradingview.md) is a popular platform that traders use for charting, screening, and analyzing [financial markets](../f/financial_market.md). Integrating TSI into [TradingView](../t/tradingview.md) charts is straightforward:

1. **Adding TSI [Indicator](../i/indicator.md)**:
    - [Open](../o/open.md) a chart in [TradingView](../t/tradingview.md).
    - Click on "Indicators" in the toolbar.
    - Search for "True Strength [Index](../i/index.md)" and select it.
2. **Customizing Parameters**:
    - Adjust the periods for the EMAs (`r` and `s`) as desired in the settings.
3. **Interpreting Signals**:
    - Observe TSI crossovers and divergences in relation to price movements.
    - Utilize [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions to make informed trading decisions.

You can explore TSI further on [TradingView](../t/tradingview.md)'s website: [TradingView](https://www.tradingview.com).

## Conclusion

The True Strength [Index](../i/index.md) is a valuable [momentum](../m/momentum.md) [oscillator](../o/oscillator.md) that provides insights into the strength and direction of [market](../m/market.md) trends. Its double smoothing technique reduces [noise](../n/noise.md) and makes it an effective tool for identifying potential entry and exit points in various [trading strategies](../t/trading_strategies.md). Whether used for manual [market](../m/market.md) analysis or integrated into more complex [algorithmic trading](../a/accountability.md) systems, TSI can significantly enhance a [trader](../t/trader.md)'s ability to navigate [financial markets](../f/financial_market.md).