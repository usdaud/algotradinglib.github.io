# Модели количественной волатильности

Модели количественной волатильности являются важнейшими инструментами в финансовой инженерии и количественных финансах. Эти модели направлены на прогнозирование и понимание волатильности цен активов, что является ключевым фактором в торговых стратегиях, управлении рисками, ценообразовании опционов и других финансовых действиях. Это всеобъемлющее руководство охватывает различные типы моделей волатильности, их использование и их последствия.

## Типы моделей волатильности

1. **Модели исторической волатильности**:
 - Эти модели рассчитывают волатильность на основе исторических ценовых данных. Общие методы включают вычисление стандартного отклонения или дисперсии прошлых доходностей за заданный период времени.

 ```python
 import numpy as np

 def historical_volatility(prices):
 returns = np.diff(np.log(prices))
 return np.std(returns) * np.sqrt(252)
 ```

2. **Модели подразумеваемой волатильности**:
 - Подразумеваемая волатильность (IV) выводится из цен опционов, отражая ожидания рынка относительно будущей волатильности. Такие модели, как модель Блэка-Шоулза, используются для обратного расчета IV из наблюдаемых цен опционов.

 ```python
 from scipy.optimize import brentq
 from scipy.stats import norm
 import numpy as np

 def black_scholes_call(S, K, T, r, sigma):
 d1 = (np.log(S / K) + (r + 0.5 * sigma ** 0.2) * T) / (sigma * np.sqrt(T))
 d2 = d1 - sigma * np.sqrt(T)
 call = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
 return call

 def implied_volatility(S, K, T, r, market_price):
 objective_function = lambda sigma: black_scholes_call(S, K, T, r, sigma) - market_price
 return brentq(objective_function, 0.01, 2)
 ```

3. **Модели ARCH и GARCH**:
 - Изобретенные Робертом Энглом, модель авторегрессионной условной гетероскедастичности (ARCH) и ее расширение, обобщенная модель ARCH (GARCH), захватывают кластеризацию волатильности и изменяющуюся во времени волатильность.

 ```python
 from arch import arch_model

 def arch_garch_model(returns):
 model = arch_model(returns, vol='Garch', p=1, q=1)
 model_fitted = model.fit(disp='off')
 return model_fitted.forecast(horizon=1).variance[-1:]
 ```

4. **Модели стохастической волатильности**:
 - Эти модели предполагают, что волатильность следует стохастическому процессу. Модель Хестона является хорошо известным примером, моделирующим волатильность с помощью процесса возврата к среднему квадратному корню.

 ```python
 import numpy as np

 def heston_model(S, K, T, r, v0, kappa, theta, sigma, rho):
 dt = T / 100
 V = v0
 S_t = S

 for _ in range(100):
 S_t = S_t * (1 + r * dt + np.sqrt(V * dt) * np.random.normal())
 V = V + kappa * (theta - V) * dt + sigma * np.sqrt(V * dt) * np.random.normal()

 return np.maximum(S_t - K, 0)
 ```

5. **Модели EGARCH**:
 - Модель экспоненциального GARCH (EGARCH) учитывает асимметричные эффекты положительных и отрицательных шоков на волатильность, часто лучше захватывая эффекты левериджа, чем симметричные модели.

 ```python
 from arch import arch_model

 def egarch_model(returns):
 model = arch_model(returns, vol='EGARCH', p=1, o=1, q=1)
 model_fitted = model.fit(disp='off')
 return model_fitted.forecast(horizon=1).variance[-1:]
 ```

6. **Стохастические дифференциальные уравнения (SDE)**:
 - SDE могут моделировать динамику цен активов и волатильностей. Модель Кокса-Ингерсолла-Росса (CIR) является известным примером для процентных ставок, часто адаптированным для волатильности.

 ```python
 import numpy as np

 def cir_model(r0, kappa, theta, sigma, T, dt=0.01):
 n = int(T / dt)
 rates = np.zeros(n)
 rates[0] = r0
 for i in range(1, n):
 r = rates[i-1]
 dr = kappa * (theta - r) * dt + sigma * np.sqrt(r * dt) * np.random.normal()
 rates[i] = r + dr
 return rates
 ```

## Применения моделей волатильности

1. **Управление рисками**:
 - Оценка и прогнозирование волатильности имеют решающее значение для практик управления рисками в финансовых учреждениях. Меры стоимости под риском (VaR) и условного VaR (CVaR) сильно зависят от точных прогнозов волатильности.

 ```python
 def value_at_risk(returns, confidence_level=0.95):
 return np.percentile(returns, 100 * (1 - confidence_level))
 ```

2. **Ценообразование опционов**:
 - Волатильность является ключевым входом в ценообразовании опционов. Такие модели, как Блэк-Шоулз, полагаются либо на историческую, либо на подразумеваемую волатильность для определения теоретических цен опционов.

 ```python
 def black_scholes_option(S, K, T, r, sigma, option_type='call'):
 d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
 d2 = d1 - sigma * np.sqrt(T)
 if option_type == 'call':
 option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
 elif option_type == 'put':
 option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
 return option_price
 ```

3. **Управление портфелем**:
 - Модели волатильности информируют распределение портфеля, количественно определяя риск, связанный с различными активами. Оптимизация среднего-дисперсии, например, использует историческую волатильность.

 ```python
 import numpy as np
 from scipy.optimize import minimize

 def portfolio_volatility(weights, cov_matrix):
 return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

 def minimize_volatility(cov_matrix):
 n_assets = cov_matrix.shape[0]
 initial_weights = np.ones(n_assets) / n_assets
 bounds = [(0, 1) for _ in range(n_assets)]
 constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
 result = minimize(portfolio_volatility, initial_weights, args=(cov_matrix,), bounds=bounds, constraints=constraints)
 return result.x
 ```

4. **Алгоритмическая торговля**:
 - Многие стратегии алгоритмической торговли включают прогнозы волатильности для корректировки размеров позиций, левериджа и времени сделок. Прогнозные модели, такие как GARCH, могут сигнализировать о точках входа и выхода.

 ```python
 def trading_signal(hist_vol, threshold):
 if hist_vol > threshold:
 return 'Sell'
 else:
 return 'Buy'
 ```

## Ключевые компании и ресурсы

- **Quantitative Brokers**:
 Они предоставляют передовые алгоритмы и решения для количественной торговли, часто используя сложные модели волатильности.

- **AQR Capital Management**:
 Ведущая глобальная инвестиционная управляющая компания, известная своим количественным подходом к инвестированию, использующая модели волатильности для различных инвестиционных стратегий.

- **WorldQuant**:
 Еще один крупный игрок в количественных финансах, фокусирующийся на исследовании и внедрении количественных моделей в торговле.

- **Институт волатильности при NYU Stern**:
 Предлагает ценные академические и практические идеи в моделировании волатильности, публикуя регулярные обновления и исследовательские статьи.

В целом, модели количественной волатильности составляют основу современной финансовой инженерии, обеспечивая практические идеи и улучшая принятие решений в управлении рисками, ценообразовании опционов, управлении портфелем и алгоритмической торговле.
