# Indicator

An indicator in [algorithmic trading](../a/accountability.md) is a mathematical calculation based on historical price, [volume](../v/volume.md), or [open interest](../o/open_interest.md) information that aims to predict future [market](../m/market.md) movements. Indicators are essential tools for [technical analysis](../t/technical_analysis.md), and they help traders make more informed decisions by identifying trends, [volatility](../v/volatility.md), [momentum](../m/momentum.md), and other [market](../m/market.md) characteristics. There are several categories and types of indicators, each serving a specific purpose. This article aims to provide a comprehensive understanding of various indicators and their applications in [algorithmic trading](../a/accountability.md).

## Moving Averages

### Simple Moving Average (SMA)
The Simple Moving Average is one of the most commonly used indicators. It calculates the average price over a specified number of periods. The SMA is often used to identify [trend](../t/trend.md) direction. For example, a 50-day SMA is the average of the last 50 days’ closing prices.

```python
def calculate_sma(prices, period):
    [return](../r/return.md) sum(prices[-period:]) / period
```

### Exponential Moving Average (EMA)
The Exponential Moving Average gives more weight to recent prices, making it more responsive to new information. The EMA formula applies a multiplicative [factor](../f/factor.md) to the most recent data points.

```python
def calculate_ema(prices, period):
    ema = [sum(prices[:period]) / period]
    [multiplier](../m/multiplier.md) = 2 / (period + 1)
    for price in prices[period:]:
        ema.append(((price - ema[-1]) * [multiplier](../m/multiplier.md)) + ema[-1])
    [return](../r/return.md) ema
```

## Oscillators

### Relative Strength Index (RSI)
The [Relative Strength](../r/relative_strength.md) [Index](../i/index.md) is a [momentum](../m/momentum.md) [oscillator](../o/oscillator.md) that measures the speed and change of price movements. The RSI oscillates between 0 and 100 and is typically used to identify [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions.

```python
def calculate_rsi(prices, period=14):
    deltas = [prices[i+1] - prices[i] for i in [range](../r/range.md)(len(prices)-1)]
    [gain](../g/gain.md) = sum([[delta](../d/delta.md) for [delta](../d/delta.md) in deltas if [delta](../d/delta.md) > 0])
    loss = abs(sum([[delta](../d/delta.md) for [delta](../d/delta.md) in deltas if [delta](../d/delta.md) < 0]))
    avg_gain = [gain](../g/gain.md) / period
    avg_loss = loss / period
    rs = avg_gain / avg_loss
    [return](../r/return.md) 100 - (100 / (1 + rs))
```

### Stochastic Oscillator
The [Stochastic Oscillator](../s/stochastic_oscillator.md) compares a particular closing price of a [security](../s/security.md) to a [range](../r/range.md) of its prices over a certain period. It generates two lines, %K and %D, to identify [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions.

```python
def calculate_stochastic_oscillator(prices, period=14):
    high_low_diff = [max(prices[i-period:i]) - min(prices[i-period:i]) for i in [range](../r/range.md)(period, len(prices))]
    %K = [(prices[i] - min(prices[i-period:i])) / high_low_diff[i-period] * 100 for i in [range](../r/range.md)(period, len(prices))]
    %D = [sum(%K[i-2:i+1]) / 3 for i in [range](../r/range.md)(2, len(%K))]
    [return](../r/return.md) %K, %D
```

## Volume Indicators

### On-Balance Volume (OBV)
The On-Balance [Volume](../v/volume.md) indicator uses [volume](../v/volume.md) flow to predict changes in stock price. It adds [volume](../v/volume.md) on up days and subtracts on down days.

```python
def calculate_obv(prices, volumes):
    obv = [volumes[0]]
    for i in [range](../r/range.md)(1, len(prices)):
        if prices[i] > prices[i-1]:
            obv.append(obv[-1] + volumes[i])
        elif prices[i] < prices[i-1]:
            obv.append(obv[-1] - volumes[i])
        else:
            obv.append(obv[-1])
    [return](../r/return.md) obv
```

### Volume-Weighted Average Price (VWAP)
The [Volume](../v/volume.md)-[Weighted Average](../w/weighted_average.md) Price provides the average price a [security](../s/security.md) has traded at throughout the day, based on both [volume](../v/volume.md) and price. It is usually used as a trading [benchmark](../b/benchmark.md).

```python
def calculate_vwap(prices, volumes):
    cumulative_price_volume = sum([price * [volume](../v/volume.md) for price, [volume](../v/volume.md) in zip(prices, volumes)])
    cumulative_volume = sum(volumes)
    [return](../r/return.md) cumulative_price_volume / cumulative_volume
```

## Volatility Indicators

### Bollinger Bands
[Bollinger Bands](../b/bollinger_band.md) consist of a middle band being a moving average and two outer bands calculated as the standard deviations from the moving average. They help to identify [volatility](../v/volatility.md) and [overbought](../o/overbought.md)/[oversold](../o/oversold.md) conditions.

```python
[import](../i/import.md) numpy as np

def calculate_bollinger_bands(prices, period=20):
    sma = np.mean(prices[-period:])
    std_dev = np.std(prices[-period:])
    upper_band = sma + (2 * std_dev)
    lower_band = sma - (2 * std_dev)
    [return](../r/return.md) upper_band, sma, lower_band
```

### Average True Range (ATR)
The [Average True Range](../a/average_true_range_(atr).md) is a [volatility](../v/volatility.md) indicator that measures the [range](../r/range.md) within which the price of an [asset](../a/asset.md) typically fluctuates. It provides an idea of how much the price is moving during a set period.

```python
def calculate_atr(high, low, close, period=14):
    tr = [max(high[i] - low[i], abs(high[i] - close[i-1]), abs(low[i] - close[i-1])) for i in [range](../r/range.md)(1, len(high))]
    atr = [sum(tr[:period]) / period]
    for i in [range](../r/range.md)(period, len(tr)):
        atr.append((atr[-1] * (period - 1) + tr[i]) / period)
    [return](../r/return.md) atr
```

## Trend Indicators

### Moving Average Convergence Divergence (MACD)
The MACD calculates the difference between two exponential moving averages (EMAs), typically a 12-period EMA and a 26-period EMA. A 9-period EMA of the MACD is called the "signal line."

```python
def calculate_macd(prices, fast_period=12, slow_period=26, signal_period=9):
    fast_ema = calculate_ema(prices, fast_period)
    slow_ema = calculate_ema(prices, slow_period)
    macd = [fast - slow for fast, slow in zip(fast_ema, slow_ema)]
    signal_line = calculate_ema(macd, signal_period)
    [return](../r/return.md) macd, signal_line
```

### Parabolic SAR
The [Parabolic SAR](../p/parabolic_sar.md) (Stop and Reverse) is used to determine the direction of an [asset](../a/asset.md)'s [momentum](../m/momentum.md) and the point in time when this [momentum](../m/momentum.md) has a higher-than-normal probability of switching directions.

```python
def calculate_parabolic_sar(high, low, af=0.02, max_af=0.2):
    sar = low[0]  # Start at the first low [value](../v/value.md)
    ep = high[0]  # Highest price (Extreme Point)
    [trend](../t/trend.md) = 1  # 1 for [uptrend](../u/uptrend.md), 0 for [downtrend](../d/downtrend.md)
    sar_list = []

    for i in [range](../r/range.md)(1, len(high)):
        sar_list.append(sar)
        if [trend](../t/trend.md) == 1:
            sar = sar + af * (ep - sar)
            if high[i] > ep:
                ep = high[i]
                af = min(af + 0.02, max_af)
            if low[i] < sar:
                [trend](../t/trend.md) = 0
                sar = ep
                ep = low[i]
                af = 0.02
        else:
            sar = sar - af * (sar - ep)
            if low[i] < ep:
                ep = low[i]
                af = min(af + 0.02, max_af)
            if high[i] > sar:
                [trend](../t/trend.md) = 1
                sar = ep
                ep = high[i]
                af = 0.02

    sar_list.append(sar)
    [return](../r/return.md) sar_list
```

## Conclusion
Indicators are invaluable tools for [algorithmic trading](../a/accountability.md), [offering](../o/offering.md) insights into [market](../m/market.md) trends, [momentum](../m/momentum.md), [volatility](../v/volatility.md), and [volume](../v/volume.md). Each indicator has its unique advantages and applications, making them suitable for different [trading strategies](../t/trading_strategies.md). By combining [multiple](../m/multiple.md) indicators, traders can create [robust](../r/robust.md) [trading algorithms](../t/trading_algorithms.md) capable of adjusting to various [market](../m/market.md) conditions.