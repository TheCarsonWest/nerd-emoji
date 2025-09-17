# [[AP Stats Home]]
# Carrying Out a Test for the Slope of a Regression Model

This note page details the execution phase of a hypothesis test for the slope of a population regression line. This test helps us determine if there is a statistically significant linear relationship between two quantitative variables in the population, based on a sample. For the initial steps of defining hypotheses, refer to [[Setting Up a Test for the Slope of a Regression Model]].

## Conditions for Inference for Regression Slope

Before performing any calculations, we must verify that the conditions for inference about the slope of a population regression line are met. These conditions are often summarized by the acronym **LINER**:

| Condition       | Description                                                                                                                                                                                                                                                                                                  | How to Check                                                                                                    |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| **L**inear      | The true relationship between the explanatory variable ($x$) and the response variable ($y$) is linear.                                                                                                                                                                                                     | Examine the scatterplot of the data; it should appear roughly linear. Check the residual plot for no obvious pattern. |
| **I**ndependent | Individual observations are independent of each other. When sampling without replacement, the population size should be at least 10 times the sample size ($N \ge 10n$).                                                                                                                                    | Assumed if data are from a random sample or randomized experiment. Check the $10\%$ condition for sampling without replacement. |
| ****N**ormal**    | For any fixed value of $x$, the response variable $y$ varies according to a Normal distribution. In practice, this means the residuals are approximately Normally distributed.                                                                                                                             | Construct a histogram or Normal probability plot of the residuals. Look for approximate symmetry and no strong skewness. |
| **E**qual   | The standard deviation of the response variable $\sigma$ is the same for all values of the explanatory variable $x$. In practice, this means the variability of the residuals should be roughly constant across the range of predicted values.                                                                     | Examine the residual plot; the scatter of points around $y=0$ should be roughly the same for all $x$ values (no fan shape). |
| **R**andom      | The data comes from a well-designed random sample or randomized experiment.                                                                                                                                                                                                                                  | State how the data were collected (random sample, randomized experiment, etc.).                                     |

Failure to meet these conditions can invalidate the results of the hypothesis test.

## Test Statistic

If the conditions are met, we can calculate the test statistic for the slope, which follows a $t$-distribution with $df = n-2$ degrees of freedom.

The test statistic is given by:
$$ t = \frac{b - \beta_0}{SE_b} $$
Where:
*   $b$ is the slope of the sample regression line (least-squares regression line). This is our point estimate for the population slope.
*   $\beta_0$ is the hypothesized value for the population slope, as stated in the null hypothesis ($H_0: \beta = \beta_0$). In most cases, we test $H_0: \beta = 0$ (no linear relationship), so $\beta_0 = 0$.
*   $SE_b$ is the standard error of the slope, which measures the variability of the sample slope $b$ from sample to sample. This value is typically provided in computer output for regression analysis.

The formula for $SE_b$ is:
$$ SE_b = \frac{s}{\sqrt{\sum (x_i - \bar{x})^2}} $$
Where $s$ is the standard deviation of the residuals (also known as the root mean square error, $s_e$), and the denominator measures the spread of the $x$ values. These values are often found in [[Linear Regression Models]] output.

## Calculating the p-value

Once the test statistic $t$ is calculated, we use it to find the p-value. The p-value is the probability of observing a sample slope as extreme as, or more extreme than, the one obtained, assuming the null hypothesis is true.

The p-value is calculated using a $t$-distribution with $df = n-2$ degrees of freedom, where $n$ is the number of data points.

*   **For a two-sided test ($H_a: \beta \ne \beta_0$):**
    $p\text{-value} = 2 \cdot P(T > |t|)$
*   **For a one-sided test ($H_a: \beta > \beta_0$):**
    $p\text{-value} = P(T > t)$
*   **For a one-sided test ($H_a: \beta < \beta_0$):**
    $p\text{-value} = P(T < t)$

The p-value can be found using a $t$-distribution table or statistical software.

## Conclusion in Context

The final step is to make a decision about the null hypothesis and interpret the results in the context of the problem.

1.  **Decision:** Compare the p-value to the chosen significance level $\alpha$.
    *   If $p\text{-value} < \alpha$, we **reject the null hypothesis** ($H_0$).
    *   If $p\text{-value} \ge \alpha$, we **fail to reject the null hypothesis** ($H_0$).

2.  **Interpretation:** State the conclusion in clear, non-technical language, referring back to the original question.

    *   **If you reject $H_0$:** There is convincing statistical evidence (at the $\alpha$ level) to suggest that there is a linear relationship between $x$ and $y$ (or that the population slope is significantly different from $\beta_0$). Specifically, address the direction of the relationship if $H_a$ was one-sided or the sign of $b$ is clear.
    *   **If you fail to reject $H_0$:** There is **not** convincing statistical evidence (at the $\alpha$ level) to suggest a linear relationship between $x$ and $y$ (or that the population slope is significantly different from $\beta_0$). This does **not** mean there is no relationship, just that we don't have enough evidence from our sample to conclude one exists at the chosen significance level.

Remember that a statistically significant relationship does not necessarily imply a strong relationship, nor does it imply causation. Always consider [[Potential Problems with Sampling]] and [[Inference and Experiments]] when interpreting results.

For further exploration, consider [[Confidence Intervals for the Slope of a Regression Model]] to estimate the true population slope.