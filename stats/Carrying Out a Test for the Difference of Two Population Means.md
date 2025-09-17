# [[AP Stats Home]]
# Carrying Out a Test for the Difference of Two Population Means

This notes page details the "Do" step of a hypothesis test for the difference between two population means ($\mu_1 - \mu_2$). This is where the test statistic is calculated and the p-value is determined, assuming the null hypothesis is true. Before proceeding, ensure you have properly [[Setting Up a Test for the Difference of Two Population Means]].

## 1. State Hypotheses

Recall that the hypotheses for this test are:
*   **Null Hypothesis ($H_0$)**: There is no difference between the two population means.
    $$H_0: \mu_1 - \mu_2 = 0 \quad \text{ or } \quad \mu_1 = \mu_2$$
*   **Alternative Hypothesis ($H_a$)**: There is a difference between the two population means (directional or non-directional).
    $$H_a: \mu_1 - \mu_2 > 0 \quad \text{ or } \quad \mu_1 > \mu_2 \quad \text{ (right-tailed)}$$
    $$H_a: \mu_1 - \mu_2 < 0 \quad \text{ or } \quad \mu_1 < \mu_2 \quad \text{ (left-tailed)}$$
    $$H_a: \mu_1 - \mu_2 \neq 0 \quad \text{ or } \quad \mu_1 \neq \mu_2 \quad \text{ (two-tailed)}$$

## 2. Check Conditions (PLAN)

Before calculating the test statistic, verify that the conditions for inference are met. These are crucial for the validity of the results.

*   **Random**: The data come from two independent random samples or two groups in a randomized experiment. Without random sampling, generalizability to the population is compromised. Without random assignment in an experiment, a cause-and-effect conclusion cannot be drawn.
*   **Independent**:
    *   **Within groups**: Individual observations within each sample/group must be independent.
    *   **Between groups**: The two samples/groups must be independent of each other. This means knowing something about one group's values doesn't give information about the other.
    *   **10% Condition**: If sampling without replacement, ensure the sample sizes $n_1$ and $n_2$ are less than 10% of their respective population sizes ($N_1$ and $N_2$). That is, $n_1 \le 0.10 N_1$ and $n_2 \le 0.10 N_2$. This ensures that the standard deviation of the sampling distribution is not significantly underestimated.
*   **Normal / Large Sample**: The sampling distribution of $\bar{x}_1 - \bar{x}_2$ must be approximately normal. This can be satisfied if:
    *   Both population distributions are approximately normal (checked with graphs of sample data like dot plots, histograms, or normal probability plots showing no strong skewness or outliers).
    *   Both sample sizes are sufficiently large ($n_1 \ge 30$ and $n_2 \ge 30$) due to [[The Central Limit Theorem]].
    *   If one or both sample sizes are small, but the population distribution is clearly not normal, then a t-test is not appropriate.

## 3. Calculate the Test Statistic

If the conditions are met, calculate the two-sample t-statistic:

$$t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

Where:
*   $\bar{x}_1$ and $\bar{x}_2$ are the sample means.
*   $\mu_1$ and $\mu_2$ are the hypothesized population means (under $H_0$, $\mu_1 - \mu_2 = 0$).
*   $s_1$ and $s_2$ are the sample standard deviations.
*   $n_1$ and $n_2$ are the sample sizes.

**Degrees of Freedom (df)**:
The degrees of freedom for this t-statistic are calculated using a complex formula (Welch-Satterthwaite equation), which typically results in a non-integer value. This is usually provided by statistical software or a calculator. For manual calculation or approximation, you can use the smaller of $n_1 - 1$ and $n_2 - 1$. However, for AP Statistics, it's generally expected to use technology for the precise df.

## 4. Determine the p-value

The p-value is the probability of observing a test statistic as extreme as, or more extreme than, the one calculated, *assuming the null hypothesis is true*.

*   **Technology**: Use a graphing calculator or statistical software to find the p-value.
*   **t-distribution table**: If using an approximate df (the smaller of $n_1 - 1$ and $n_2 - 1$), you can use a t-distribution table to find a range for the p-value.

The p-value depends on the alternative hypothesis:
*   **$H_a: \mu_1 - \mu_2 > 0$ (right-tailed)**: $p\text{-value} = P(T \ge t)$
*   **$H_a: \mu_1 - \mu_2 < 0$ (left-tailed)**: $p\text{-value} = P(T \le t)$
*   **$H_a: \mu_1 - \mu_2 \neq 0$ (two-tailed)**: $p\text{-value} = 2 \times P(T \ge |t|)$

[[Interpreting p-Values]] is a critical skill for the conclusion.

## 5. Formulate a Conclusion

Finally, compare your p-value to the chosen significance level ($\alpha$, often 0.05).

*   **If p-value < $\alpha$**: Reject the null hypothesis. There is convincing evidence that the true difference in population means is what the alternative hypothesis suggests.
*   **If p-value $\ge \alpha$**: Fail to reject the null hypothesis. There is not convincing evidence that the true difference in population means is what the alternative hypothesis suggests.

Always state your conclusion in the context of the problem, referring back to the specific populations and variables involved. Be mindful of [[Potential Errors When Performing Tests]]. This process is similar to [[Carrying Out a Test for a Population Mean]] but extended to two independent samples.