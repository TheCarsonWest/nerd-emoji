# [[AP Stats Home]]
# Concluding a Test for a Population Proportion

Concluding a test for a population proportion is the final and crucial step in the hypothesis testing process. After [[Setting Up a Test for a Population Proportion]] and calculating the test statistic and p-value, this stage involves using the p-value to make a decision about the null hypothesis and then stating that decision in the context of the problem.

## The Decision Rule

The decision to reject or fail to reject the null hypothesis is based on comparing the calculated p-value to the predetermined significance level, $\alpha$ (alpha). The significance level is the probability of making a Type I error (rejecting a true null hypothesis). Common values for $\alpha$ are 0.05, 0.01, or 0.10.

| Comparison           | Decision                         | Implication                                                                                             |
| :------------------- | :------------------------------- | :------------------------------------------------------------------------------------------------------ |
| **p-value $\le \alpha$** | **Reject the Null Hypothesis ($H_0$)** | There is sufficient evidence to conclude that the alternative hypothesis ($H_a$) is true.                   |
| **p-value $ > \alpha$** | **Fail to Reject the Null Hypothesis ($H_0$)** | There is not sufficient evidence to conclude that the alternative hypothesis ($H_a$) is true. (This does not mean we accept $H_0$). |

### [[Interpreting p-Values]]
The p-value represents the probability of observing a sample statistic (or one more extreme) given that the null hypothesis is true. A small p-value indicates that such an observed result is unlikely to occur by random chance if the null hypothesis were true, thus providing evidence against $H_0$.

## Stating the Conclusion in Context

Regardless of the statistical decision, it is imperative to translate it into a clear, concise statement that addresses the original research question within the real-world context of the problem.

### Components of a Complete Conclusion:
1.  **State the statistical decision:** "We reject $H_0$" or "We fail to reject $H_0$."
2.  **Refer to the p-value and significance level:** "Because the p-value ($p = \text{____}$) is less than/greater than $\alpha = \text{____}$."
3.  **Contextualize the decision:** Explain what the decision means in terms of the alternative hypothesis ($H_a$).

#### Example Conclusion Structure:
*   **If you reject $H_0$:** "Because the p-value (e.g., $p = 0.02$) is less than $\alpha = 0.05$, we reject the null hypothesis. There is statistically significant evidence to conclude that [state $H_a$ in context]."
*   **If you fail to reject $H_0$:** "Because the p-value (e.g., $p = 0.15$) is greater than $\alpha = 0.05$, we fail to reject the null hypothesis. There is not statistically significant evidence to conclude that [state $H_a$ in context]."

## Important Considerations

### Never "Accept" the Null Hypothesis
It is crucial to never state that you "accept" the null hypothesis. Failing to reject the null hypothesis simply means that the data do not provide enough evidence to overturn it. It does not prove that the null hypothesis is true. Think of it like a legal trial: you can find someone "not guilty" (fail to reject the null), but that doesn't necessarily mean they are "innocent" (accept the null) – it just means there wasn't enough evidence to convict.

### [[Potential Errors When Performing Tests]]
When making a conclusion, there's always a possibility of making an error:
*   **Type I Error:** Rejecting the null hypothesis when it is actually true. The probability of this error is $\alpha$.
*   **Type II Error:** Failing to reject the null hypothesis when it is actually false. The probability of this error is denoted by $\beta$.

Your conclusion should implicitly acknowledge these possibilities without explicitly stating that an error has occurred (since you don't know the true state of nature). Choosing an appropriate $\alpha$ level involves balancing the risks of these two types of errors. A lower $\alpha$ reduces the chance of a Type I error but increases the chance of a Type II error.

The test statistic for a population proportion (often denoted as $z$) is calculated as:
$$z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$$
where $\hat{p}$ is the sample proportion, $p_0$ is the hypothesized population proportion, and $n$ is the sample size. The p-value is then derived from this $z$-score using the [[The Normal Distribution, Revisited]].