# X-Technical Indicators

[Technical indicators](../t/technical_indicators.md) are mathematical calculations based on the price, [volume](../v/volume.md), or [open interest](../o/open_interest.md) of a [security](../s/security.md) or contract. They are a fundamental aspect of [technical analysis](../t/technical_analysis.md) and are used by traders to predict future price movements. Here, we [will](../w/will.md) delve into a variety of [technical indicators](../t/technical_indicators.md), exploring both their theoretical underpinnings and practical applications.

## Moving Averages

### Simple Moving Average (SMA)
The Simple Moving Average (SMA) is the [arithmetic mean](../a/arithmetic_mean.md) of a given set of prices over a specific number of days in the past. It is calculated by summing the closing prices of a [security](../s/security.md) for a period and then dividing this total by the number of periods. For example, a 30-day SMA sums the closing prices for the last 30 days and then divides the result by 30.

### Exponential Moving Average (EMA)
The Exponential Moving Average (EMA) gives more weight to recent prices to make it more responsive to new information. The EMA is calculated using the following formula:

```
EMA = (Price_today * K) + (EMA_yesterday * (1 - K))
```

Where:
- `K` is the smoothing constant calculated as `2 / (N + 1)`.
- `N` is the number of days in EMA.

## Momentum Indicators

### Relative Strength Index (RSI)
The [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI) measures the speed and change of price movements. The RSI oscillates between zero and 100. Traditionally, RSI readings of 70 or above indicate that a [security](../s/security.md) is becoming [overbought](../o/overbought.md), while readings of 30 or below indicate that it is [oversold](../o/oversold.md).

### Moving Average Convergence Divergence (MACD)
The MACD is a [trend](../t/trend.md)-following [momentum](../m/momentum.md) [indicator](../i/indicator.md) that shows the relationship between two moving averages of a [security](../s/security.md)’s price. The MACD is calculated by subtracting the 26-period EMA from the 12-period EMA. A nine-period EMA of the MACD known as the "signal line" is then plotted on top of the MACD line, which can function as a trigger for buy and sell signals.

## Oscillators

### Stochastic Oscillator
The [Stochastic Oscillator](../s/stochastic_oscillator.md) compares a particular closing price of a [security](../s/security.md) to a [range](../r/range.md) of its prices over a certain period. The [oscillator](../o/oscillator.md) ranges from 0 to 100 and is used to identify [overbought](../o/overbought.md) and [oversold](../o/oversold.md) conditions. It is calculated using the formula:

```
%K = (Current Close - Lowest Low) / (Highest High - Lowest Low) * 100
```

The `%D` line is a 3-day simple moving average of `%K`.

### Commodity Channel Index (CCI)
The [Commodity](../c/commodity.md) Channel [Index](../i/index_instrument.md) (CCI) measures the variation of a [security](../s/security.md)'s price from its average price. High positive readings suggest that prices are unusually high compared to their average, whereas low negative readings indicate that prices are unusually low. CCI is calculated with:

```
CCI = (Typical Price - Moving Average of Typical Price) / (0.015 * Mean Deviation)
```

Where `Typical Price = (High + Low + Close) / 3`.

## Volume-Based Indicators

### On-Balance Volume (OBV)
On-Balance [Volume](../v/volume.md) (OBV) measures buying and selling pressure as a cumulative [indicator](../i/indicator.md) that adds [volume](../v/volume.md) on up days and subtracts [volume](../v/volume.md) on down days. It is a running total of [volume](../v/volume.md) that shows if [volume](../v/volume.md) is flowing in or out of a [security](../s/security.md).

### Chaikin Money Flow (CMF)
The Chaikin [Money Flow](../m/money_flow.md) (CMF) is used to measure the accumulation-[distribution](../d/distribution.md) line over a specific period. It uses both price and [volume](../v/volume.md) to measure buying and selling pressure.

```
CMF = {Sum of [[Volume](../v/volume.md) * ((Close - Low) - (High - Close)) / (High - Low)]} / Sum of [Volume](../v/volume.md)
```

## Volatility Indicators

### Bollinger Bands
[Bollinger Bands](../b/bollinger_bands.md) consist of a middle band being a simple moving average, and an upper and lower band at standard deviations above and below the SMA. The formula for [Bollinger Bands](../b/bollinger_bands.md) is:

```
Upper Band = SMA + ([Standard Deviation](../s/standard_deviation.md) * N)
Lower Band = SMA - ([Standard Deviation](../s/standard_deviation.md) * N)
```

Where `N` is the number of days in the calculation, the [default](../d/default.md) being 20.

### Average True Range (ATR)
The [Average True Range](../a/average_true_range_(atr).md) (ATR) is an [indicator](../i/indicator.md) that measures [market](../m/market.md) [volatility](../v/volatility.md). It is typically derived from the 14-day simple moving average of a series of true [range](../r/range.md) indicators.

```
True [Range](../r/range.md) (TR) = Maximum[(High - Low), (High - Close_previous), (Low - Close_previous)]
```

ATR is the moving average of TR over a specified period.

## Trend Indicators

### Parabolic SAR
The [Parabolic SAR](../p/parabolic_sar.md) is a [trend](../t/trend.md)-following [indicator](../i/indicator.md) that helps identify potential [reversal](../r/reversal.md) points in the price direction of a [security](../s/security.md). It is represented on the chart by a series of dots placed either above or below the price bars (depending on the [trend](../t/trend.md) direction).

The SAR is calculated as follows:
- If in an [uptrend](../u/uptrend.md), SAR_n+1 = SAR_n + AF * (EP - SAR_n)
- If in a [downtrend](../d/downtrend.md), SAR_n+1 = SAR_n - AF * (SAR_n - EP)

Where:
- `AF` is the acceleration [factor](../f/factor.md) ([default](../d/default.md) is 0.02).
- `EP` is the highest high in an [uptrend](../u/uptrend.md) and the lowest low in a [downtrend](../d/downtrend.md).

### Ichimoku Cloud
The [Ichimoku Cloud](../i/ichimoku_cloud.md) is a collection of [technical indicators](../t/technical_indicators.md) that shows [support and resistance](../s/support_and_resistance.md) levels, [momentum](../m/momentum.md), and [trend](../t/trend.md) direction. It provides more data points than the standard [candlestick](../c/candlestick.md) charts by generating five different lines:

- Tenkan-sen (Conversion Line): (Highest High + Lowest Low) / 2 over the last 9 periods.
- Kijun-sen (Base Line): (Highest High + Lowest Low) / 2 over the last 26 periods.
- Senkou Span A (Leading Span A): (Tenkan-sen + Kijun-sen) / 2, plotted 26 periods ahead.
- Senkou Span B (Leading Span B): (Highest High + Lowest Low) / 2 over the last 52 periods, plotted 26 periods ahead.
- Chikou Span (Lagging Span): Closing price plotted 26 periods back.

## Companies and Tools

### MetaTrader 5 (MT5)
MetaTrader 5 is a multi-[asset](../a/asset.md) platform that allows trading Forex, [stocks](../s/stock.md), and [futures](../f/futures.md). It offers [advanced technical analysis](../a/advanced_technical_analysis.md) tools, [automated trading systems](../a/automated_trading_systems.md) (trading bots, Expert Advisors), and copy trading.

Visit MetaTrader [here](https://www.metatrader5.com/en).

### TradingView
[TradingView](../t/tradingview.md) is a social network for traders and investors, [offering](../o/offering.md) live quotes, stock charts, and expert trading ideas. It also provides a wide [range](../r/range.md) of [technical analysis](../t/technical_analysis.md) tools and indicators to aid in trading decisions.

Visit [TradingView](../t/tradingview.md) [here](https://www.tradingview.com/).

### QuantConnect
[QuantConnect](../q/quantconnect.md) is an [algorithmic trading](../a/algorithmic_trading.md) platform that provides data, [broker](../b/broker.md) integrations, and an IDE to design and backtest [trading strategies](../t/trading_strategies.md) in [multiple](../m/multiple.md) programming languages. It supports the development of indicators to be utilized in custom [trading algorithms](../t/trading_algorithms.md).

Visit [QuantConnect](../q/quantconnect.md) [here](https://www.quantconnect.com/).

## Conclusion

X-[Technical Indicators](../t/technical_indicators.md) [offer](../o/offer.md) a myriad of tools for traders to assess [market](../m/market.md) conditions and make informed trading decisions. By employing these indicators, traders can [gain](../g/gain.md) insights into trends, [momentum](../m/momentum.md), [volatility](../v/volatility.md), and [volume](../v/volume.md), thus enhancing their strategies and improving potential outcomes.
