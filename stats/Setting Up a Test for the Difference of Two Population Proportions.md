# [[AP Stats Home]]
# Setting Up a Test for the Difference of Two Population Proportions

When we want to compare the proportion of "successes" between two distinct populations or groups, we use a two-sample $z$-test for the difference of population proportions. This test helps us determine if an observed difference in sample proportions is statistically significant or if it could reasonably occur by chance, assuming there's no real difference in the populations.

## 1. Defining Parameters and Hypotheses

Before we can perform any calculations, we must clearly define the population parameters and state our null and alternative hypotheses.

*   **Population Parameters**:
    *   $p_1$: The true proportion of "successes" for Population 1.
    *   $p_2$: The true proportion of "successes" for Population 2.

*   **Null Hypothesis ($H_0$)**:
    The null hypothesis always assumes no difference between the two population proportions.
    $$H_0: p_1 - p_2 = 0 \quad \text{or} \quad H_0: p_1 = p_2$$

*   **Alternative Hypothesis ($H_a$)**:
    The alternative hypothesis reflects the claim or the question we are trying to answer. It can be one-sided (greater than or less than) or two-sided (not equal to).
    *   One-sided (right-tailed): $H_a: p_1 - p_2 > 0 \quad \text{or} \quad H_a: p_1 > p_2$
    *   One-sided (left-tailed): $H_a: p_1 - p_2 < 0 \quad \text{or} \quad H_a: p_1 < p_2$
    *   Two-sided: $H_a: p_1 - p_2 \neq 0 \quad \text{or} \quad H_a: p_1 \neq p_2$

    **Example**: If we are testing if a new drug (Group 1) has a higher success rate than a placebo (Group 2), our hypotheses would be $H_0: p_1 = p_2$ and $H_a: p_1 > p_2$.

## 2. Conditions for Inference

To ensure the validity of our test results, specific conditions must be met. These are crucial for the sampling distribution of the difference in sample proportions to be approximately normal.

| Condition               | Description                                                                                                                                                                                                                                                                                                                                                            |
| :---------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Random**              | The data must come from two independent random samples from the populations of interest, or from two groups in a randomized experiment. [[Random Sampling and a Collection]]                                                                                                                                                                                               |
| **Independent**         | Observations within each sample must be independent. When sampling without replacement, the population size must be at least 10 times the sample size for both populations. That is, $N_1 \ge 10n_1$ and $N_2 \ge 10n_2$. Also, the two samples/groups themselves must be independent of each other.                                                                       |
| **Normal (Large Counts)** | The sampling distribution of $\hat{p}_1 - \hat{p}_2$ must be approximately normal. This is satisfied if there are at least 10 "successes" and at least 10 "failures" in *each* sample, using the *pooled* proportion. <br> $n_1 \hat{p}_c \ge 10$, $n_1 (1 - \hat{p}_c) \ge 10$ <br> $n_2 \hat{p}_c \ge 10$, $n_2 (1 - \hat{p}_c) \ge 10$ |

## 3. Calculating the Pooled Proportion

When we assume the null hypothesis ($H_0: p_1 = p_2$) is true, we are assuming that the true population proportions are equal. In this case, it makes sense to "pool" the data from both samples to get a better estimate of this common population proportion. This pooled proportion, denoted $\hat{p}_c$ (sometimes $\hat{p}$), is used in the standard error calculation for the test statistic.

Let $x_1$ and $x_2$ be the number of successes in Sample 1 and Sample 2, respectively.
Let $n_1$ and $n_2$ be the sample sizes for Sample 1 and Sample 2, respectively.

The pooled proportion is calculated as:
$$\hat{p}_c = \frac{x_1 + x_2}{n_1 + n_2}$$
where $x_1 = n_1 \hat{p}_1$ and $x_2 = n_2 \hat{p}_2$.

## 4. Test Statistic

The test statistic for the difference of two population proportions is a $z$-score, which measures how many standard errors the observed difference in sample proportions ($\hat{p}_1 - \hat{p}_2$) is from the hypothesized difference (which is 0 under $H_0$).

The formula for the $z$-test statistic is:
$$z = \frac{(\hat{p}_1 - \hat{p}_2) - 0}{\sqrt{\hat{p}_c(1 - \hat{p}_c)\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$$

Where:
*   $\hat{p}_1$ is the sample proportion for Population 1 ($x_1/n_1$).
*   $\hat{p}_2$ is the sample proportion for Population 2 ($x_2/n_2$).
*   $\hat{p}_c$ is the [[Pooled Proportion]] (calculated above).
*   $n_1$ and $n_2$ are the sample sizes.

This $z$-statistic follows a standard normal distribution if the conditions are met and the null hypothesis is true. Once the test statistic is calculated, it is used to find the [[Interpreting p-Values|p-value]] for the test. For the next steps in the process, refer to [[Carrying Out a Test for the Difference of Two Population Proportions]].