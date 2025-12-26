# Divergence

Divergence is a fundamental concept in [technical analysis](../t/technical_analysis.md) that refers to a situation where the price of an [asset](../a/asset.md) is moving in the opposite direction of an [indicator](../i/indicator.md). This phenomenon is often interpreted as a signal that the current price [trend](../t/trend.md) may be weakening or reversing. Divergence can be used to predict potential reversals in price direction, and thus it is a critical tool in the arsenal of algorithmic traders.

## Types of Divergence

Divergence comes in two main types: Regular Divergence and Hidden Divergence.

### Regular Divergence

Regular Divergence is a situation where the price of an [asset](../a/asset.md) and a specific technical [indicator](../i/indicator.md), most commonly the [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI) or Moving Average Convergence Divergence (MACD), move in opposite directions. It can be either bullish or bearish.

#### Bullish Regular Divergence

Bullish Regular Divergence occurs when the price of an [asset](../a/asset.md) creates a lower low while the [indicator](../i/indicator.md) forms a higher low. This suggests that the downward [momentum](../m/momentum.md) is slowing down, even though the price continues to fall, and could be indicative of an upcoming bullish [reversal](../r/reversal.md).

- **Example:** If [Bitcoin](../b/bitcoin.md)’s price makes a lower low, but the RSI [indicator](../i/indicator.md) makes a higher low, this could suggest that selling pressure is decreasing, and a price increase might be forthcoming.

#### Bearish Regular Divergence

Bearish Regular Divergence occurs when the price creates a higher high, but the [indicator](../i/indicator.md) forms a lower high. This suggests that the upward [momentum](../m/momentum.md) is weakening, even though the price continues to rise, and could be indicative of an impending bearish [reversal](../r/reversal.md).

- **Example:** If the S&P 500 makes a higher high, but the MACD forms a lower high, this divergence could indicate that buying pressure is decreasing, possibly leading to a price drop.

### Hidden Divergence

Hidden Divergence occurs when the price of an [asset](../a/asset.md) moves in the same direction as the [trend](../t/trend.md), but the [indicator](../i/indicator.md) moves in the opposite direction. Like Regular Divergence, it can also be either bullish or bearish.

#### Bullish Hidden Divergence

Bullish Hidden Divergence happens when the price creates a higher low while the [indicator](../i/indicator.md) forms a lower low. This suggests that the upward [trend](../t/trend.md) is likely to continue even though the [indicator](../i/indicator.md) is signalling otherwise.

- **Example:** In a scenario where Apple Inc.’s stock price forms a higher low, but the RSI forms a lower low, this could validate the continuation of the upward [trend](../t/trend.md).

#### Bearish Hidden Divergence

Bearish Hidden Divergence occurs when the price creates a lower high, but the [indicator](../i/indicator.md) forms a higher high. This indicates that the downward [trend](../t/trend.md) is likely to continue even though the [indicator](../i/indicator.md) suggests otherwise.

- **Example:** If Tesla's stock price creates a lower high, but the MACD forms a higher high, this could confirm that the downward [trend](../t/trend.md) [will](../w/will.md) continue.

## Indicators Commonly Used to Identify Divergence

Several [technical indicators](../t/technical_indicator.md) can be employed to detect divergence, and the choice of [indicator](../i/indicator.md) often depends on the [asset](../a/asset.md) being traded and the [trading strategy](../t/trading_strategy.md) in use. The most commonly used indicators include:

### Relative Strength Index (RSI)

The RSI measures the speed and change of price movements and oscillates between 0 and 100. It is traditionally used to identify [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions but can also be highly effective for spotting divergence.

- **[Bullish Divergence](../b/bullish_divergence.md):** Identified when RSI forms higher lows while the price forms lower lows.
- **[Bearish Divergence](../b/bearish_divergence.md):** Identified when RSI forms lower highs while the price forms higher highs.

### Moving Average Convergence Divergence (MACD)

The MACD is a [trend](../t/trend.md)-following [momentum](../m/momentum.md) [indicator](../i/indicator.md) that shows the relationship between two moving averages of a [security](../s/security.md)’s price. It consists of the MACD line, the signal line, and the [histogram](../h/histogram.md).

- **[Bullish Divergence](../b/bullish_divergence.md):** Occurs when the MACD line forms higher lows while the price forms lower lows.
- **[Bearish Divergence](../b/bearish_divergence.md):** Occurs when the MACD line forms lower highs while the price forms higher highs.

### Stochastic Oscillator

The [Stochastic Oscillator](../s/stochastic_oscillator.md) is a [momentum](../m/momentum.md) [indicator](../i/indicator.md) that compares a particular closing price of a [security](../s/security.md) to a [range](../r/range.md) of its prices over a certain period of time. It oscillates between 0 and 100.

- **[Bullish Divergence](../b/bullish_divergence.md):** Identified when the [stochastic oscillator](../s/stochastic_oscillator.md) forms higher lows while the price forms lower lows.
- **[Bearish Divergence](../b/bearish_divergence.md):** Identified when the [stochastic oscillator](../s/stochastic_oscillator.md) forms lower highs while the price forms higher highs.

### Commodity Channel Index (CCI)

CCI is an [oscillator](../o/oscillator.md) used to identify cyclical trends in commodities but can also be applied to [stocks](../s/stock.md). It is particularly good at identifying divergence.

- **[Bullish Divergence](../b/bullish_divergence.md):** Occurs when CCI forms higher lows while the price forms lower lows.
- **[Bearish Divergence](../b/bearish_divergence.md):** Occurs when CCI forms lower highs while the price forms higher highs.

## Implementation in Algorithmic Trading

[Algorithmic trading](../a/accountability.md) systems can be programmed to automatically detect divergence using predefined criteria and execute trades based on these signals. The [efficiency](../e/efficiency.md) of such algorithms depends on the quality of the data, the sophistication of the models, and the [execution](../e/execution.md) speed.

### Data Collection

For accurate detection of divergence, high-quality real-time and historical data are required. This data can be sourced from various providers, including:

- **[Bloomberg](../b/bloomberg.md)**: bloomberg.com
- **[Reuters](../r/reuters.md)**: reuters.com
- **[Quandl](../q/quandl.md)**: quandl.com

### Signal Detection

Once the data is collected, the next step involves [signal detection](../s/signal_detection_in_trading.md). This can be done using several programming languages and platforms, including Python with libraries like Pandas and NumPy, or specialized trading platforms like MetaTrader.

- **Python**: Python can be used to write scripts that continuously monitor live [market](../m/market.md) data for divergence signals.
- **MetaTrader**: MetaTrader’s MQL5 language allows for the creation of automated trading robots (Expert Advisors) that can detect divergence signals in real-time.

### Example Code in Python

A simple example of how to detect bullish and [bearish divergence](../b/bearish_divergence.md) using Python is as follows:

```python
[import](../i/import.md) pandas as pd
[import](../i/import.md) numpy as np

def find_divergence(prices, [indicator](../i/indicator.md)):
    divergences = []
    for i in [range](../r/range.md)(1, len(prices)):
        if prices[i] < prices[i-1] and [indicator](../i/indicator.md)[i] > [indicator](../i/indicator.md)[i-1]:
            divergences.append(('[Bullish Divergence](../b/bullish_divergence.md)', prices.[index](../i/index_instrument.md)[i]))
        elif prices[i] > prices[i-1] and [indicator](../i/indicator.md)[i] < [indicator](../i/indicator.md)[i-1]:
            divergences.append(('[Bearish Divergence](../b/bearish_divergence.md)', prices.[index](../i/index_instrument.md)[i]))
    [return](../r/return.md) divergences

# Example usage with dummy data
prices = pd.Series([100, 102, 101, 105, 104])
[indicator](../i/indicator.md) = pd.Series([70, 72, 71, 73, 71])

divergences = find_divergence(prices, [indicator](../i/indicator.md))
for d in divergences:
    print(d)
```

### Execution of Trades

The final step is to execute trades based on the detected divergence signals. The [efficiency](../e/efficiency.md) of this process can be significantly enhanced by employing low-latency trading [infrastructure](../i/infrastructure.md) and direct [market](../m/market.md) access.

- **[Algorithmic Execution](../a/algorithmic_execution.md) Services**: Many brokers [offer](../o/offer.md) [algorithmic execution](../a/algorithmic_execution.md) services, which can be utilized to ensure faster and more efficient [trade](../t/trade.md) [execution](../e/execution.md).
- **Direct [Market](../m/market.md) Access (DMA)**: Using DMA can reduce latency and enhance the effectiveness of the [trading strategy](../t/trading_strategy.md).

## Conclusion

Divergence is a powerful tool in [technical analysis](../t/technical_analysis.md) that can provide early signals of potential [trend](../t/trend.md) reversals. When implemented in [algorithmic trading](../a/accountability.md) systems, it can enhance the ability to make informed and timely trading decisions. Utilizing various [technical indicators](../t/technical_indicator.md), collecting high-quality data, accurately detecting signals, and efficiently executing trades are all critical components of leveraging divergence in [algorithmic trading](../a/accountability.md).