# Money Flow Index (MFI)

The [Money Flow](../m/money_flow.md) [Index](../i/index.md) (MFI) is a [momentum](../m/momentum.md) [indicator](../i/indicator.md) that uses both price and [volume](../v/volume.md) data to identify [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions in an [asset](../a/asset.md). It is similar to the [Relative Strength](../r/relative_strength.md) [Index](../i/index.md) (RSI) but includes [volume](../v/volume.md), whereas the RSI considers only price. The MFI is a useful tool for traders and investors to gauge [market sentiment](../m/market_sentiment.md) and potential [reversal](../r/reversal.md) points in the [market](../m/market.md).

### Calculation of MFI

The MFI is calculated through a multi-step process that involves the use of typical price, [money flow](../m/money_flow.md), and [money flow](../m/money_flow.md) ratio:

1. **Typical Price (TP):**
   \[
   TP = \frac{\text{High} + \text{Low} + \text{Close}}{3}
   \]

2. **Raw [Money Flow](../m/money_flow.md) (RMF):**
   \[
   RMF = TP \times \text{[Volume](../v/volume.md)}
   \]

3. **Positive and Negative [Money Flow](../m/money_flow.md):**
   - If today's Typical Price is greater than yesterday's Typical Price, it is considered a positive [money flow](../m/money_flow.md).
   - If today's Typical Price is less than yesterday's Typical Price, it is considered a negative [money flow](../m/money_flow.md).

4. **[Money Flow](../m/money_flow.md) Ratio (MFR):**
   \[
   MFR = \frac{\text{Positive [Money Flow](../m/money_flow.md) (over 14 periods)}}{\text{Negative [Money Flow](../m/money_flow.md) (over 14 periods)}}
   \]

5. **[Money Flow](../m/money_flow.md) [Index](../i/index.md) (MFI):**
   \[
   MFI = 100 - \frac{100}{1 + MFR}
   \]

### Interpretation of MFI

The MFI is typically calculated over a 14-day period and ranges between 0 and 100. Here are the primary interpretations of MFI values:

- **[Overbought](../o/overbought.md) Condition:** MFI above 80.
- **[Oversold](../o/oversold.md) Condition:** MFI below 20.
- **[Trend](../t/trend.md) Strength and Reversals:** Divergences between the MFI and the price can indicate potential and significant [market](../m/market.md) reversals. For instance, a price that is making a new high while the MFI is making a lower high can signal an impending downturn.

### Applications and Examples

#### Overbought and Oversold Conditions
When the MFI crosses below 20, it indicates that the [security](../s/security.md) is potentially [oversold](../o/oversold.md) and could be a buying opportunity. Conversely, when the MFI exceeds 80, the [security](../s/security.md) could be [overbought](../o/overbought.md) and present a selling opportunity. This concept can be especially useful for swing traders.

#### Divergences
Detected divergences between the MFI and the price can serve as a signal for traders. For instance, if a stock price is reaching higher highs but the MFI is not, this [bearish divergence](../b/bearish_divergence.md) might suggest that the upward [momentum](../m/momentum.md) could be weakening. 

### Example Calculation

Assume the following data points (for simplicity):

- High: $50, Low: $42, Close: $46, [Volume](../v/volume.md): 200,000
- High: $48, Low: $41, Close: $44, [Volume](../v/volume.md): 220,000

#### Step-by-Step Calculation:

1. **Typical Price (TP):**
   \[
   TP_1 = \frac{50 + 42 + 46}{3} = 46
   \]
   \[
   TP_2 = \frac{48 + 41 + 44}{3} = 44.33
   \]

2. **Raw [Money Flow](../m/money_flow.md) (RMF):**
   \[
   RMF_1 = 46 \times 200000 = 9200000
   \]
   \[
   RMF_2 = 44.33 \times 220000 = 9752600
   \]

3. **Positive and Negative [Money Flow](../m/money_flow.md):**
   - For TP_2 (44.33 < 46), RMF is negative
   - For TP_1 (no previous day to compare yet)

   Let's assume you have 14 periods and sum positive and negative [money](../m/money.md) flows accordingly.

4. **[Money Flow](../m/money_flow.md) Ratio (MFR):**
   Suppose,
   \[
   \text{Sum of Positive [Money Flow](../m/money_flow.md)} = 50000000
   \]
   \[
   \text{Sum of Negative [Money Flow](../m/money_flow.md)} = 30000000
   \]
   \[
   MFR = \frac{50000000}{30000000} = 1.67
   \]

5. **[Money Flow](../m/money_flow.md) [Index](../i/index.md) (MFI):**
   \[
   MFI = 100 - \frac{100}{1 + 1.67} \approx 62.5
   \]

   With an MFI of 62.5, the [security](../s/security.md) isn’t in [overbought](../o/overbought.md) or [oversold](../o/oversold.md) territory.

### Practical Use Cases

#### Stock Trading
Traders can use the MFI to determine entry and exit points. For instance, high MFI readings might prompt [profit](../p/profit.md)-taking, while low readings may suggest buying opportunities.

#### Comparing Different Securities
Using the MFI, traders can compare [multiple](../m/multiple.md) securities to identify [relative strength](../r/relative_strength.md) among them. For example, if two [stocks](../s/stock.md) are in the same [industry](../i/industry.md) but have vastly different MFI readings, one might be a better buy or sell candidate based on its [market](../m/market.md) [momentum](../m/momentum.md).

### MFI in Algorithmic Trading

In [algorithmic trading](../a/algorithmic_trading.md), the MFI can be incorporated into [trading algorithms](../t/trading_algorithms.md) to automate buy or sell decisions based on predefined threshold levels. Here are some simplified protocol steps:

- **Data Input:** Fetch daily high, low, close, and [volume](../v/volume.md) data for the target [security](../s/security.md).
- **MFI Calculation:** Implement the MFI calculation formula within the trading system.
- **Trigger Conditions:** Set conditions for triggering trades, such as:
  ```python
  if MFI < 20:
      Buy()
  elif MFI > 80:
      Sell()
  ```
- **[Backtesting](../b/backtesting.md):** Test the strategy using historical data to validate its effectiveness.

### Popular Platforms and Tools

Several trading platforms and tools [offer](../o/offer.md) built-in MFI indicators, such as:

- **MetaTrader 4 & 5:** Popular choices among forex traders that [offer](../o/offer.md) MFI as a [default](../d/default.md) [indicator](../i/indicator.md).
- **[TradingView](../t/tradingview.md):** An online [trading platform](../t/trading_platform.md) known for its user-friendly interface and integrated MFI [indicator](../i/indicator.md).
- **[Thinkorswim](../t/thinkorswim.md) by TD [Ameritrade](../a/ameritrade.md):** A powerful [trading platform](../t/trading_platform.md) that includes MFI indicators.
- **Python Libraries:** Libraries like `ta-lib` can be used for calculating MFI within custom [trading algorithms](../t/trading_algorithms.md).

### References and Resources

- [TD Ameritrade Thinkorswim Platform](https://www.tdameritrade.com/tools-and-platforms/thinkorswim.page)
- [TradingView Platform](https://www.tradingview.com/)
- [MetaTrader Platform](https://www.metatrader4.com/en)

### Conclusion

The [Money Flow](../m/money_flow.md) [Index](../i/index.md) (MFI) is a compelling tool that blends price and [volume](../v/volume.md) to give traders insights into the strength of [market](../m/market.md) movements. Its application in identifying [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions, along with potential divergences, makes it a valuable addition to any [trader](../t/trader.md)’s toolkit. Be it for manual or [algorithmic trading](../a/algorithmic_trading.md), understanding and utilizing the MFI can help in making more informed and potentially profitable trading decisions.
