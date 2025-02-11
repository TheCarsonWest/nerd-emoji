# [[Evidence Evaluation & Citation]]
# [[Statistical Significance]]

**Definition:** Statistical significance refers to the probability of obtaining results as extreme as, or more extreme than, the results actually observed, assuming that the null hypothesis is true.  It's typically represented by the *p*-value.

*p*-value: The probability of observing the obtained results (or more extreme results) if the null hypothesis were true.  A small *p*-value (typically < 0.05) suggests strong evidence against the null hypothesis, leading to its rejection.  $p < \alpha$

**Null Hypothesis ($H_0$):**  A statement that there is no effect, no difference, or no relationship between variables.  For example, in a clinical trial comparing a new drug to a placebo, the null hypothesis might be that there is no difference in effectiveness between the two treatments.

**Alternative Hypothesis ($H_1$ or $H_a$):**  A statement that contradicts the null hypothesis. It proposes that there *is* an effect, difference, or relationship.

**Type I Error (False Positive):** Rejecting the null hypothesis when it is actually true.  The probability of a Type I error is denoted by $\alpha$ (alpha), often set at 0.05.

**Type II Error (False Negative):** Failing to reject the null hypothesis when it is actually false. The probability of a Type II error is denoted by $\beta$ (beta).

**Power ([[1 - $\beta$):** The probability of correctly rejecting the null hypothesis when it is false.  High power is desirable. [[Power Analysis]]

**Factors Affecting [[Statistical Significance]]:**

* **Sample size:** Larger samples generally lead to smaller *p*-values, increasing the likelihood of statistical significance.
* **Effect size:** The magnitude of the difference or relationship between variables. A larger effect size is more likely to yield statistical significance.
* **Variance:**  Higher variance in the data can make it harder to detect statistically significant effects.

**Interpreting *p*-values:**  A low *p*-value doesn't necessarily mean the effect is large or practically important.  It only indicates the likelihood of the observed results occurring by chance. [[Effect Size]]

**Confidence Intervals:** Provide a range of plausible values for a population parameter. A confidence interval that does not include the null hypothesis value suggests statistical significance.  A 95% confidence interval corresponds to an $\alpha$ level of 0.05.

**Relationship between Significance and Importance:** Statistical significance does not imply practical significance. A result might be statistically significant but have a small effect size that is not meaningful in a real-world context.  ([[Practical Significance]])


## $$ \text{p-value} = P(\text{data} | H_0) $$


This equation represents the probability of observing the data given that the null hypothesis is true.  A small p-value suggests evidence against the null hypothesis.

**Further Notes:**

* [[Hypothesis Testing]]
* [[Statistical Tests]]
* [[Choosing the Right Statistical Test]]

