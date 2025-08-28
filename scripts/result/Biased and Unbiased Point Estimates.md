# [[AP Stats Home]]
# Biased and Unbiased Point Estimates

In statistics, we often want to estimate unknown population parameters (like the population mean $\mu$ or population proportion $p$) using data from a sample. A **point estimate** is a single value, calculated from sample data, that is used to estimate an unknown population parameter.

## Unbiased Point Estimates

An estimator is considered **unbiased** if its sampling distribution has a mean that is equal to the true value of the parameter being estimated. In other words, an unbiased estimator does not systematically over- or under-estimate the true parameter over many samples. If we were to take an infinite number of samples and calculate the estimate for each, the average of those estimates would equal the true population parameter.

For an estimator $\hat{\theta}$ of a parameter $\theta$, it is unbiased if:

$$
E[\hat{\theta}] = \theta
$$

Where $E[\hat{\theta}]$ represents the expected value (mean) of the sampling distribution of the estimator.

**Examples of Unbiased Estimators:**

*   **Sample Mean ($\bar{x}$)**: Is an unbiased estimator of the population mean ($\mu$).
    $$
    E[\bar{x}] = \mu
    $$
    This is a fundamental concept explored in [[Sampling Distributions for Sample Means]].
*   **Sample Proportion ($\hat{p}$)**: Is an unbiased estimator of the population proportion ($p$).
    $$
    E[\hat{p}] = p
    $$
    This is discussed further in [[Sampling Distributions for Sample Proportions]].

## Biased Point Estimates

An estimator is considered **biased** if its sampling distribution has a mean that is not equal to the true value of the parameter being estimated. This means the estimator consistently tends to over-estimate or under-estimate the true parameter. The **bias** of an estimator $\hat{\theta}$ is defined as the difference between its expected value and the true parameter value:

$$
Bias(\hat{\theta}) = E[\hat{\theta}] - \theta
$$

If $Bias(\hat{\theta}) \neq 0$, the estimator is biased.

**Examples of Biased Estimators:**

*   **Sample Standard Deviation ($s_x$) for small samples (without Bessel's correction)**: While the sample variance $s_x^2$ (calculated with $n-1$ in the denominator) is an unbiased estimator of the population variance $\sigma^2$, the sample standard deviation $s_x$ itself (the square root of the sample variance) is generally a *biased* estimator of the population standard deviation $\sigma$, especially for smaller sample sizes. It tends to underestimate $\sigma$. This is why [[Summary Statistics for a Quantitative Variable]] uses $n-1$ in the denominator for sample variance/standard deviation calculations.

## Bias vs. Variability

It's crucial to distinguish between bias and variability (or precision).

*   **Bias** refers to the accuracy of an estimator – whether it consistently hits the target parameter on average. A high-bias estimator is systematically off target.
*   **Variability** (or precision) refers to the spread of the estimator's sampling distribution. A high-variability estimator yields estimates that are widely scattered around its mean (which could be the true parameter or a biased value).

[[Potential Problems with Sampling]] can lead to both biased estimates (if the sampling method is flawed) and high variability (if the sample size is too small or the population is very diverse).

Consider a dartboard analogy:
*   **Unbiased and Low Variability**: Darts are clustered tightly around the bullseye.
*   **Biased and Low Variability**: Darts are clustered tightly, but far from the bullseye.
*   **Unbiased and High Variability**: Darts are scattered widely, but their center is on the bullseye.
*   **Biased and High Variability**: Darts are scattered widely, and their center is far from the bullseye.

## [[Mean Squared Error (MSE)]]

Sometimes, we prefer a slightly biased estimator if it has significantly lower variability, leading to overall better performance. The **Mean Squared Error (MSE)** is a measure that combines both bias and variability:

$$
MSE(\hat{\theta}) = E[(\hat{\theta} - \theta)^2] = Bias(\hat{\theta})^2 + Var(\hat{\theta})
$$

Where $Var(\hat{\theta})$ is the variance of the estimator. An estimator with a smaller MSE is generally preferred, even if it has a small bias.

## Summary Table

| Estimator        | Parameter Estimated | Unbiased?                               | Notes                                                              | Related Topic                                               |
| :--------------- | :------------------ | :-------------------------------------- | :----------------------------------------------------------------- | :---------------------------------------------------------- |
| Sample Mean $\bar{x}$  | Population Mean $\mu$ | Yes                                     | Average of sample means equals population mean                     | [[Sampling Distributions for Sample Means]]                 |
| Sample Proportion $\hat{p}$ | Population Proportion $p$ | Yes                                     | Average of sample proportions equals population proportion         | [[Sampling Distributions for Sample Proportions]]           |
| Sample Variance $s_x^2$ | Population Variance $\sigma^2$ | Yes (when using $n-1$ denominator) | Using $n$ in the denominator results in a biased (underestimated) variance | [[Summary Statistics for a Quantitative Variable]]          |
| Sample Standard Deviation $s_x$ | Population Standard Deviation $\sigma$ | No (generally biased)               | Tends to slightly underestimate $\sigma$, especially for small $n$ | [[Describing the Distribution of a Quantitative Variable]] |