# Average Directional Index

The Average Directional [Index](../i/index_instrument.md) (ADX) is a [technical analysis](../t/technical_analysis.md) [indicator](../i/indicator.md) developed by J. Welles Wilder Jr. in 1978. It is used to quantify the strength of a [trend](../t/trend.md) in a financial [market](../m/market.md), whether the [trend](../t/trend.md) is upward or downward. The ADX is part of the Directional Movement System and is typically plotted as a single line, which helps traders to distinguish between strong and weak trends.

## Components of ADX

The ADX is calculated using the Moving Average of price [range](../r/range.md) [expansion](../e/expansion.md). The system it belongs to also involves two other indicators:

1. **Positive Directional [Index](../i/index_instrument.md) (+DI)**: Measures the presence and strength of upward movement in the [market](../m/market.md).
2. **Negative Directional [Index](../i/index_instrument.md) (-DI)**: Measures the presence and strength of downward movement in the [market](../m/market.md).

When combined, the ADX, +DI, and -DI provide a comprehensive view of [market](../m/market.md) trends and their strengths.

### Calculating the ADX

1. **Calculate True [Range](../r/range.md) (TR)**: The TR for each period is the greatest of the following:
 - Current High minus Current Low
 - Absolute [value](../v/value.md) of Current High minus Previous Close
 - Absolute [value](../v/value.md) of Current Low minus Previous Close

2. **Calculate the Directional Movement (+DM and -DM)**:
 - +DM equals Current High minus Previous High, if Current High minus Previous High is greater than Current Low minus Previous Low. Otherwise, +DM is zero.
 - -DM equals Previous Low minus Current Low, if Previous Low minus Current Low is greater than Current High minus Previous High. Otherwise, -DM is zero.

3. **Smooth the TR, +DM, and -DM values** typically over a 14-day period.

4. **Calculate the +DI and -DI** by dividing the smoothed +DM and -DM by the smoothed TR.

5. **Calculate the Directional Movement [Index](../i/index_instrument.md) (DX)**:
 - DX = ABS(+DI - -DI) / (+DI + -DI) * 100

6. **Calculate the ADX** by smoothing the DX values, usually with a 14-bar Moving Average.

### Interpreting the ADX

- An **ADX [value](../v/value.md) above 25** typically indicates a strong [trend](../t/trend.md).
- An **ADX [value](../v/value.md) below 20** signals a weak [trend](../t/trend.md) or a ranging [market](../m/market.md).
- ADX values can help traders avoid [false signals](../f/false_signals_in_trading.md) by confirming the [trend](../t/trend.md) strength.

## Use Cases in Algorithmic Trading

In [algorithmic trading](../a/algorithmic_trading.md), the ADX is often used in various strategic approaches, including:

1. **[Trend Following](../t/trend_following.md)**: Algorithms can enter or exit trades based on whether the ADX indicates a strong or weak [trend](../t/trend.md).
2. **[Volatility](../v/volatility.md) Filters**: ADX values can act as filters to ensure that trades are only initiated when there is sufficient [market](../m/market.md) movement.
3. **[Risk Management](../r/risk_management.md)**: ADX can be used to adjust [position sizing](../p/position_sizing.md) according to [trend](../t/trend.md) strength to manage [risk](../r/risk.md) better.

## Limitations of ADX

While the ADX is a valuable tool, it has some limitations:

- **[Lagging Indicator](../l/lagging_indicator.md)**: Like many [trend](../t/trend.md)-following indicators, the ADX is often slow to respond to rapid [market](../m/market.md) changes.
- **No Directional Bias**: The ADX indicates [trend](../t/trend.md) strength but does not specify the direction – traders must use +DI and -DI or other indicators for directional cues.
- **Complex Calculation**: The multi-step calculation can be complex without software or algorithmic assistance.

## Implementation in Trading Algorithms

### Python Example

Below is a simplified Python implementation using the `pandas` library for calculating the ADX:

```python
[import](../i/import.md) pandas as pd

def calculate_adx(data, period=14):
    # Calculate True [Range](../r/range.md) (TR)
    data['ATR'] = data['High'] - data['Low']
    data['ATR_1'] = abs(data['High'] - data['Close'].shift(1))
    data['ATR_2'] = abs(data['Low'] - data['Close'].shift(1))
    data['TrueRange'] = data[['ATR', 'ATR_1', 'ATR_2']].max(axis=1)
    
    # Calculate +DM and -DM
    data['+DM'] = data['High'].diff()
    data['-DM'] = data['Low'].diff()
    data['+DM'] = data['+DM'].apply([lambda](../l/lambda.md) x: x if x > 0 else 0)
    data['-DM'] = data['-DM'].apply([lambda](../l/lambda.md) x: abs(x) if x < 0 else 0)
    
    # Smooth the True [Range](../r/range.md) and Directional Movement
    data['smoothed_TR'] = data['TrueRange'].rolling(window=period).mean()
    data['smoothed_+DM'] = data['+DM'].rolling(window=period).mean()
    data['smoothed_-DM'] = data['-DM'].rolling(window=period).mean()
    
    # Calculate +DI and -DI
    data['+DI'] = 100 * (data['smoothed_+DM'] / data['smoothed_TR'])
    data['-DI'] = 100 * (data['smoothed_-DM'] / data['smoothed_TR'])
    
    # Calculate DX
    data['DX'] = (abs(data['+DI'] - data['-DI']) / (data['+DI'] + data['-DI'])) * 100
    
    # Calculate ADX
    data['ADX'] = data['DX'].rolling(window=period).mean()
    
    [return](../r/return.md) data['ADX']

# Example Data
data = pd.DataFrame{
    'High': [1.20, 1.25, 1.30, 1.35, 1.40],
    'Low': [1.10, 1.15, 1.18, 1.20, 1.25],
    'Close': [1.15, 1.20, 1.25, 1.32, 1.35]
})

adx_values = calculate_adx(data)
print(adx_values)
```

## Popular Tools and Platforms that Support ADX

Several financial platforms and tools support the ADX [indicator](../i/indicator.md). Notable examples include:

1. **MetaTrader**: One of the most popular trading platforms that [offer](../o/offer.md) ADX built-in indicators.
2. **[TradeStation](../t/tradestation.md)**: A comprehensive [trading platform](../t/trading_platform.md) that supports advanced [indicator](../i/indicator.md) scripting, including ADX.
3. **[TradingView](../t/tradingview.md)**: An online platform known for its powerful charting tools and extensive [indicator](../i/indicator.md) library, including ADX.

Each of these platforms provides customization features allowing traders to tweak ADX settings to fit their [trading strategies](../t/trading_strategies.md).

**MetaTrader**: MetaTrader

**[TradeStation](../t/tradestation.md)**: TradeStation

**[TradingView](../t/tradingview.md)**: TradingView

In conclusion, the Average Directional [Index](../i/index_instrument.md) (ADX) is an essential tool in the arsenal of both manual and algorithmic traders. It provides a quantitative measure of [trend](../t/trend.md) strength, helping traders make informed decisions on [market](../m/market.md) entry and exit points. While it has its limitations, when used correctly, the ADX can significantly enhance the effectiveness of a [trading strategy](../t/trading_strategy.md).
