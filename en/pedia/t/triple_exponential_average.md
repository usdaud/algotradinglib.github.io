# Triple Exponential Average (TRIX)

The Triple Exponential Average (TRIX) is a momentum indicator that displays the percent rate of change of a triple exponentially smoothed moving average of a security's closing price. The indicator was developed by Jack Hutson in the early 1980s. It is designed to keep traders from reacting prematurely to price fluctuations by filtering out the "noise" that is inherent in securities trading. 

#### Components and Calculation

A TRIX line oscillates around a zero line. Positive values indicate upward momentum, while negative values indicate downward momentum. The TRIX is a much smoother indicator than other typical [momentum indicators](../m/momentum_indicators.md) because it uses triple [exponential smoothing](../e/exponential_smoothing.md).

The calculation of TRIX involves three main steps:
1. **Single [Exponential Smoothing](../e/exponential_smoothing.md) (EMA1):** First, a single smoothing of the closing price over a chosen period (e.g., 15 days) is calculated:
   
   \[
   EMA1_t = \frac {P_t + (n-1) \times EMA1_{t-1}} {n}
   \]

   where \(P_t\) is the price at time \(t\) and \(n\) is the number of periods.

2. **Double [Exponential Smoothing](../e/exponential_smoothing.md) (EMA2):** Then, a second [exponential smoothing](../e/exponential_smoothing.md) is applied to the result of the first smoothing:

   \[
   EMA2_t = \frac {EMA1_t + (n-1) \times EMA2_{t-1}} {n}
   \]

3. **Triple [Exponential Smoothing](../e/exponential_smoothing.md) (EMA3):** Finally, a third [exponential smoothing](../e/exponential_smoothing.md) is applied to the result of the second smoothing:

   \[
   EMA3_t = \frac {EMA2_t + (n-1) \times EMA3_{t-1}} {n}
   \]

Once EMA3 is computed, the TRIX is derived by calculating the percentage change between the current and previous value of EMA3:

\[
TRIX_t = \frac {EMA3_t - EMA3_{t-1}} {EMA3_{t-1}} \times 100
\]

#### Applications in Trading

1. **Trend Direction:** A TRIX above zero indicates an uptrend, while a TRIX below zero indicates a downtrend.

2. **Signal Line Crossovers:** Traders often use a signal line, which is an additional moving average (usually a 9-day moving average) of the TRIX itself. The crossover of the TRIX and its signal line can be used as a buy/sell trigger:
   - **Buy Signal:** When TRIX crosses above the signal line
   - **Sell Signal:** When TRIX crosses below the signal line

3. **Divergence:** TRIX can show divergence with the price action:
   - **[Bullish Divergence](../b/bullish_divergence.md):** If the prices are making new lows, but the TRIX fails to make new lows, it could be a sign of an impending bullish reversal.
   - **[Bearish Divergence](../b/bearish_divergence.md):** If prices are making new highs, but the TRIX fails to make new highs, it could be a sign of an impending bearish reversal.

#### Advantages of Using TRIX

- **Noise Filtration:** By using triple smoothing, TRIX eliminates a lot of the short-term volatility that can result in [false signals](../f/false_signals_in_trading.md).
- **Simplified Analysis:** TRIX provides a single line that can indicate both the direction and momentum of a trend, simplifying the analytical process for traders.
- **Divergence Signal:** As mentioned, TRIX’s ability to show divergence with price action can signal potential reversals before they happen, giving traders a strategic advantage.

#### Limitations and Considerations

- **Lag:** Like all moving averages, the TRIX is a lagging indicator. It responds to price movements with a delay, meaning that it may not forecast future price movements accurately.
- **Complexity:** The triple smoothing process can be complex and might not be suitable for beginners who are unfamiliar with [exponential smoothing](../e/exponential_smoothing.md) techniques.
- **[False Signals](../f/false_signals_in_trading.md):** While TRIX is designed to minimize noise, no indicator is perfect. There can still be periods of low volatility where TRIX may generate multiple [false signals](../f/false_signals_in_trading.md).

#### Integration with Other Indicators

Many traders use TRIX in combination with other [technical indicators](../t/technical_indicators.md) to confirm signals and trends. Common complementary indicators include:

- **Relative Strength Index (RSI):** Helps to identify overbought and oversold conditions.
- **Moving Average Convergence Divergence (MACD):** Offers insights into trend direction and momentum.
- **[Volume Indicators](../v/volume_indicators.md):** Showing the strength behind price movements.

#### Conclusion

The Triple Exponential Average (TRIX) is a versatile momentum indicator that can be a valuable tool for traders looking to identify trends, reversals, and entry/exit points in the market. By smoothing out price data three times, TRIX aims to eliminate noise and focus on the true underlying trend. However, like all indicators, it is most effective when combined with other tools and methods in a comprehensive trading strategy.

For more information on TRIX and other [technical indicators](../t/technical_indicators.md), you can visit [Investopedia](https://www.investopedia.com/terms/t/trix.asp).
