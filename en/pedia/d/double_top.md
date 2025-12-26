# Double Top

In [technical analysis](../t/technical_analysis.md), a double top is a bearish [reversal](../r/reversal.md) pattern that typically signals the end of an [uptrend](../u/uptrend.md). This pattern is recognized by two peaks of approximately equal height that are separated by a valley. The double top is one of the most commonly used [chart patterns](../c/chart_patterns.md) in algotrading due to its relative ease of identification and high predictive [value](../v/value.md).

## Structure of a Double Top Pattern

A double top pattern consists of four key elements:

1. **First Peak**: The [market](../m/market.md) reaches a new high, which is then followed by a decline. This high is considered the first peak.
2. **[Trough](../t/trough.md)**: After the first peak, the price declines to a support level, known as the [trough](../t/trough.md).
3. **Second Peak**: The price subsequently rebounds to a level near the first peak, forming the second peak.
4. **[Breakout](../b/breakout.md) ([Neckline](../n/neckline.md))**: Once the price falls below the [trough](../t/trough.md) level, it confirms the double top pattern, which is also referred to as the "[neckline](../n/neckline.md)" or "confirmation line."

### Characteristics

- **Height and Width**: The peaks can vary in height and width, but in a typical double top, both peaks are of almost the same height. The [trough](../t/trough.md) should also be of a reasonable depth to signify a clear price decline.
- **[Volume](../v/volume.md)**: [Volume](../v/volume.md) generally increases during the formation of the first peak and drops during the second peak. A significant increase in [volume](../v/volume.md) during the [breakout](../b/breakout.md) confirms the pattern.
- **Time Frame**: The time frame between the peaks can [range](../r/range.md) from a few days to several months. Traders often consider longer time frames more reliable indicators.

## Importance in Algotrading

### Predictive Power

The double top pattern is considered highly reliable in predicting [reversal](../r/reversal.md) trends. Algotrading systems use this pattern to execute trades that [profit](../p/profit.md) from the anticipated price decline following the confirmation of the pattern.

### Automation

The structure and form of a double top make it amenable to automated detection using [computational algorithms](../c/computational_algorithms.md). Algotrading software can be programmed to scan price charts and automatically identify double top formations.

### Integration with Indicators

Double tops can be integrated with other [technical indicators](../t/technical_indicator.md) to enhance the accuracy of [trade](../t/trade.md) signals. Algorithms often combine double tops with [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI), Moving Averages, and [Volume indicators](../v/volume_indicators.md) to filter out [false signals](../f/false_signals_in_trading.md).

## Example of Algorithm Implementation

### Pseudocode

Here is a simplified pseudocode to detect a double top pattern:
```
function detectDoubleTop(prices):
  peaks = findPeaks(prices)
  [trough](../t/trough.md) = findTrough(peaks)
  
  if peak[1] almostEqual(p[2]) and volumeDuring(peak[1]) > volumeDuring([trough](../t/trough.md)):
    if prices.breakBelow([trough](../t/trough.md)):
      [return](../r/return.md) "Double Top Detected"

  [return](../r/return.md) "No Double Top"
```

### Python Example

Below is an example of how one might implement the detection of a double top pattern in Python:
```python
[import](../i/import.md) numpy as np

def find_peaks(prices):
    # Simplified peak detection logic
    peaks = []
    for i in [range](../r/range.md)(1, len(prices)-1):
        if prices[i-1] < prices[i] > prices[i+1]:
            peaks.append((i, prices[i]))
    [return](../r/return.md) peaks

def find_trough(peaks, prices):
    trough_index = min([range](../r/range.md)(peaks[0][0] + 1, peaks[1][0]), key=[lambda](../l/lambda.md) i: prices[i])
    [return](../r/return.md) trough_index, prices[trough_index]

def detect_double_top(prices):
    peaks = find_peaks(prices)
    if len(peaks) < 2:
        [return](../r/return.md) "No Double Top"
    
    trough_index, trough_price = find_trough(peaks, prices)
    peak1, peak2 = peaks[0][1], peaks[1][1]
    
    if np.isclose(peak1, peak2, atol=0.01):
        if prices[trough_index] > prices[peaks[1][0]]:
            [return](../r/return.md) "Double Top Detected at [index](../i/index_instrument.md)", peaks[1][0]
    
    [return](../r/return.md) "No Double Top"

# Example usage
prices = np.array([100, 110, 120, 115, 110, 120, 115, 100, 90])
print(detect_double_top(prices))
```

### Real-World Resources

To further delve into the algorithms and frameworks for detecting double tops, consider exploring:

- **[QuantConnect](../q/quantconnect.md)**- **Kaggle Datasets and Notebooks**
## Trading Strategies Based on Double Top

### Short Selling

One common [trading strategy](../t/trading_strategy.md) upon identifying a confirmed double top is [short selling](../s/short_selling.md). This involves borrowing [shares](../s/shares.md) to sell at the current high price with the intention of buying them back at a lower price once the [market](../m/market.md) declines.

### Stop-Loss and Take-Profit

Setting strategic stop-loss and take-[profit](../p/profit.md) levels is crucial. The stop-loss is generally placed slightly above the second peak, while the take-[profit](../p/profit.md) level may be set at a distance equating to the height of the double top pattern beneath the [neckline](../n/neckline.md).

### Leverage with Other Patterns

Algotraders often combine the double top pattern with other [chart patterns](../c/chart_patterns.md) and indicators for a more comprehensive [trading strategy](../t/trading_strategy.md). For instance, patterns like Head and Shoulders or indicators like MACD can validate the signal inferred from the double top.

## Limitations and Considerations

### False Signals

While the double top is a reliable [indicator](../i/indicator.md), it is not infallible. [False signals](../f/false_signals_in_trading.md) can occur, and thus it's essential to use supplementary indicators or filters to confirm the pattern.

### Market Conditions

Double tops are more effective in markets characterized by high [volatility](../v/volatility.md). In low [volatility](../v/volatility.md) environments, the pattern may produce fewer reliable signals.

### Pattern Symmetry

Perfect symmetry in double tops is rare. Traders and algorithms must account for slight variations in peak heights and [trough](../t/trough.md) depths to avoid premature or delayed [trade](../t/trade.md) entries.

### External Factors

[Market](../m/market.md) events, such as economic news and global financial events, can influence the effectiveness of technical patterns like the double top. Algorithms should be programmed to pause or modify trading activity during such times to avoid erratic [market](../m/market.md) behavior.

## Conclusion

The double top pattern remains an essential tool in the arsenal of both manual and algorithmic traders. Its straightforward identification, combined with a considerable degree of reliability, makes it a popular choice for predicting [market](../m/market.md) reversals. By leveraging modern computational tools and integrating [multiple](../m/multiple.md) indicators, traders and developers can enhance the efficacy of [trading strategies](../t/trading_strategies.md) based on double tops. However, it is equally important to remain cautious of the limitations and to use comprehensive [risk management techniques](../r/risk_management_techniques.md) to ensure consistent trading success.