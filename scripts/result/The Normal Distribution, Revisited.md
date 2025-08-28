# [[AP Stats Home]]
# AP Statistics: The Normal Distribution, Revisited

The Normal Distribution is a fundamental concept in statistics, often serving as a model for quantitative data. While we've previously introduced its basic shape and properties ([[The Normal Distribution]]), this page delves deeper into its applications, standardization, and how we use it to calculate probabilities. It's crucial for understanding topics like [[Sampling Distributions for Sample Means]] and [[The Central Limit Theorem]].

---

## Key Properties of the Normal Distribution

A normal distribution, often called the "bell curve," is a symmetric, unimodal distribution characterized by its mean ($\mu$) and standard deviation ($\sigma$). Its probability density function is given by:

$$ f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} $$

While we don't typically calculate probabilities directly from this formula, it defines the curve's shape.

**Important Characteristics:**
*   **Symmetry:** The mean, median, and mode are all equal and located at the center of the distribution.
*   **Total Area:** The total area under the curve is 1, representing 100% of the data.
*   **Asymptotic:** The tails of the curve extend infinitely in both directions but never quite touch the horizontal axis.

---

## The Empirical Rule (68-95-99.7 Rule)

This rule provides a quick way to estimate the proportion of data within certain standard deviations of the mean for any normal distribution.

| Interval               | Proportion of Data |
| :--------------------- | :----------------- |
| $\mu \pm 1\sigma$      | Approximately 68%  |
| $\mu \pm 2\sigma$      | Approximately 95%  |
| $\mu \pm 3\sigma$      | Approximately 99.7% |

This rule is extremely useful for quick estimations and understanding the spread of data in a normal distribution. For instance, roughly 95% of observations fall within two standard deviations of the mean.

---

## Standardizing Normal Distributions: Z-Scores

To compare values from different normal distributions or to find probabilities for any normal distribution, we standardize the values using a **z-score**. A z-score measures how many standard deviations an observation ($x$) is away from the mean ($\mu$).

The formula for a z-score is:

$$ z = \frac{x - \mu}{\sigma} $$

*   A positive z-score indicates the observation is above the mean.
*   A negative z-score indicates the observation is below the mean.
*   A z-score of 0 means the observation is equal to the mean.

The distribution of z-scores for a normal distribution is called the **Standard Normal Distribution**, which has a mean of 0 and a standard deviation of 1.

---

## Calculating Probabilities with Z-Scores

Once a value $x$ is converted to a z-score, we can use the Standard Normal Distribution (Z-table or calculator) to find the probability of observing a value less than, greater than, or between certain values.

**Steps:**
1.  **State the Problem:** Clearly define the probability you want to find (e.g., $P(X < x_0)$).
2.  **Standardize:** Convert the $x$ value(s) to z-score(s) using $z = (x - \mu) / \sigma$.
3.  **Sketch (Optional but Recommended):** Draw a normal curve and shade the area corresponding to the desired probability.
4.  **Use Table/Calculator:**
    *   **Z-table:** Provides the area to the left of a given z-score.
    *   **Calculator (e.g., `normalcdf`):** Allows direct calculation of areas between two z-scores (or from $-\infty$ to $z$, or $z$ to $\infty$).

**Example:** If heights are normally distributed with $\mu = 68$ inches and $\sigma = 3$ inches, what is the probability a randomly selected person is taller than 71 inches?
1.  $P(X > 71)$
2.  $z = \frac{71 - 68}{3} = \frac{3}{3} = 1$
3.  We need $P(Z > 1)$.
4.  Using a calculator `normalcdf(1, E99, 0, 1)` or Z-table (finding $P(Z < 1)$ and subtracting from 1), we get approximately $1 - 0.8413 = 0.1587$.

---

## Assessing Normality

While the Normal Distribution is widely used, it's essential to determine if a dataset can reasonably be modeled by it. [[Graphical Representations of Summary Statistics]] and [[Representing a Quantitative Variable with Graphs]] can help.

**Methods for Assessing Normality:**
*   **Histogram/Stemplot:** Look for a roughly symmetric, unimodal, bell-shaped distribution.
*   **Normal Probability Plot (or Normal Quantile Plot):**
    *   Plot the observed data values against the corresponding z-scores (or expected values from a normal distribution).
    *   If the data are approximately normal, the points on the plot will fall close to a straight line.
    *   Systematic deviations from a straight line indicate non-normality (e.g., curvature suggests skewness or heavy tails).

Understanding these methods is crucial for justifying the use of normal distribution-based inference procedures later on.