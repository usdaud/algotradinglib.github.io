# 1-2-3 Reversal Pattern

The 1-2-3 [Reversal](../r/reversal.md) Pattern is a classic [technical analysis](../t/technical_analysis.md) pattern commonly used in [algorithmic trading](../a/algorithmic_trading.md) for identifying potential changes in [market](../m/market.md) trends. This pattern signifies a [reversal](../r/reversal.md) in the existing [trend](../t/trend.md), whether upwards or downwards, and helps traders to plan their [entry and exit strategies](../e/entry_and_exit_strategies.md) accordingly. Understanding and identifying this pattern correctly can lead to profitable trading opportunities by capitalizing on [trend](../t/trend.md) reversals.

## Structure of the 1-2-3 Reversal Pattern

The 1-2-3 [Reversal](../r/reversal.md) Pattern is composed of three main points:

1. **Point 1**: This refers to the last extreme point of the existing [trend](../t/trend.md). In a [downtrend](../d/downtrend.md), this would be the lowest low, and in an [uptrend](../u/uptrend.md), this would be the highest high.
2. **Point 2**: This is formed when the price makes a considerable [retracement](../r/retracement.md) from Point 1. For a [downtrend](../d/downtrend.md) [reversal](../r/reversal.md), Point 2 is a higher high than Point 1. Conversely, for an [uptrend](../u/uptrend.md) [reversal](../r/reversal.md), Point 2 is a lower low than Point 1.
3. **Point 3**: This occurs when the price pulls back again but does not break below the prior [retracement](../r/retracement.md) in a [downtrend](../d/downtrend.md) or above the prior [retracement](../r/retracement.md) in an [uptrend](../u/uptrend.md). To qualify as a Point 3, the price must not extend beyond the first [retracement](../r/retracement.md) swing (Point 2).

The pattern becomes actionable when the price moves beyond Point 2 after Point 3 is formed, signalling a [trend reversal](../t/trend_reversal.md).

## Identifying and Trading the 1-2-3 Reversal Pattern

### Downtrend to Uptrend Reversal
- **Point 1**: Identify the lowest point in the [downtrend](../d/downtrend.md).
- **Point 2**: Wait for the price to increase and form a higher high (relative to Point 1).
- **Point 3**: Observe the subsequent low which should be higher than Point 1 but lower than Point 2.
- **Confirmation**: A break above Point 2 is a confirmation that the [trend](../t/trend.md) is reversing to an [uptrend](../u/uptrend.md).

### Uptrend to Downtrend Reversal
- **Point 1**: Identify the highest point in the [uptrend](../u/uptrend.md).
- **Point 2**: Wait for the price to decrease and form a lower low (relative to Point 1).
- **Point 3**: Observe the subsequent high which should be lower than Point 1 but higher than Point 2.
- **Confirmation**: A break below Point 2 is a confirmation that the [trend](../t/trend.md) is reversing to a [downtrend](../d/downtrend.md).

### Trading Strategies Involving the 1-2-3 Reversal Pattern
#### Entry
- **Entry Signal (Buy)**: Place a buy [order](../o/order.md) slightly above Point 2 after confirming that Point 3 is higher than Point 1.
- **Entry Signal (Sell)**: Place a sell [order](../o/order.md) slightly below Point 2 after confirming that Point 3 is lower than Point 1.

#### Stop-Loss
- **Stop-Loss for Long Trades**: Set a stop-loss slightly below Point 3.
- **Stop-Loss for Short Trades**: Set a stop-loss slightly above Point 3.

#### Take-Profit
- **Take-[Profit](../p/profit.md) Levels**: Create [multiple](../m/multiple.md) take-[profit](../p/profit.md) levels based on [Fibonacci extensions](../f/fibonacci_extensions.md) or previous support/resistance levels. This helps in maximizing profits while managing risks.

## Algorithmic Implementation
### Data and Software Requirements
To implement the 1-2-3 [Reversal](../r/reversal.md) Pattern algorithmically, you need:
- Historical price data
- [Real-time market data](../r/real-time_market_data.md) for live trading
- Programming knowledge (e.g., Python, R)
- [Trading platform](../t/trading_platform.md) API (e.g., MetaTrader, [Interactive Brokers](../i/interactive_brokers.md))

### Coding the Patterns
An algorithm could be programmed to constantly scan the [market](../m/market.md) for the conditions that constitute Points 1, 2, and 3. Here’s a pseudo-code example in Python:

```python
def identify_123_reversal(candlestick_data):
    patterns = []
    for i in [range](../r/range.md)(len(candlestick_data) - 3):
        if (candlestick_data[i] < candlestick_data[i+1]) and \
           (candlestick_data[i+1] > candlestick_data[i+2]) and \
           (candlestick_data[i+2] > candlestick_data[i+1]) and \
           (candlestick_data[i+2] > candlestick_data[i+3]):
            patterns.append((i, i+1, i+2))
    [return](../r/return.md) patterns

def place_trade(password, type, point, stop_loss):
    # Implementation to place the [trade](../t/trade.md) through API
    pass

# Simulation data
candlestick_data = [100, 105, 102, 107, 108, 105, 106] # example data
patterns = identify_123_reversal(candlestick_data)

if patterns:
    # Place a [trade](../t/trade.md) based on the identified pattern
    first, second, third = patterns[0]
    place_trade(password='API_KEY', type='BUY', point=candlestick_data[second], stop_loss=candlestick_data[third])
```

### Backtesting
To ensure the robustness of your 1-2-3 [Reversal](../r/reversal.md) Pattern algorithm, you must backtest it using historical data. This helps to:
- Evaluate [performance metrics](../p/performance_metrics.md) ([profit factor](../p/profit_factor.md), max [drawdown](../d/drawdown.md))
- Optimize the parameters (stop-loss, take-[profit](../p/profit.md))
- Identify [market](../m/market.md) conditions where the pattern works best

### Risk Management
Integrate [risk management](../r/risk_management.md) practices such as [position sizing](../p/position_sizing.md), setting stop-loss and take-[profit](../p/profit.md) levels, and diversifying trades to minimize potential losses and enhance profitability.

## Examples of Algorithmic Trading Firms
Several [algorithmic trading](../a/algorithmic_trading.md) firms employ various [market](../m/market.md) strategies, including [pattern recognition](../p/pattern_recognition.md) such as the 1-2-3 [Reversal](../r/reversal.md) Pattern. These firms invest heavily in technology and [quantitative analysis](../q/quantitative_analysis.md) to [gain](../g/gain.md) [market](../m/market.md) advantages:

- **Two Sigma**: A renowned [hedge fund](../h/hedge_fund.md) that implements [machine learning](../m/machine_learning.md) and advanced algorithms.
- **Renaissance Technologies**: Another leading [hedge fund](../h/hedge_fund.md) known for its [quantitative trading](../q/quantitative_trading.md) strategies.

## Conclusion
The 1-2-3 [Reversal](../r/reversal.md) Pattern offers a systematic approach to identifying [trend](../t/trend.md) reversals, providing traders with [robust](../r/robust.md) opportunities to [capitalize](../c/capitalize.md) on changing [market](../m/market.md) directions. By integrating [algorithmic trading](../a/algorithmic_trading.md) techniques, traders can efficiently and accurately recognize these patterns, making data-driven decisions to enhance [trading performance](../t/trading_performance.md). Proper implementation and rigorous [backtesting](../b/backtesting.md) are crucial to leveraging the full potential of this pattern in the ever-evolving [financial markets](../f/financial_market.md).
