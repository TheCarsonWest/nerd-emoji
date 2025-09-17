# [[AP Stats Home]]
# Justifying a Claim About a Population Mean Based on a Confidence Interval

When we construct a confidence interval for a population mean, we are estimating a range of plausible values for the true population mean ($\mu$). This interval can then be used to evaluate a specific claim or hypothesis about the value of $\mu$ without necessarily performing a formal [[Setting Up a Test for a Population Mean]]. This method provides a clear and interpretable way to make a decision or justification based on sample data.

## The Purpose

The primary purpose of justifying a claim about a population mean using a confidence interval is to determine if a hypothesized value for the population mean ($\mu_0$) is consistent with the data we've observed. If the hypothesized value falls within our interval of plausible values, we consider it a plausible value for $\mu$. If it falls outside, we consider it implausible.

## How to Justify a Claim

To justify a claim about a population mean based on a confidence interval, follow these steps:

1.  **Identify the Claim/Hypothesized Value**: Clearly state the specific value for the population mean ($\mu_0$) that is being claimed or hypothesized.
2.  **Construct the Confidence Interval**: Calculate a confidence interval for the population mean using your sample data. Ensure the conditions for inference are met (random sample, nearly normal sampling distribution, etc.). Refer to [[Constructing a Confidence Interval for a Population Mean]] for details. A general form for a confidence interval for $\mu$ is:

    $$
    \bar{x} \pm t^* \left( \frac{s}{\sqrt{n}} \right)
    $$
    where $\bar{x}$ is the sample mean, $t^*$ is the critical t-value for the desired confidence level and $n-1$ degrees of freedom, $s$ is the sample standard deviation, and $n$ is the sample size.
3.  **Compare the Claim to the Interval**: Check whether the hypothesized value $\mu_0$ falls within the calculated confidence interval.

    *   **If $\mu_0$ is *inside* the confidence interval**: This means that the hypothesized value is among the plausible values for the population mean, given our data and chosen confidence level. We **do not have convincing evidence** to reject the claim that the true population mean is $\mu_0$.
    *   **If $\mu_0$ is *outside* the confidence interval**: This means that the hypothesized value is *not* among the plausible values for the population mean, given our data and chosen confidence level. We **have convincing evidence** to reject the claim that the true population mean is $\mu_0$. We would conclude that the true population mean is likely different from $\mu_0$ (either greater or smaller, depending on which side of the interval $\mu_0$ falls).

## Connection to Hypothesis Testing

There is a strong connection between confidence intervals and [[Setting Up a Test for a Population Mean]]. For a two-sided hypothesis test with a significance level $\alpha$, if a hypothesized mean $\mu_0$ falls outside a $100(1-\alpha)\%$ confidence interval, then we would reject the null hypothesis $H_0: \mu = \mu_0$ at the $\alpha$ significance level. Conversely, if $\mu_0$ falls inside the confidence interval, we would fail to reject $H_0$.

This means that a $95\%$ confidence interval for $\mu$ corresponds to a two-sided hypothesis test with $\alpha = 0.05$.

## Example

Suppose a company claims that the mean weight of their product is 100 grams. You take a sample of 30 products and construct a 95% confidence interval for the mean weight, which is found to be (98.5 grams, 101.2 grams).

*   **Claimed value ($\mu_0$)**: 100 grams.
*   **Confidence Interval**: (98.5, 101.2) grams.

Since 100 grams falls *within* the interval (98.5, 101.2), we **do not have convincing evidence** to reject the company's claim. Based on this 95% confidence interval, 100 grams is a plausible value for the true mean weight of the product.

## Important Considerations

*   **Confidence Level**: The conclusion depends on the chosen confidence level. A higher confidence level (e.g., 99%) results in a wider interval, making it more likely that $\mu_0$ falls within it, and thus less likely to reject a claim.
*   **"Fail to Reject" vs. "Accept"**: If $\mu_0$ is inside the interval, we state that we "do not have convincing evidence to reject the claim," not that we "accept the claim." This nuance is crucial, as the interval only provides a range of *plausible* values, not a definitive confirmation of a single value.
*   [[Potential Errors When Performing Tests]]: Just like with hypothesis tests, there's always a possibility of making an incorrect conclusion (Type I or Type II error) when using confidence intervals to justify a claim.
*   **Conditions**: Always ensure the conditions for constructing the confidence interval are met (random sample, normal population or large sample size for [[The Central Limit Theorem]]) to ensure the validity of your inference.

By carefully considering where a hypothesized population mean falls relative to your confidence interval, you can make informed decisions and justify claims in a statistically sound manner.