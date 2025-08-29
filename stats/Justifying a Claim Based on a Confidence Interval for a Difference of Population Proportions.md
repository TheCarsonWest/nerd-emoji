# [[AP Stats Home]]
# Justifying a Claim Based on a Confidence Interval for a Difference of Population Proportions

When comparing two population proportions, a confidence interval for their difference provides a range of plausible values for $(p_1 - p_2)$. This interval is a powerful tool for making an informed decision or justifying a claim about whether there's a significant difference between the two proportions, or if one proportion is greater/less than the other.

## The Purpose of Justification

The goal is to determine if the confidence interval for $(p_1 - p_2)$ supports a specific claim about the relationship between $p_1$ and $p_2$. Common claims include:
*   $p_1 \neq p_2$ (there is a difference)
*   $p_1 > p_2$ (or $p_1 - p_2 > 0$)
*   $p_1 < p_2$ (or $p_1 - p_2 < 0$)
*   $p_1 = p_2$ (there is no difference)

For a deeper understanding of how these intervals are constructed, refer to [[Constructing a Confidence Interval for a Population Proportion]] and [[Sampling Distributions for Differences in Sample Proportions]].

## Interpreting the Confidence Interval

The key to justifying a claim lies in observing where the value 0 falls relative to the confidence interval $(L, U)$, where $L$ is the lower bound and $U$ is the upper bound.

### Case 1: The Interval Contains 0

If the confidence interval $(L, U)$ for $(p_1 - p_2)$ includes 0:
*   This means that 0 is a plausible value for the true difference between $p_1$ and $p_2$.
*   Therefore, we *do not have convincing evidence* to claim that $p_1$ and $p_2$ are different.
*   It is plausible that $p_1 = p_2$.
*   We cannot conclude that one proportion is definitively greater or less than the other.

**Example:** A 95% confidence interval for $(p_1 - p_2)$ is $(-0.05, 0.03)$. Since this interval contains 0, we cannot conclude there's a significant difference between $p_1$ and $p_2$ at the 95% confidence level.

### Case 2: The Interval Does Not Contain 0

If the confidence interval $(L, U)$ for $(p_1 - p_2)$ does not include 0, this provides convincing evidence of a difference between $p_1$ and $p_2$. There are two sub-cases:

1.  **Interval is Entirely Above 0 ($L > 0$):**
    *   This means all plausible values for $(p_1 - p_2)$ are positive.
    *   Therefore, we have convincing evidence that $p_1 - p_2 > 0$, which implies $p_1 > p_2$.
    *   We can claim that $p_1$ is significantly greater than $p_2$.

    **Example:** A 95% confidence interval for $(p_1 - p_2)$ is $(0.02, 0.08)$. Since the entire interval is above 0, we are 95% confident that $p_1$ is between 2% and 8% higher than $p_2$. We have convincing evidence that $p_1 > p_2$.

2.  **Interval is Entirely Below 0 ($U < 0$):**
    *   This means all plausible values for $(p_1 - p_2)$ are negative.
    *   Therefore, we have convincing evidence that $p_1 - p_2 < 0$, which implies $p_1 < p_2$.
    *   We can claim that $p_1$ is significantly less than $p_2$.

    **Example:** A 95% confidence interval for $(p_1 - p_2)$ is $(-0.10, -0.03)$. Since the entire interval is below 0, we are 95% confident that $p_1$ is between 3% and 10% lower than $p_2$. We have convincing evidence that $p_1 < p_2$.

## Summary Table for Justifying Claims

| Claim about $p_1$ vs. $p_2$ | Condition on Interval $(L, U)$ for $(p_1 - p_2)$ | Conclusion                                                                                                                                                                                                                                                                                                            |
| :-------------------------- | :------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $p_1 = p_2$                 | Interval contains 0                                | We *do not have convincing evidence* at the given confidence level to conclude that $p_1$ and $p_2$ are different. It is plausible that $p_1 = p_2$.                                                                                                                                                            |
| $p_1 \neq p_2$              | Interval does not contain 0 ($L > 0$ or $U < 0$) | We *have convincing evidence* at the given confidence level that $p_1$ and $p_2$ are different. (Specify if $p_1 > p_2$ or $p_1 < p_2$ based on whether the interval is entirely positive or entirely negative).                                                                                                        |
| $p_1 > p_2$                 | Interval is entirely above 0 ($L > 0$)           | We *have convincing evidence* at the given confidence level that $p_1 > p_2$, because all plausible values for $(p_1 - p_2)$ are positive.                                                                                                                                                                       |
| $p_1 < p_2$                 | Interval is entirely below 0 ($U < 0$)           | We *have convincing evidence* at the given confidence level that $p_1 < p_2$, because all plausible values for $(p_1 - p_2)$ are negative.                                                                                                                                                                       |

## The Role of Confidence Level

The confidence level (e.g., 90%, 95%, 99%) reflects the strength of our conclusion. A 95% confidence interval implies that if we were to repeat the sampling process many times, 95% of the intervals constructed would capture the true difference.

A higher confidence level will result in a wider interval, making it more likely to contain 0, and thus less likely to show a significant difference. Conversely, a lower confidence level will result in a narrower interval, making it more likely to exclude 0.

## [[Confidence Intervals vs. Hypothesis Tests]]

Justifying a claim based on a confidence interval is closely related to performing a [[Setting Up a Test for the Difference of Two Population Proportions]]. In fact, a confidence interval can be used to perform a two-sided hypothesis test:
*   If a $(1-\alpha) \times 100\%$ confidence interval for $(p_1 - p_2)$ contains 0, then a two-sided hypothesis test at significance level $\alpha$ would *fail to reject* the null hypothesis $H_0: p_1 = p_2$.
*   If the interval does not contain 0, then the two-sided test would *reject* $H_0$.

Confidence intervals provide more information than a hypothesis test alone because they give a range of plausible values for the true difference, not just a "yes/no" decision.

The general form of a confidence interval for the difference of two population proportions is:
$$(\hat{p}_1 - \hat{p}_2) \pm z^* \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}$$
where $\hat{p}_1$ and $\hat{p}_2$ are the sample proportions, $n_1$ and $n_2$ are the sample sizes, and $z^*$ is the critical value from the standard normal distribution corresponding to the desired confidence level.