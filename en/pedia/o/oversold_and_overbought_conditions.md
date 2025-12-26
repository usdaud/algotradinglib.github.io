# Oversold and Overbought Conditions

In the context of [financial markets](../f/financial_market.md), the terms "[oversold](../o/oversold.md)" and "[overbought](../o/overbought.md)" are widely used to indicate potential [reversal](../r/reversal.md) points by identifying when assets have moved too far in a single direction. These concepts serve as crucial indicators in both manual and [algorithmic trading](../a/algorithmic_trading.md) strategies. This detailed overview [will](../w/will.md) explore these conditions, how they are measured, and their application in algotrading.

### Definitions
- **[Oversold](../o/oversold.md) Condition**: An [asset](../a/asset.md) is deemed "[oversold](../o/oversold.md)" when its price has fallen sharply and to a level considered lower than its true [value](../v/value.md), often due to panic selling or extreme [market](../m/market.md) reactions. This suggests that the [asset](../a/asset.md) might be [undervalued](../u/undervalued.md) and due for a price [correction](../c/correction.md) or [reversal](../r/reversal.md).

- **[Overbought](../o/overbought.md) Condition**: Conversely, an "[overbought](../o/overbought.md)" condition describes a situation where an [asset](../a/asset.md)'s price has risen sharply and potentially beyond its true [value](../v/value.md), typically due to exuberant buying. This indicates the likelihood of a [downtrend](../d/downtrend.md) or price [correction](../c/correction.md).

### Indicators to Identify Oversold and Overbought Conditions

#### Relative Strength Index (RSI)
The [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI) is one of the most commonly used [momentum oscillators](../m/momentum_oscillators.md) for identifying [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions. Developed by J. Welles Wilder Jr., RSI ranges from 0 to 100, with levels generally interpreted as follows:
- RSI above 70: [Overbought](../o/overbought.md)
- RSI below 30: [Oversold](../o/oversold.md)

The RSI formula is:

```
RSI = 100 - [100 / (1 + RS)]
```

Where RS ([Relative Strength](../r/relative_strength.md)) is the average of 'n' days' up closes divided by the average of 'n' days' down closes.

#### Moving Average Convergence Divergence (MACD)
MACD is another popular tool. It measures the relationship between two exponential moving averages (EMAs) of a [security](../s/security.md)’s price. The calculation involves:
- MACD Line: (12-day EMA - 26-day EMA)
- Signal Line: 9-day EMA of the MACD Line

[Overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions in MACD are often identified by analysing the difference between these lines, known as a [histogram](../h/histogram.md):
- A large positive MACD [value](../v/value.md) suggests that the [security](../s/security.md) may be [overbought](../o/overbought.md).
- A large negative MACD [value](../v/value.md) indicates that the [security](../s/security.md) may be [oversold](../o/oversold.md).

#### Stochastic Oscillator
Created by George Lane, the [stochastic oscillator](../s/stochastic_oscillator.md) compares a specific closing price of a [security](../s/security.md) to a [range](../r/range.md) of its prices over a certain period:
- Values above 80 typically indicate [overbought](../o/overbought.md) conditions.
- Values below 20 indicate [oversold](../o/oversold.md) conditions.

The formula is:

```
%K = (Current Close - Lowest Low) / (Highest High - Lowest Low) * 100
%D = 3-day SMA of %K
```

### Application in Algorithmic Trading

#### Trading Algorithms
[Algorithmic trading](../a/algorithmic_trading.md) leverages mathematical and statistical models to execute trades based on pre-determined criteria. For detecting [oversold](../o/oversold.md) and [overbought](../o/overbought.md) conditions, algorithms integrate [technical indicators](../t/technical_indicators.md) like RSI, MACD, and stochastic oscillators within their codebase to generate [trading signals](../t/trading_signals.md). These signals can trigger buy/sell orders automatically when certain thresholds are met.

##### Sample Algorithm Strategy
Consider a simple strategy using the RSI:

1. **Buy Signal**: If the RSI drops below 30 ([oversold](../o/oversold.md)), buy the [asset](../a/asset.md).
2. **Sell Signal**: If the RSI rises above 70 ([overbought](../o/overbought.md)), sell the [asset](../a/asset.md).

This algorithm can be refined with additional parameters such as stop-loss and take-[profit](../p/profit.md) levels to manage [risk](../r/risk.md).

```python
class SimpleRSIStrategy:
    def __init__(self, [asset](../a/asset.md), period=14, rsi_oversold=30, rsi_overbought=70):
        self.[asset](../a/asset.md) = [asset](../a/asset.md)
        self.period = period
        self.rsi_oversold = rsi_oversold
        self.rsi_overbought = rsi_overbought

    def calculate_rsi(self, prices):
        gains = [0 if x<0 else x for x in [i - j for i, j in zip(prices[1:], prices[:-1])]]
        losses = [-x if x<0 else 0 for x in [i - j for i, j in zip(prices[1:], prices[:-1])]]
        average_gain = sum(gains) / self.period
        average_loss = sum(losses) / self.period
        rs = average_gain / average_loss
        rsi = 100 - (100 / (1 + rs))
        [return](../r/return.md) rsi

    def generate_signals(self, prices):
        if len(prices) < self.period:
            [return](../r/return.md) None
        rsi = self.calculate_rsi(prices)
        if rsi < self.rsi_oversold:
            [return](../r/return.md) 'buy'
        elif rsi > self.rsi_overbought:
            [return](../r/return.md) 'sell'
        [return](../r/return.md) '[hold](../h/hold.md)'
```

#### Backtesting
Before deploying such strategies in live markets, [backtesting](../b/backtesting.md) is crucial. [Backtesting](../b/backtesting.md) involves running the algorithm against historical data to evaluate performance. High win rates or returns in backtests suggest a potentially profitable strategy when applied to future [market](../m/market.md) conditions.

##### Sample Backtest Framework
```python
from datetime [import](../i/import.md) datetime

class Backtester:
    def __init__(self, strategy, historical_data):
        self.strategy = strategy
        self.historical_data = historical_data

    def run_backtest(self):
        positions = []
        signals = []
        for i in [range](../r/range.md)(len(self.historical_data)):
            prices = self.historical_data[:i+1]
            signal = self.strategy.generate_signals(prices)
            signals.append(signal)
            if signal == 'buy':
                positions.append({"action": "buy", "price": prices[-1], "date": datetime.now()})
            elif signal == 'sell' and positions:
                bought_position = positions.pop()
                profit_loss = prices[-1] - bought_position["price"]
                print(f'Sold at {prices[-1]}. Bought at {bought_position["price"]}. [Profit](../p/profit.md)/Loss: {profit_loss}')

# Sample historical data (e.g., closing prices)
historical_prices = [100, 102, 101, 98, 95, 90, 85, 88, 92, 95, 97, 98, 100]
strategy = SimpleRSIStrategy([asset](../a/asset.md)='ABC')
backtester = Backtester(strategy, historical_prices)
backtester.run_backtest()
```

### Psychological Considerations
Traders should be aware that [oversold](../o/oversold.md) and [overbought indicators](../o/overbought_indicators.md) do not guarantee reversals. [Market sentiment](../m/market_sentiment.md), economic factors, and unexpected news can influence prices beyond [technical indicators](../t/technical_indicators.md). Therefore, incorporating [risk management](../r/risk_management.md) strategies is always essential.

### Notable Companies Specializing in Algorithmic Trading and Analytics
Several companies [offer](../o/offer.md) platforms and tools for developing and deploying [algorithmic trading](../a/algorithmic_trading.md) strategies:

- **[QuantConnect](../q/quantconnect.md)**- **[AlgoTrader](../a/algotrader.md)**- **Quantopian** (now part of [Robinhood](../r/robinhood.md))- **Kite by [Zerodha](../z/zerodha.md)**
### Conclusion
Understanding and applying the concepts of [oversold](../o/oversold.md) and [overbought](../o/overbought.md) conditions in [algorithmic trading](../a/algorithmic_trading.md) can provide valuable insights and improve trading efficacy. Utilizing [technical indicators](../t/technical_indicators.md) like RSI, MACD, and stochastic oscillators within algorithmic systems enables traders to identify potential [market](../m/market.md) reversals and make informed trading decisions. However, these indicators should be part of a broader strategy that includes [risk management](../r/risk_management.md) and thorough [backtesting](../b/backtesting.md) to enhance profitability and reduce potential losses.
