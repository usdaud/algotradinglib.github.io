# Williams %R

---

### Introduction to Williams %R

Williams %R is a [momentum](../m/momentum.md)-based [technical analysis](../t/technical_analysis.md) [indicator](../i/indicator.md), developed by Larry Williams in the 1970s. It’s designed to gauge whether a [security](../s/security.md) is [overbought](../o/overbought.md) or [oversold](../o/oversold.md) by comparing its closing price to its high-low [range](../r/range.md) over a certain period. This [oscillator](../o/oscillator.md) ranges from 0 to -100; typically, readings above -20 suggest that the instrument is [overbought](../o/overbought.md), while readings below -80 indicate that it’s [oversold](../o/oversold.md). The Williams %R is instrumental in [algorithmic trading](../a/algorithmic_trading.md) strategies due to its predictive power and adaptability.

---

### Calculation of Williams %R

The formula for Williams %R is straightforward:

\[ \%R = \frac{(Highest\_High - Current\_Close)}{(Highest\_High - Lowest\_Low)} \times -100 \]

Where:
- `Highest_High` is the highest price over the past `n` periods.
- `Current_Close` is the most recent closing price.
- `Lowest_Low` is the lowest price over the past `n` periods.

For example, in a 14-day period, if the highest price is 150, the lowest is 130, and the closing price today is 145, Williams %R would be calculated as:

\[ \%R = \frac{(150 - 145)}{(150 - 130)} \times -100 = -25 \]

---

### Interpretation in Algo Trading

Williams %R is a [leading indicator](../l/leading_indicator.md) in that it provides signals ahead of price changes, making it useful for algorithmic traders. Here’s how you can interpret the values:

1. **[Overbought](../o/overbought.md) Conditions**:
 - When %R is above -20, the [asset](../a/asset.md) is considered [overbought](../o/overbought.md). It suggests that the price might see a [correction](../c/correction.md) soon.
 - Algorithms might trigger sell signals or [stop-loss orders](../s/stop-loss_orders.md) in this zone.

2. **[Oversold](../o/oversold.md) Conditions**:
 - When %R is below -80, the [asset](../a/asset.md) is considered [oversold](../o/oversold.md). It indicates that the price could rebound.
 - Algo-traders might use this as a trigger for entering long positions.

3. **[Divergence](../d/divergence.md)**:
 - [Divergence](../d/divergence.md) between the Williams %R and price can indicate potential reversals. If prices are rising and %R is falling, a bearish [reversal](../r/reversal.md) could be implied, and vice versa.

---

### Implementation in Algorithmic Strategies

#### Mean Reversion Strategy

A [mean reversion](../m/mean_reversion.md) strategy assumes that [asset](../a/asset.md) prices [will](../w/will.md) revert to their historical mean. Williams %R is well-suited for such strategies due to its [overbought](../o/overbought.md) and [oversold](../o/oversold.md) signals.

**Pseudo-code Example**:

```python
def calculate_williams_r(data, period):
    highest_high = max(data['High'][-period:])
    lowest_low = min(data['Low'][-period:])
    current_close = data['Close'][-1]
    
    williams_r = ((highest_high - current_close) / (highest_high - lowest_low)) * -100
    [return](../r/return.md) williams_r

def execute_mean_reversion_strategy(data, period):
    williams_r = calculate_williams_r(data, period)
    
    if williams_r < -80:
        [return](../r/return.md) "Buy"
    elif williams_r > -20:
        [return](../r/return.md) "Sell"
    else:
        [return](../r/return.md) "[Hold](../h/hold.md)"

# Sample data for testing
sample_data = {
    'High': [147, 150, 149, 152, 150],
    'Low': [137, 135, 140, 145, 142],
    'Close': [145, 148, 146, 150, 149]
}

# Run the strategy with a 14-day lookback period
signal = execute_mean_reversion_strategy(sample_data, 14)
print(signal)
```

#### Momentum-Based Strategy

[Momentum](../m/momentum.md)-based strategies [capitalize](../c/capitalize.md) on existing [market](../m/market.md) trends. Traders can use Williams %R to confirm the strength of these trends.

**Pseudo-code Example**:

```python
def calculate_williams_r(data, period):
    highest_high = max(data['High'][-period:])
    lowest_low = min(data['Low'][-period:])
    current_close = data['Close'][-1]
    
    williams_r = ((highest_high - current_close) / (highest_high - lowest_low)) * -100
    [return](../r/return.md) williams_r

def execute_momentum_strategy(data, period):
    williams_r = calculate_williams_r(data, period)
    
    if williams_r > -50:
        # Confirm [uptrend](../u/uptrend.md)
        if data['Close'][-1] > data['Close'][-2]:
            [return](../r/return.md) "Buy"
    elif williams_r < -50:
        # Confirm [downtrend](../d/downtrend.md)
        if data['Close'][-1] < data['Close'][-2]:
            [return](../r/return.md) "Sell"
    [return](../r/return.md) "[Hold](../h/hold.md)"

# Sample data for testing
sample_data = {
    'High': [147, 150, 149, 152, 150],
    'Low': [137, 135, 140, 145, 142],
    'Close': [145, 148, 146, 150, 149]
}

# Run the strategy with a 14-day lookback period
signal = execute_momentum_strategy(sample_data, 14)
print(signal)
```

---

### Advanced Topics

#### Combining Williams %R with Other Indicators

While Williams %R provides valuable insights, combining it with other indicators such as Moving Averages (MAs), [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI), or [Bollinger Bands](../b/bollinger_bands.md) can enhance the reliability of [trading signals](../t/trading_signals.md).

For example, an algo-[trader](../t/trader.md) could use Williams %R in conjunction with a Moving Average to filter out [noise](../n/noise.md) and confirm true signals:

```python
def calculate_moving_average(data, period):
    [return](../r/return.md) sum(data['Close'][-period:]) / period

def execute_combined_strategy(data, period, ma_period):
    williams_r = calculate_williams_r(data, period)
    moving_average = calculate_moving_average(data, ma_period)
    
    if williams_r < -80 and data['Close'][-1] > moving_average:
        [return](../r/return.md) "Buy"
    elif williams_r > -20 and data['Close'][-1] < moving_average:
        [return](../r/return.md) "Sell"
    [return](../r/return.md) "[Hold](../h/hold.md)"

# Sample data for testing
sample_data = {
    'High': [147, 150, 149, 152, 150],
    'Low': [137, 135, 140, 145, 142],
    'Close': [145, 148, 146, 150, 149]
}

# Run the strategy with a 14-day lookback period and a 10-day MA
signal = execute_combined_strategy(sample_data, 14, 10)
print(signal)
```

---

### Real-World Application and Case Studies

#### High-Frequency Trading (HFT)

HFT firms employ strategies that require rapid decision-making and [execution](../e/execution.md). Williams %R is particularly useful in this context for its quick responsiveness to price changes.

For example, firms like Citadel Securities and Virtu Financial may incorporate Williams %R into their algorithms for rapid [trade](../t/trade.md) signals. Visit Citadel Securities or Virtu Financial for more details on these firms.

#### Quantitative Hedge Funds

[Quantitative hedge funds](../q/quantitative_hedge_funds.md) often use a multitude of indicators to optimize strategies. Firms like Renaissance Technologies might integrate Williams %R with advanced statistical methods to enhance [predictive models](../p/predictive_models_in_trading.md). For more details, [check](../c/check.md) out Renaissance Technologies.

#### Retail Investors

Platforms like MetaTrader or [TradeStation](../t/tradestation.md) allow retail investors to implement Williams %R in their custom algorithms. These platforms typically provide [backtesting](../b/backtesting.md) tools to validate strategies before deployment.

---

### Conclusion

Williams %R is a versatile and powerful [indicator](../i/indicator.md) that holds tremendous [value](../v/value.md) in the realm of [algorithmic trading](../a/algorithmic_trading.md). Its ability to signal [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions, combined with its simplicity, makes it an indispensable tool for both novice and experienced traders. By integrating Williams %R with other [technical indicators](../t/technical_indicators.md) and employing [robust](../r/robust.md) [backtesting](../b/backtesting.md) methodologies, traders can enhance their strategies’ accuracy and profitability.
