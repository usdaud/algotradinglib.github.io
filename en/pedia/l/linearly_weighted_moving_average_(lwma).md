# Linearly Weighted Moving Average (LWMA)

A Linearly [Weighted](../w/weighted.md) Moving Average (LWMA) is a type of moving average used in statistical analysis and financial trading. Unlike a simple moving average (SMA) that gives [equal weight](../e/equal_weight.md) to all data points within the window, the LWMA assigns more weight to recent data points. This makes the LWMA more responsive to recent price movements, which is particularly useful in time-sensitive [trading strategies](../t/trading_strategies.md).

## Concept and Calculation

LWMA is calculated by multiplying each price within the selected period by a predefined weight and then summing up the results. The weight assigned to each price decreases linearly from the latest price to the oldest price. Here's a step-by-step explanation of how to compute the LWMA:

1. **Define the Time Period (n)**: Decide the length of the period over which the average [will](../w/will.md) be computed (e.g., 10 days).
2. **Assign Weights**: Assign weights to each data point. For an n-period LWMA, the most recent data point receives a weight of n, the second most recent receives n-1, and so on until the oldest data point which receives a weight of 1.
3. **Multiply and Sum**: Multiply each data point by its weight and then sum these products.
4. **Normalize**: Divide the sum of the products by the sum of the weights to normalize the average.

The formula can be expressed as:

\[ LWMA = \frac{\sum_{i=1}^{n} (Price_i \times Weight_i)}{\sum_{i=1}^{n} Weight_i} \]

where:
* \( Price_i \) is the price at the ith position within the window.
* \( Weight_i \) is the weight assigned to the ith position.
* \( n \) is the total number of time periods.

For a 5-day LWMA, the latest price would be multiplied by 5, the second latest by 4, and so on. The sum of these products would then be divided by the sum of weights (which is 5+4+3+2+1=15 in this case).

## Features and Benefits

### Increased Sensitivity

Due to its higher weighting on recent data, the LWMA is more sensitive to new information compared to an SMA. This makes it a useful tool for traders looking to capture short-term price movements.

### Smoothing Effect

While being sensitive, the LWMA still provides a degree of smoothing, removing some of the "[noise](../n/noise.md)" from the price data and providing a clearer [trend](../t/trend.md) direction. This balance makes it suitable for various [trading strategies](../t/trading_strategies.md), from [swing trading](../s/swing_trading.md) to [day trading](../d/day_trading.md).

### Lag Reduction

A common problem with moving averages is the lag they introduce. Because the LWMA gives more weight to recent prices, it reduces the lag compared to SMAs and makes it more reactive to swift [market](../m/market.md) changes.

## Applications in Trading

### Trend Identification

Traders often use LWMAs to identify trends in [asset](../a/asset.md) prices. When the price of an [asset](../a/asset.md) is consistently above its LWMA, it suggests an [uptrend](../u/uptrend.md). Conversely, when the price is below its LWMA, it indicates a [downtrend](../d/downtrend.md).

### Support and Resistance Levels

LWMAs can act as dynamic [support and resistance](../s/support_and_resistance.md) levels. When the price of an [asset](../a/asset.md) is above the LWMA, it often acts as support, where prices tend to bounce during pullbacks. Conversely, when the price is below the LWMA, it can act as a resistance level.

### Crossover Strategies

One popular [trading strategy](../t/trading_strategy.md) is the moving average crossover strategy. Traders can use two LWMAs of different periods (e.g., a 10-day and a 50-day LWMA). A buy signal is generated when the short-term LWMA crosses above the long-term LWMA, indicating a potential upward [trend](../t/trend.md). Conversely, a sell signal is generated when the short-term LWMA crosses below the long-term LWMA.

### Oscillator Development

The LWMA can also be incorporated into oscillators by comparing its values over different time frames. This can help traders identify [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions.

## Comparison with Other Moving Averages

### Simple Moving Average (SMA)

The SMA is straightforward but assigns [equal weight](../e/equal_weight.md) to all data points, making it less responsive to recent price changes. This can result in significant lag, which may cause traders to miss timely entry or exit points.

### Exponential Moving Average (EMA)

The EMA, like the LWMA, assigns more weight to recent prices but does so exponentially rather than linearly. This can make the EMA even more sensitive to recent price changes compared to the LWMA. However, the choice between LWMA and EMA often comes down to [trader](../t/trader.md) preference and specific strategy requirements.

### Weighted Moving Average (WMA)

While similar in concept to the LWMA, the WMA can use a variety of weighting schemes, not necessarily linear. This flexibility allows for customization based on the [trader](../t/trader.md)'s need but can also complicate the calculation and interpretation.

## Limitations

### Sensitivity to Noise

While the LWMA is sensitive to recent price changes, this can also make it more susceptible to [market](../m/market.md) "[noise](../n/noise.md)," leading to potential [false signals](../f/false_signals_in_trading.md).

### Complexity

The calculation of LWMA is more complex compared to SMA, especially for manual calculations or when implementing custom [trading algorithms](../t/trading_algorithms.md).

### Not Foolproof

No moving average, including LWMA, can guarantee profitable trades. They should be used as part of a broader [trading strategy](../t/trading_strategy.md) that includes other indicators and [risk management techniques](../r/risk_management_techniques.md).

## Implementation in Trading Platforms

Most trading platforms and financial software provide built-in functions to calculate LWMAs. Here's how to implement LWMA in some popular platforms:

### Python (with pandas)

```python
[import](../i/import.md) pandas as pd

def lwma(prices, window):
    weights = pd.Series([range](../r/range.md)(1, window + 1))
    lwma = prices.rolling(window).apply([lambda](../l/lambda.md) prices: (weights * prices).sum() / weights.sum(), raw=False)
    [return](../r/return.md) lwma

# Example Usage
data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
lwma_5 = lwma(data, 5)
print(lwma_5)

```

### MetaTrader 4 (MQL4)

```mql4
int lwmaPeriod = 14;

double LWMA(int period, int shift)
{
    double lwma = 0;
    double sum = 0;
    double weightSum = 0;
    for (int i = 0; i < period; i++)
    {
        double price = iClose(NULL, 0, shift + i);
        lwma += price * (period - i);
        sum += price;
        weightSum += period - i;
    }
    [return](../r/return.md) lwma / weightSum;
}

// Example Usage
double result = LWMA(lwmaPeriod, 0);
```

### SQL (for database processing)

```sql
WITH weights AS (
    SELECT generate_series AS weight
    FROM generate_series(1, 14)
),
prices_with_weights AS (
    SELECT
        time,
        close_price,
        ROW_NUMBER() OVER ([ORDER](../o/order.md) BY time DESC) AS rownum
    FROM
        price_data
    [ORDER](../o/order.md) BY
        time DESC
    LIMIT 14
)
SELECT SUM(close_price * weights.weight) / SUM(weights.weight) AS lwma
FROM prices_with_weights, weights
WHERE prices_with_weights.rownum = weights.weight;
```

## Conclusion

The Linearly [Weighted](../w/weighted.md) Moving Average is a powerful tool for traders and analysts who require a balance between responsiveness and smoothing in their data analysis. By assigning greater weight to more recent prices, the LWMA can quickly adapt to changing [market](../m/market.md) conditions while still filtering out some of the [noise](../n/noise.md) associated with price [volatility](../v/volatility.md). As with all [technical indicators](../t/technical_indicator.md), the LWMA should be used in conjunction with other analytical tools and [risk management](../r/risk_management.md) practices to optimize [trading performance](../t/trading_performance.md).