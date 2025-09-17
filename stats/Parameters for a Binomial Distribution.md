# [[AP Stats Home]]
# Parameters for a Binomial Distribution

Understanding the parameters for a binomial distribution is crucial for correctly applying and interpreting binomial probability models. A [[Introduction to the Binomial Distribution]] arises when we are interested in the number of "successes" in a fixed number of independent trials, where each trial has only two possible outcomes.

## The Binomial Setting (BINS)

Before defining the parameters, let's quickly review the conditions that must be met for a random variable to follow a binomial distribution. These are often remembered by the acronym **BINS**:

*   **B**inary: Each trial has only two possible outcomes, usually labeled "success" and "failure."
*   **I**ndependent: The outcome of one trial does not affect the outcome of any other trial.
*   **N**umber: The number of trials, $n$, is fixed in advance.
*   **S**uccess: The probability of success, $p$, is the same for each trial.

Once these conditions are met, we can define the two fundamental parameters that completely characterize a specific binomial distribution.

## The Parameters

The two parameters of a binomial distribution are the number of trials ($n$) and the probability of success on any single trial ($p$).

### Number of Trials ($n$)

*   **Definition**: The number of independent observations or repetitions of the process. This value is fixed *before* the experiment begins.
*   **Characteristics**:
    *   Must be a positive integer.
    *   Represents the total count of opportunities for success or failure.
*   **Example**: If you flip a coin 10 times, $n = 10$. If you ask 50 randomly selected students if they prefer online or in-person classes, $n = 50$.

### Probability of Success ($p$)

*   **Definition**: The likelihood of observing a "success" on any single, independent trial.
*   **Characteristics**:
    *   Must be a value between 0 and 1, inclusive ($0 \le p \le 1$).
    *   It is assumed to be constant for every trial.
*   **Example**: If the coin is fair, $p = 0.5$ for getting a head (success). If 70% of students prefer online classes, then $p = 0.7$ for a randomly selected student preferring online classes.

### Probability of Failure ($q$)

While not an independent parameter, the probability of failure ($q$) is directly derived from $p$.
*   **Definition**: The likelihood of observing a "failure" on any single, independent trial.
*   **Formula**:
    $$q = 1 - p$$
*   **Example**: If $p = 0.7$, then $q = 1 - 0.7 = 0.3$.

## Notation

A random variable $X$ that follows a binomial distribution with $n$ trials and probability of success $p$ is denoted as:

$$X \sim B(n, p)$$

This notation concisely tells us that $X$ is a binomial random variable, along with its specific parameters.

## Mean and Standard Deviation of a Binomial Distribution

Once $n$ and $p$ are known, we can easily calculate the mean (expected number of successes) and the standard deviation (variability of successes) for the binomial distribution. These are specific formulas for binomial distributions, distinct from the general formulas for [[Mean and Standard Deviation of Random Variables]].

| Statistic         | Formula                                 | Description                                 |
| :---------------- | :-------------------------------------- | :------------------------------------------ |
| Mean ($E[X]$ or $\mu_X$) | $$\mu_X = np$$                       | Expected number of successes in $n$ trials. |
| Variance ($\sigma_X^2$) | $$\sigma_X^2 = np(1-p) = npq$$       | Measures the spread of the distribution.    |
| Standard Deviation ($\sigma_X$) | $$\sigma_X = \sqrt{np(1-p)} = \sqrt{npq}$$ | Standard variability from the mean.         |

**Example**: For $X \sim B(10, 0.5)$:
*   Mean: $\mu_X = 10 \times 0.5 = 5$
*   Standard Deviation: $\sigma_X = \sqrt{10 \times 0.5 \times 0.5} = \sqrt{2.5} \approx 1.58$

These parameters ($n$ and $p$) are fundamental for calculating binomial probabilities, understanding the shape of the distribution, and making inferences about population proportions. They are directly used in the binomial probability formula and form the basis for approximating binomial distributions with a [[The Normal Distribution, Revisited]] under certain conditions.