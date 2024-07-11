# Fama and French Three Factor Model

The Fama and French Three Factor Model is an influential theory in the field of financial economics, specifically in the realm of asset pricing. Developed by Eugene Fama and Kenneth French in the early 1990s, the model extends the Capital Asset Pricing Model (CAPM) by adding two additional factors to better explain the variations in stock returns. These factors are Size (SMB, Small Minus Big) and Value (HML, High Minus Low). The Fama and French model has since become a cornerstone in both academic research and practical financial management.

## Background

### Capital Asset Pricing Model (CAPM)

Before delving into the specifics of the Fama and French Three Factor Model, it's important to briefly touch on its predecessor, the Capital Asset Pricing Model (CAPM). Developed in the early 1960s by William Sharpe, John Lintner, and Jan Mossin, the CAPM is a single-factor model that describes the relationship between systematic risk and expected return for assets. The formula for the CAPM is:

\[ E(R_i) = R_f + \beta_i (E(R_m) - R_f) \]

- \( E(R_i) \): Expected return of the investment
- \( R_f \): Risk-free rate
- \( \beta_i \): Beta coefficient of the investment
- \( E(R_m) \): Expected return of the market

While the CAPM has been widely used, it has its limitations. Empirical evidence showed that it could not fully explain stock returns due to the exclusion of other significant factors influencing asset prices.

### Introduction to the Fama and French Three Factor Model

Eugene Fama and Kenneth French introduced their model in a seminal 1992 paper titled "The Cross-Section of Expected Stock Returns." The primary departure from CAPM is the inclusion of two additional factors—Size (SMB) and Value (HML)—alongside the market risk factor (the excess return on the market, or \( R_m - R_f \)). Their extended model is expressed as:

\[ E(R_i) = R_f + \beta_i (E(R_m) - R_f) + \text{SMB}_i \times \text{SMB} + \text{HML}_i \times \text{HML} \]

- \( \text{SMB} \): Small Minus Big, a factor representing the outperformance of small-cap stocks over large-cap stocks
- \( HML \): High Minus Low, a factor representing the outperformance of value stocks (high book-to-market ratio) over growth stocks (low book-to-market ratio)

## Components of the Model

### Market Risk Premium (MRP)

The Market Risk Premium (MRP) reflects the difference between the expected return of the market and the risk-free rate. It accounts for the general market risk that stocks are exposed to. In the Fama and French Three Factor Model, this is represented by:

\[ \beta_i (E(R_m) - R_f) \]

The market risk component remains consistent with the CAPM, emphasizing that this factor alone is not sufficient to explain the complexities of asset returns fully.

### Size (SMB - Small Minus Big)

The Size factor captures the additional risk and return characteristics associated with small-capitalization stocks. Empirical evidence indicates that small-cap stocks tend to outperform large-cap stocks over the long term. This difference is attributed to various factors, such as higher growth potential and greater financial risk faced by smaller firms. The SMB factor is calculated as follows:

\[ \text{SMB} = \frac{1}{3} (R_{small, value} + R_{small, neutral} + R_{small, growth} - R_{big, value} - R_{big, neutral} - R_{big, growth}) \]

Where:
- \( R_{small, value} \): Return on small-cap value stocks
- \( R_{small, neutral} \): Return on small-cap neutral stocks
- \( R_{small, growth} \): Return on small-cap growth stocks
- \( R_{big, value} \): Return on large-cap value stocks
- \( R_{big, neutral} \): Return on large-cap neutral stocks
- \( R_{big, growth} \): Return on large-cap growth stocks

### Value (HML - High Minus Low)

The Value factor represents the difference in returns between value stocks and growth stocks. Value stocks are characterized by high book-to-market ratios, meaning they have a relatively low market valuation compared to their book value. Conversely, growth stocks have low book-to-market ratios and are generally considered to have higher future growth potential. The HML factor is computed as follows:

\[ \text{HML} = \frac{1}{2} (R_{small, value} + R_{big, value} - R_{small, growth} - R_{big, growth}) \]

Where:
- \( R_{small, value} \): Return on small-cap value stocks
- \( R_{big, value} \): Return on large-cap value stocks
- \( R_{small, growth} \): Return on small-cap growth stocks
- \( R_{big, growth} \): Return on large-cap growth stocks

## Empirical Validation

### Initial Evidence

Fama and French initially validated their model using data from the New York Stock Exchange (NYSE), American Stock Exchange (AMEX), and NASDAQ for the period from 1963 to 1990. They found that their three-factor model significantly improved the explanation of stock returns compared to CAPM. The model's inclusion of the SMB and HML factors addressed the anomalies evident with a single-factor CAPM, such as the higher average returns of small-cap stocks and value stocks.

### Broad Acceptance

Over the years, numerous studies have corroborated the efficacy of the Fama and French Three Factor Model across different periods and diverse markets. Some of the most significant supporting evidence comes from:

- **International Markets**: The model has been validated in international equity markets, proving its applicability beyond the U.S. equities.
- **Different Time Periods**: Research covering various time periods continues to support the findings that small-cap and value stocks tend to outperform their large-cap and growth counterparts.

### Criticisms and Limitations

Despite its broad acceptance, the Fama and French Three Factor Model is not without its criticisms. Some of the key limitations include:

- **Model Complexity**: Adding more factors increases the complexity of the model which can make it less intuitive for practitioners.
- **Factor Stability**: There is ongoing debate about whether SMB and HML remain stable over time or are susceptible to changes in market conditions and investor behavior.
- **Other Anomalies**: Even with three factors, the model does not capture all anomalies (such as momentum).

## Real-World Applications

### Investment Management

Many investment firms and fund managers have adopted the Fama and French Three Factor Model to inform their asset allocation, risk management, and performance evaluation practices. The model is particularly popular in the realm of factor investing, where investors construct portfolios based on exposure to various risk factors.

### Hedge Funds

Hedge funds, including quantitative and algorithmic trading firms, often use the three-factor model as a component of more complex models to predict asset prices and identify arbitrage opportunities. By incorporating SMB and HML, these entities refine their strategies to gain an edge in the market.

### Financial Education

The model is a staple in finance curricula at universities around the world. It serves as a bridge between the simpler CAPM and more intricate asset pricing models, providing students with a deeper understanding of the multi-dimensional nature of risk and return.

## Extensions of the Model

### Fama and French Five Factor Model

In 2015, Fama and French expanded their model into a five-factor framework by adding two more factors: profitability and investment. The five-factor model aims to account for even more dimensions of stock returns. The additional factors are:

- **Robust Minus Weak (RMW)**: Represents the returns of stocks with robust profitability minus those with weak profitability.
- **Conservative Minus Aggressive (CMA)**: Represents the returns of stocks with conservative investment policies minus those with aggressive investment policies.

### Other Multi-Factor Models

Numerous other multi-factor models have been developed in the finance literature, taking inspiration from Fama and French to incorporate additional factors like momentum, liquidity, and others. These models aim to offer even more refined explanations for asset returns.

## Conclusion

The Fama and French Three Factor Model has had a profound impact on the field of asset pricing, offering significant improvements over the Capital Asset Pricing Model (CAPM). By introducing the Size (SMB) and Value (HML) factors, Fama and French provided a more comprehensive framework for understanding stock returns. Despite its limitations, the model remains a cornerstone in financial economics and continues to be widely used in both academic research and practical financial management.

For further reading and to explore more about the contributions of Eugene Fama and Kenneth French, you can visit their respective academic and professional profiles:

- [Eugene F. Fama at University of Chicago](https://www.chicagobooth.edu/faculty/directory/f/eugene-f-fama)
- [Kenneth R. French at Dartmouth College](https://faculty.tuck.dartmouth.edu/ken-french/)