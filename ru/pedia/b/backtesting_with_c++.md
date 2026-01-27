# Бэктестинг на C++

Бэктестинг — важный процесс в алгоритмической торговле, который включает проверку торговой стратегии на исторических данных, чтобы оценить ее эффективность до запуска на реальных рынках. В этом материале мы подробно рассмотрим бэктестинг и реализацию на C++. От понимания преимуществ и ограничений до построения полноценной системы — это руководство охватывает ключевые аспекты.

## Введение в бэктестинг

Бэктестинг — это метод симуляции работы торговой стратегии на исторических данных. Он помогает понять, как стратегия могла бы работать в прошлом, и использовать этот опыт для оценки потенциальных результатов в будущем. Он позволяет уточнять стратегии, выявлять риски и улучшать алгоритмы.

### Важность бэктестинга

1. **Проверка стратегии**: прежде чем рисковать реальными деньгами, важно убедиться, что стратегия работает как задумано. Бэктестинг дает эту проверку.
2. **Управление рисками**: определение возможных просадок и неблагоприятных условий помогает лучше управлять риском.
3. **Метрики эффективности**: такие показатели, как profit factor, коэффициент Шарпа и максимальная просадка, помогают количественно оценить стратегию.
4. **Операционные инсайты**: бэктестинг выявляет операционные нюансы и помогает настроить стратегию для более эффективного использования ресурсов.

### Ограничения бэктестинга

1. **Историческая предвзятость**: будущее не всегда похоже на прошлое. Стратегии, хорошо работающие на истории, могут показывать иные результаты в реальной торговле.
2. **Качество и доступность данных**: точность результатов зависит от качества и детализации исторических данных.
3. **Переобучение**: чрезмерная подгонка параметров под историю приводит к слабым результатам в будущем.

## Настройка окружения

Для бэктестинга на C++ требуется среда разработки и библиотеки. Основные компоненты:

1. **Компилятор**: GCC или Visual Studio.
2. **IDE**: Visual Studio, CLion и другие C++ IDE.
3. **Библиотеки**:
 - Boost: утилиты для работы со временем, файлами и т. д.
 - QT: фреймворк для GUI при необходимости.
 - Talib: функции технического анализа (в основном в Python, но доступна интеграция с C++).

### Установка библиотек

Убедитесь, что компилятор и библиотеки установлены. Например, установка Boost на Linux:

```sh
sudo apt-get install libboost-all-dev
```

## Построение системы бэктестинга на C++

Ниже — пошаговая схема создания системы бэктестинга.

### Шаг 1: Работа с данными

Эффективная обработка данных — ключ к бэктестингу. Мы будем читать исторические цены (обычно CSV) и обрабатывать их.

#### Чтение CSV

Простой парсер CSV можно реализовать через файловые операции:

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

struct MarketData {
    std::string date;
    double open;
    double high;
    double low;
    double close;
    double volume;
};

std::vector<MarketData> readCSV(const std::string& fileName) {
    std::ifstream file(fileName);
    std::vector<MarketData> data;
    std::string line, token;

    // Skip the header line
    std::getline(file, line);

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        MarketData entry;

        std::getline(ss, entry.date, ',');
        ss >> entry.open;
        ss.ignore();
        ss >> entry.high;
        ss.ignore();
        ss >> entry.low;
        ss.ignore();
        ss >> entry.close;
        ss.ignore();
        ss >> entry.volume;

        data.push_back(entry);
    }

    return data;
}
```

### Шаг 2: Реализация стратегии

Нужно определить логику сигналов покупки и продажи. Рассмотрим простую стратегию пересечения скользящих средних.

#### Пересечение скользящих средних

Сигнал на покупку возникает, когда короткая средняя пересекает длинную снизу вверх, и сигнал на продажу — когда пересекает сверху вниз.

```cpp
#include <numeric>

// Calculate Simple Moving Average
double calculateSMA(const std::vector<double>& prices, int period) {
    double sum = std::accumulate(prices.end() - period, prices.end(), 0.0);
    return sum / period;
}

// Signal Generation
enum Signal { NONE, BUY, SELL };

Signal generateSignal(const std::vector<double>& shortMA, const std::vector<double>& longMA, size_t index) {
    if (shortMA[index] > longMA[index] && shortMA[index - 1] <= longMA[index - 1])
        return BUY;
    if (shortMA[index] < longMA[index] && shortMA[index - 1] >= longMA[index - 1])
        return SELL;
    return NONE;
}

std::vector<Signal> backtestStrategy(const std::vector<MarketData>& data, int shortPeriod, int longPeriod) {
    std::vector<Signal> signals(data.size(), NONE);
    std::vector<double> shortMA(data.size(), 0.0);
    std::vector<double> longMA(data.size(), 0.0);

    for (size_t i = longPeriod; i < data.size(); ++i) {
        std::vector<double> prices(data.begin() + i - shortPeriod, data.begin() + i);
        shortMA[i] = calculateSMA(prices, shortPeriod);

        prices.assign(data.begin() + i - longPeriod, data.begin() + i);
        longMA[i] = calculateSMA(prices, longPeriod);

        signals[i] = generateSignal(shortMA, longMA, i);
    }

    return signals;
}
```

### Шаг 3: Симуляция сделок

Симулируем сделки на основе сигналов стратегии. Для этого ведем учет позиций и рассчитываем прибыль/убыток.

#### Симуляция сделок

Мы будем вести систему отслеживания позиции и рассчитывать P&L по совершенным сделкам.

```cpp
enum Position { FLAT, LONG, SHORT };

struct Trade {
    std::string date;
    Position position;
    double price;
};

std::vector<Trade> simulateTrades(const std::vector<MarketData>& data, const std::vector<Signal>& signals) {
    std::vector<Trade> trades;
    Position currentPosition = FLAT;

    for (size_t i = 0; i < data.size(); ++i) {
        if (signals[i] == BUY && currentPosition == FLAT) {
            trades.push_back({data[i].date, LONG, data[i].close});
            currentPosition = LONG;
        }
        else if (signals[i] == SELL && currentPosition == LONG) {
            trades.push_back({data[i].date, FLAT, data[i].close});
            currentPosition = FLAT;
        }
    }

    return trades;
}
```

### Шаг 4: Метрики эффективности

Количественная оценка результатов необходима для понимания эффективности стратегии. Среди основных метрик — общая доходность, годовая доходность, коэффициент Шарпа и максимальная просадка.

#### Расчет метрик

```cpp
#include <cmath>

class PerformanceMetrics {
public:
    static double calculateTotalReturn(const std::vector<Trade>& trades) {
        if (trades.empty()) return 0.0;

        double initialCapital = trades.front().price;
        double finalCapital = trades.back().price;

        return (finalCapital - initialCapital) / initialCapital;
    }

    static double calculateAnnualizedReturn(const std::vector<Trade>& trades, int years) {
        double totalReturn = calculateTotalReturn(trades);
        return std::pow(1 + totalReturn, 1.0 / years) - 1;
    }

    // Assume daily returns are available
    static double calculateSharpeRatio(const std::vector<double>& dailyReturns, double riskFreeRate) {
        double mean = std::accumulate(dailyReturns.begin(), dailyReturns.end(), 0.0) / dailyReturns.size();
        double variance = 0.0;

        for (double r : dailyReturns) {
            variance += std::pow(r - mean, 2);
        }
        variance /= dailyReturns.size();

        double stddev = std::sqrt(variance);
        return (mean - riskFreeRate) / stddev;
    }
};
```

## Заключение

Бэктестинг — ключевой элемент алгоритмической торговли, позволяющий проверять стратегии на исторических данных. Использование C++ дает скорость и эффективность, позволяя работать с большими объемами данных и сложными алгоритмами.

В этом материале мы рассмотрели весь цикл бэктестинга на C++: чтение данных, реализация стратегии, симуляция сделок и оценка результатов. Это базовое руководство дает инструменты и знания для построения устойчивых систем бэктестинга и улучшения торговых стратегий.
