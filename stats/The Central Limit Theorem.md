# [[AP Stats Home]]
# The Central Limit Theorem (CLT)

The Central Limit Theorem (CLT) is one of the most fundamental theorems in statistics, providing a bridge between sample statistics and population parameters. It's a powerful concept that allows us to make inferences about a population even when we don't know its original distribution.

## What is the Central Limit Theorem?

The Central Limit Theorem states that, regardless of the shape of the original population distribution, the sampling distribution of the sample mean ($\bar{x}$) will approach a [[The Normal Distribution|Normal Distribution]] as the sample size ($n$) increases. This holds true for almost any population distribution, whether it's skewed, uniform, or bimodal, as long as the population has a finite mean and variance.

### Why is it Important?

The CLT is crucial for statistical inference because it allows us to use normal distribution-based procedures (like constructing [[Constructing a Confidence Interval for a Population Mean|confidence intervals]] or [[Setting Up a Test for a Population Mean|hypothesis tests]]) for sample means, even when the original population data is not normally distributed. It's the theoretical backbone for many statistical methods.

## Conditions for the Central Limit Theorem

To apply the Central Limit Theorem, certain conditions must be met:

1.  **Random Condition**: The data must come from a [[Random Sampling and a Collection|random sample]] or a [[Introduction to Experimental Design|randomized experiment]]. This ensures the sample is representative and reduces bias.
2.  **Independence Condition**:
    *   **10% Condition**: When sampling without replacement, the sample size ($n$) should be no more than 10% of the population size ($N$). This ensures that the probability of selecting an item doesn't significantly change with each draw, maintaining approximate independence. $n \le 0.10 N$.
    *   Individual observations must be independent of each other.
3.  **Large Enough Sample Size (Normality Condition)**: This is the most critical condition for the CLT. While "large enough" can vary, a common guideline is:
    *   If the population distribution is approximately normal, any sample size $n \ge 1$ is sufficient.
    *   If the population distribution is unknown or not normal, a sample size of $n \ge 30$ is generally considered large enough for the sampling distribution of $\bar{x}$ to be approximately normal. For highly skewed distributions, a larger sample size may be necessary.

## Parameters of the Sampling Distribution of the Sample Mean

When the conditions for the CLT are met, the sampling distribution of the sample mean $\bar{x}$ has the following characteristics:

*   **Mean of the Sampling Distribution** ($\mu_{\bar{x}}$):
    The mean of the sampling distribution of $\bar{x}$ is equal to the population mean ($\mu$).
    $$ \mu_{\bar{x}} = \mu $$

*   **Standard Deviation of the Sampling Distribution** ($\sigma_{\bar{x}}$):
    The standard deviation of the sampling distribution of $\bar{x}$, also known as the [[Standard Error of the Mean]], is given by the population standard deviation ($\sigma$) divided by the square root of the sample size ($n$).
    $$ \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} $$
    This equation shows that as $n$ increases, $\sigma_{\bar{x}}$ decreases, meaning sample means become less variable and cluster more tightly around the population mean.

| Statistic                 | Population Parameter | Sampling Distribution of $\bar{x}$ Parameter |
| :------------------------ | :------------------- | :------------------------------------------- |
| Mean                      | $\mu$                | $\mu_{\bar{x}} = \mu$                        |
| Standard Deviation        | $\sigma$             | $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$ |

### Example Application

Imagine a population with a highly skewed distribution, like income. Even though individual incomes are skewed, if we take many random samples of, say, 50 people each and calculate the mean income for each sample, the distribution of these sample means will tend to be approximately normal. This allows us to use the normal distribution to calculate probabilities related to sample means, such as the probability that a sample of 50 people will have an average income greater than a certain value.

The CLT is fundamental to understanding [[Sampling Distributions for Sample Means]] and [[Sampling Distributions for Sample Proportions]], providing the theoretical justification for their approximately normal shape under appropriate conditions.