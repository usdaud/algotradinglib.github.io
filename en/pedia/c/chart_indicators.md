# Chart Indicators

In the realm of [algorithmic trading](../a/algorithmic_trading.md) (or algo trading), chart indicators play a crucial role in making informed trading decisions. Chart indicators, also known as [technical indicators](../t/technical_indicators.md), are mathematical calculations based on the price, volume, or open interest of a security or contract. The primary goal of these indicators is to predict future price movements and trends, facilitating traders to make more rational decisions. Below, a detailed exploration of chart indicators, their types, and their applications in [algorithmic trading](../a/algorithmic_trading.md) is presented.

### Moving Averages

#### Simple Moving Average (SMA)
Simple Moving Average (SMA) is one of the most common and straightforward indicators. It calculates the average of a selected range of prices, typically closing prices, by the number of periods in that range. 
```markdown
SMA = (P1 + P2 + ... + Pn) / n
```
Where P1, P2, ..., Pn are the closing prices of the security for n periods.

#### Exponential Moving Average (EMA)
Exponential Moving Average (EMA) gives more weight to the most recent prices, making it more sensitive to recent price moves. It reacts more quickly to price changes compared to SMA.
```markdown
EMA_today = (Price_today * K) + (EMA_yesterday * (1 - K))
K = 2 / (n + 1)
```

### Relative Strength Index (RSI)

The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. Oscillating between 0 and 100, RSI is typically used to identify overbought or oversold conditions in a market.
```markdown
RSI = 100 - (100 / (1 + RS))
RS = Average Gain / Average Loss
```

### Moving Average Convergence Divergence (MACD)

MACD is a trend-following momentum indicator that shows the relationship between two moving averages of prices. The formula is:
```markdown
MACD = EMA(12) - EMA(26)
Signal Line = EMA(9 of MACD)
```
### Bollinger Bands

[Bollinger Bands](../b/bollinger_bands.md) are volatility bands placed above and below a moving average. Volatility is based on the standard deviation, which changes as volatility increases and decreases. The bands are named after their inventor, John Bollinger.
```markdown
Middle Band = 20-day SMA
Upper Band = Middle Band + (20-day Standard Deviation of Price * 2)
Lower Band = Middle Band - (20-day Standard Deviation of Price * 2)
```

### Stochastic Oscillator

The [Stochastic Oscillator](../s/stochastic_oscillator.md) is a momentum indicator comparing a particular closing price of a security to a range of its prices over a certain period. It generates values between 0 and 100.
```markdown
%K = (Current Close - Lowest Low) / (Highest High - Lowest Low) * 100
%D = 3-day SMA of %K
```

### Fibonacci Retracement

Fibonacci Retracement is a method of [technical analysis](../t/technical_analysis.md) for determining potential [support and resistance](../s/support_and_resistance.md) levels. They are created by taking two extreme points (major peak and trough) on a stock chart and dividing the vertical distance by the key Fibonacci ratios of 23.6%, 38.2%, 50%, 61.8%, and 100%.

### Ichimoku Cloud

The [Ichimoku Cloud](../i/ichimoku_cloud.md) is a collection of [technical indicators](../t/technical_indicators.md) that show [support and resistance](../s/support_and_resistance.md) levels, as well as momentum and trend direction. It is made up of five lines, and the space between two of these lines is shaded in, creating what is known as the cloud.
```markdown
Tenkan-sen (Conversion Line) = (9-period high + 9-period low) / 2
Kijun-sen (Base Line) = (26-period high + 26-period low) / 2
Senkou Span A (Leading Span A) = (Conversion Line + Base Line) / 2
Senkou Span B (Leading Span B) = (52-period high + 52-period low) / 2
Chikou Span (Lagging Span) = Close plotted 26 days in the past
```

### Average True Range (ATR)

ATR is a measure of volatility introduced by market technician J. Welles Wilder Jr. The ATR of a market is the average of the true ranges over a specified period.
```markdown
True Range (TR) = max[(High - Low), abs(High - Previous Close), abs(Low - Previous Close)]
ATR = Moving Average of TR over a specified period, usually 14-days.
```

### On-Balance Volume (OBV)

On-Balance Volume (OBV) is a momentum indicator that uses volume flow to predict changes in stock price. The idea behind OBV is that volume precedes price; hence, OBV rises or falls before the stock price.

### Commodity Channel Index (CCI)

CCI is a momentum-based oscillator used to help determine when an investment vehicle is reaching a condition of being overbought or oversold.
```markdown
CCI = (Typical Price - SMA) / (0.015 * Mean Deviation)
Typical Price (TP) = (High + Low + Close) / 3
```

### Parabolic SAR (Stop and Reverse)

The [Parabolic SAR](../p/parabolic_sar.md) is used to determine the direction of an asset's momentum and the point in time when this momentum has a higher-than-normal probability of switching directions. It trails the price as a trend develops and can potentially be useful to set a trailing stop.
```markdown
SAR(Tomorrow) = SAR(Today) + AF [EP(Today) – SAR(Today)]
Where AF (Acceleration Factor) starts at 0.02 and increases by 0.02, with a maximum of 0.20.

EP (Extreme Point) is the highest high for an uptrend or the lowest low for a downtrend.
```

### Pivot Point

[Pivot points](../p/pivot_points.md) are used to identify potential [support and resistance](../s/support_and_resistance.md) levels. They are calculated using the high, low, and closing prices of the previous trading session.
```markdown
Pivot Point (P) = (High + Low + Close) / 3
Support 1 (S1) = (P x 2) – High
Resistance 1 (R1) = (P x 2) – Low
```

### Chaikin Money Flow (CMF)

CMF is a volume-weighted average of accumulation and distribution over a specified period. It gauges the buying and selling pressure for a financial asset during a given period.
```markdown
CMF = ∑ [(Close - Low) - (High - Close)] / (High - Low) * Volume / Total Volume over a specified period
```

### Volume Weighted Average Price (VWAP)

VWAP provides the average price a security has traded at throughout the day, based on both volume and price. It provides deeper insight into where the market has traded most heavily.
```markdown
VWAP = Cumulative (Price * Volume) / Cumulative Volume
```

### Williams %R

[Williams %R](../w/williams_%r.md) is a momentum indicator that measures overbought and oversold levels, similar to the [Stochastic Oscillator](../s/stochastic_oscillator.md).
```markdown
%R = (Highest High - Close) / (Highest High - Lowest Low) * -100
```

### Keltner Channels

[Keltner Channels](../k/keltner_channels.md) are volatility-based envelopes set above and below an exponential moving average.
```markdown
Middle Line = EMA
Upper Envelop = EMA + (ATR * 2)
Lower Envelop = EMA - (ATR * 2)
```

### Custom Indicators in Algorithmic Trading

In [algorithmic trading](../a/algorithmic_trading.md), custom indicators can be created by combining two or more of the standard indicators or by modifying the calculations according to specific requirements. With the versatility of programming languages such as Python, R, or C++, traders can implement and back-test their unique strategies using custom indicators.

### Companies Providing Chart Indicators Services

Several platforms and companies provide comprehensive tools for [technical analysis](../t/technical_analysis.md), including chart indicators. Some notable mentions include:

- **[TradingView](../t/tradingview.md)**: A financial visualization platform that offers a broad array of charts and indicators, enabling traders to perform complex [technical analysis](../t/technical_analysis.md). [TradingView](https://www.tradingview.com)
- **MetaTrader 4 and 5**: Trading platforms widely used for forex and CFD trading, providing numerous built-in [technical indicators](../t/technical_indicators.md) and the ability to script custom ones. [MetaTrader](https://www.metatrader4.com/)
- **[Thinkorswim](../t/thinkorswim.md)**: Offered by TD [Ameritrade](../a/ameritrade.md), [Thinkorswim](../t/thinkorswim.md) is a professional-level trading platform providing a wide range of [technical analysis](../t/technical_analysis.md) tools and indicators. [Thinkorswim](https://www.thinkorswim.com/)
- **[NinjaTrader](../n/ninjatrader.md)**: Known for its advanced charting and trading capabilities, [NinjaTrader](../n/ninjatrader.md) offers extensive support for [algorithmic trading](../a/algorithmic_trading.md) and custom indicator development. [NinjaTrader](https://ninjatrader.com/)

### Conclusion

Chart indicators are an indispensable part of [algorithmic trading](../a/algorithmic_trading.md), providing insights into market trends, volatility, and momentum. Mastery of these tools enables traders to develop more effective [trading strategies](../t/trading_strategies.md) that can be back-tested and optimized. Whether using standard indicators or developing custom ones, understanding how these indicators work and their appropriate application can significantly enhance [trading performance](../t/trading_performance.md).