# Triangular Moving Average (TMA)

The Triangular Moving Average (TMA) is a unique form of a moving average that applies a double-smoothing process to price data. This [technical analysis](../t/technical_analysis.md) tool is widely used by traders to smooth out price fluctuations and better identify trends. Unlike simple and exponential moving averages, the TMA reduces the lag effect inherent in these metrics by averaging the average values themselves, producing a more refined depiction of the [trend](../t/trend.md).

## Objective and Concept

The primary objective of the Triangular Moving Average is to smooth price data to identify trends over a specified period. The TMA achieves this by calculating the average of an average, thereby giving more weight to the central elements of the period under consideration. This results in a smoother curve, which can reduce the impact of short-term [volatility](../v/volatility.md) and [noise](../n/noise.md), making it easier to identify the [underlying](../u/underlying.md) [trend](../t/trend.md).

## Calculation

The calculation of the Triangular Moving Average involves several steps. First, you calculate the moving average over a specified period. Then, you calculate a moving average of that moving average. Let's break this down:

1. **First-level Moving Average (FLMA):**  
   The first step is to calculate a simple moving average (SMA) of the [time series](../t/time_series.md) data over a specified period, `N`. This can be denoted as:
   \[
   FLMA_t = \frac{1}{N} \sum_{i=0}^{N-1} P_{t-i}
   \]
   where \( P \) represents the price, \( t \) represents the current time period, and \( N \) represents the number of periods.

2. **Second-level Moving Average (SLMA):**  
   Next, we calculate the simple moving average of the first-level moving averages over the same period. This can be expressed as:
   \[
   SLMA_t = \frac{1}{N} \sum_{i=0}^{N-1} FLMA_{t-i}
   \]

This double-smoothing process ensures that the final Triangular Moving Average curve is smoother and better represents the overall [market](../m/market.md) [trend](../t/trend.md).

## Implementation

Implementation of the TMA in trading platforms can significantly vary, but most platforms that support programming or scripting (like MetaTrader, [NinjaTrader](../n/ninjatrader.md), Python with libraries like Pandas and NumPy) allow you to compute it easily.

### Example in Python

Here is an example of how you might calculate the TMA using Python:

```python
[import](../i/import.md) numpy as np
[import](../i/import.md) pandas as pd

def moving_average(data, window_size):
    [return](../r/return.md) data.rolling(window=window_size).mean()

def triangular_moving_average(data, period):
    first_ma = moving_average(data, period)
    second_ma = moving_average(first_ma, period)
    [return](../r/return.md) second_ma

# Example usage
data = pd.Series([your_time_series_data_here])  # Replace with your data
period = 10
tma = triangular_moving_average(data, period)
print(tma)
```

In this example, `your_time_series_data_here` should be replaced with actual price data.

## Comparisons with Other Moving Averages

One of the main benefits of the TMA is its reduced lag, which is a common [issue](../i/issue.md) with Simple Moving Averages (SMA). While the Exponential Moving Average (EMA) also aims to reduce lag by weighting recent prices more heavily, the TMA's double-smoothing process can produce an even more reliable signal by focusing on the central values. Here are some key differences:

- **SMA** provides [equal weight](../e/equal_weight.md) to all prices within the given period.
- **EMA** gives more weight to the latest prices.
- **TMA** focuses on the central prices, [offering](../o/offering.md) a more balanced and smoother representation.

## Applications

### Trend Identification

As with other moving averages, the TMA is primarily used to identify trends. Because it is smoother than other moving averages, it can be particularly effective at revealing longer-term trends and reducing the impact of short-term price swings.

### Crossover Strategies

Traders often use moving averages to form "crossover strategies." These involve using two or more moving averages with different periods. For example, a [trader](../t/trader.md) might use a short-period TMA and a long-period TMA. A buy signal could be generated when the short-period TMA crosses above the long-period TMA, and a sell signal could be generated when the opposite occurs.

### Price Filters

Another common application is to use TMAs to filter out false price movements or breakouts. Here, the TMA serves as a dynamic support or resistance level. Trades might be initiated or closed based on the price's relationship with the TMA.

## Limitations

While the Triangular Moving Average has its strengths, it also has some limitations:

- **Lag:** Despite reduced lag compared to SMAs, there's still an inherent lag because it's based on historical prices.
- **Responsiveness:** In very volatile markets, the TMA might smooth out too much, causing traders to miss quick-moving opportunities.
- **Complexity:** The calculation is more complex than SMAs and EMAs, which might be a downside for those looking for simpler indicators.

## Conclusion

The Triangular Moving Average is a highly effective technical tool for smoothing price data and identifying trends. Its double-smoothing process creates a more refined [trend](../t/trend.md) line, which can be particularly useful for identifying longer-term trends and reducing the [noise](../n/noise.md) present in shorter-term price movements. However, like any [indicator](../i/indicator.md), it has its limitations and should be used in combination with other tools and techniques for best results.

Understanding the mechanics and applications of the TMA can help traders improve their [market](../m/market.md) analysis and develop more effective [trading strategies](../t/trading_strategies.md). By [offering](../o/offering.md) a clearer picture of the [underlying](../u/underlying.md) [trend](../t/trend.md), the TMA allows traders to make more informed decisions, contributing to more successful trading outcomes.
