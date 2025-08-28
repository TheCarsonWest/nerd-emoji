# [[AP Stats Home]]
# Justifying a Claim About the Difference of Two Means Based on a Confidence Interval

When comparing two population means, $\mu_1$ and $\mu_2$, a confidence interval for their difference, $\mu_1 - \mu_2$, is a powerful tool for making a justified claim. This method allows us to infer whether there's a statistically significant difference between the two means, or if one mean is larger or smaller than the other, based on sample data. This builds upon the concepts introduced in [[Confidence Intervals for the Difference of Two Means]].

## The Purpose of Justification

The primary goal is to use the constructed confidence interval (e.g., a 95% confidence interval) to support or refute a claim about the true difference between the two population means. Common claims often revolve around whether the means are equal, or if one is greater than the other.

## Relating Confidence Intervals to Hypotheses

Though we're not performing a formal [[Setting Up a Test for the Difference of Two Population Means]], the interpretation of the confidence interval is closely related to potential null hypotheses. The most common null hypothesis is that there is no difference between the two population means, i.e., $H_0: \mu_1 - \mu_2 = 0$.

A $100(1-\alpha)\%$ confidence interval for $\mu_1 - \mu_2$ provides a range of plausible values for the true difference.

## Decision Rule Based on the Confidence Interval

The key to justifying a claim lies in observing whether a specific value (most commonly 0, representing no difference) is included within the interval, or where the entire interval lies relative to that value.

Let $(L, U)$ be the calculated confidence interval for $\mu_1 - \mu_2$, where $L$ is the lower bound and $U$ is the upper bound.

| Condition                      | Interpretation                                                                                                                                                                                                                                                                                                    | Conclusion (Claim)                                                                                                                                                                 |
| :----------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0 is contained in $(L, U)$** | The confidence interval includes 0. This means that a difference of zero between the two population means is a plausible value.                                                                                                                                                                                     | We do **not have convincing evidence** to claim a difference between $\mu_1$ and $\mu_2$. It is plausible that $\mu_1 = \mu_2$.                                                    |
| **$L > 0$**                    | The entire confidence interval is above 0. This means that all plausible values for $\mu_1 - \mu_2$ are positive.                                                                                                                                                                                                | We **have convincing evidence** to claim that $\mu_1 - \mu_2 > 0$, or equivalently, $\mu_1 > \mu_2$. The first mean is significantly larger than the second.                      |
| **$U < 0$**                    | The entire confidence interval is below 0. This means that all plausible values for $\mu_1 - \mu_2$ are negative.                                                                                                                                                                                                | We **have convincing evidence** to claim that $\mu_1 - \mu_2 < 0$, or equivalently, $\mu_1 < \mu_2$. The first mean is significantly smaller than the second.                     |

### Example Justification

Suppose a 95% confidence interval for the difference in mean test scores ($\mu_{\text{Method A}} - \mu_{\text{Method B}}$) is $(2.5, 7.8)$.

**Justification:** "We are 95% confident that the true difference in mean test scores between Method A and Method B (Method A - Method B) lies between 2.5 and 7.8 points. Since the entire interval is above 0, we have convincing evidence to claim that the mean test score for students using Method A is significantly higher than for students using Method B."

If the interval was $(-3.1, 1.2)$:

**Justification:** "We are 95% confident that the true difference in mean test scores between Method A and Method B (Method A - Method B) lies between -3.1 and 1.2 points. Since the interval includes 0, we do not have convincing evidence to claim a significant difference in mean test scores between the two methods. It is plausible that the mean scores are equal."

## Importance of Context

Always state your conclusion in the context of the problem. This means referring to the specific populations, variables, and units involved.

## Relationship to Hypothesis Testing

Justifying a claim using a confidence interval is directly related to a two-sided [[Carrying Out a Test for the Difference of Two Population Means]] at the corresponding significance level $\alpha$.
If a $100(1-\alpha)\%$ confidence interval for $\mu_1 - \mu_2$ **does not contain** 0, then a hypothesis test for $H_0: \mu_1 - \mu_2 = 0$ versus $H_A: \mu_1 - \mu_2 \neq 0$ would result in **rejecting** $H_0$ at the $\alpha$ significance level.
Conversely, if the confidence interval **does contain** 0, then we would **fail to reject** $H_0$.

For one-sided claims, while confidence intervals can provide strong evidence, a formal one-sided hypothesis test is generally more appropriate for specific claims like $\mu_1 > \mu_2$. However, if the entire interval is above (or below) 0, it certainly provides evidence for a one-sided claim.

This method of justification is a critical skill for [[Selecting, Implementing, and Communicating Inference Procedures]].