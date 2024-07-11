# Net-Net

## Introduction

In the realm of finance and investment, the term "Net-Net" refers to a specific strategy popularized by Benjamin Graham, known as the "father of value investing." This investment strategy focuses on identifying companies that are trading at a significant discount to their net current asset value (NCAV). The concept originates from Graham's principles in his seminal work, "The Intelligent Investor," where he outlined his methodology for finding deeply undervalued stocks. The Net-Net strategy is a classic form of value investing and is often associated with finding "cigar butt" stocks—companies that are financially distressed but have residual value.

## Definition

The term "Net-Net" represents a calculation to determine the intrinsic value of a company based on its balance sheet, particularly its current assets and liabilities. The formula for calculating the NCAV is:

```
NCAV = Current Assets - Total Liabilities
```

In other words, the Net-Net value of a firm is the net current assets, which is the difference between the firm's current assets (cash, receivables, inventory) and its total liabilities (both current and non-current). A company is considered a Net-Net if its market capitalization is less than its NCAV, implying it is trading at a substantial discount to its liquidation value.

## Criteria for Net-Net Stocks

To qualify as a Net-Net stock, several criteria are generally evaluated:

1. **Current Ratio**: The company should have a high current ratio (current assets divided by current liabilities), typically greater than 2. This indicates that the company has sufficient liquidity to cover its short-term obligations.

2. **Low Price-to-NCAV**: The stock's price should be lower than its NCAV per share. Typically, a stock trading at 66% or less of its NCAV is considered a Net-Net.

3. **Market Cap**: The market capitalization of the company should be small, as larger companies rarely trade at such distressed levels.

4. **Financial Health**: While many Net-Net stocks are distressed, some level of financial health is desired. This could include positive earnings, low debt levels, or a history of profitability.

5. **Industry Considerations**: Companies in industries prone to cyclic downturns or structural declines might frequently appear as Net-Nets, so sector-specific risks need to be evaluated.

## How to Identify Net-Net Stocks

### Screening Tools

Investors can use various screening tools to identify potential Net-Net stocks. Some popular financial data providers include:

- **Yahoo Finance**: Allows users to screen for stocks based on various financial criteria, including current assets and liabilities.
- **Finviz**: A stock screener that offers filters for financial ratios and balance sheet data.
- **GuruFocus**: Provides comprehensive data on value investing metrics, including NCAV calculations.

### Manual Analysis

**Step-by-Step Process**:

1. **Collect Financial Statements**: Obtain the company's latest financial reports, including the balance sheet, income statement, and cash flow statement.
  
2. **Calculate Current Assets**: Sum the company's cash, cash equivalents, accounts receivable, and inventory.

3. **Calculate Total Liabilities**: Sum both current and long-term liabilities from the balance sheet.

4. **Determine NCAV**: Subtract total liabilities from current assets to obtain the NCAV.

5. **Compare to Market Cap**: Divide the NCAV by the number of outstanding shares to get the NCAV per share. Compare this to the current stock price.

## Risks and Considerations

Although Net-Net stocks can offer significant upside potential, they come with a variety of risks:

1. **Financial Distress**: Many Net-Net stocks are in poor financial health and may face bankruptcy or severe operational challenges.
  
2. **Liquidity Issues**: Small-cap stocks often have lower liquidity, making it difficult to buy or sell large positions without affecting the stock price.

3. **Limited Information**: Smaller and distressed companies may provide less transparency and have less analyst coverage, making it harder to assess their true financial condition.

4. **Market Timing**: Timing the market entry and exit is crucial. Holding a Net-Net stock too long could result in value erosion if the company continues to deteriorate.

## Case Studies

### Case Study 1: Company X

**Background**: Company X is a small-cap manufacturer facing operational issues and declining sales. The stock price has plummeted over the past year.

**Financials**:
- Current Assets: $150 million
- Total Liabilities: $100 million
- Outstanding Shares: 10 million
- Current Stock Price: $4

**NCAV Calculation**:
```
NCAV = $150 million - $100 million = $50 million
NCAV per share = $50 million / 10 million shares = $5
```

Since Company X's stock price ($4) is below its NCAV per share ($5), it qualifies as a Net-Net stock.

### Case Study 2: Company Y

**Background**: Company Y operates in the retail sector, which has been hit hard by economic downturns. The company's revenue has been stable, but margins have contracted.

**Financials**:
- Current Assets: $80 million
- Total Liabilities: $60 million
- Outstanding Shares: 5 million
- Current Stock Price: $8

**NCAV Calculation**:
```
NCAV = $80 million - $60 million = $20 million
NCAV per share = $20 million / 5 million shares = $4
```

Since Company Y's stock price ($8) is above its NCAV per share ($4), it does not qualify as a Net-Net stock.

## Modern Applications

While traditional Net-Net investing focused on manual analysis of financial statements, modern algorithms and fintech solutions have streamlined the process. Platforms like QuantConnect and Alpaca allow investors to build and backtest algorithmic trading strategies, including those based on Net-Net criteria.

### Algorithmic Trading

**Steps to Implement a Net-Net Algorithm**:

1. **Data Collection**: Use APIs to gather financial statement data.
2. **Screening**: Implement the NCAV calculation and other criteria within your algorithm.
3. **Backtesting**: Test the effectiveness of your strategy using historical data.
4. **Execution**: Deploy the algorithm in a live trading environment.

**Example**:

```python
# Pseudo-code for a Net-Net trading strategy
def net_net_strategy(stock_list):
    selected_stocks = []
    for stock in stock_list:
        financials = get_financials(stock)
        ncav = financials['current_assets'] - financials['total_liabilities']
        ncav_per_share = ncav / financials['outstanding_shares']
        if financials['stock_price'] < ncav_per_share * 0.66:
            selected_stocks.append(stock)
    return selected_stocks
```

## Conclusion

The Net-Net investment strategy remains a cornerstone of value investing, offering significant upside by uncovering deeply undervalued stocks. While it does come with inherent risks, modern tools and algorithmic trading platforms have made the strategy more accessible and efficient. Whether through manual analysis or automated algorithms, the core principles of Net-Net investing continue to provide valuable insights for discerning investors.

For more information about algorithmic trading platforms, you can visit:
- [QuantConnect](https://www.quantconnect.com/)
- [Alpaca](https://alpaca.markets/)