# Wilcoxon Test

The Wilcoxon Test is a non-parametric statistical test used to compare two paired groups. Unlike parametric tests such as the [t-test](../t/t-test.md), non-parametric tests do not make any assumptions about the [underlying](../u/underlying.md) [distribution](../d/distribution.md) of the data. This makes the Wilcoxon Test particularly useful in situations where the data does not meet the normality assumption or when dealing with ordinal data or ranks. The test is named after Frank Wilcoxon, who developed it in the 1940s.

## Types of Wilcoxon Tests

There are two main types of Wilcoxon Tests:

1. **Wilcoxon Signed-Rank Test:** Used for comparing two related samples, matched samples, or repeated measurements on a single sample to assess whether their population mean ranks differ.
2. **Wilcoxon Rank-Sum Test (also known as Mann-Whitney U Test):** Used for comparing two independent samples to determine whether there is a difference in their population mean ranks.

### Wilcoxon Signed-Rank Test

The Wilcoxon Signed-Rank Test is the non-parametric counterpart to the paired samples [t-test](../t/t-test.md). It assesses whether the [median](../m/median.md) of the differences between pairs of observations is zero or not.

#### When to Use

Use the Wilcoxon Signed-Rank Test when:
- The differences between pairs are continuous, ordinal, or approximately interval.
- The differences between pairs are symmetrically distributed about a [median](../m/median.md).
- The sample size is small and the data do not meet the assumptions of the paired [t-test](../t/t-test.md).

#### Assumptions

1. The pairs are chosen randomly and independently.
2. The pairs are related.
3. The measurement scale is at least ordinal.

#### Procedure

1. **Calculate the Differences:** Compute the differences between each pair of observations.
2. **Ignore Zero Differences:** If any differences are zero, they are excluded from the test.
3. **Rank the Absolute Differences:** Rank the absolute values of the remaining differences.
4. **Assign Signs to the Ranks:** Assign a positive or negative sign to the ranks based on the sign of the differences.
5. **Sum the Ranks:** Calculate the sum of the ranks for the positive differences and the sum for the negative differences.
6. **Compute the Test Statistic:** The test statistic is the smaller of the absolute values of these two sums.
7. **Determine the P-[Value](../v/value.md):** Use the test statistic to find the corresponding p-[value](../v/value.md), which [will](../w/will.md) help in accepting or rejecting the [null hypothesis](../n/null_hypothesis.md).

### Example Calculation

Following is a step-by-step example:

1. Suppose we have pairs of data:
 - Pair 1: (5, 7)
 - Pair 2: (9, 13)
 - Pair 3: (4, 4)
 - Pair 4: (6, 8)
 - Pair 5: (6, 5)

2. Differences:
 - Pair 1: -2
 - Pair 2: -4
 - Pair 3: 0 (ignored)
 - Pair 4: -2
 - Pair 5: 1

3. Absolute Differences:
 - Pair 1: 2
 - Pair 2: 4
 - Pair 4: 2
 - Pair 5: 1

4. Ranks:
 - Rank 1: 1
 - Rank 2: 2.5 (for both Pair 1 and Pair 4)
 - Rank 4: 4

5. Assign Signs and Sum the Ranks:
 - Positive Ranks Sum: 1 (for Pair 5)
 - Negative Ranks Sum: 2.5 + 2.5 + 4 = 9

6. Test Statistic: Minimum of 1 and 9 = 1

7. Compare with critical [value](../v/value.md) or determine p-[value](../v/value.md) to conclude.

### Wilcoxon Rank-Sum Test (Mann-Whitney U Test)

The Wilcoxon Rank-Sum Test is designed to test the [null hypothesis](../n/null_hypothesis.md) that two populations are equal in terms of their central tendency.

#### When to Use

Use the Wilcoxon Rank-Sum Test when:
- The data from both samples are continuous, ordinal, or approximately interval.
- The distributions are not necessarily normal, and sample sizes might be different.

#### Assumptions

1. The samples are independent.
2. The measurement scale is at least ordinal.

#### Procedure

1. **Combine and Rank:** Combine the data from both samples and rank them from smallest to largest. Assign ranks, with average ranks for ties.
2. **Separate Ranks:** Separate the ranks back into their respective samples.
3. **Sum the Ranks:** Calculate the sum of the ranks for each sample.
4. **Compute U:** Use the rank sums to compute the U statistic.
5. **Determine the P-[Value](../v/value.md):** Use the U statistic to find the corresponding p-[value](../v/value.md) to make a conclusion about the [null hypothesis](../n/null_hypothesis.md).

### Example Calculation

1. Suppose we have two samples:
 - Sample 1: 10, 15, 20
 - Sample 2: 15, 20, 25, 30

2. Combine and Rank:
 - 10 (1.0), 15 (2.5), 15 (2.5)
 - 20 (4.5), 20 (4.5), 25 (6.0), 30 (7.0)

3. Separate Ranks:
 - Sample 1 Ranks: 1, 2.5, 4.5
 - Sample 2 Ranks: 2.5, 4.5, 6, 7

4. Sum the Ranks:
 - Sum of Ranks of Sample 1: 1 + 2.5 + 4.5 = 8
 - Sum of Ranks of Sample 2: 2.5 + 4.5 + 6 + 7 = 20

5. Compute U:
 - U1 = R1 - ((n1 * (n1 + 1)) / 2)
 - U2 = R2 - ((n2 * (n2 + 1)) / 2)
 - Then, U is the smaller [value](../v/value.md) of U1 and U2. Calculate accordingly.

## Application in Finance and Trading

Wilcoxon Tests, especially the Wilcoxon Signed-Rank Test, are often used in [finance](../f/finance.md) and trading contexts to compare the performance of different [trading algorithms](../t/trading_algorithms.md), financial models, or investment strategies when the performance data does not meet normality assumptions.

### Algorithmic Trading

In [algorithmic trading](../a/algorithmic_trading.md), Wilcoxon Tests can be used to:

- Compare the performance of two [trading strategies](../t/trading_strategies.md) on different assets or time periods.
- Evaluate the effectiveness of an adaptation or new version of a trading algorithm.
- Statistically validate quant trading hypotheses without assuming normality.

### Fintech Applications

FinTech companies apply Wilcoxon Tests for:

- Model validation: By comparing [predictive models](../p/predictive_models_in_trading.md) on test datasets with non-normal distributions.
- A/B testing: Evaluating different financial products or user interface changes where response metrics may not be normally distributed.
- [Risk](../r/risk.md) assessment: Comparing [historical returns](../h/historical_returns.md) distributions to assess [risk models](../r/risk_models_in_trading.md).

### Practical Example

For instance, a FinTech company like Robinhood might use the Wilcoxon Signed-Rank Test to evaluate a new feature in their trading app that is designed to help users improve [trading performance](../t/trading_performance.md). They could compare the [trading performance metrics](../t/trading_performance_metrics.md) (such as daily returns) of a sample of users before and after introducing the new feature, checking if the new feature has a statistically significant impact.

## Advantages and Limitations

### Advantages

1. **No assumptions about normality:** The tests are non-parametric and do not assume a [normal distribution](../n/normal_distribution_in_trading.md).
2. **[Robust](../r/robust.md) to outliers:** Less affected by outliers compared to parametric tests.
3. **Small sample sizes:** Works well even with small sample sizes where parametric tests might [fail](../f/fail.md).

### Limitations

1. **Less Power:** Wilcoxon Tests are generally less powerful than their parametric counterparts if the [underlying](../u/underlying.md) [distribution](../d/distribution.md) is normal.
2. **[Scalability](../s/scalability.md) Issues:** May become cumbersome with very large datasets.
3. **Interpretation:** Results can be less intuitive compared to parametric tests.

In conclusion, the Wilcoxon Test is a versatile statistical tool that provides a [robust](../r/robust.md) alternative to parametric tests, especially when dealing with non-normal distributions or ordinal data. Its applications in [finance](../f/finance.md) and trading, particularly in [algorithmic trading](../a/algorithmic_trading.md) and FinTech, highlight its importance in practical, real-world scenarios. Whether comparing [trading algorithms](../t/trading_algorithms.md) or evaluating financial models, the Wilcoxon Test remains a valuable tool for data scientists and financial analysts.