# [[AP Stats Home]]
# Sampling Distributions for Differences in Sample Means

When we are interested in comparing two population means ($\mu_1$ and $\mu_2$), we often take independent random samples from each population. The difference in the sample means, $\bar{x}_1 - \bar{x}_2$, serves as our point estimate for the true difference in population means. The sampling distribution of this statistic is crucial for making inferences about $\mu_1 - \mu_2$.

## Understanding the Sampling Distribution

The sampling distribution of the difference in sample means, $\bar{x}_1 - \bar{x}_2$, describes the distribution of all possible differences in sample means that could occur if we were to repeatedly take independent random samples of specific sizes ($n_1$ and $n_2$) from two populations.

### Mean of the Sampling Distribution

The mean of the sampling distribution of $\bar{x}_1 - \bar{x}_2$ is equal to the true difference in the population means:

$$ \mu_{\bar{x}_1 - \bar{x}_2} = \mu_1 - \mu_2 $$

This property holds true provided the samples are independent. This indicates that $\bar{x}_1 - \bar{x}_2$ is an [[Biased and Unbiased Point Estimates|unbiased estimator]] of $\mu_1 - \mu_2$.

### Standard Deviation of the Sampling Distribution

The standard deviation of the sampling distribution of $\bar{x}_1 - \bar{x}_2$ is calculated by combining the variances of the individual sample means. Assuming independent samples, we use the formula:

$$ \sigma_{\bar{x}_1 - \bar{x}_2} = \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}} $$

Where:
*   $\sigma_1$ and $\sigma_2$ are the standard deviations of the two populations.
*   $n_1$ and $n_2$ are the sample sizes from the two populations.

**Conditions for using this formula:**
*   **10% Condition:** Both sample sizes $n_1$ and $n_2$ must be less than 10% of their respective population sizes ($N_1$ and $N_2$) to ensure independence of observations within each sample and allow us to treat the standard deviation as constant. That is, $n_1 \le 0.10 N_1$ and $n_2 \le 0.10 N_2$.
*   **Independence:** The two samples must be independent of each other.

### Shape of the Sampling Distribution

The shape of the sampling distribution of $\bar{x}_1 - \bar{x}_2$ can be approximated as Normal under certain conditions:

*   **If both original populations are Normal:** The sampling distribution of $\bar{x}_1 - \bar{x}_2$ will be approximately Normal regardless of sample sizes ($n_1, n_2$).
*   **If neither or only one original population is Normal:** The sampling distribution of $\bar{x}_1 - \bar{x}_2$ will be approximately Normal if both sample sizes are sufficiently large (generally $n_1 \ge 30$ and $n_2 \ge 30$). This is due to the [[The Central Limit Theorem]].

## Conditions for Inference with Differences in Sample Means

When performing inference (e.g., constructing [[Confidence Intervals for the Difference of Two Means]] or [[Setting Up a Test for the Difference of Two Population Means]]), we must check the following conditions:

1.  **Random Condition:**
    *   The data must come from two independent random samples, or the data must come from two groups in a randomized experiment.
2.  **10% Condition:**
    *   When sampling without replacement, $n_1 \le 0.10 N_1$ and $n_2 \le 0.10 N_2$ to ensure independence within samples.
3.  **Normal/Large Sample Condition:**
    *   Both population distributions are Normal, OR
    *   Both sample sizes are large ($n_1 \ge 30$ and $n_2 \ge 30$), OR
    *   Graphs of the sample data (e.g., dot plots, histograms, box plots) show no strong skewness or outliers for either sample. (This is especially important for smaller sample sizes if the population distribution is unknown).

### Summary Table of Sampling Distribution Characteristics

| Characteristic                      | Formula/Rule                                                              | Conditions                                                                                                                                           |
| :---------------------------------- | :------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mean ($\mu_{\bar{x}_1 - \bar{x}_2}$) | $\mu_1 - \mu_2$                                                           | Independent Samples                                                                                                                                  |
| Std. Dev. ($\sigma_{\bar{x}_1 - \bar{x}_2}$) | $\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$                  | 10% Condition for both samples ($n_1 \le 0.10 N_1$, $n_2 \le 0.10 N_2$) AND Independent Samples                                                      |
| Shape                               | Normal                                                                    | Both populations are Normal, OR $n_1 \ge 30$ and $n_2 \ge 30$ (by [[The Central Limit Theorem]]), OR graphical displays show no strong skew/outliers |

Understanding this sampling distribution is fundamental for constructing confidence intervals and performing hypothesis tests to compare two population means.