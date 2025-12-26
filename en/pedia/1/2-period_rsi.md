# 2-Period RSI

The [Relative Strength](../r/relative_strength.md) [Index](../i/index_instrument.md) (RSI) is a well-known [momentum](../m/momentum.md) [oscillator](../o/oscillator.md) developed by J. Welles Wilder, which measures the speed and change of price movements. The RSI oscillates between zero and 100 and is typically used to identify [overbought](../o/overbought.md) or [oversold](../o/oversold.md) conditions in a [market](../m/market.md). While the typical RSI calculation uses a 14-period lookback, the 2-period RSI is a variation designed for shorter time frames to provide more sensitive and frequent signals. This approach is particularly useful for active traders who engage in short-term trades.

## Understanding RSI

Before diving into the specifics of the 2-period RSI, it's crucial to comprehend the [basis](../b/basis.md) of the traditional RSI. The RSI calculates a ratio of the upward movements to the total absolute size of all price movements within a specific time period:

```
RS = (Average [Gain](../g/gain.md) over N periods) / (Average Loss over N periods)
RSI = 100 - [100 / (1 + RS)]
```

In these formulas, "RS" refers to the [Relative Strength](../r/relative_strength.md), "Average [Gain](../g/gain.md)" is the mean of all gains during the selected period, and "Average Loss" is the mean of all losses during the chosen period.

## 2-Period RSI Calculation

For the 2-period RSI, the calculation adjusts the lookback period to only two periods instead of the conventional 14. This produces faster and more responsive indicators, allowing traders to capture shorter-term price changes more effectively.

Here's how to compute it:

1. **Calculate the Average [Gain](../g/gain.md) and Loss:**
 For each of the last two periods, determine if the price has increased or decreased, and by how much.

2. **Determine RS:**
 Divide the average [gain](../g/gain.md) by the average loss to get the [relative strength](../r/relative_strength.md) (RS).

3. **Plug RS into the RSI formula:**
 Use the RS [value](../v/value.md) in the RSI formula: `RSI = 100 - [100 / (1 + RS)]`.

### Example Calculation

If a [trader](../t/trader.md) is looking at a stock price for the last three days:

- Day 1: Price goes from $50 to $52 ([Gain](../g/gain.md) = $2)
- Day 2: Price goes from $52 to $51 (Loss = $1)
- Day 3: Price goes from $51 to $53 ([Gain](../g/gain.md) = $2)

Average [Gain](../g/gain.md) = (2 + 2) / 2 = 2\
Average Loss = 1 / 2 = 0.5\
RS = 2 / 0.5 = 4\
RSI = 100 - [100 / (1 + 4)] = 100 - 20 = 80

## Trading with 2-Period RSI

### Buy and Sell Signals

The main advantage of a 2-period RSI is that it provides more frequent signals than a 14-period RSI, making it viable for [day trading](../d/day_trading.md) or [swing trading](../s/swing_trading.md). Here are some typical signals:

- **Buy Signal:** When the 2-period RSI falls below 10, it might indicate that a stock or other [financial instrument](../f/financial_instrument.md) is [oversold](../o/oversold.md), creating a potential buying opportunity.
- **Sell Signal:** When the 2-period RSI rises above 90, it might suggest that the instrument is [overbought](../o/overbought.md), creating a potential selling opportunity.

### Combining with Other Indicators

To enhance reliability, traders often combine the 2-period RSI with other indicators such as moving averages, MACD (Moving Average Convergence [Divergence](../d/divergence.md)), or [support and resistance](../s/support_and_resistance.md) levels. Using [multiple](../m/multiple.md) indicators helps confirm signals and reduces false positives.

### Backtesting and Optimization

Before deploying any [trading strategy](../t/trading_strategy.md) utilizing the 2-period RSI, it's crucial to backtest it to understand its performance in various [market](../m/market.md) conditions. Traders can optimize the lookback period and signal thresholds based on historical data to fine-tune the strategy.

## Advantages and Limitations

### Advantages

- **Responsiveness:** The 2-period RSI reacts quickly to [market](../m/market.md) movements, making it highly suitable for [short-term trading](../s/short-term_trading.md).
- **Simplicity:** The calculation is straightforward and can be easily implemented in various trading platforms.

### Limitations

- **Higher False Positive Rate:** Due to its high sensitivity, the 2-period RSI can produce more [false signals](../f/false_signals_in_trading.md), potentially leading to reduced accuracy.
- **[Market](../m/market.md) [Noise](../n/noise.md):** In highly volatile markets, the short-term nature of the 2-period RSI may cause traders to react to [market](../m/market.md) "[noise](../n/noise.md)" rather than significant trends.

## Practical Application

Many trading platforms and brokerages [offer](../o/offer.md) built-in tools to calculate and plot the RSI, including the 2-period variant. Platforms like MetaTrader, [TradingView](../t/tradingview.md), and [ThinkOrSwim](../t/thinkorswim.md) are widely used for such purposes.

### MetaTrader Implementation

For custom [indicator](../i/indicator.md) creation on MetaTrader, traders can use the MQL4/MQL5 scripting language. The following is a basic implementation outline:

```mql4
int OnInit()
  {
   IndicatorBuffers(1);
   SetIndexBuffer(0,RSIBuffer);
   SetIndexStyle(0,DRAW_LINE);
   string short_name = "2-Period RSI";
   IndicatorShortName(short_name);
   IndicatorDigits(Digits);
   [return](../r/return.md)(INIT_SUCCEEDED);
  }
int OnCalculateconst int rates_total,
              const int prev_calculated,
              const datetime &time[],
              const double &[open](../o/open.md)[],
              const double &high[],
              const double &low[],
              const double &close[],
              const long &tick_volume[],
              const long &[volume](../v/volume.md)[],
              const int &spread[])
  {
   int limit = rates_total-prev_calculated;
   double [gain](../g/gain.md), loss;
   for(int i=rates_total-limit; i>=0; i--)
     {
      [gain](../g/gain.md) = 0.0;
      loss = 0.0;
      for(int j=1; j<=2; j++)
        {
         double diff = close[i-j+1] - close[i-j];
         if (diff > 0) [gain](../g/gain.md) += diff;
         else loss -= diff;
        }
      [gain](../g/gain.md) /= 2.0;
      loss /= 2.0;
      if (loss == 0.0) RSIBuffer[i] = 100;
      else if ([gain](../g/gain.md) == 0.0) RSIBuffer[i] = 0;
      else
        {
         double RS = [gain](../g/gain.md)/loss;
         RSIBuffer[i] = 100.0 - (100.0 / (1.0 + RS));
        }
     }
   [return](../r/return.md)(rates_total);
  }
```

### TradingView Implementation

On [TradingView](../t/tradingview.md), traders can utilize Pine Script to create a custom 2-period RSI [indicator](../i/indicator.md):

```pinescript
//@version=4
study(title="2-Period RSI", shorttitle="2-RSI", [overlay](../o/overlay.md)=false)
rsiLength = 2
source = close
rsiValue = rsi(source, rsiLength)
plot(rsiValue, title="2-Period RSI", color=color.blue)
hline(90, "[Overbought](../o/overbought.md)", color=color.red)
hline(10, "[Oversold](../o/oversold.md)", color=color.green)
```

### ThinkOrSwim Implementation

[ThinkOrSwim](../t/thinkorswim.md) offers a custom scripting language called ThinkScript. Below is an example of a 2-period RSI implementation:

```thinkscript
declare lower;
input length = 2;
def NetChgAvg = WildersAverage(close - close[1], length);
def TotChgAvg = WildersAverage(Absvalue(close - close[1]), length);
def ChgRatio = if TotChgAvg != 0 then NetChgAvg / TotChgAvg else 0;
plot RSI = 50 * (ChgRatio + 1);
RSI.SetDefaultColor(GetColor(1));
plot [Overbought](../o/overbought.md) = 90;
[Overbought](../o/overbought.md).SetDefaultColor(GetColor(5));
plot [Oversold](../o/oversold.md) = 10;
[Oversold](../o/oversold.md).SetDefaultColor(GetColor(5));
```

## Conclusion

The 2-period RSI is a powerful tool for short-term traders looking to capture quick [market](../m/market.md) movements. While it offers benefits of responsiveness and simplicity, traders should be aware of its limitations and employ complementary indicators and [backtesting](../b/backtesting.md) to optimize their strategies. By effectively integrating the 2-period RSI into a broader trading plan, traders can enhance their chances of successful trades in fast-paced [market](../m/market.md) environments.
