# [[AP Stats Home]]
# Carrying Out a Test for a Population Mean

After carefully [[Setting Up a Test for a Population Mean]] by defining hypotheses and choosing a significance level, the next crucial step is to *carry out* the test. This involves checking necessary conditions, calculating the test statistic, and determining the p-value.

## Conditions for Inference

Before proceeding with a one-sample $t$-test for a population mean, certain conditions must be met to ensure the validity of the results. These are often remembered by the acronym "RANDOM, NORMAL, INDEPENDENT."

1.  **Random**: The data must come from a [[Random Sampling and a Collection]] or a randomized experiment. This ensures that the sample is representative of the population of interest.
2.  **Normal**: The sampling distribution of the sample mean must be approximately Normal. This can be satisfied in a few ways:
    *   The population distribution is stated to be Normal.
    *   The sample size is large (typically $n \geq 30$), allowing the [[The Central Limit Theorem]] to apply.
    *   If $n < 30$, inspect a graph of the sample data (e.g., dot plot, box plot, histogram) for strong skewness or outliers. If the graph shows no strong skewness or outliers, it's generally safe to proceed.
3.  **Independent**: Individual observations must be independent.
    *   **10% Condition**: When sampling without replacement, the sample size $n$ must be no more than 10% of the population size $N$ ($n \leq 0.10N$). This ensures that the probability of selecting an item doesn't significantly change with each draw.

## Calculating the Test Statistic

If the conditions are met, we can calculate the test statistic for a population mean, which follows a $t$-distribution. This is given by:

$$
t = \frac{\bar{x} - \mu_0}{s_x / \sqrt{n}}
$$

Where:
*   $\bar{x}$ is the sample mean.
*   $\mu_0$ is the hypothesized population mean (from the null hypothesis $H_0$).
*   $s_x$ is the sample standard deviation.
*   $n$ is the sample size.

This $t$-statistic measures how many standard errors the sample mean ($\bar{x}$) is away from the hypothesized population mean ($\mu_0$).

## Degrees of Freedom

The $t$-distribution is a family of distributions, characterized by its [[Degrees of Freedom]]. For a one-sample $t$-test, the degrees of freedom (df) are calculated as:

$$
df = n - 1
$$

Where $n$ is the sample size. The shape of the $t$-distribution becomes more like the standard Normal distribution as the degrees of freedom increase.

## Determining the P-value

The p-value is the probability of observing a test statistic as extreme as, or more extreme than, the one calculated from the sample data, assuming the null hypothesis is true.

To find the p-value:
1.  **Identify the direction of the alternative hypothesis ($H_a$)**:
    *   If $H_a: \mu > \mu_0$, the p-value is the area to the right of the calculated $t$-statistic.
    *   If $H_a: \mu < \mu_0$, the p-value is the area to the left of the calculated $t$-statistic.
    *   If $H_a: \mu \neq \mu_0$, the p-value is twice the area in the tail beyond the calculated $t$-statistic (since it's a two-sided test).
2.  **Use a $t$-distribution table or technology (calculator/software)**: Look up the calculated $t$-value with $df = n-1$ to find the corresponding probability.

A smaller p-value provides stronger evidence against the null hypothesis. For a more in-depth understanding of its meaning, refer to [[Interpreting p-Values]].

## Making a Decision and Stating a Conclusion

After calculating the p-value, compare it to the predetermined significance level ($\alpha$).

*   **If p-value $\leq \alpha$**: We **reject** the null hypothesis ($H_0$). There is statistically significant evidence to conclude that the alternative hypothesis ($H_a$) is true.
*   **If p-value $> \alpha$**: We **fail to reject** the null hypothesis ($H_0$). There is not enough statistically significant evidence to conclude that the alternative hypothesis ($H_a$) is true. *Note: We never "accept" the null hypothesis.*

Finally, state your conclusion in the context of the problem, relating it back to the original research question. This final step is similar to [[Concluding a Test for a Population Proportion]], but adapted for a population mean. Remember to always acknowledge the possibility of [[Potential Errors When Performing Tests]].