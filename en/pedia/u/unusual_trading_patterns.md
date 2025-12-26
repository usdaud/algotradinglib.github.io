# Unusual Trading Patterns

In the realm of [financial markets](../f/financial_market.md), trading patterns refer to recognizable geometric shapes or movements in price charts that are consistent enough to [offer](../o/offer.md) predictive power for future price movements. These trading patterns are critical for traders, especially in [algorithmic trading](../a/algorithmic_trading.md) (often referred to as algo trading), where the development and [backtesting](../b/backtesting.md) of strategies are highly reliant on identifying such patterns. However, traditional trading patterns (like head and shoulders, cup and [handle](../h/handle.md), etc.) are well-studied and well-understood by many traders. What sets the experts apart is their ability to recognize and [leverage](../l/leverage.md) unusual trading patterns that aren't as widely known or acknowledged. In this context, we [will](../w/will.md) explore some less conventional and more sophisticated trading patterns that can [offer](../o/offer.md) significant trading advantages.

## 1. **Abandoned Baby Pattern**

The 'Abandoned Baby' pattern is a rare but valuable [reversal](../r/reversal.md) signal that traders and algorithms can use to detect a change in [market sentiment](../m/market_sentiment.md). A [bullish abandoned baby](../b/bullish_abandoned_baby.md) consists of:
1. A large bearish candle.
2. A [doji](../d/doji.md) candle that [gaps](../g/gap.md) down from the previous candle.
3. A large bullish candle that [gaps](../g/gap.md) up from the [doji](../d/doji.md).

Conversely, a bearish abandoned baby involves:
1. A large bullish candle.
2. A [doji](../d/doji.md) candle that [gaps](../g/gap.md) up from the previous candle.
3. A large bearish candle that [gaps](../g/gap.md) down from the [doji](../d/doji.md).

Since the pattern in itself shows extensive [gaps](../g/gap.md) indicating a sudden change in the [market](../m/market.md) [momentum](../m/momentum.md), algorithms can be programmed to identify such [gaps](../g/gap.md) and execute trades accordingly.

Web Resources:
- **[TradingView](../t/tradingview.md)** Abandoned Baby Guide

## 2. **Waterfall Decline Pattern**

The 'Waterfall Decline' pattern occurs when an [asset](../a/asset.md) experiences a sharp, rapid decline through a series of consecutive declining candlesticks with little to no [retracement](../r/retracement.md). This pattern suggests strong bearish [momentum](../m/momentum.md) and can often precede a significant [correction](../c/correction.md) or [reversal](../r/reversal.md).

### Key Features:
- Series of four to seven consecutive bearish candlesticks.
- Small body candles indicative of strong sell pressure.
- Often followed by a short-term bounce or a steep decline continuation.

### Algorithmic Detection:
Using Moving Averages and [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI), [trading algorithms](../t/trading_algorithms.md) can detect the sharp downward movements and trigger short-selling strategies.

## 3. **Diamond Top/Bottom Patterns**

Diamond patterns are rare but can be powerful indicators of [trend](../t/trend.md) reversals. A 'Diamond Top' typically indicates a bullish-to-bearish [reversal](../r/reversal.md), while a 'Diamond Bottom' suggests a bearish-to-bullish [reversal](../r/reversal.md).

### Key Phases:
1. Initial [trend](../t/trend.md) ([uptrend](../u/uptrend.md) for Diamond Top, [downtrend](../d/downtrend.md) for Diamond Bottom).
2. Broadening phase where price [volatility](../v/volatility.md) increases.
3. Symmetrical narrowing signifying a contraction in price movement.
4. [Breakout](../b/breakout.md) from the narrowing [range](../r/range.md) confirming the pattern.

### Practical Implementation:
[Automated trading systems](../a/automated_trading_systems.md) can recognize diamond shapes by analyzing price peaks and troughs. After validating the symmetry and [volume](../v/volume.md) trends within the pattern, algorithms can execute trades anticipating the [reversal](../r/reversal.md).

## 4. **Bump and Run Reversal Pattern**

Described in the notable work by Thomas Bulkowski, the 'Bump and Run [Reversal](../r/reversal.md)' pattern is an unusual yet effective signal of an impending price [reversal](../r/reversal.md). This pattern generally occurs in three phases:
1. **Lead-in Phase**: Gentle slope of price increases.
2. **Bump Phase**: Rapid acceleration in price, creating a steep slope.
3. **Run Phase**: Price reverses and declines back to the Lead-in [trendline](../t/trendline.md).

### Trading Strategy:
Identifying the 'bump' phase is crucial. By defining a threshold for the acceleration slope, [trading algorithms](../t/trading_algorithms.md) can trigger alerts and position adjustments to [capitalize](../c/capitalize.md) on the forthcoming 'run' phase.

## 5. **Scallop Patterns**

Scallop patterns are curved formations that signify continuations or reversals, depending on their orientation (bullish scallops rise, bearish scallops fall). They are less straightforward but can [offer](../o/offer.md) excellent entry points once identified.

### Identification Steps:
1. A prior [trend](../t/trend.md) ([uptrend](../u/uptrend.md) for bullish, [downtrend](../d/downtrend.md) for bearish).
2. A rounded price movement that appears as a 'U'-shape.
3. A [breakout](../b/breakout.md) that confirms the continuation of the prior [trend](../t/trend.md).

### Automation:
By employing polynomial regression lines, [trading algorithms](../t/trading_algorithms.md) can fit curves to detect scallop shapes, confirming a potential continuation or [reversal](../r/reversal.md) signal.

## 6. **Three-Line Strike Pattern**

The 'Three-Line Strike' pattern is a rare occurrence but a [robust](../r/robust.md) [reversal](../r/reversal.md) [indicator](../i/indicator.md) that consists of three same-color candles followed by a large candle in the opposite color that engulfs the previous three.

### Detection:
1. Identify three consecutive candles moving in one direction (up/down).
2. Spot an engulfing candle that completely negates the movement of the three.

### Algo Consideration:
Specific rules about candle body sizes and [volume](../v/volume.md) changes are programmed into the system to catch these patterns and act swiftly.

## 7. **Island Reversal Pattern**

'Island [Reversal](../r/reversal.md)' patterns involve a solitary [candlestick](../c/candlestick.md) or a group of candlesticks isolated by [gaps](../g/gap.md) on either side, forming an "island". This pattern indicates a strong [reversal](../r/reversal.md) signal.

### Phases:
1. Strong [trend](../t/trend.md) (up/down).
2. Gap creating an isolated candle or group of candles (the island).
3. Gap in the opposite direction, confirming the [reversal](../r/reversal.md).

### Application:
Gap detection algorithms are essential, ensuring that the [gaps](../g/gap.md) are sufficiently wide to validate the pattern. [Volume](../v/volume.md) spikes and price [gaps](../g/gap.md) are additional layers of confirmation.

## 8. **Hikkake Pattern**

The '[Hikkake Pattern](../h/hikkake_pattern.md)' consists of a failed [breakout](../b/breakout.md), leading to a [reversal](../r/reversal.md). It's a subtle but powerful pattern discovered by Dan Chesler.

### Structure:
1. An inside bar indicating [consolidation](../c/consolidation.md).
2. A [breakout](../b/breakout.md) bar that moves outside the inside bar's [range](../r/range.md).
3. A subsequent bar that closes within the [range](../r/range.md) of the inside bar, indicating a failed [breakout](../b/breakout.md).

### Strategy:
Algorithms track inside bars and [breakout failures](../b/breakout_failures.md), setting triggers when the conditions of this pattern emerge, allowing for entry against the initial [breakout](../b/breakout.md) direction.

## 9. **Wolfe Wave Pattern**

The '[Wolfe Wave](../w/wolfe_wave.md)' pattern is a natural, harmonically balanced formation created by [supply](../s/supply.md) and [demand](../d/demand.md). It anticipates where the price is heading and is often used by contrarian traders.

### Elements:
1. Five-wave structure versus the [trend](../t/trend.md).
2. Lines connecting waves one and three, and waves two and four, forming a [wedge](../w/wedge.md).
3. Target lines projecting from wave one through wave four.

### Execution:
[Pattern recognition](../p/pattern_recognition.md) algorithms plot these waves, ensuring accuracy, especially in dynamic markets. Wolfe Waves often provide precise entry and exit points.


## 10. **Gartley Pattern**

The '[Gartley Pattern](../g/gartley_pattern.md)' is a complex harmonic pattern involving Fibonacci retracements. It was identified by H.M. Gartley in his book 'Profits in the [Stock Market](../s/stock_market.md).'

### Components:
1. Initial price move (X to A).
2. [Retracement](../r/retracement.md) (A to B), forming a 61.8% or 78.6% Fibonacci level.
3. Extension (B to C) and [retracement](../r/retracement.md) (C to D), following the 78.6% level.

### Detection:
Algorithmic systems, leveraging Fibonacci algorithms, scan for these retracements and extensions, executing trades at the 'D' point where the likelihood of [reversal](../r/reversal.md) is high.

H.M. Gartley's Book

## Conclusion

Unusual trading patterns [offer](../o/offer.md) sophisticated traders and algorithms significant advantages in anticipating [market](../m/market.md) movements more accurately and earlier than the more traditional patterns. The ability to detect, understand, and execute trades based on these patterns involves integrating advanced [pattern recognition](../p/pattern_recognition.md) algorithms, sophisticated [backtesting](../b/backtesting.md), and a keen understanding of [market](../m/market.md) behavior. These strategies encompass a mix of classic [technical analysis](../t/technical_analysis.md) augmented with cutting-edge algorithmic detection methods, providing a [robust](../r/robust.md) approach to exploiting [market](../m/market.md) inefficiencies.