# Индикатор

Индикатор в алгоритмической торговле - это математический расчет, основанный на исторической информации о цене, объеме или открытом интересе, целью которого является прогнозирование будущих рыночных движений. Индикаторы являются важнейшими инструментами технического анализа и помогают трейдерам принимать более обоснованные решения, выявляя тренды, волатильность, моментум и другие рыночные характеристики. Существует несколько категорий и типов индикаторов, каждый из которых служит определенной цели. Данная статья направлена на формирование всестороннего понимания различных индикаторов и их применения в алгоритмической торговле.

## Скользящие средние

### Простая скользящая средняя (SMA)

Простая скользящая средняя - один из наиболее часто используемых индикаторов. Она рассчитывает среднюю цену за указанное количество периодов. SMA часто используется для определения направления тренда. Например, 50-дневная SMA - это среднее значение цен закрытия за последние 50 дней.

```python
def calculate_sma(prices, period):
    return sum(prices[-period:]) / period
```

### Экспоненциальная скользящая средняя (EMA)

Экспоненциальная скользящая средняя придает больший вес недавним ценам, что делает ее более чувствительной к новой информации. Формула EMA применяет мультипликативный коэффициент к самым последним точкам данных.

```python
def calculate_ema(prices, period):
    ema = [sum(prices[:period]) / period]
    multiplier = 2 / (period + 1)
    for price in prices[period:]:
        ema.append(((price - ema[-1]) * multiplier) + ema[-1])
    return ema
```

## Осцилляторы

### Индекс относительной силы (RSI)

Индекс относительной силы - это осциллятор моментума, который измеряет скорость и изменение ценовых движений. RSI колеблется между 0 и 100 и обычно используется для выявления состояний перекупленности или перепроданности.

```python
def calculate_rsi(prices, period=14):
    deltas = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
    gain = sum([delta for delta in deltas if delta > 0])
    loss = abs(sum([delta for delta in deltas if delta < 0]))
    avg_gain = gain / period
    avg_loss = loss / period
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))
```

### Стохастический осциллятор

Стохастический осциллятор сравнивает конкретную цену закрытия ценной бумаги с диапазоном ее цен за определенный период. Он генерирует две линии, %K и %D, для выявления состояний перекупленности или перепроданности.

```python
def calculate_stochastic_oscillator(prices, period=14):
    high_low_diff = [max(prices[i-period:i]) - min(prices[i-period:i]) for i in range(period, len(prices))]
    %K = [(prices[i] - min(prices[i-period:i])) / high_low_diff[i-period] * 100 for i in range(period, len(prices))]
    %D = [sum(%K[i-2:i+1]) / 3 for i in range(2, len(%K))]
    return %K, %D
```

## Индикаторы объема

### Балансовый объем (OBV)

Индикатор балансового объема использует поток объема для прогнозирования изменений цены акций. Он добавляет объем в дни роста и вычитает в дни падения.

```python
def calculate_obv(prices, volumes):
    obv = [volumes[0]]
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            obv.append(obv[-1] + volumes[i])
        elif prices[i] < prices[i-1]:
            obv.append(obv[-1] - volumes[i])
        else:
            obv.append(obv[-1])
    return obv
```

### Средневзвешенная по объему цена (VWAP)

Средневзвешенная по объему цена показывает среднюю цену, по которой ценная бумага торговалась в течение дня, на основе как объема, так и цены. Обычно используется как торговый ориентир.

```python
def calculate_vwap(prices, volumes):
    cumulative_price_volume = sum([price * volume for price, volume in zip(prices, volumes)])
    cumulative_volume = sum(volumes)
    return cumulative_price_volume / cumulative_volume
```

## Индикаторы волатильности

### Полосы Боллинджера

Полосы Боллинджера состоят из средней полосы, являющейся скользящей средней, и двух внешних полос, рассчитанных как стандартные отклонения от скользящей средней. Они помогают выявлять волатильность и состояния перекупленности/перепроданности.

```python
import numpy as np

def calculate_bollinger_bands(prices, period=20):
    sma = np.mean(prices[-period:])
    std_dev = np.std(prices[-period:])
    upper_band = sma + (2 * std_dev)
    lower_band = sma - (2 * std_dev)
    return upper_band, sma, lower_band
```

### Средний истинный диапазон (ATR)

Средний истинный диапазон - это индикатор волатильности, измеряющий диапазон, в котором обычно колеблется цена актива. Он дает представление о том, насколько цена движется в течение установленного периода.

```python
def calculate_atr(high, low, close, period=14):
    tr = [max(high[i] - low[i], abs(high[i] - close[i-1]), abs(low[i] - close[i-1])) for i in range(1, len(high))]
    atr = [sum(tr[:period]) / period]
    for i in range(period, len(tr)):
        atr.append((atr[-1] * (period - 1) + tr[i]) / period)
    return atr
```

## Трендовые индикаторы

### Схождение/расхождение скользящих средних (MACD)

MACD вычисляет разницу между двумя экспоненциальными скользящими средними (EMA), обычно 12-периодной EMA и 26-периодной EMA. 9-периодная EMA от MACD называется "сигнальной линией".

```python
def calculate_macd(prices, fast_period=12, slow_period=26, signal_period=9):
    fast_ema = calculate_ema(prices, fast_period)
    slow_ema = calculate_ema(prices, slow_period)
    macd = [fast - slow for fast, slow in zip(fast_ema, slow_ema)]
    signal_line = calculate_ema(macd, signal_period)
    return macd, signal_line
```

### Параболический SAR

Параболический SAR (Stop and Reverse) используется для определения направления моментума актива и момента времени, когда этот моментум имеет повышенную вероятность смены направления.

```python
def calculate_parabolic_sar(high, low, af=0.02, max_af=0.2):
    sar = low[0]  # Начинаем с первого минимума
    ep = high[0]  # Наивысшая цена (Extreme Point)
    trend = 1  # 1 для восходящего тренда, 0 для нисходящего
    sar_list = []

    for i in range(1, len(high)):
        sar_list.append(sar)
        if trend == 1:
            sar = sar + af * (ep - sar)
            if high[i] > ep:
                ep = high[i]
                af = min(af + 0.02, max_af)
            if low[i] < sar:
                trend = 0
                sar = ep
                ep = low[i]
                af = 0.02
        else:
            sar = sar - af * (sar - ep)
            if low[i] < ep:
                ep = low[i]
                af = min(af + 0.02, max_af)
            if high[i] > sar:
                trend = 1
                sar = ep
                ep = high[i]
                af = 0.02

    sar_list.append(sar)
    return sar_list
```

## Заключение

Индикаторы являются бесценными инструментами для алгоритмической торговли, предоставляя информацию о рыночных трендах, моментуме, волатильности и объеме. Каждый индикатор имеет свои уникальные преимущества и области применения, что делает их подходящими для различных торговых стратегий. Комбинируя несколько индикаторов, трейдеры могут создавать надежные торговые алгоритмы, способные адаптироваться к различным рыночным условиям.
