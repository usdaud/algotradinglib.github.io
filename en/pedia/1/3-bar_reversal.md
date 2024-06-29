# 3-Bar Reversal

## Introduction
3-Bar Reversal is a technical trading pattern used primarily in [algorithmic trading](../a/algorithmic_trading.md). It is a type of price pattern that indicates a potential reversal in the current trend of a financial instrument. Although commonly employed in manual [trading strategies](../t/trading_strategies.md), its rules-based structure makes it ideal for integration into [automated trading systems](../a/automated_trading_systems.md). This strategy is popular among day traders and swing traders looking to capture quick reversals in the market.

## Anatomy of the 3-Bar Reversal Pattern
The 3-Bar Reversal pattern consists of three consecutive bars (candlesticks):

1. **First Bar**: The trend-setting bar which could be either bullish or bearish.
2. **Second Bar**: A smaller bar that continues in the same direction as the first bar but has less momentum.
3. **Third Bar**: The reversal bar, which moves in the opposite direction of the first two bars, signaling a reversal.

### Bullish 3-Bar Reversal
1. **First Bar**: A bearish bar, indicating a downtrend.
2. **Second Bar**: A smaller bearish bar that continues the downtrend but with less momentum.
3. **Third Bar**: A bullish bar that closes above the high of the first bar.

### Bearish 3-Bar Reversal
1. **First Bar**: A bullish bar, indicating an uptrend.
2. **Second Bar**: A smaller bullish bar that continues the uptrend but with less momentum.
3. **Third Bar**: A bearish bar that closes below the low of the first bar.

## Mathematical Formulation
The pattern can be mathematically expressed for algorithmic implementation. Let's denote the opening price, closing price, high, and low of the bar at time \( t \) as \( O_t \), \( C_t \), \( H_t \), \( L_t \), respectively.

### Bullish Reversal Conditions:
1. \( C_{t-2} < O_{t-2} \) (Bearish first bar)
2. \( C_{t-1} < C_{t-2} \) and \( C_{t-1} > L_{t-2} \) (Bearish second bar with less momentum)
3. \( C_{t} > O_{t} \) and \( C_{t} > H_{t-2} \) (Bullish reversal bar)

### Bearish Reversal Conditions:
1. \( C_{t-2} > O_{t-2} \) (Bullish first bar)
2. \( C_{t-1} > C_{t-2} \) and \( C_{t-1} < H_{t-2} \) (Bullish second bar with less momentum)
3. \( C_{t} < O_{t} \) and \( C_{t} < L_{t-2} \) (Bearish reversal bar)

## Example
Consider a stock trading at various price points over three consecutive periods:

### Bullish Reversal:
* **Day 1**: Open = $100, Close = $95, High = $101, Low = $94
* **Day 2**: Open = $94, Close = $92, High = $96, Low = $91
* **Day 3**: Open = $93, Close = $97, High = $98, Low = $92

In this example, the third day's closing price ($97) is higher than the first day's high ($101), confirming a bullish 3-bar reversal.

### Bearish Reversal:
* **Day 1**: Open = $100, Close = $105, High = $106, Low = $99
* **Day 2**: Open = $104, Close = $107, High = $108, Low = $103
* **Day 3**: Open = $106, Close = $102, High = $107, Low = $100

Here, the third day's closing price ($102) is lower than the first day’s low ($100), indicating a bearish 3-bar reversal.

## Applications in Algorithmic Trading
Algorithmic traders use 3-bar [reversal patterns](../r/reversal_patterns.md) to automate the decision-making process. The pattern is incorporated into [trading algorithms](../t/trading_algorithms.md) to:

1. **Identify Entry Points**: The completion of a 3-bar reversal pattern is treated as a signal to enter a trade in the direction of the reversal.
2. **Set [Stop-Loss Orders](../s/stop-loss_orders.md)**: To manage risk, [stop-loss orders](../s/stop-loss_orders.md) are often set at the high (for bearish reversals) or low (for bullish reversals) of the reversal bar.
3. **Optimize Algorithms**: [Backtesting](../b/backtesting.md) on historical data is used to optimize parameters and ensure the effectiveness of the 3-bar reversal strategy.

## Coding the 3-Bar Reversal Strategy

### Python Example with `pandas`
```python
import pandas as pd

def identify_3_bar_reversal(data):
    signals = []

    for i in range(2, len(data)):
        first_bar = data.iloc[i-2]
        second_bar = data.iloc[i-1]
        third_bar = data.iloc[i]

        # Check Bullish Reversal
        if (first_bar['Close'] < first_bar['Open'] and
            second_bar['Close'] < first_bar['Close'] and
            third_bar['Close'] > third_bar['Open'] and
            third_bar['Close'] > first_bar['High']):
            signals.append((data.index[i], "BUY"))

        # Check Bearish Reversal
        elif (first_bar['Close'] > first_bar['Open'] and
              second_bar['Close'] > first_bar['Close'] and
              third_bar['Close'] < third_bar['Open'] and
              third_bar['Close'] < first_bar['Low']):
            signals.append((data.index[i], "SELL"))

    return signals

# Sample Data
data = pd.DataFrame({
    'Open': [100, 94, 93, 100, 104, 106],
    'Close': [95, 92, 97, 105, 107, 102],
    'High': [101, 96, 98, 106, 108, 107],
    'Low': [94, 91, 92, 99, 103, 100]
}, index=pd.date_range(start='2023-01-01', periods=6))

signals = identify_3_bar_reversal(data)
print(signals)
```

## Limitations of the 3-Bar Reversal
Although effective, the 3-bar reversal pattern has its limitations:
1. **False Signals**: Like all trading patterns, it can generate false signals, leading to potential losses.
2. **Parameter Sensitivity**: The effectiveness can vary with different market conditions and instrument types.
3. **Lagging Indicator**: Being a reversal pattern, it lags behind the current price action and may miss the optimal entry or exit points.

## Case Study: QuantConnect Integration
QuantConnect is a cloud-based platform that provides [algorithmic trading](../a/algorithmic_trading.md) infrastructure capable of implementing various [trading strategies](../t/trading_strategies.md), including the 3-bar reversal pattern. Users can write code in Python, C#, or F# to backtest and deploy their strategies. For more details, visit their website: [QuantConnect](https://www.quantconnect.com/).

### Implementation Example:
```python
from AlgorithmImports import *

class ThreeBarReversalAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2022, 1, 1)  # Set Start Date
        self.SetEndDate(2022, 12, 31)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash
        self.AddEquity("SPY", Resolution.Daily)
        self.window = RollingWindow[QuoteBar](3)

    def OnData(self, data):
        self.window.Add(data["SPY"])

        if self.window.IsReady:
            first_bar = self.window[2]
            second_bar = self.window[1]
            third_bar = self.window[0]

            # Check for Bullish Reversal
            if (first_bar.Close < first_bar.Open and
                second_bar.Close < first_bar.Close and
                third_bar.Close > third_bar.Open and
                third_bar.Close > first_bar.High):
                self.SetHoldings("SPY", 1)
                self.Debug(f"BUY Signal on {self.Time}")

            # Check for Bearish Reversal
            elif (first_bar.Close > first_bar.Open and
                  second_bar.Close > first_bar.Close and
                  third_bar.Close < third_bar.Open and
                  third_bar.Close < first_bar.Low):
                self.SetHoldings("SPY", -1)
                self.Debug(f"SELL Signal on {self.Time}")
```

## Conclusion
The 3-Bar Reversal is a powerful pattern for detecting potential trend reversals in financial markets. Its structured nature facilitates easy integration into [algorithmic trading](../a/algorithmic_trading.md) systems, where it can be used to trigger buy and sell signals based on predefined criteria. However, it's essential to consider its limitations and backtest thoroughly to ensure its effectiveness in different market conditions.

By leveraging platforms like QuantConnect, traders can develop, backtest, and deploy sophisticated strategies that incorporate the 3-bar reversal pattern, aligning automated decisions with their trading goals.