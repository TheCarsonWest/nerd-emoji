# [[AP Stats Home]]
# Confidence Intervals for the Difference of Two Means

Confidence intervals are a fundamental tool in AP Statistics, allowing us to estimate an unknown population parameter with a certain level of confidence. When we are interested in comparing two different population means ($\mu_1$ and $\mu_2$), we use a confidence interval for the difference of two means ($\mu_1 - \mu_2$). This is particularly useful when comparing the effectiveness of two treatments, the average performance of two groups, or the mean values from two distinct populations.

## Purpose

The primary goal of constructing a confidence interval for the difference of two means is to estimate the true difference between the population means, $\mu_1 - \mu_2$, based on sample data from two independent groups. The interval provides a range of plausible values for this difference at a specified confidence level.

## Conditions for Inference

Before constructing a confidence interval, several conditions must be met to ensure the validity of the procedure. These are often referred to as the "PANIC" or "NICE" conditions, depending on the acronym used.

1.  **Random**: The data for both samples must come from [[Random Sampling and a Collection]] or [[Introduction to Experimental Design]] for two independent groups.
    *   Sample 1 is a simple random sample (SRS) from Population 1.
    *   Sample 2 is a simple random sample (SRS) from Population 2.
    *   The two samples must be independent of each other.
2.  **Normal (Large Sample)**:
    *   For each sample, either the population distribution is normal, or the sample size is large enough ($n_1 \ge 30$ and $n_2 \ge 30$) for the [[The Central Limit Theorem]] to apply, making the sampling distribution of the sample mean approximately normal.
    *   If population distributions are unknown and sample sizes are less than 30, a graph (e.g., boxplot or histogram) of the sample data should show no strong skewness or outliers.
3.  **Independent**:
    *   **Within groups**: Individual observations within each sample must be independent. This is typically ensured by random sampling.
    *   **Between groups**: The two samples must be independent of each other.
    *   **10% Condition**: If sampling without replacement, the sample size ($n_1$ and $n_2$) must be no more than 10% of their respective population sizes ($N_1$ and $N_2$). That is, $n_1 \le 0.10 N_1$ and $n_2 \le 0.10 N_2$.

## The Formula

The general formula for a confidence interval is:

$$ \text{Estimate} \pm (\text{Critical Value} \times \text{Standard Error of the Estimate}) $$

For the difference of two means, we use a t-distribution because the population standard deviations ($\sigma_1, \sigma_2$) are almost always unknown and estimated by sample standard deviations ($s_1, s_2$).

The formula for a Two-Sample t-Interval for $\mu_1 - \mu_2$ is:

$$ (\bar{x}_1 - \bar{x}_2) \pm t^* \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}} $$

Where:
*   $\bar{x}_1$ and $\bar{x}_2$ are the sample means for group 1 and group 2, respectively.
*   $s_1$ and $s_2$ are the sample standard deviations for group 1 and group 2, respectively.
*   $n_1$ and $n_2$ are the sample sizes for group 1 and group 2, respectively.
*   $t^*$ is the critical value from the t-distribution with appropriate degrees of freedom.

### Degrees of Freedom (df)

The calculation of degrees of freedom for the two-sample t-procedure is complex. AP Statistics students typically use one of two methods:

1.  **Conservative Method**: Use the smaller of $(n_1 - 1)$ and $(n_2 - 1)$ as the degrees of freedom. This method is always acceptable and provides a slightly wider (more conservative) interval.
    $$ df = \min(n_1 - 1, n_2 - 1) $$
2.  **Technology Method**: Use a calculator or statistical software which employs Welch's approximation. This provides a more accurate, but more complex, fractional degree of freedom. This is the preferred method when using technology.

## Interpretation

After constructing the interval, we interpret it in context:

"We are [Confidence Level]% confident that the true difference in the population means ($\mu_1 - \mu_2$) is between [Lower Bound] and [Upper Bound]."

### [[Justifying a Claim About the Difference of Two Means Based on a Confidence Interval]]

The interpretation of the interval's relationship to zero is critical:
*   If the interval contains 0: It is plausible that there is no true difference between the population means ($\mu_1 = \mu_2$). We do not have sufficient evidence to conclude that one mean is different from the other.
*   If the interval is entirely above 0: We are confident that $\mu_1 > \mu_2$.
*   If the interval is entirely below 0: We are confident that $\mu_1 < \mu_2$.

For more on single population mean intervals, refer to [[Constructing a Confidence Interval for a Population Mean]]. For the theoretical basis, see [[Sampling Distributions for Differences in Sample Means]].