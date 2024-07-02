# Technical Analysis Frameworks

[Technical analysis](../t/technical_analysis.md) is an essential component of [algorithmic trading](../a/algorithmic_trading.md), where historical market data is analyzed to predict future price movements. Unlike [fundamental analysis](../f/fundamental_analysis.md) that considers [economic indicators](../e/economic_indicators.md) and financial statements, [technical analysis](../t/technical_analysis.md) focuses solely on price charts, trading volume, and other market-generated data. This document delves into various popular [technical analysis](../t/technical_analysis.md) frameworks employed in [algorithmic trading](../a/algorithmic_trading.md).

### Moving Averages

#### Simple Moving Average (SMA)
The Simple Moving Average (SMA) is the arithmetic mean of a given set of prices over a specified number of periods. It smooths out price data to identify trends over time.

**Formula:**
\[ \text{SMA} = \frac{P_1 + P_2 + ... + P_n}{n} \]

#### Exponential Moving Average (EMA)
The Exponential Moving Average (EMA) gives more weight to the most recent prices, making it more responsive to new information.

**Formula:**
\[ \text{EMA}_t = \alpha \cdot P_t + (1 - \alpha) \cdot EMA_{t-1} \]
Where \( \alpha = \frac{2}{n + 1} \)

#### Moving Average Convergence Divergence (MACD)
MACD is a trend-following momentum indicator that shows the relationship between two moving averages of prices.

**Formulas:**
\[ \text{MACD Line} = EMA_{12} - EMA_{26} \]
\[ \text{Signal Line} = EMA_9(\text{MACD Line}) \]

### Relative Strength Index (RSI)

The Relative Strength Index (RSI) measures the magnitude of recent price changes to evaluate overbought or oversold conditions in asset prices.

**Formula:**
\[ RSI = 100 - \frac{100}{1 + RS} \]
\[ RS = \frac{\text{Average Gain}}{\text{Average Loss}} \]

### Bollinger Bands

[Bollinger Bands](../b/bollinger_bands.md) consist of a middle band (usually a 20-day SMA) and two outer bands set two standard deviations away from the middle band, capturing volatility.

**Formulas:**
\[ \text{Middle Band} = 20\text{-day SMA} \]
\[ \text{Upper Band} = \text{Middle Band} + (2 \cdot \sigma_{20}) \]
\[ \text{Lower Band} = \text{Middle Band} - (2 \cdot \sigma_{20}) \]

### Stochastic Oscillator

The [Stochastic Oscillator](../s/stochastic_oscillator.md) compares a particular closing price of an asset to its price range over a period, providing indications of momentum.

**Formulas:**
\[ \%K = \frac{(C - L_{14})}{(H_{14} - L_{14})} \times 100 \]
\[ \%D = 3\text{-day SMA of } \%K \]

### Fibonacci Retracement

Fibonacci retracement levels are horizontal lines that indicate possible [support and resistance](../s/support_and_resistance.md) levels based on the Fibonacci sequence. Key levels include 23.6%, 38.2%, 50%, 61.8%, and 100%.

### Ichimoku Cloud

Ichimoku Kinko Hyo ([Ichimoku Cloud](../i/ichimoku_cloud.md)) provides [support and resistance](../s/support_and_resistance.md) levels along with trend direction, momentum, and [trading signals](../t/trading_signals.md).

#### Components:
- **Tenkan-sen (Conversion Line)**
\[ \text{Tenkan-sen} = \frac{(\text{Highest High} + \text{Lowest Low})}{2} \text{ for the past 9 periods} \]

- **Kijun-sen (Base Line)**
\[ \text{Kijun-sen} = \frac{(\text{Highest High} + \text{Lowest Low})}{2} \text{ for the past 26 periods} \]

- **Senkou Span A (Leading Span A)**
\[ \text{Senkou Span A} = \frac{(\text{Tenkan-sen} + \text{Kijun-sen})}{2} \]

- **Senkou Span B (Leading Span B)**
\[ \text{Senkou Span B} = \frac{(\text{Highest High} + \text{Lowest Low})}{2} \text{ for the past 52 periods} \]

- **Chikou Span (Lagging Span)**
\[ \text{Chikou Span} = \text{Current closing price shifted 26 periods back} \]

### Volume Analysis

#### On-Balance Volume (OBV)
OBV uses volume flow to predict changes in stock price. OBV is a cumulative total of volume, adding volume on up days and subtracting on down days.

**Formula:**
\[ OBV_t = OBV_{t-1} + V \text{ (if } P_t > P_{t-1}) \]
\[ OBV_t = OBV_{t-1} - V \text{ (if } P_t < P_{t-1}) \]

#### Volume-Weighted Average Price (VWAP)
VWAP calculates a trading period's average price, weighted by volume, often used to assess the efficiency of trade executions.

**Formula:**
\[ VWAP = \frac{\sum{(P_t \times V_t)}}{\sum{V_t}} \]

### Candlestick Patterns

[Candlestick patterns](../c/candlestick_patterns.md) visually depict price movements using bars representing open, high, low, and close (OHLC) prices for a given period.

#### Common Patterns:
- **Doji**: Indicates indecision, where the opening and closing prices are virtually the same.
- **Hammer**: A bullish reversal pattern, where a small body is at the upper end with a long lower wick.
- **Engulfing Pattern**: When a larger candle follows and engulfs a smaller preceding candle, indicating a potential reversal.

### Advanced Techniques

#### Machine Learning and AI
Algorithmic traders increasingly employ machine learning and artificial intelligence to enhance [technical analysis](../t/technical_analysis.md) strategies. Techniques such as supervised learning, unsupervised learning, and reinforcement learning are used to identify patterns and optimize [trading algorithms](../t/trading_algorithms.md).

#### Backtesting and Optimization
[Backtesting](../b/backtesting.md) involves testing a trading strategy using historical data to validate its effectiveness. Algorithmic traders use [backtesting](../b/backtesting.md) tools like QuantConnect (https://www.quantconnect.com/) and MetaTrader 5 (https://www.metatrader5.com/) to fine-tune their strategies.

#### Algorithmic Trading Platforms
Several platforms enable algorithmic traders to deploy and manage their strategies, often integrating [technical analysis](../t/technical_analysis.md) frameworks.

- **QuantConnect**: An open-source cloud platform for [algorithmic trading](../a/algorithmic_trading.md) and [quantitative research](../q/quantitative_research.md).
  [QuantConnect](https://www.quantconnect.com/)
  
- **MetaTrader 5**: A popular platform offering comprehensive tools for both [technical analysis](../t/technical_analysis.md) and [algorithmic trading](../a/algorithmic_trading.md).
  [MetaTrader 5](https://www.metatrader5.com/)
  
- **Interactive Brokers**: Offers advanced trading tools, including algo trading capabilities.
  [Interactive Brokers](https://www.interactivebrokers.com/)

### Conclusion

[Technical analysis](../t/technical_analysis.md) frameworks play a crucial role in [algorithmic trading](../a/algorithmic_trading.md) by providing traders with actionable insights derived from historical market data. From moving averages and [momentum indicators](../m/momentum_indicators.md) to [candlestick patterns](../c/candlestick_patterns.md) and machine learning techniques, a wide range of tools is available to help traders develop robust [trading strategies](../t/trading_strategies.md). As technology continues to evolve, the ability to incorporate advanced analytics and machine learning into [technical analysis](../t/technical_analysis.md) frameworks will further enhance the precision and effectiveness of [algorithmic trading](../a/algorithmic_trading.md).
