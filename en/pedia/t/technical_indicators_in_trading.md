# Technical Indicators

[Technical indicators](../t/technical_indicators.md) are mathematical calculations based on the historical price, [volume](../v/volume.md), or [open interest](../o/open_interest.md) of a [security](../s/security.md) or contract. Traders use these indicators in [technical analysis](../t/technical_analysis.md) to predict future price movements in the markets. Here, we [will](../w/will.md) discuss some of the most commonly used [technical indicators](../t/technical_indicators.md) in trading, their calculation methods, and how traders can use them to develop [trading strategies](../t/trading_strategies.md).

### Moving Averages

Moving Averages (MAs) are one of the most popular [technical indicators](../t/technical_indicators.md) used by traders. They smooth out price data to create a single flowing line, making it easier to identify the direction of the [trend](../t/trend.md). 

#### Simple Moving Average (SMA)

The Simple Moving Average is calculated by adding the closing prices of a [security](../s/security.md) over a specific number of periods and then dividing the sum by the number of periods.

**Formula:**
\[ \text{SMA} = \frac{\sum_{i=1}^{n} P_i}{n} \]
where:
- \( P_i \) is the closing price
- \( n \) is the number of periods

#### Exponential Moving Average (EMA)

The Exponential Moving Average gives more weight to recent prices, making it more responsive to new information.

**Formula:**
\[ \text{EMA} = \Big(\frac{P - \text{Previous EMA}}{K + 1}\Big) + \text{Previous EMA} \]
where:
- \( P \) is the current closing price
- \( K \) is the smoothing [factor](../f/factor.md)

### Relative Strength Index (RSI)

The [Relative Strength](../r/relative_strength.md) [Index](../i/index.md) is a [momentum](../m/momentum.md) [oscillator](../o/oscillator.md) that measures the speed and change of price movements. It oscillates between 0 and 100 and is typically used to identify [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions. 

**Formula:**
\[ \text{RSI} = 100 - \frac{100}{1 + \frac{\text{Average [Gain](../g/gain.md)}}{\text{Average Loss}}} \]

Traders use RSI by looking for readings above 70 indicating [overbought](../o/overbought.md) conditions, and readings below 30 indicating [oversold](../o/oversold.md) conditions.

### Moving Average Convergence Divergence (MACD)

The MACD is a [trend](../t/trend.md)-following [momentum](../m/momentum.md) [indicator](../i/indicator.md) that shows the relationship between two moving averages of a [security](../s/security.md)'s price. It consists of two components: the MACD line and the signal line. 

**Calculation:**
1. Calculate the 12-day EMA
2. Calculate the 26-day EMA
3. Subtract the 26-day EMA from the 12-day EMA to get the MACD line
4. Calculate the 9-day EMA of the MACD line to get the signal line

[Trading signals](../t/trading_signals.md) are generated when the MACD line crosses the signal line. 

### Bollinger Bands

[Bollinger Bands](../b/bollinger_bands.md) consist of three lines: a middle band (moving average usually set at 20 periods), and an upper and lower band. The distance between the bands is based on the [standard deviation](../s/standard_deviation.md) of price changes.

**Formula:**
- Middle Band: 20-day SMA
- Upper Band: 20-day SMA + (2 * [Standard Deviation](../s/standard_deviation.md))
- Lower Band: 20-day SMA - (2 * [Standard Deviation](../s/standard_deviation.md))

[Bollinger Bands](../b/bollinger_bands.md) are used to identify [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions.

### Stochastic Oscillator

The [Stochastic Oscillator](../s/stochastic_oscillator.md) is a [momentum](../m/momentum.md) [indicator](../i/indicator.md) that compares a particular closing price to a [range](../r/range.md) of prices over a specific period. It oscillates between 0 and 100.

**Formula:**
\[ \%K = \frac{(C - L14)}{(H14 - L14)} \times 100 \]
where:
- \( C \) is the most recent closing price
- \( L14 \) is the lowest price over the last 14 periods
- \( H14 \) is the highest price over the last 14 periods

The \%K line and \%D line (3-period moving average of \%K) are used to generate [trading signals](../t/trading_signals.md).

### Fibonacci Retracement

[Fibonacci retracement](../f/fibonacci_retracement.md) is based on the idea that markets [will](../w/will.md) retrace a predictable portion of a move, after which they [will](../w/will.md) continue to move in the original direction. Common [Fibonacci retracement](../f/fibonacci_retracement.md) levels are 23.6%, 38.2%, 50%, 61.8%, and 100%.

Traders use these levels as potential [support and resistance](../s/support_and_resistance.md) areas.

### Average Directional Index (ADX)

The [Average Directional Index](../a/average_directional_index_(adx).md) is used to quantify [trend](../t/trend.md) strength. It ranges from 0 to 100, with readings above 25 indicating a strong [trend](../t/trend.md). 

**Calculation:**
1. Calculate the True [Range](../r/range.md) (TR)
2. Calculate the +DI and -DI (Directional Indices)
3. Smooth the +DI and -DI using the moving average technique
4. Calculate the ADX by smoothing the difference between +DI and -DI

### Volume Indicators

[Volume indicators](../v/volume_indicators.md) use [volume](../v/volume.md) data to analyze [market](../m/market.md) strength or weakness.

#### On-Balance Volume (OBV)

The On-Balance [Volume](../v/volume.md) is a cumulative [volume](../v/volume.md)-based [indicator](../i/indicator.md) that measures buying and selling pressure.

**Formula:**
\[ \text{OBV} = \text{Previous OBV} + \text{Current [Volume](../v/volume.md) (if price closes up)} \]
\[ \text{OBV} = \text{Previous OBV} - \text{Current [Volume](../v/volume.md) (if price closes down)} \]

#### Chaikin Money Flow (CMF)

The Chaikin [Money Flow](../m/money_flow.md) uses price and [volume](../v/volume.md) to measure accumulation and [distribution](../d/distribution.md) over a specific period.

**Formula:**
\[ \text{CMF} = \frac{\sum_{i=1}^n \text{ADL}_i \cdot V_i}{\sum_{i=1}^n V_i} \]
where:
- \( ADL \) is the Accumulation/[Distribution](../d/distribution.md) Line
- \( V \) is the [volume](../v/volume.md)

### Companies Providing Technical Analysis Tools

Several companies provide platforms and tools that help traders use these [technical indicators](../t/technical_indicators.md). Here are a few notable ones:

- **[TradingView](../t/tradingview.md)**: A popular charting platform that provides numerous [technical indicators](../t/technical_indicators.md) and drawing tools. More info: [TradingView](https://www.tradingview.com/)
  
- **MetaTrader**: A widely used [trading platform](../t/trading_platform.md) [offering](../o/offering.md) a [range](../r/range.md) of [technical indicators](../t/technical_indicators.md). More info: [MetaTrader](https://www.metatrader4.com/)

- **[Thinkorswim](../t/thinkorswim.md) by TD [Ameritrade](../a/ameritrade.md)**: An advanced [trading platform](../t/trading_platform.md) with customizable [technical indicators](../t/technical_indicators.md). More info: [Thinkorswim](https://www.tdameritrade.com/tools-and-platforms/thinkorswim.page)

### Conclusion

[Technical indicators](../t/technical_indicators.md) are essential tools in a [trader](../t/trader.md)’s arsenal. They provide insights into price trends, [momentum](../m/momentum.md), [volatility](../v/volatility.md), and [volume](../v/volume.md), helping traders make informed decisions. While each [indicator](../i/indicator.md) has its strengths and weaknesses, combining them can create a more comprehensive [trading strategy](../t/trading_strategy.md).
