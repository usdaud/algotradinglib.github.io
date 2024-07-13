# 8-Period RSI

The 8-Period [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI) is a popular [technical analysis](../t/technical_analysis.md) [indicator](../i/indicator.md) used by traders to evaluate [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions in the [market](../m/market.md). Developed by J. Welles Wilder Jr. in 1978, the RSI is a [momentum](../m/momentum.md) [oscillator](../o/oscillator.md) that measures the speed and change of price movements. It oscillates between zero and 100 and is typically used to identify the strength and weakness of a stock or [asset](../a/asset.md) over a specified time period. Although the most standard and widely used period for RSI is 14 days, the 8-period RSI can provide more responsive and quicker signals.

## The Fundamentals of RSI

### Calculation of RSI

The RSI is calculated using the following formula:

```
RSI = 100 - (100 / (1 + RS))
```

Where RS ([Relative Strength](../r/relative_strength.md)) is calculated as:

```
RS = Average [Gain](../g/gain.md) / Average Loss
```

For an 8-period RSI:
- Average [Gain](../g/gain.md) is the average of all gains over the last 8 periods.
- Average Loss is the average of all losses over the last 8 periods.

### Steps in Calculation:

1. **Determine Closing Prices**: Calculate the [gain](../g/gain.md) or loss from the previous period. Gains are counted as positive numbers, while losses are counted as absolute values (positive numbers), as the concept of 'loss' inherently carries a negative [value](../v/value.md).
   
2. **Calculate Averages**: Compute the average [gain](../g/gain.md) and average loss for the initial 8 periods. For subsequent periods, apply the smoothing technique recommended by Wilder:

    ```
    Average [Gain](../g/gain.md) = [(Previous Average [Gain](../g/gain.md) * (n-1)) + Current [Gain](../g/gain.md)] / n
    Average Loss = [(Previous Average Loss * (n-1)) + Current Loss] / n
    ```

3. **Compute RS**: Divide the average [gain](../g/gain.md) by the average loss.

4. **Calculate the RSI**: Utilize the RS [value](../v/value.md) in the RSI formula to get your final RSI reading.

## Significance in Trading

### Interpretation of RSI

- **[Overbought](../o/overbought.md) and [Oversold](../o/oversold.md) Levels**: If the RSI is above 70, the [asset](../a/asset.md) is generally considered [overbought](../o/overbought.md), indicating that it may be [overvalued](../o/overvalued.md) and a [pullback](../p/pullback.md) or [reversal](../r/reversal.md) could occur. Conversely, if the RSI is below 30, the [asset](../a/asset.md) is considered [oversold](../o/oversold.md), suggesting it may be [undervalued](../u/undervalued.md) and a [rally](../r/rally.md) could be forthcoming.

- **[Divergence](../d/divergence.md)**: If the price of an [asset](../a/asset.md) is making a new high or low that is not confirmed by the RSI, this [divergence](../d/divergence.md) can indicate a potential [reversal](../r/reversal.md). For instance, when price makes a higher high but the RSI makes a lower high, it may show weakening [momentum](../m/momentum.md) and a potential top.

- **[Failure Swings](../f/failure_swings.md)**: Bullish [failure swings](../f/failure_swings.md) occur when the RSI moves below 30 ([oversold](../o/oversold.md) area) back above 30, followed by a [retracement](../r/retracement.md) above 30 and then a break above the previous high. This is indicative of a potential upward [reversal](../r/reversal.md). Bearish [failure swings](../f/failure_swings.md) are the opposite and occur in the [overbought](../o/overbought.md) area.

### 8-Period RSI vs 14-Period RSI

The 8-period RSI is shorter-term and more sensitive to recent price movements compared to the traditional 14-period RSI. This means it can generate quicker signals for buying and selling but might also result in more [false signals](../f/false_signals_in_trading.md). Traders looking for swift entry and exit points may prefer a shorter period RSI like 8 periods, while those with a longer horizon may stick with the standard 14 periods for more reliable signals.

## Practical Application in Algo Trading

[Algorithmic trading](../a/algorithmic_trading.md) or "algo trading" leverages [mathematical models](../m/mathematical_models_in_trading.md) and financial theories to execute trades automatically. The 8-period RSI can be integrated into [trading algorithms](../t/trading_algorithms.md) to automate the buying and selling process based on predictive RSI signals.

### Developing an RSI-Based Algorithm

1. **Defining Parameters**:
    - Time Frame: Decide whether the algorithm [will](../w/will.md) be used for [intraday trading](../i/intraday_trading.md), [swing trading](../s/swing_trading.md), or longer-term positions.
    - [Asset Class](../a/asset_class.md): Specify which [stocks](../s/stock.md), commodities, or forex pairs the algorithm [will](../w/will.md) [trade](../t/trade.md).

2. **Identifying Rules**:
    - [Trading Signals](../t/trading_signals.md): Buy when the 8-period RSI crosses above a certain threshold (e.g., 30 from below), and sell when it crosses below a certain threshold (e.g., 70 from above).
    - [Position Sizing](../p/position_sizing.md): Determine the amount or percentage of the portfolio to allocate for each [trade](../t/trade.md).

3. **[Backtesting](../b/backtesting.md) and [Optimization](../o/optimization.md)**:
    - Historical Data: Use past [market](../m/market.md) data to backtest the algorithm, ensuring it would have performed well historically.
    - Optimize Parameters: Adjust the RSI thresholds and other parameters to maximize returns and minimize [risk](../r/risk.md).

4. **Implementation and Monitoring**:
    - [Execution](../e/execution.md): Deploy the algorithm on a [trading platform](../t/trading_platform.md), ensuring it can execute trades as intended without lag.
    - Real-time Monitoring: Continuously monitor the performance of the algorithm and adjust parameters as needed to adapt to changing [market](../m/market.md) conditions.

### Tools and Platforms

Numerous platforms and tools are available to help traders develop, backtest, and implement RSI-based algorithms:

- **MetaTrader 4 & 5**: Popular trading platforms that support automated trading through Expert Advisors (EAs). 
- **[NinjaTrader](../n/ninjatrader.md)**: Offers advanced charting and [algorithmic trading](../a/algorithmic_trading.md) capabilities.
- **[QuantConnect](../q/quantconnect.md)**: A cloud-based [algorithmic trading](../a/algorithmic_trading.md) platform that allows [backtesting](../b/backtesting.md) and live trading using Python and C#.
- **[Interactive Brokers](../i/interactive_brokers.md) API**: Allows for direct access to [market](../m/market.md) data and trading operations through custom-built algorithms.

## Real-World Example

Consider a [trading strategy](../t/trading_strategy.md) implemented using the 8-period RSI for a stock like Apple Inc. (AAPL). The algorithm might be built with the following criteria:

- **Entry Condition**: Buy AAPL stock when the 8-period RSI crosses above 30, indicating it's moving out of an [oversold](../o/oversold.md) condition.
- **Exit Condition**: Sell AAPL stock when the 8-period RSI crosses below 70, signaling it might be moving out of an [overbought](../o/overbought.md) condition.
- **Stop-Loss**: Place a [stop-loss order](../s/stop-loss_order.md) at 5% below the entry price to manage [risk](../r/risk.md).

Running this algorithm over historical data can help determine its effectiveness, and live testing can allow for real-time performance evaluation.

## Conclusion

The 8-period RSI is a powerful tool in the arsenal of technical traders, [offering](../o/offering.md) timely insights into [market](../m/market.md) conditions. When used within the framework of [algorithmic trading](../a/algorithmic_trading.md), it allows for the automation of buy and sell decisions, potentially capitalizing on [market](../m/market.md) efficiencies and reducing emotional bias. As with any [trading strategy](../t/trading_strategy.md), thorough [backtesting](../b/backtesting.md), proper [risk management](../r/risk_management.md), and continuous monitoring are crucial for success.

For more information on platforms that support [algorithmic trading](../a/algorithmic_trading.md), you can visit:
- [MetaTrader](https://www.metatrader4.com/)
- [NinjaTrader](https://ninjatrader.com/)
- [QuantConnect](https://www.quantconnect.com/)
- [Interactive Brokers](https://www.interactivebrokers.com/)