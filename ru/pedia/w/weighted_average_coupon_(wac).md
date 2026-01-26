# Средневзвешенный купон

[Перевод с английского языка]

The Weighted Average Coupon (WAC) is a financial metric used primarily in the mortgage-backed securities (MBS) industry. It represents the average interest rate of a pool of loans, mortgages, or other assets, weighted by the balance of each loan at a given point in time. Understanding the WAC is essential for investors and analysts to assess the yield, risk, and performance characteristics of a specific MBS.

Note: LIBOR publication ended for most tenors after 2023, and markets shifted to risk-free reference rates such as SOFR (USD), SONIA (GBP), and ESTR (EUR).

To elucidate the concept more thoroughly, we'll explore various facets of WAC, including its calculation, significance in the financial industry, relationship with other securities, and real-world applications in portfolio management.

## Calculation of WAC

The WAC is calculated by summing the products of the coupon rates and their corresponding weights (which are typically the principal balances of the individual loans) and then dividing the result by the total principal balance. The formula for WAC is represented as follows:

```markdown
\[ \text{WAC} = \frac{\sum (R_i \times P_i)}{\sum P_i} \]

where,
R_i = Coupon rate of the individual loan
P_i = Principal balance of the individual loan
```

To put this formula into perspective, let's consider a simple example:

1. Loan 1: $100,000 at 4.5% coupon rate (R1)
2. Loan 2: $150,000 at 5.0% coupon rate (R2)
3. Loan 3: $250,000 at 4.8% coupon rate (R3)

The WAC would be calculated as follows:

```markdown
\[ \text{WAC} = \frac{(100,000 \times 0.045) + (150,000 \times 0.05) + (250,000 \times 0.048)}{100,000 + 150,000 + 250,000} \]

\[ \text{WAC} = \frac{4,500 + 7,500 + 12,000}{500,000} \]

\[ \text{WAC} = \frac{24,000}{500,000} \]
\[ \text{WAC} = 0.048 \text{ or } 4.8\% \]
```

In this example, the WAC of the pool of loans would be 4.8%.

## Importance of WAC in Mortgage-Backed Securities (MBS)

The concept of WAC is particularly significant in the context of MBS for several reasons:

### Yield Analysis

The WAC offers investors a way to determine the potential yield of a mortgage-backed security. Higher WAC values generally indicate higher interest payments, which can lead to higher returns for investors. Conversely, lower WAC values may suggest lower yields.

### Risk Assessment

WAC can serve as an indicator of the credit and interest rate risk associated with a pool of mortgages. For instance, a higher WAC might suggest that the loans in the pool carry higher interest rates due to borrowers' higher risk profiles. Understanding this aspect helps investors make more informed decisions regarding the risk they are assuming.

### Prepayment Dynamics

Prepayments can significantly affect the WAC over time. Prepayments occur when borrowers pay off their mortgages early, which typically happens when interest rates decline, prompting refinancing. As high-interest loans are paid off faster, the WAC of the remaining loans may decrease. Monitoring the WAC helps in predicting and managing the impact of prepayment on the overall return of the MBS.

## Relationship with Other Metrics

### Weighted Average Maturity (WAM)

WAM is another critical metric that often goes hand-in-hand with WAC. While WAC focuses on the average interest rate, WAM looks at the average time until the loans in the pool mature, weighted by their principal balance. Both metrics together can provide a more comprehensive picture of the MBS in terms of its expected returns and risks.

### Weighted Average Loan Age (WALA)

WALA measures the average age of the loans in the pool, weighted by their balances. This gives insight into how seasoned the loans are, which can further impact the prepayment rates and, consequently, the WAC.

### Spread Analysis

Analysts compare the WAC with other interest rate benchmarks, such as the yield on U.S. Treasury securities or LIBOR. This spread analysis helps in understanding the relative risk premium associated with the MBS.

## Applications in Portfolio Management

WAC plays a critical role in portfolio management, especially for institutions that invest heavily in mortgage-backed securities. Here are some specific applications:

### Diversification Strategy

Portfolio managers use WAC to diversify their holdings across different types of mortgage-backed securities. By balancing securities with different WACs, they can achieve a more consistent return while managing risk.

### Performance Monitoring

Regular monitoring of the WAC helps in assessing the performance of the mortgage portfolio. Changes in the WAC over time can indicate shifts in the interest rate environment or borrower behavior, prompting necessary adjustments to the portfolio.

### Hedging Strategies

Understanding the WAC is vital for developing effective hedging strategies. For instance, if the WAC is expected to decline due to increasing prepayments, managers might hedge against interest rate changes to protect the portfolio's value.

## Real-World Examples

### Agency Mortgage-Backed Securities

Agency MBS are issued by government-sponsored enterprises (GSEs) like Fannie Mae, Freddie Mac, or Ginnie Mae. The WAC for these securities is generally lower due to the high credit quality of the underlying mortgages. Investors rely on the WAC to gauge the expected return and risk of these relatively low-risk securities.

### Non-Agency Mortgage-Backed Securities

Non-agency MBS do not have the backing of GSEs and therefore carry higher credit risk. The WAC of non-agency MBS is typically higher to compensate for this increased risk. Investors need to scrutinize the WAC alongside other credit metrics to make well-informed investment decisions.

## Technological Integration in WAC Analysis

With advancements in financial technology, the analysis and monitoring of WAC have become more sophisticated. Financial institutions leverage big data and machine learning algorithms to predict changes in WAC more accurately, adapting their strategies in near real-time.

### Fintech Platforms

Fintech platforms have emerged that offer comprehensive analytics for mortgage-backed securities, including detailed WAC calculations and projections. Services like Yieldbook and Intex Solutions provide a plethora of tools for investors to assess the WAC and other vital metrics of their MBS portfolios.

For more information on such platforms, you can visit:

- Yieldbook
- Intex Solutions

### Algorithmic Trading

Algorithmic trading systems use complex algorithms to trade MBS based on the WAC and other financial indicators. These systems can execute trades at high speeds and volumes, ensuring optimal investment returns. The growing reliance on algorithmic trading has necessitated precise and timely WAC calculations, which are now an integral part of many trading algorithms.

### Cloud Computing

Cloud-based solutions enable the processing of vast amounts of financial data, making it easier to compute and analyze WAC across diverse mortgage pools. Cloud platforms like AWS and Google Cloud offer robust analytics services that can be tailored to continuous monitoring and updating of WAC, facilitating real-time portfolio management.

## Conclusion

The Weighted Average Coupon (WAC) is a fundamental metric in the mortgage-backed securities industry, providing crucial insights into the average interest rate of a pool of loans. It helps investors assess the yield, risk, and potential performance of MBS investments. By understanding the calculation, significance, and applications of WAC, investors can make more informed decisions, thereby optimizing their portfolios and managing risks effectively. The integration of advanced technologies further enhances the accuracy and applicability of WAC, making it an indispensable tool in modern financial analysis and portfolio management.