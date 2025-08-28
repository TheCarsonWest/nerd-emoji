# [[AP Stats Home]]
# Carrying Out a Test for the Difference of Two Population Proportions

This note page details the practical steps involved in executing a hypothesis test for comparing two population proportions, often following the setup discussed in [[Setting Up a Test for the Difference of Two Population Proportions]]. The goal is to determine if there's a statistically significant difference between two population proportions ($p_1$ and $p_2$) based on sample data.

## 1. State Hypotheses

Before carrying out the test, the null and alternative hypotheses must be clearly stated. This was covered in [[Setting Up a Test for the Difference of Two Population Proportions]].
*   **Null Hypothesis ($H_0$):** $p_1 = p_2$ (or $p_1 - p_2 = 0$). This assumes no difference between the population proportions.
*   **Alternative Hypothesis ($H_a$):**
    *   $p_1 \neq p_2$ (Two-sided test)
    *   $p_1 < p_2$ (One-sided, left-tailed test)
    *   $p_1 > p_2$ (One-sided, right-tailed test)

## 2. Check Conditions

Before performing any calculations, it is crucial to verify that the necessary conditions for inference are met. These ensure the validity of the sampling distribution and the resulting p-value.

| Condition Name   | Description                                                                                                                                                                      |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Random**       | The data should come from two independent random samples or two groups in a randomized experiment. Without random assignment/sampling, generalization to the population is problematic. |
| **Independent**  |   [[The 10% Condition]]: When sampling without replacement, both sample sizes ($n_1$ and $n_2$) must be less than 10% of their respective population sizes ($N_1$ and $N_2$). This ensures the independence of observations within each sample.                                                                                              |
| **Normal (Large Counts)** | The sampling distribution of $\hat{p}_1 - \hat{p}_2$ is approximately normal if the number of successes and failures in both samples are sufficiently large. Specifically:                                                                                                                                                                                                                                                           |
|                  |   $n_1 \hat{p}_1 \ge 10$, $n_1 (1 - \hat{p}_1) \ge 10$                                                                                                                                       |
|                  |   $n_2 \hat{p}_2 \ge 10$, $n_2 (1 - \hat{p}_2) \ge 10$                                                                                                                                      |

*Note: For the Large Counts condition for a hypothesis test, we use the **pooled proportion** ($ \hat{p}_c $) to calculate the expected counts, assuming $H_0$ is true. This means we use $\hat{p}_c$ instead of $\hat{p}_1$ and $\hat{p}_2$ when checking the Normal condition.*

## 3. Calculate the Test Statistic (z-score)

If the conditions are met, we can calculate the test statistic. For two population proportions, we use a z-statistic. Since we assume $H_0: p_1 = p_2$ is true, we pool the sample data to estimate the common population proportion.

### Pooled Proportion ($\hat{p}_c$)
The pooled proportion is calculated as:
$$ \hat{p}_c = \frac{X_1 + X_2}{n_1 + n_2} $$
where $X_1$ and $X_2$ are the number of successes in sample 1 and sample 2, respectively, and $n_1$ and $n_2$ are the respective sample sizes.

### Standard Error
The standard error for the difference in sample proportions, using the pooled proportion under $H_0$, is:
$$ SE_{\hat{p}_1 - \hat{p}_2} = \sqrt{\frac{\hat{p}_c(1 - \hat{p}_c)}{n_1} + \frac{\hat{p}_c(1 - \hat{p}_c)}{n_2}} $$

### z-Test Statistic
The z-test statistic is then calculated as:
$$ z = \frac{(\hat{p}_1 - \hat{p}_2) - (p_1 - p_2)}{\sqrt{\frac{\hat{p}_c(1 - \hat{p}_c)}{n_1} + \frac{\hat{p}_c(1 - \hat{p}_c)}{n_2}}} $$
Under $H_0$, we assume $p_1 - p_2 = 0$, simplifying the formula to:
$$ z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\frac{\hat{p}_c(1 - \hat{p}_c)}{n_1} + \frac{\hat{p}_c(1 - \hat{p}_c)}{n_2}}} $$

## 4. Calculate the p-value

The p-value is the probability of observing a test statistic as extreme as, or more extreme than, the one calculated, assuming the null hypothesis is true. This probability is found using the standard normal distribution (Z-distribution). [[Interpreting p-Values]] provides more details on its meaning.

*   **For $H_a: p_1 \neq p_2$ (Two-sided):** $P(|Z| \ge |z|) = 2 \cdot P(Z \ge |z|)$
*   **For $H_a: p_1 < p_2$ (Left-sided):** $P(Z \le z)$
*   **For $H_a: p_1 > p_2$ (Right-sided):** $P(Z \ge z)$

You can use a z-table or statistical software/calculator to find this probability.

## 5. Make a Decision and Conclusion

Finally, compare the p-value to the chosen significance level ($\alpha$) (e.g., $\alpha = 0.05$).

*   **If p-value $\le \alpha$:** Reject the null hypothesis ($H_0$). There is convincing evidence to support the alternative hypothesis ($H_a$).
*   **If p-value $> \alpha$:** Fail to reject the null hypothesis ($H_0$). There is not convincing evidence to support the alternative hypothesis ($H_a$).

State your conclusion in the context of the problem, referring back to the original claim about the two population proportions. Remember to mention the significance level used. [[Concluding a Test for a Population Proportion]] offers general guidance on forming conclusions. Be mindful of [[Potential Errors When Performing Tests]].