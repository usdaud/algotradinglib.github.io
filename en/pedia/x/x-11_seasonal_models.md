# X-11 Seasonal Adjustment

In the realm of [econometrics](../e/econometrics_in_trading.md) and [time series analysis](../t/time_series_analysis.md), the [X-11 seasonal adjustment](../x/x-11_seasonal_adjustment.md) method plays a pivotal role. Developed in the 1960s by the United States Census Bureau, the X-11 method is a widely respected approach for removing seasonal effects from monthly and quarterly economic data. The evolution of the X-11 methodology has given rise to several sophisticated versions, such as X-12 and X-13, but this document [will](../w/will.md) focus on the foundation: the classic X-11 method.

### Introduction to Seasonal Adjustment

Seasonal adjustment refers to the process of identifying and removing the periodic fluctuations in [time series](../t/time_series.md) data that occur at regular intervals less than a year, such as monthly or quarterly. These fluctuations can obscure the true [underlying](../u/underlying.md) trends and cyclical components. Seasonal adjustments are crucial for accurate [economic forecasting](../e/economic_forecasting.md), [trend analysis](../t/trend_analysis.md), and policy making.

### The X-11 Method in Detail

The X-11 method is a class of procedures based on moving average techniques that are designed to [handle](../h/handle.md) various complexities associated with [time series](../t/time_series.md) data. The algorithm attempts to isolate and adjust for seasonal effects while preserving the true structure of the data. Below are steps and components integral to the X-11 adjustment procedure:

#### 1. Decomposition of Time Series

X-11 breaks down [time series](../t/time_series.md) data into three primary components:
- **[Trend](../t/trend.md)/Cycle Component**: Indicates the long-term progression in the data, excluding seasonal fluctuations.
- **Seasonal Component**: Reflects regular, repetitive variations tied to calendar rhythms.
- **Irregular Component**: Encompasses random, irregular influences that cannot be attributed to [trend](../t/trend.md) or seasonal factors.

#### 2. Estimation of Seasonal Adjustment Factors

The seasonal component is typically estimated using a series of moving averages that capture the seasonal pattern. This involves calculating:
- **Centered Moving Averages**: To smooth the [time series](../t/time_series.md) by averaging values around each point.
- **Seasonal Factors**: Derived from the smoothed series to reflect seasonal effects over a base period, often a full year.

#### 3. Application of Multiple Filters

The method applies [multiple](../m/multiple.md) passes of moving averages, filters, and adjustments to refine the seasonal [factor](../f/factor.md) estimates and isolate the true [underlying](../u/underlying.md) [trend](../t/trend.md):
- **Symmetric Moving Averages**: Applied to mitigate endpoint issues and ensure smoother [seasonality](../s/seasonality.md).
- **Extreme [Value](../v/value.md) Adjustments**: To [handle](../h/handle.md) outliers that could distort seasonal estimates.

#### 4. Iterative Process

The X-11 involves repetitive cycles of estimating and adjusting:
- Extract initial estimates of seasonal and irregular components.
- Refine seasonal factors by re-estimating using the adjusted series.
- Repeat the adjustment process until stable seasonal factors are achieved.

### Key Features and Advantages

- **Empirically Tested**: The X-11 has demonstrated [robust](../r/robust.md) performance across various datasets.
- **Flexibility**: Can adapt to different periodicities and frequencies in data.
- **Detailed Diagnostics**: Provides comprehensive output diagnostics to evaluate the quality of the seasonal adjustment, including measures of residuals and their [distribution](../d/distribution.md).

### Advanced Extensions: X-12 and X-13 Models

The development of X-12-ARIMA and X-13-ARIMA-SEATS represents advancements of the original X-11 model, incorporating enhanced diagnostics, regression diagnostics, and the use of ARIMA models for pre-adjustment.

- **X-12-ARIMA**: Adds an ARIMA (AutoRegressive Integrated Moving Average) component to better [handle](../h/handle.md) irregular components and provide more [robust](../r/robust.md) seasonal adjustments.
- **X-13-ARIMA-SEATS**: Combines X-12 enhancements with the SEATS (Seasonal Extraction in ARIMA [Time Series](../t/time_series.md)) method, enabling model-based adjustments.

### Practical Applications in Economic Data

Seasonal adjustments using the X-11 method are vital for a wide [range](../r/range.md) of [economic indicators](../e/economic_indicators.md), including:
- **Gross Domestic Product (GDP)**
- **Consumer Price [Index](../i/index_instrument.md) (CPI)**
- **[Unemployment](../u/unemployment.md) rates**

### Implementation and Software Tools

[Multiple](../m/multiple.md) statistical software packages implement the X-11 method and its extensions:
- **SAS**: Provides PROC X11 implementing X-11 adjustments.
- **EViews**: Offers built-in functionality for X-12-ARIMA and X-13-ARIMA-SEATS adjustments.
- **Demetra**: A tool developed by Eurostat for seasonal adjustment using various methods including X-12-ARIMA and X-13.

For more details on their implementations:
- SAS: SAS Seasonal Adjustment
- EViews: EViews
- Eurostat Demetra: Demetra+

### Conclusion

The [X-11 seasonal adjustment](../x/x-11_seasonal_adjustment.md) method is a cornerstone in [time series analysis](../t/time_series_analysis.md), allowing economists and analysts to discern the genuine trends within obfuscated data. With its [robust](../r/robust.md) processing and iterative refinement, X-11 continues to be a fundamental tool in the arsenal of statistical methods, ensuring more accurate economic analysis and [forecasting](../f/forecasting.md).
