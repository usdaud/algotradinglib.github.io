# Multiple Linear Regression

## Overview

Multiple [Linear Regression](../l/linear_regression.md) (MLR) is a statistical technique that utilizes several explanatory variables to predict the outcome of a response variable. This method extends simple [linear regression](../l/linear_regression.md), which uses only one explanatory variable. The goal of MLR is to model the linear relationship between the independent variables and the dependent variable by fitting a linear equation to the observed data.

## The Regression Equation

The general form of the multiple [linear regression](../l/linear_regression.md) equation is:

\[ Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_n X_n + \epsilon \]

Where:
- \( Y \) is the dependent variable.
- \( \beta_0 \) is the intercept.
- \( \beta_1, \beta_2, \dots, \beta_n \) are the coefficients for each independent variable \( X_1, X_2, \dots, X_n \).
- \( X_1, X_2, \dots, X_n \) are the independent variables.
- \( \epsilon \) is the error term.

## Assumptions of Multiple Linear Regression

1. **Linearity**: There is a linear relationship between the dependent and independent variables.
2. **Independence**: Observations are independent of each other.
3. **Homoscedasticity**: The residuals (error terms) have constant variance at every level of \( X \).
4. **No multicollinearity**: Independent variables are not highly correlated with each other.
5. **Normality**: The residuals of the model are normally distributed.

## Fitting the Model

To fit a multiple [linear regression](../l/linear_regression.md) model, the ordinary least squares (OLS) method is used. OLS minimizes the sum of the squared residuals, providing the best-fitting line that predicts \( Y \) from \( X_1, X_2, \dots, X_n \).

## Model Evaluation

- **R-squared (\( R^2 \))**: Measures the proportion of variance in the dependent variable that is predictable from the independent variables. Values range from 0 to 1, with higher values indicating better model fit.
- **Adjusted R-squared**: A modified version of \( R^2 \) that adjusts for the number of independent variables in the model.
- **F-statistic**: Tests the overall significance of the model.
- **p-values for coefficients**: Test the significance of individual regression coefficients.

## Applications in Algo Trading

### Predictive Modelling

In [algorithmic trading](../a/algorithmic_trading.md), multiple [linear regression](../l/linear_regression.md) can be used to predict future stock prices, returns, or other financial metrics based on multiple predictors such as historical prices, trading volume, [economic indicators](../e/economic_indicators.md), or other relevant factors. By specifying a model with multiple predictors, traders can capture more complex patterns and relationships within the data.

### Example Companies Using MLR in Trading

1. **Two Sigma**: Employs advanced statistical models, including MLR, to predict market trends and inform trading decisions.
   - [Two Sigma Website](https://www.twosigma.com)

2. **QuantConnect**: Provides a platform for [algorithmic trading](../a/algorithmic_trading.md) where users can develop [trading strategies](../t/trading_strategies.md) using multiple [linear regression](../l/linear_regression.md) and other advanced statistical models.
   - [QuantConnect Website](https://www.quantconnect.com)

### Implementation Using Python and R

#### Python

```python
import pandas as pd
import statsmodels.api as sm

# Load data
data = pd.read_csv('data.csv')

# Define independent variables and dependent variable
X = data[['X1', 'X2', 'X3']]
Y = data['Y']

# Add constant to the model
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(Y, X).fit()

# Display the model summary
print(model.summary())
```

#### R

```r
# Load data
data <- read.csv('data.csv')

# Fit the model
model <- lm(Y ~ X1 + X2 + X3, data=data)

# Display the model summary
summary(model)
```

## Limitations and Considerations

1. **Overfitting**: Including too many variables can lead to overfitting, where the model captures noise instead of the actual pattern. Use techniques like cross-validation to mitigate this risk.
2. **Multicollinearity**: High correlation among independent variables can distort estimates and lead to erroneous conclusions. Variance inflation factor (VIF) is commonly used to detect multicollinearity.
3. **Assumption Violations**: Ensure that the key assumptions of MLR are met. Violations can lead to biased or inefficient estimates.

## Conclusion

Multiple [Linear Regression](../l/linear_regression.md) is a powerful and widely-used tool in both statistical analysis and [algorithmic trading](../a/algorithmic_trading.md). It allows traders to model and predict financial metrics based on multiple relevant factors, making it an essential technique in the quant's toolkit. However, careful consideration must be given to the model's assumptions, potential limitations, and the risk of overfitting to ensure robust and reliable results.
