# [[AP Stats Home]]
# Carrying Out a Chi-Square Test for Goodness of Fit

The Chi-Square Test for Goodness of Fit is a powerful statistical tool used to determine if an observed distribution of a categorical variable differs significantly from a hypothesized or expected distribution. Before carrying out the test, it's essential to have properly [[Setting Up a Chi-Square Goodness of Fit Test]] by stating hypotheses and defining parameters.

---

## Conditions for Inference

Before calculating the test statistic and p-value, we must verify that the conditions for performing a Chi-Square Goodness of Fit test are met. These are:

1.  **Random**: The data must come from a random sample or a randomized experiment. This ensures that the sample is representative of the population.
2.  **Independent**:
    *   The individual observations within the sample must be independent of each other.
    *   When sampling without replacement, the sample size $n$ must be less than $10\%$ of the population size ($N$). That is, $n \le 0.10N$.
3.  **Large Counts** (Expected Counts): All expected counts must be at least 5. This condition ensures that the $\chi^2$ distribution is a good approximation for the sampling distribution of the test statistic. If this condition is not met for any category, categories may need to be combined, which can alter the hypotheses.

---

## Calculating the Chi-Square Test Statistic

The Chi-Square ($\chi^2$) test statistic measures how far the observed counts deviate from the expected counts. The formula is:

$$
\chi^2 = \sum \frac{(\text{Observed} - \text{Expected})^2}{\text{Expected}}
$$

Where:
*   **Observed (O)**: The actual count for each category from the sample.
*   **Expected (E)**: The count that would be expected for each category if the null hypothesis were true. These are calculated as $E = n \times p_i$, where $n$ is the total sample size and $p_i$ is the hypothesized proportion for that category. [[Expected Counts in Two-Way Tables]] is a related concept for two-way tables, but here we use the hypothesized proportions.
*   **$\sum$**: Sum of these values over all categories.

A larger $\chi^2$ value indicates a greater discrepancy between the observed and expected distributions, providing stronger evidence against the null hypothesis.

---

## Degrees of Freedom

The degrees of freedom ($df$) for a Chi-Square Goodness of Fit test are calculated as:

$$
df = \text{number of categories} - 1
$$

The degrees of freedom determine the specific shape of the $\chi^2$ distribution used to calculate the p-value.

---

## Obtaining the P-Value

Once the $\chi^2$ test statistic and degrees of freedom are calculated, the p-value can be found. The p-value is the probability of observing a $\chi^2$ test statistic as extreme as, or more extreme than, the one calculated, assuming the null hypothesis is true.

Since the Chi-Square test is always right-tailed (larger $\chi^2$ values indicate stronger evidence against $H_0$), the p-value is the area under the $\chi^2$ distribution curve to the right of the calculated test statistic.

*   You can use a calculator's `$\chi^2$cdf` function (e.g., `$\chi^2$cdf(lower_bound = $\chi^2$_statistic, upper_bound = E99, df)`).
*   Alternatively, statistical software will provide the p-value directly.

A small p-value (typically less than the significance level $\alpha$) suggests that the observed differences are unlikely to have occurred by chance if the null hypothesis were true, leading to rejection of $H_0$. [[Interpreting p-Values]] provides more detail on this.

---

## Conclusion

The final step is to make a conclusion in the context of the problem, linking back to the null and alternative hypotheses. This involves comparing the p-value to the chosen significance level $\alpha$.

*   **If p-value $< \alpha$**: We reject the null hypothesis ($H_0$). There is convincing evidence that the observed distribution of the categorical variable is significantly different from the hypothesized distribution.
*   **If p-value $\ge \alpha$**: We fail to reject the null hypothesis ($H_0$). There is not convincing evidence that the observed distribution of the categorical variable is significantly different from the hypothesized distribution.

Remember that failing to reject $H_0$ does not mean we accept $H_0$; it simply means we don't have enough evidence to claim a difference. [[Concluding a Test for a Population Proportion]] offers a general framework for drawing conclusions in hypothesis tests.