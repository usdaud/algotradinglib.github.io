# 2-Week High/Low Strategy

### Introduction

The 2-Week High/Low strategy is a commonly used method in [algorithmic trading](../a/algorithmic_trading.md) that leverages the highest and lowest prices of a [security](../s/security.md) over a 14-day period to make trading decisions. This strategy is popular for its simplicity and effectiveness in identifying potential [breakout](../b/breakout.md) and [reversal](../r/reversal.md) points in the [market](../m/market.md). 

### Definition

In the context of stock trading, the 2-Week High/Low refers to the highest and lowest prices at which a stock has traded during the most recent 14-day period. Traders use these levels as significant points of reference to speculate on future price movements.

### Components of the Strategy

1. **Identification of High and Low Prices:**
   The primary component of this strategy is identifying the highest and lowest prices within the past 14 trading days. These prices are used as benchmarks for setting up potential [trade](../t/trade.md) entries and exits.

2. **Entry Signals:**
   - **[Breakout](../b/breakout.md) Entry:** In a [breakout](../b/breakout.md) strategy, traders look for the price to break above the 2-week high. This indicates a bullish signal, suggesting that the price may continue to rise. Conversely, a price moving below the 2-week low indicates a bearish signal, suggesting that the price may continue to fall.
   - **[Reversal](../r/reversal.md) Entry:** In a [reversal](../r/reversal.md) strategy, the [trader](../t/trader.md) anticipates that the price [will](../w/will.md) revert after reaching a new 2-week high or low. This strategy aims to [profit](../p/profit.md) from the corrective move after the [breakout](../b/breakout.md) surge.

3. **Exit Signals:**
   Traders set exit points either by [trailing stop](../t/trailing_stop.md)-loss mechanisms or by setting predefined [profit](../p/profit.md) targets based on the [percentage change](../p/percentage_change.md) from the entry price levels.

### Algorithmic Implementation

Automating the 2-Week High/Low strategy involves using programming languages and trading platforms that can execute trades based on pre-defined algorithms. Here's how one can implement such a strategy:

1. **Data Collection:**
   Collect historical price data for the stock, specifically focusing on the past 14 days to determine the high and low points.

2. **Strategy Development:**
   - **Python and Pandas:** A commonly used programming environment for developing the strategy. Python’s Pandas library is powerful for handling and analyzing [time series](../t/time_series.md) data.
   
   ```python
   [import](../i/import.md) pandas as pd

   def calculate_2_week_high_low(df):
       df['2_week_high'] = df['Close'].rolling(window=14).max()
       df['2_week_low'] = df['Close'].rolling(window=14).min()
       [return](../r/return.md) df
   ```

3. **Signal Generation:**
   Generate buy and sell signals when the price exceeds the 2-week high or falls below the 2-week low.

   ```python
   def generate_signals(df):
       df['Signal'] = 0
       df['Signal'][14:] = np.where(df['Close'][14:] > df['2_week_high'].shift(1)[14:], 1, 0)
       df['Signal'][14:] = np.where(df['Close'][14:] < df['2_week_low'].shift(1)[14:], -1, df['Signal'][14:])
       [return](../r/return.md) df
   ```

4. **[Backtesting](../b/backtesting.md):**
   Test the strategy on historical data to assess its performance:
   
   ```python
   def backtest_strategy(df):
       df['Returns'] = df['Close'].pct_change()
       df['Strategy_Returns'] = df['Signal'].shift(1) * df['Returns']
       [return](../r/return.md) df
   
   result = pd.DataFrame()
   result['Cumulative_Strategy_Returns'] = (1 + backtest_strategy(stock_data)['Strategy_Returns']).cumprod() - 1
   ```

### Practical Applications in Trading

1. **[Trend Following](../t/trend_following.md):**
   In trending markets, the 2-week high/low strategy can help traders [capitalize](../c/capitalize.md) on the persistent directional moves. When the price continues to set new highs or lows within the 14-day period, the strategy confirms the strength of the [trend](../t/trend.md).

2. **[Volatility](../v/volatility.md) Breakouts:**
   The strategy is useful in identifying [volatility](../v/volatility.md) breakouts where the price surpasses significant levels established in the last 2 weeks. Traders can capture the [momentum](../m/momentum.md) that usually follows such breakouts.

3. **Contrarian Approaches:**
   Although primarily used for detecting breakouts, some traders might use the 2-week highs/lows as areas to look for potential reversals. For instance, a stock hitting its 2-week high might face resistance, leading to a [retracement](../r/retracement.md).

### Refinements and Variations

While the basic 2-week high/low strategy is straightforward, traders often refine it for better accuracy:

1. **Additional Filters:**
   Incorporating filters such as moving averages or [volume](../v/volume.md) thresholds to avoid false breakouts.

2. **[Risk Management](../r/risk_management.md):**
   Utilization of [risk management](../r/risk_management.md) tools, including [stop-loss orders](../s/stop-loss_orders.md) and [position sizing](../p/position_sizing.md) to mitigate potential losses.

3. **Combining Indicators:**
   Blending the 2-week high/low signals with other [technical indicators](../t/technical_indicators.md) like RSI ([Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md)) or MACD (Moving Average Convergence [Divergence](../d/divergence.md)) for more [robust](../r/robust.md) [trade](../t/trade.md) signals.

### Tools and Platforms

Various tools and platforms facilitate implementation:

1. **[QuantConnect](../q/quantconnect.md):** [QuantConnect](https://www.quantconnect.com/) offers a cloud-based platform to design, backtest, and execute algorithmic strategies in [multiple](../m/multiple.md) programming languages.
2. **[TradingView](../t/tradingview.md):** [TradingView](https://www.tradingview.com/) provides an easy-to-use interface for [technical analysis](../t/technical_analysis.md) and scripting custom [trading strategies](../t/trading_strategies.md) using Pine Script.
3. **MetaTrader:** [MetaTrader](https://www.metatrader5.com/) supports [algorithmic trading](../a/algorithmic_trading.md) with its MQL4/MQL5 language for customized strategy scripts.

### Case Study

Let's consider a hypothetical application:
- **Stock:** XYZ Inc.
- **Period:** January 1, 2023, to March 1, 2023
- **Strategy Applied:** The algorithm buys the stock when it breaks above its 2-week high; it shorts the stock when it breaks below its 2-week low.

#### Results:
- **Total Trades:** 10
- **Winning Trades:** 7
- **Losing Trades:** 3
- **Net [Profit](../p/profit.md):** 8%

This simple analysis demonstrates the efficacy of the strategy, though in real-[market](../m/market.md) conditions, more sophisticated [risk](../r/risk.md) and [money management](../m/money_management.md) techniques would be implemented.

### Conclusion

The 2-week High/Low strategy is a straightforward yet effective trading approach that can be easily adapted and deployed in [algorithmic trading](../a/algorithmic_trading.md) systems. With proper implementation and [risk management](../r/risk_management.md), it serves as a valuable tool for capturing [price momentum](../p/price_momentum.md) and trading breakouts in various [market](../m/market.md) conditions.