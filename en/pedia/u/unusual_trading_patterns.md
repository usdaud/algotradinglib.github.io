# Unusual Trading Patterns

In the realm of financial markets, trading patterns refer to recognizable geometric shapes or movements in price charts that are consistent enough to offer predictive power for future price movements. These trading patterns are critical for traders, especially in algorithmic trading (often referred to as algo trading), where the development and backtesting of strategies are highly reliant on identifying such patterns. However, traditional trading patterns (like head and shoulders, cup and handle, etc.) are well-studied and well-understood by many traders. What sets the experts apart is their ability to recognize and leverage unusual trading patterns that aren't as widely known or acknowledged. In this context, we will explore some less conventional and more sophisticated trading patterns that can offer significant trading advantages.

## 1. **Abandoned Baby Pattern**

The 'Abandoned Baby' pattern is a rare but valuable reversal signal that traders and algorithms can use to detect a change in market sentiment. A bullish abandoned baby consists of:
1. A large bearish candle.
2. A doji candle that gaps down from the previous candle.
3. A large bullish candle that gaps up from the doji.

Conversely, a bearish abandoned baby involves:
1. A large bullish candle.
2. A doji candle that gaps up from the previous candle.
3. A large bearish candle that gaps down from the doji.

Since the pattern in itself shows extensive gaps indicating a sudden change in the market momentum, algorithms can be programmed to identify such gaps and execute trades accordingly.

Web Resources:
- **TradingView** [Abandoned Baby Guide](https://www.tradingview.com/chart-patterns/abandoned-baby/)

## 2. **Waterfall Decline Pattern**

The 'Waterfall Decline' pattern occurs when an asset experiences a sharp, rapid decline through a series of consecutive declining candlesticks with little to no retracement. This pattern suggests strong bearish momentum and can often precede a significant correction or reversal.

### Key Features:
- Series of four to seven consecutive bearish candlesticks.
- Small body candles indicative of strong sell pressure.
- Often followed by a short-term bounce or a steep decline continuation.

### Algorithmic Detection:
Using Moving Averages and Relative Strength Index (RSI), trading algorithms can detect the sharp downward movements and trigger short-selling strategies. 

## 3. **Diamond Top/Bottom Patterns**

Diamond patterns are rare but can be powerful indicators of trend reversals. A 'Diamond Top' typically indicates a bullish-to-bearish reversal, while a 'Diamond Bottom' suggests a bearish-to-bullish reversal.

### Key Phases:
1. Initial trend (uptrend for Diamond Top, downtrend for Diamond Bottom).
2. Broadening phase where price volatility increases.
3. Symmetrical narrowing signifying a contraction in price movement.
4. Breakout from the narrowing range confirming the pattern.

### Practical Implementation:
Automated trading systems can recognize diamond shapes by analyzing price peaks and troughs. After validating the symmetry and volume trends within the pattern, algorithms can execute trades anticipating the reversal.

## 4. **Bump and Run Reversal Pattern**

Described in the notable work by Thomas Bulkowski, the 'Bump and Run Reversal' pattern is an unusual yet effective signal of an impending price reversal. This pattern generally occurs in three phases:
1. **Lead-in Phase**: Gentle slope of price increases.
2. **Bump Phase**: Rapid acceleration in price, creating a steep slope.
3. **Run Phase**: Price reverses and declines back to the Lead-in trendline.

### Trading Strategy:
Identifying the 'bump' phase is crucial. By defining a threshold for the acceleration slope, trading algorithms can trigger alerts and position adjustments to capitalize on the forthcoming 'run' phase.

## 5. **Scallop Patterns**

Scallop patterns are curved formations that signify continuations or reversals, depending on their orientation (bullish scallops rise, bearish scallops fall). They are less straightforward but can offer excellent entry points once identified.

### Identification Steps:
1. A prior trend (uptrend for bullish, downtrend for bearish).
2. A rounded price movement that appears as a 'U'-shape.
3. A breakout that confirms the continuation of the prior trend.

### Automation:
By employing polynomial regression lines, trading algorithms can fit curves to detect scallop shapes, confirming a potential continuation or reversal signal.

## 6. **Three-Line Strike Pattern**

The 'Three-Line Strike' pattern is a rare occurrence but a robust reversal indicator that consists of three same-color candles followed by a large candle in the opposite color that engulfs the previous three.

### Detection:
1. Identify three consecutive candles moving in one direction (up/down).
2. Spot an engulfing candle that completely negates the movement of the three.

### Algo Consideration:
Specific rules about candle body sizes and volume changes are programmed into the system to catch these patterns and act swiftly.

## 7. **Island Reversal Pattern**

'Island Reversal' patterns involve a solitary candlestick or a group of candlesticks isolated by gaps on either side, forming an "island". This pattern indicates a strong reversal signal.

### Phases:
1. Strong trend (up/down).
2. Gap creating an isolated candle or group of candles (the island).
3. Gap in the opposite direction, confirming the reversal.

### Application:
Gap detection algorithms are essential, ensuring that the gaps are sufficiently wide to validate the pattern. Volume spikes and price gaps are additional layers of confirmation.

## 8. **Hikkake Pattern**

The 'Hikkake Pattern' consists of a failed breakout, leading to a reversal. It's a subtle but powerful pattern discovered by Dan Chesler.

### Structure:
1. An inside bar indicating consolidation.
2. A breakout bar that moves outside the inside bar's range.
3. A subsequent bar that closes within the range of the inside bar, indicating a failed breakout.

### Strategy:
Algorithms track inside bars and breakout failures, setting triggers when the conditions of this pattern emerge, allowing for entry against the initial breakout direction.

## 9. **Wolfe Wave Pattern**

The 'Wolfe Wave' pattern is a natural, harmonically balanced formation created by supply and demand. It anticipates where the price is heading and is often used by contrarian traders.

### Elements:
1. Five-wave structure versus the trend.
2. Lines connecting waves one and three, and waves two and four, forming a wedge.
3. Target lines projecting from wave one through wave four.

### Execution:
Pattern recognition algorithms plot these waves, ensuring accuracy, especially in dynamic markets. Wolfe Waves often provide precise entry and exit points.

[AlgoTrading Company](https://www.algotradingcompany.com)

## 10. **Gartley Pattern**

The 'Gartley Pattern' is a complex harmonic pattern involving Fibonacci retracements. It was identified by H.M. Gartley in his book 'Profits in the Stock Market.'

### Components:
1. Initial price move (X to A).
2. Retracement (A to B), forming a 61.8% or 78.6% Fibonacci level.
3. Extension (B to C) and retracement (C to D), following the 78.6% level.

### Detection:
Algorithmic systems, leveraging Fibonacci algorithms, scan for these retracements and extensions, executing trades at the 'D' point where the likelihood of reversal is high.

[H.M. Gartley's Book](https://www.bookstore.com/hm-gartley-profits-stock-market)

## Conclusion

Unusual trading patterns offer sophisticated traders and algorithms significant advantages in anticipating market movements more accurately and earlier than the more traditional patterns. The ability to detect, understand, and execute trades based on these patterns involves integrating advanced pattern recognition algorithms, sophisticated backtesting, and a keen understanding of market behavior. These strategies encompass a mix of classic technical analysis augmented with cutting-edge algorithmic detection methods, providing a robust approach to exploiting market inefficiencies.