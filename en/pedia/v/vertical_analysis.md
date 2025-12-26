# Vertical Analysis

Vertical analysis, sometimes referred to as common-size [financial statement analysis](../f/financial_statement_analysis.md), is an important [financial statement analysis](../f/financial_statement_analysis.md) tool used to evaluate the proportional size of different financial statement line items within a single [accounting](../a/accounting.md) period. This relative size analysis is crucial in algorithms and [automated trading systems](../a/automated_trading_systems.md) for making informed decisions based on the [financial health](../f/financial_health.md) and performance of a company. For algo trading, vertical analysis is employed to scale financial data to a common size, enabling the comparison of [financial statements](../f/financial_statements.md) across various periods or between companies of different sizes.

## Understanding Vertical Analysis

In vertical analysis, each item on a financial statement is [listed](../l/listed.md) as a percentage of another item. For instance, in an [income statement](../i/income_statement.md), [revenue](../r/revenue.md) is typically used as the base item, and each line item is expressed as a percentage of total [revenue](../r/revenue.md). On a [balance sheet](../b/balance_sheet.md), total assets are often used as the base, and each line item is expressed as a percentage of total assets.

The aim is to remove the effect of size and scale, making it easier to compare and analyze performance across different periods or companies. By highlighting changes in relative proportions, vertical analysis can pinpoint trends and flag potential issues that absolute values may not reveal.

## Application in Algo Trading

Algo trading involves the use of algorithms and automated systems to execute trades based on predefined criteria and strategies. Vertical analysis can be integrated into these algorithms to provide insights on:

1. **Profitability**: By analyzing the percentage of [revenue](../r/revenue.md) invested in COGS (Cost of Goods Sold), operating expenses, and net [income](../i/income.md), algorithms can gauge the profitability of a company.
2. **[Efficiency](../e/efficiency.md)**: Assessing the costs relative to [revenue](../r/revenue.md) can highlight how effectively a company is managing its resources.
3. **[Solvency](../s/solvency.md) and [Liquidity](../l/liquidity.md)**: In the [balance sheet](../b/balance_sheet.md), vertical analysis can reveal the proportion of [current assets](../c/current_assets.md) to total assets to understand [liquidity](../l/liquidity.md), or the proportion of [debt](../d/debt.md) to total assets to evaluate [financial risk](../f/financial_risk.md).
4. **[Trend Analysis](../t/trend_analysis.md)**: By comparing vertical analysis percentages over [multiple](../m/multiple.md) periods, algorithms can identify trends and patterns that are crucial for long-term decision making.

### Example Implementation in an Algorithm

A basic structure of an algorithm that uses vertical analysis might include steps such as:

1. **Data Collection**: Fetching [financial statements](../f/financial_statements.md) data from reliable sources.
2. **Normalization**: Performing vertical analysis to convert absolute figures into percentages.
3. **Analysis**: Running predefined rules or models to evaluate the health of the company based on these percentages.
4. **[Execution](../e/execution.md)**: Making trading decisions (buy/sell/[hold](../h/hold.md)) based on the analysis outcomes.

Here’s a simplified pseudocode example:

```python
def vertical_analysis(financial_statements):
    # Extract [revenue](../r/revenue.md) from [income](../i/income.md) statements
    [revenue](../r/revenue.md) = financial_statements['income_statement']['[revenue](../r/revenue.md)']
    cogs = financial_statements['income_statement']['cogs']
    operating_expenses = financial_statements['income_statement']['operating_expenses']
    net_income = financial_statements['income_statement']['net_income']
    
    # Perform vertical analysis
    vertical_income_statement = {
        'cogs': cogs / [revenue](../r/revenue.md),
        'operating_expenses': operating_expenses / [revenue](../r/revenue.md),
        'net_income': net_income / [revenue](../r/revenue.md)
    }
    
    # Extract total assets from [balance sheet](../b/balance_sheet.md)
    total_assets = financial_statements['balance_sheet']['total_assets']
    current_assets = financial_statements['balance_sheet']['current_assets']
    total_liabilities = financial_statements['balance_sheet']['total_liabilities']
    
    # Perform vertical analysis
    vertical_balance_sheet = {
        'current_assets': current_assets / total_assets,
        'total_liabilities': total_liabilities / total_assets,
    }
    
    # Analyze the vertical analysis results
    if vertical_income_statement['net_income'] > 0.10 and vertical_balance_sheet['total_liabilities'] < 0.50:
        [return](../r/return.md) "BUY"
    elif vertical_income_statement['net_income'] < 0.05 or vertical_balance_sheet['total_liabilities'] > 0.70:
        [return](../r/return.md) "SELL"
    else:
        [return](../r/return.md) "[HOLD](../h/hold.md)"

# Simulated financial data
financial_statements = {
    'income_statement': {'[revenue](../r/revenue.md)': 500000, 'cogs': 300000, 'operating_expenses': 100000, 'net_income': 50000},
    'balance_sheet': {'total_assets': 1000000, 'current_assets': 400000, 'total_liabilities': 600000}
}

decision = vertical_analysis(financial_statements)
print(decision)
```

### Benefits of Vertical Analysis in Algo Trading

1. **Simplified Comparison**: With everything scaled to a common size, it is easier to compare line items across different companies irrespective of their sizes.
2. **Enhanced Detection**: Vertical analysis can help in detecting trends and anomalies that may not be visible in raw numbers.
3. **Informed Decision Making**: Provides a clearer picture of a company’s [financial health](../f/financial_health.md) which can feed into better [trading strategies](../t/trading_strategies.md).
4. **[Efficiency](../e/efficiency.md)**: Automated vertical analysis can quickly process large volumes of financial data, making algo trading more efficient.

### Real-life Application and Performance

Algo trading firms and platforms frequently incorporate vertical analysis into their algorithms. One example is Two Sigma, an [investment management](../i/investment_management.md) [firm](../f/firm.md) that heavily relies on [data science](../d/data_science_in_trading.md) and technology for their [trading strategies](../t/trading_strategies.md). By integrating vertical analysis into their algorithms, they can better understand the [financial statements](../f/financial_statements.md) of potential investments and execute trades based on this relative performance evaluation.

### Conclusion

Vertical analysis is a powerful tool that helps in simplifying the comparison of [financial statements](../f/financial_statements.md). By integrating vertical analysis with [algorithmic trading](../a/algorithmic_trading.md), traders can enhance their strategies to make more informed and effective trading decisions. The ability to see beyond raw numbers and analyze proportions provides a significant edge in the competitive world of algo trading.