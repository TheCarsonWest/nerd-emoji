# [[AP Stats Home]]
# The Normal Distribution

The Normal Distribution is one of the most important and widely used probability distributions in statistics. It's often referred to as the "bell curve" due to its characteristic symmetric, unimodal shape. Many natural phenomena and sampling distributions approximate a normal distribution, making it a crucial tool for statistical inference.

## Characteristics of the Normal Distribution

*   **Symmetry**: The distribution is perfectly symmetric around its mean ($\mu$). This means the mean, median, and mode are all equal and located at the center of the curve.
*   [[Unimodal]]: It has a single peak.
*   **Asymptotic**: The tails of the distribution extend indefinitely in both directions, approaching, but never quite touching, the horizontal axis.
*   **Defined by two parameters**: A specific normal distribution is completely described by its mean ($\mu$) and standard deviation ($\sigma$).
    *   The mean ($\mu$) determines the center of the distribution.
    *   The standard deviation ($\sigma$) determines the spread or variability of the distribution. A larger $\sigma$ means a wider, flatter curve, while a smaller $\sigma$ means a narrower, taller curve.

The probability density function (PDF) for a normal distribution is given by:
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$
While you won't typically need to use this formula in AP Statistics, it illustrates how the mean and standard deviation define the curve.

## The Empirical Rule (68-95-99.7 Rule)

A key feature of the normal distribution is the predictable proportion of data that falls within certain standard deviation ranges from the mean. This is known as the Empirical Rule:

| Range of Standard Deviations | Approximate Percentage of Data |
| :--------------------------- | :----------------------------- |
| $\mu \pm 1\sigma$            | 68%                            |
| $\mu \pm 2\sigma$            | 95%                            |
| $\mu \pm 3\sigma$            | 99.7%                          |

This rule is incredibly useful for quickly estimating probabilities or proportions for normally distributed data without complex calculations. For example, if test scores are normally distributed with a mean of 70 and a standard deviation of 5, approximately 95% of students scored between 60 and 80 (70 $\pm$ 2 * 5).

## [[Standardizing Normal Distributions]] (Z-Scores)

To compare values from different normal distributions or to find probabilities for values not covered by the Empirical Rule, we convert observations to a standard scale using a [[z-score]]. A z-score measures how many standard deviations an observation is away from the mean.

The formula for a z-score is:
$$z = \frac{x - \mu}{\sigma}$$
Where:
*   $x$ is the individual observation
*   $\mu$ is the mean of the distribution
*   $\sigma$ is the standard deviation of the distribution

A positive z-score indicates the observation is above the mean, while a negative z-score indicates it's below the mean.

## The Standard Normal Distribution

When an observation has been standardized using the z-score formula, it comes from a special normal distribution called the **Standard Normal Distribution**. This distribution has a mean of 0 ($\mu = 0$) and a standard deviation of 1 ($\sigma = 1$). Its probability density function is often denoted as $\phi(z)$.

Using the standard normal distribution, we can find the proportion of observations falling below, above, or between any given values. This is typically done using:
1.  **Z-tables**: These tables provide the cumulative proportion (area to the left) for various z-scores.
2.  **Calculators/Software**: Most graphing calculators (e.g., TI-83/84) have functions like `normalcdf` (normal cumulative distribution function) to calculate probabilities for any normal distribution, or specifically for the standard normal distribution.

Understanding the normal distribution is fundamental, as it underpins many inferential procedures discussed later in AP Statistics, especially when dealing with [[Sampling Distributions for Sample Means]] and [[Sampling Distributions for Sample Proportions]]. For a deeper dive into its applications and how it relates to sampling, refer to [[The Normal Distribution, Revisited]] and [[The Central Limit Theorem]].