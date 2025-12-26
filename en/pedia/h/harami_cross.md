# Harami Cross

The Harami Cross is a widely recognized [candlestick](../c/candlestick.md) pattern in [technical analysis](../t/technical_analysis.md) that can be instrumental in identifying potential reversals in a financial [market](../m/market.md)'s price [trend](../t/trend.md). The term "harami" itself is derived from the Japanese word for "pregnant," which reflects the visual appearance of the pattern. The Harami Cross pattern is a specific type of the Harami pattern and constitutes a two-candle formation that signals a possible change in [market](../m/market.md) direction. Given its significance and nuanced interpretation, this pattern is closely monitored by traders who employ [algorithmic trading strategies](../a/algorithmic_trading_strategies.md), aiming to refine the precision of their entries and exits in the [market](../m/market.md).

## Structure and Characteristics

The Harami Cross formation consists of two specific candlesticks:

1. **First [Candlestick](../c/candlestick.md)**: This is a large-bodied candle that indicates a strong bullish (white/green) or bearish (black/red) move.
2. **Second [Candlestick](../c/candlestick.md)**: This candle is a [Doji](../d/doji.md), a candle where the opening and closing prices are nearly the same, creating a very small body. The [Doji](../d/doji.md) must be contained within the body of the first [candlestick](../c/candlestick.md), signifying indecision among traders.

### Bullish Harami Cross

A [Bullish Harami](../b/bullish_harami.md) Cross occurs in a [downtrend](../d/downtrend.md) and suggests a potential [reversal](../r/reversal.md) to an [uptrend](../u/uptrend.md). The first candle is a long bearish candle, showing that the sellers were in control. The next day, a [Doji](../d/doji.md) appears within the body of the previous candle, indicating indecision among [market](../m/market.md) participants. The appearance of the [Doji](../d/doji.md) suggests that selling pressure may be diminishing, possibly leading to an upward [reversal](../r/reversal.md).

### Bearish Harami Cross

A Bearish Harami Cross manifests in an [uptrend](../u/uptrend.md) and signals a possible shift to a [downtrend](../d/downtrend.md). The first candle is a long bullish candle, highlighting control by the buyers. The following day features a [Doji](../d/doji.md) within the body of the first candle, showing a state of indecision. The presence of the [Doji](../d/doji.md) signifies a reduction in buying pressure, implying that a downward [reversal](../r/reversal.md) could be near.

## Interpretation and Trading Strategy

The Harami Cross is significant because it highlights a period of [market](../m/market.md) indecision, which often precedes a [reversal](../r/reversal.md). Traders employing this pattern as part of their strategy generally look for confirmation before entering a [trade](../t/trade.md):

1. **Confirmation**: This could come in various forms, such as a gap in the direction of the anticipated [reversal](../r/reversal.md), high trading [volume](../v/volume.md), or a subsequent candle that breaks the high or low of the [Doji](../d/doji.md).
2. **Stop-Loss Placement**: For a [Bullish Harami](../b/bullish_harami.md) Cross, typically a stop-loss is placed below the low of the first [candlestick](../c/candlestick.md). For a Bearish Harami Cross, a stop-loss is often placed above the high of the first [candlestick](../c/candlestick.md).
3. **[Profit](../p/profit.md) Targets**: Traders may set [profit](../p/profit.md) targets based on [Fibonacci retracement](../f/fibonacci_retracement.md) levels, previous support/resistance levels, or a fixed [risk](../r/risk.md)-to-reward ratio.

## Algorithmic Trading Applications

In the context of [algorithmic trading](../a/algorithmic_trading.md), the Harami Cross pattern can be codified into a trading algorithm to automate buy and sell decisions. Such an algorithm would typically include:

1. **[Pattern Recognition](../p/pattern_recognition.md)**: Using historical price data to identify the two-candle formation of the Harami Cross.
2. **Confirmation Requirements**: Implement rules for additional confirmation before executing trades to filter out [false signals](../f/false_signals_in_trading.md).
3. **[Risk Management](../r/risk_management.md)**: Incorporate automated stop-loss and take-[profit](../p/profit.md) rules to manage [risk](../r/risk.md) and [lock in profits](../l/lock_in_profits.md).
4. **[Backtesting](../b/backtesting.md)**: Apply the algorithm to historical data to evaluate its performance and make any necessary adjustments.

### Example: Algorithmic Trading Strategy

**Step 1**: Identify the Harami Cross pattern in historical price data.
```python
def identify_harami_cross(data):
    patterns = []
    for i in [range](../r/range.md)(1, len(data)):
        if is_doji(data[i]) and within_candle_body(data[i], data[i-1]):
            patterns.append((data[i-1], data[i]))
    [return](../r/return.md) patterns

def is_doji(candle):
    [return](../r/return.md) abs(candle['close'] - candle['[open](../o/open.md)']) < 0.1 * (candle['high'] - candle['low'])

def within_candle_body([doji](../d/doji.md), previous_candle):
    [return](../r/return.md) ([doji](../d/doji.md)['high'] <= previous_candle['high'] and
            [doji](../d/doji.md)['low'] >= previous_candle['low'])
```

**Step 2**: Define confirmation criteria and [trade](../t/trade.md) [execution](../e/execution.md) rules.
```python
def confirm_and_trade(patterns, data):
    trades = []
    for pattern in patterns:
        [index](../i/index_instrument.md) = data.[index](../i/index_instrument.md)(pattern[1])
        if confirmation(data, [index](../i/index_instrument.md)):
            action = 'buy' if pattern[0]['close'] < pattern[0]['[open](../o/open.md)'] else 'sell'
            stop_loss = data[[index](../i/index_instrument.md)+1]['low'] if action == 'buy' else data[[index](../i/index_instrument.md)+1]['high']
            [trade](../t/trade.md) = execute_trade(action, data[[index](../i/index_instrument.md)+2], stop_loss)
            trades.append([trade](../t/trade.md))
    [return](../r/return.md) trades

def confirmation(data, [index](../i/index_instrument.md)):
    if [index](../i/index_instrument.md) + 2 >= len(data):
        [return](../r/return.md) False
    [return](../r/return.md) data[[index](../i/index_instrument.md)+2]['close'] > data[[index](../i/index_instrument.md)+1]['high'] if data[[index](../i/index_instrument.md)+1]['close'] < data[[index](../i/index_instrument.md)+1]['open'] else data[[index](../i/index_instrument.md)+2]['close'] < data[[index](../i/index_instrument.md)+1]['low']

def execute_trade(action, entry_candle, stop_loss):
    [return](../r/return.md) {
        'action': action,
        'entry_price': entry_candle['[open](../o/open.md)'],
        'stop_loss': stop_loss,
        'timestamp': entry_candle['timestamp']
    }
```

**Step 3**: Backtest the algorithm on historical data.
```python
historical_data = load_historical_data()
patterns = identify_harami_cross(historical_data)
trades = confirm_and_trade(patterns, historical_data)

for [trade](../t/trade.md) in trades:
    print([trade](../t/trade.md))
```

## Real-World Applications and Tools

[Algorithmic trading platforms](../a/algorithmic_trading_platforms.md) and tools allow traders to implement and automate strategies based on the Harami Cross and other patterns. Some widely used platforms include:

- **MetaTrader (MT4/MT5)**: Popular among forex and CFD traders, it supports custom indicators and trading scripts. More details at MetaTrader.
- **[NinjaTrader](../n/ninjatrader.md)**: A [robust](../r/robust.md) platform for [futures](../f/futures.md) and forex trading, [offering](../o/offering.md) extensive [backtesting](../b/backtesting.md) and automation capabilities. More information can be found at NinjaTrader.
- **[QuantConnect](../q/quantconnect.md)**: An [open](../o/open.md)-source [algorithmic trading](../a/algorithmic_trading.md) platform that provides data, coding environments, and [backtesting](../b/backtesting.md) tools for developing and testing [trading algorithms](../t/trading_algorithms.md). Explore more at QuantConnect.

## Conclusion

The Harami Cross is a potent tool in the arsenal of technical analysts and algorithmic traders. By recognizing the pattern and understanding its implications, traders can anticipate potential [market](../m/market.md) reversals and enhance their [trading strategies](../t/trading_strategies.md). Integrating this pattern into an algorithmic approach allows for systematic and emotion-free trading, leveraging the speed and precision of automated systems to [capitalize](../c/capitalize.md) on [market](../m/market.md) opportunities.