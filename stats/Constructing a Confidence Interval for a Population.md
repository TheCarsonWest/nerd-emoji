# [[AP Stats Home]]
# Constructing a Confidence Interval for a Population Proportion

A **confidence interval** provides an estimated range of values which is likely to include an unknown population parameter, in this case, the population proportion ($p$). Instead of just a single point estimate (our sample proportion $\hat{p}$), a confidence interval gives us a range of plausible values for $p$ and quantifies our confidence that this range captures the true parameter.

## Purpose and Point Estimate

Our goal is to estimate an unknown population proportion $p$ (e.g., the true proportion of all U.S. adults who support a certain policy). We use a sample proportion, denoted by $\hat{p}$, as our **point estimate** for $p$.
The formula for the sample proportion is:
$$\hat{p} = \frac{\text{number of successes in the sample}}{\text{sample size}} = \frac{x}{n}$$

## General Formula

A confidence interval generally follows the form:
$$ \text{Point Estimate} \pm \text{Margin of Error} $$
For a population proportion, this translates to:
$$ \hat{p} \pm z^* \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} $$
Where:
*   $\hat{p}$ is the sample proportion.
*   $z^*$ is the [[Critical Values]] for the desired confidence level.
*   $\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$ is the standard error of the sample proportion.

## Conditions for Inference

Before constructing a confidence interval for a population proportion, several conditions must be met to ensure the validity of the procedure. These are often remembered as "RANDOM, NORMAL, INDEPENDENT":

| Condition      | Description                                                                                                                                                                                                                                                                                         |
| :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Random**     | The data must come from a [[Random Sampling and a Collection]] or a [[Randomized Comparative Experiment]]. This ensures the sample is representative of the population.                                                                                                                               |
| **Normal**     | The sampling distribution of $\hat{p}$ must be approximately normal. This is checked by verifying that the expected number of successes ($np$) and failures ($n(1-p)$) are both at least 10. Since $p$ is unknown, we use $\hat{p}$: $n\hat{p} \ge 10$ and $n(1-\hat{p}) \ge 10$. This condition allows us to use $z^*$ critical values. |
| **Independent** | Individual observations must be independent. This is ensured if sampling without replacement, the population size is at least 10 times the sample size ($N \ge 10n$). This is the [[10% Condition]].                                                                                                      |

If these conditions are met, we can use the Normal approximation for the [[Sampling Distributions for Sample Proportions]].

## Steps for Construction (PANIC/PHANTOMS)

A common mnemonic to remember the steps for constructing a confidence interval is **PANIC** (Parameter, Assumptions, Name, Interval, Conclude) or **PHANTOMS** (Parameter, Hypotheses, Assumptions, Name, Test Statistic, Obtain p-value, Make a decision, State conclusion). Here, we'll focus on the construction:

1.  **Parameter (P)**: Define the population proportion of interest, $p$.
2.  **Assumptions (A)**: Check the three conditions (Random, Normal, Independent). If any are violated, the interval may not be reliable.
3.  **Name (N)**: State the specific inference procedure you are using: a one-sample z-interval for a population proportion.
4.  **Interval (I)**:
    *   Calculate the point estimate $\hat{p}$.
    *   Find the appropriate [[Critical Values|critical value]] $z^*$ for your chosen confidence level (e.g., for 95% confidence, $z^* \approx 1.96$).
    *   Calculate the standard error: $SE_{\hat{p}} = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$.
    *   Construct the interval using the formula: $\hat{p} \pm z^* \cdot SE_{\hat{p}}$.
5.  **Conclude (C)**: Interpret the confidence interval in the context of the problem.

## Interpretation of a Confidence Interval

The interpretation of a confidence interval is crucial and must be phrased carefully. For example, a 95% confidence interval for the proportion of voters who support a candidate might be (0.48, 0.52).

A correct interpretation would be:
"We are 95% confident that the interval from 0.48 to 0.52 captures the true proportion of all voters who support the candidate."

**Common Misinterpretations to Avoid:**
*   **Do NOT** say: "There is a 95% probability that the true proportion is in this interval." (Once the interval is calculated, the true proportion is either in it or it isn't; probability applies to the method, not the specific interval).
*   **Do NOT** say: "95% of all samples would have a sample proportion in this interval." (The interval estimates $p$, not $\hat{p}$).
*   **Do NOT** say: "95% of the data falls within this interval." (This is about the population distribution, not the parameter $p$).

The confidence level refers to the success rate of the method: If we were to take many, many samples and construct a confidence interval from each, about 95% of those intervals would capture the true population proportion.

This note page sets the foundation for understanding how to quantify uncertainty when estimating a population proportion. For applying this to specific claims, refer to [[Justifying a Claim Based on a Confidence Interval for a Population Proportion]].