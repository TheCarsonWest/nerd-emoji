# [[AP Stats Home]]
# Justifying a Claim Based on a Confidence Interval for a Population Proportion

When making claims about an unknown population proportion, a confidence interval provides a plausible range of values for that proportion. Instead of simply stating a point estimate, a confidence interval incorporates the uncertainty inherent in [[Sampling Distributions for Sample Proportions]]. This note page focuses on how to use a [[Constructing a Confidence Interval for a Population]] proportion to support or refute a specific claim.

---

## Understanding the Confidence Interval

A confidence interval for a population proportion $p$ is typically expressed as:

$$
\hat{p} \pm z^* \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

Where:
*   $\hat{p}$ is the sample proportion.
*   $z^*$ is the critical value from the standard normal distribution corresponding to the desired confidence level.
*   $n$ is the sample size.

This interval gives a range of values within which we are, for example, 95% confident the true population proportion $p$ lies.

---

## The Role of the Claimed Value

To justify a claim using a confidence interval, we compare the claimed value of the population proportion (often denoted as $p_0$) with the calculated interval. The claim could be one of two types:

1.  **A specific value claim**: The true proportion is equal to some value, e.g., $p = 0.5$.
2.  **A directional claim**: The true proportion is greater than, less than, or not equal to some value, e.g., $p > 0.5$, $p < 0.5$, or $p \neq 0.5$.

---

## Justification Rules

The decision rule for justifying a claim based on a confidence interval is straightforward:

| Claim Type                      | Confidence Interval Result                                    | Conclusion                                                                                                |
| :------------------------------ | :-------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| $p = p_0$ (specific value)      | $p_0$ is *within* the interval                                | We do not have convincing evidence to reject the claim that $p = p_0$. $p_0$ is a plausible value.        |
|                                 | $p_0$ is *outside* the interval                               | We have convincing evidence to reject the claim that $p = p_0$. $p_0$ is not a plausible value.           |
| $p > p_0$ (directional)         | The *entire* interval is above $p_0$                          | We have convincing evidence to support the claim that $p > p_0$.                                          |
|                                 | The interval *overlaps* or is *entirely below* $p_0$           | We do not have convincing evidence to support the claim that $p > p_0$.                                   |
| $p < p_0$ (directional)         | The *entire* interval is below $p_0$                          | We have convincing evidence to support the claim that $p < p_0$.                                          |
|                                 | The interval *overlaps* or is *entirely above* $p_0$           | We do not have convincing evidence to support the claim that $p < p_0$.                                   |
| $p \neq p_0$ (directional)      | $p_0$ is *outside* the interval                               | We have convincing evidence to support the claim that $p \neq p_0$.                                       |
|                                 | $p_0$ is *within* the interval                                | We do not have convincing evidence to support the claim that $p \neq p_0$. $p_0$ is a plausible value.    |

---

## Interpreting the Conclusion

When concluding, it's crucial to phrase your justification carefully:

*   **Avoid definitive statements**: Never say "we have proven" or "the true proportion is." Instead, use phrases like "we have convincing evidence," "it is plausible," or "we do not have convincing evidence to reject/support."
*   **Contextualize**: Always state your conclusion in the context of the problem.
*   **Relationship to Significance Tests**: A 95% confidence interval is equivalent to a two-sided [[Setting Up a Test for a Population Proportion]] at the $\alpha = 0.05$ significance level. If the null hypothesized value ($p_0$) falls outside the 95% confidence interval, then a two-sided test would reject the null hypothesis at $\alpha = 0.05$. This connection is part of [[Concluding a Test for a Population Proportion]].

---

## Example Scenario

A company claims that 80% of its customers are satisfied. A random sample of 200 customers reveals 150 are satisfied. A 95% confidence interval for the true proportion of satisfied customers is calculated as $(0.697, 0.803)$.

**Claim**: The true proportion of satisfied customers is $p = 0.80$.

**Justification**: The claimed value, $p_0 = 0.80$, falls *within* the 95% confidence interval $(0.697, 0.803)$. Therefore, we do not have convincing evidence to reject the company's claim that 80% of its customers are satisfied. The value 0.80 is a plausible proportion for satisfied customers based on this sample.

**Claim**: The true proportion of satisfied customers is $p < 0.85$.

**Justification**: The entire 95% confidence interval $(0.697, 0.803)$ is below 0.85. Therefore, we have convincing evidence to support the claim that the true proportion of satisfied customers is less than 0.85.

---

[[Confidence Level and Margin of Error]]