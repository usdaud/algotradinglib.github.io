# 3-Bar Reversal

## Introduction
3-Bar [Reversal](../r/reversal.md) is a technical trading pattern used primarily in [algorithmic trading](../a/algorithmic_trading.md). It is a type of price pattern that indicates a potential [reversal](../r/reversal.md) in the current [trend](../t/trend.md) of a [financial instrument](../f/financial_instrument.md). Although commonly employed in manual [trading strategies](../t/trading_strategies.md), its rules-based structure makes it ideal for integration into [automated trading systems](../a/automated_trading_systems.md). This strategy is popular among day traders and swing traders looking to capture quick reversals in the [market](../m/market.md).

## Anatomy of the 3-Bar Reversal Pattern
The 3-Bar [Reversal](../r/reversal.md) pattern consists of three consecutive bars (candlesticks):

1. **First Bar**: The [trend](../t/trend.md)-setting bar which could be either bullish or bearish.
2. **Second Bar**: A smaller bar that continues in the same direction as the first bar but has less [momentum](../m/momentum.md).
3. **Third Bar**: The [reversal](../r/reversal.md) bar, which moves in the opposite direction of the first two bars, signaling a [reversal](../r/reversal.md).

### Bullish 3-Bar Reversal
1. **First Bar**: A bearish bar, indicating a [downtrend](../d/downtrend.md).
2. **Second Bar**: A smaller bearish bar that continues the [downtrend](../d/downtrend.md) but with less [momentum](../m/momentum.md).
3. **Third Bar**: A bullish bar that closes above the high of the first bar.

### Bearish 3-Bar Reversal
1. **First Bar**: A bullish bar, indicating an [uptrend](../u/uptrend.md).
2. **Second Bar**: A smaller bullish bar that continues the [uptrend](../u/uptrend.md) but with less [momentum](../m/momentum.md).
3. **Third Bar**: A bearish bar that closes below the low of the first bar.

## Mathematical Formulation
The pattern can be mathematically expressed for algorithmic implementation. Let's denote the [opening price](../o/opening_price.md), closing price, high, and low of the bar at time \( t \) as \( O_t \), \( C_t \), \( H_t \), \( L_t \), respectively.

### Bullish Reversal Conditions:
1. \( C_{t-2} < O_{t-2} \) (Bearish first bar)
2. \( C_{t-1} < C_{t-2} \) and \( C_{t-1} > L_{t-2} \) (Bearish second bar with less [momentum](../m/momentum.md))
3. \( C_{t} > O_{t} \) and \( C_{t} > H_{t-2} \) (Bullish [reversal](../r/reversal.md) bar)

### Bearish Reversal Conditions:
1. \( C_{t-2} > O_{t-2} \) (Bullish first bar)
2. \( C_{t-1} > C_{t-2} \) and \( C_{t-1} < H_{t-2} \) (Bullish second bar with less [momentum](../m/momentum.md))
3. \( C_{t} < O_{t} \) and \( C_{t} < L_{t-2} \) (Bearish [reversal](../r/reversal.md) bar)

## Example
Consider a stock trading at various price points over three consecutive periods:

### Bullish Reversal:
* **Day 1**: [Open](../o/open.md) = $100, Close = $95, High = $101, Low = $94
* **Day 2**: [Open](../o/open.md) = $94, Close = $92, High = $96, Low = $91
* **Day 3**: [Open](../o/open.md) = $93, Close = $97, High = $98, Low = $92

In this example, the third day's closing price ($97) is higher than the first day's high ($101), confirming a bullish 3-bar [reversal](../r/reversal.md).

### Bearish Reversal:
* **Day 1**: [Open](../o/open.md) = $100, Close = $105, High = $106, Low = $99
* **Day 2**: [Open](../o/open.md) = $104, Close = $107, High = $108, Low = $103
* **Day 3**: [Open](../o/open.md) = $106, Close = $102, High = $107, Low = $100

Here, the third day's closing price ($102) is lower than the first day’s low ($100), indicating a bearish 3-bar [reversal](../r/reversal.md).

## Applications in Algorithmic Trading
Algorithmic traders use 3-bar [reversal patterns](../r/reversal_patterns.md) to automate the decision-making process. The pattern is incorporated into [trading algorithms](../t/trading_algorithms.md) to:

1. **Identify Entry Points**: The completion of a 3-bar [reversal](../r/reversal.md) pattern is treated as a signal to enter a [trade](../t/trade.md) in the direction of the [reversal](../r/reversal.md).
2. **Set [Stop-Loss Orders](../s/stop-loss_orders.md)**: To manage [risk](../r/risk.md), [stop-loss orders](../s/stop-loss_orders.md) are often set at the high (for bearish reversals) or low (for bullish reversals) of the [reversal](../r/reversal.md) bar.
3. **Optimize Algorithms**: [Backtesting](../b/backtesting.md) on historical data is used to optimize parameters and ensure the effectiveness of the 3-bar [reversal](../r/reversal.md) strategy.

## Coding the 3-Bar Reversal Strategy

### Python Example with `pandas`
```python
[import](../i/import.md) pandas as pd

def identify_3_bar_reversal(data):
    signals = []

    for i in [range](../r/range.md)(2, len(data)):
        first_bar = data.iloc[i-2]
        second_bar = data.iloc[i-1]
        third_bar = data.iloc[i]

        # [Check](../c/check.md) Bullish [Reversal](../r/reversal.md)
        if (first_bar['Close'] < first_bar['[Open](../o/open.md)'] and
            second_bar['Close'] < first_bar['Close'] and
            third_bar['Close'] > third_bar['[Open](../o/open.md)'] and
            third_bar['Close'] > first_bar['High']):
            signals.append((data.[index](../i/index_instrument.md)[i], "BUY"))

        # [Check](../c/check.md) Bearish [Reversal](../r/reversal.md)
        elif (first_bar['Close'] > first_bar['[Open](../o/open.md)'] and
              second_bar['Close'] > first_bar['Close'] and
              third_bar['Close'] < third_bar['[Open](../o/open.md)'] and
              third_bar['Close'] < first_bar['Low']):
            signals.append((data.[index](../i/index_instrument.md)[i], "SELL"))

    [return](../r/return.md) signals

# Sample Data
data = pd.DataFrame{
    '[Open](../o/open.md)': [100, 94, 93, 100, 104, 106],
    'Close': [95, 92, 97, 105, 107, 102],
    'High': [101, 96, 98, 106, 108, 107],
    'Low': [94, 91, 92, 99, 103, 100]
}, [index](../i/index_instrument.md)=pd.date_range(start='2023-01-01', periods=6))

signals = identify_3_bar_reversal(data)
print(signals)
```

## Limitations of the 3-Bar Reversal
Although effective, the 3-bar [reversal](../r/reversal.md) pattern has its limitations:
1. **[False Signals](../f/false_signals_in_trading.md)**: Like all trading patterns, it can generate [false signals](../f/false_signals_in_trading.md), leading to potential losses.
2. **Parameter Sensitivity**: The effectiveness can vary with different [market](../m/market.md) conditions and instrument types.
3. **[Lagging Indicator](../l/lagging_indicator.md)**: Being a [reversal](../r/reversal.md) pattern, it lags behind the current [price action](../p/price_action.md) and may miss the optimal entry or exit points.

## Case Study: QuantConnect Integration
[QuantConnect](../q/quantconnect.md) is a cloud-based platform that provides [algorithmic trading](../a/algorithmic_trading.md) [infrastructure](../i/infrastructure.md) capable of implementing various [trading strategies](../t/trading_strategies.md), including the 3-bar [reversal](../r/reversal.md) pattern. Users can write code in Python, C#, or F# to backtest and deploy their strategies.

### Implementation Example:
```python
from AlgorithmImports [import](../i/import.md) *

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

            # [Check](../c/check.md) for Bullish [Reversal](../r/reversal.md)
            if (first_bar.Close < first_bar.[Open](../o/open.md) and
                second_bar.Close < first_bar.Close and
                third_bar.Close > third_bar.[Open](../o/open.md) and
                third_bar.Close > first_bar.High):
                self.SetHoldings("SPY", 1)
                self.Debug(f"BUY Signal on {self.Time}")

            # [Check](../c/check.md) for Bearish [Reversal](../r/reversal.md)
            elif (first_bar.Close > first_bar.[Open](../o/open.md) and
                  second_bar.Close > first_bar.Close and
                  third_bar.Close < third_bar.[Open](../o/open.md) and
                  third_bar.Close < first_bar.Low):
                self.SetHoldings("SPY", -1)
                self.Debug(f"SELL Signal on {self.Time}")
```

## Conclusion
The 3-Bar [Reversal](../r/reversal.md) is a powerful pattern for detecting potential [trend](../t/trend.md) reversals in [financial markets](../f/financial_market.md). Its structured nature facilitates easy integration into [algorithmic trading](../a/algorithmic_trading.md) systems, where it can be used to trigger buy and sell signals based on predefined criteria. However, it's essential to consider its limitations and backtest thoroughly to ensure its effectiveness in different [market](../m/market.md) conditions.

By leveraging platforms like [QuantConnect](../q/quantconnect.md), traders can develop, backtest, and deploy sophisticated strategies that incorporate the 3-bar [reversal](../r/reversal.md) pattern, aligning automated decisions with their trading goals.
