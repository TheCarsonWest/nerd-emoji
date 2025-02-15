# [[Source Analysis Techniques]]
# [[Statistical Significance Testing]]

**Goal:** Determine if observed results are likely due to chance or a real effect.

**Key Concepts:**

* **Null Hypothesis ($H_0$):**  There is no effect (e.g., no difference between groups, no relationship between variables).  We aim to *reject* or *fail to reject* this hypothesis, not "prove" it.
* **Alternative Hypothesis ($H_1$ or $H_a$):** There *is* an effect (e.g., there is a difference, there is a relationship).  This is what we hope to find evidence for.
* **Significance Level ($\alpha$):** The probability of rejecting the null hypothesis when it is actually true (Type I error). Commonly set at 0.05 (5%).  [[Type I and Type II Errors]]
* **p-value:** The probability of observing results as extreme as, or more extreme than, the ones obtained, *assuming the null hypothesis is true*. A small p-value suggests evidence against the null hypothesis.
* **Test Statistic:** A value calculated from the sample data that is used to assess the evidence against the null hypothesis.  The specific test statistic depends on the type of test being used.
* **Critical Region:** The range of values of the test statistic that lead to rejection of the null hypothesis.  This is determined by the significance level and the distribution of the test statistic under the null hypothesis.
* **Degrees of Freedom (df):**  A parameter that influences the shape of the sampling distribution of the test statistic.  Often related to sample size and the number of groups being compared.

**Types of Tests:**

* **t-test:** Used to compare the means of two groups.  [[t-test variations]]
* **ANOVA (Analysis of Variance):** Used to compare the means of three or more groups. [[ANOVA Details]]
* **Chi-squared test:** Used to analyze categorical data and assess the association between categorical variables. [[Chi-squared Test Details]]
* **Correlation test:** Used to measure the strength and direction of the linear relationship between two continuous variables. [[Correlation]]


**Steps in Hypothesis Testing:**

1. State the null and alternative hypotheses.
2. Set the significance level ($\alpha$).
3. Select an appropriate statistical test.
4. Calculate the test statistic and p-value.
5. Make a decision: Reject or fail to reject the null hypothesis based on the p-value and significance level.
6. Interpret the results in the context of the research question.


**Important Considerations:**

* **Statistical significance vs. practical significance:** A statistically significant result may not always be practically meaningful.  [[Practical Significance]]
* **Assumptions of different tests:**  Different tests have different assumptions about the data (e.g., normality, independence).  Violation of these assumptions can affect the validity of the results.
* **Effect size:**  Measures the magnitude of the effect, providing additional information beyond statistical significance. [[Effect Size Measures]]
* $p-value < \alpha \implies \text{Reject } H_0$
* $p-value \ge \alpha \implies \text{Fail to reject } H_0$


**Example:**  Suppose we want to test if a new drug lowers blood pressure.

$H_0$: The new drug has no effect on blood pressure.
$H_1$: The new drug lowers blood pressure.


We could use a t-test to compare the average blood pressure of patients who received the drug to the average blood pressure of patients who received a placebo.  If the p-value is less than 0.05, we would reject the null hypothesis and conclude that the drug is effective in lowering blood pressure.
