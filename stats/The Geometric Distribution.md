# [[AP Stats Home]]
# The Geometric Distribution

The geometric distribution is a discrete probability distribution that models the number of trials needed to achieve the *first* success in a sequence of [[Independent Events and Unions of Events|independent]] Bernoulli trials. Unlike the [[Introduction to the Binomial Distribution|Binomial Distribution]] which counts the number of successes in a fixed number of trials, the geometric distribution focuses on the waiting time for that very first success.

## Conditions for a Geometric Setting (BITS)

For a random variable $X$ to follow a geometric distribution, the following conditions must be met:

*   **B**inary: Each trial has only two possible outcomes: "success" or "failure."
*   **I**ndependent: The outcomes of each trial are independent of each other.
*   **T**rials: We are counting the number of trials until the **first** success occurs.
*   **S**uccess: The probability of success ($p$) remains the same for each trial.

If these conditions are met, $X$ is a geometric random variable, denoted as $X \sim \text{Geom}(p)$.

## Probability Mass Function (PMF)

The probability that the first success occurs on the $k$-th trial is given by:

$$P(X = k) = (1 - p)^{k-1} p$$

where:
*   $k$ is the number of the trial on which the first success occurs ($k = 1, 2, 3, \ldots$).
*   $p$ is the probability of success on any given trial.
*   $(1-p)$ is the probability of failure on any given trial.
*   $(1-p)^{k-1}$ represents $k-1$ consecutive failures before the first success.

**Example:**
Suppose the probability of hitting a target is $p=0.2$. What is the probability that the first hit occurs on the 4th shot?
$P(X=4) = (1-0.2)^{4-1} (0.2) = (0.8)^3 (0.2) = 0.512 \times 0.2 = 0.1024$.

## Mean (Expected Value) of a Geometric Distribution

The mean or expected number of trials until the first success is:

$$E(X) = \mu_X = \frac{1}{p}$$

This makes intuitive sense: if the probability of success is $p=0.25$, you'd expect to wait $1/0.25 = 4$ trials on average to get a success.

## Standard Deviation of a Geometric Distribution

The standard deviation of a geometric distribution is:

$$\sigma_X = \sqrt{\frac{1-p}{p^2}}$$

## Cumulative Probability

We are often interested in the probability that the first success occurs *on or before* a certain trial, or *after* a certain trial.

*   **Probability of first success on or before the $k$-th trial:**
    $P(X \le k) = P(X=1) + P(X=2) + \dots + P(X=k)$
    This can also be calculated as:
    $$P(X \le k) = 1 - P(X > k) = 1 - (1-p)^k$$
    This is because $P(X > k)$ means the first $k$ trials were all failures.

*   **Probability of first success after the $k$-th trial:**
    $$P(X > k) = (1-p)^k$$
    This means the first $k$ trials were all failures.

## Comparing Geometric vs. Binomial

It's crucial to distinguish between geometric and binomial distributions.

| Feature         | [[Introduction to the Binomial Distribution|Binomial Distribution]] | The Geometric Distribution |
| :-------------- | :------------------------------------ | :----------------------- |
| **Random Variable** | Number of successes in a fixed number of trials ($n$) | Number of trials until the first success |
| **Number of Trials** | Fixed ($n$)                           | Variable (can be infinite) |
| **Question Type** | "How many successes in $n$ trials?"    | "How many trials until the first success?" |
| **Probability Function** | $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$ | $P(X=k) = (1-p)^{k-1} p$ |

## Calculator Functions (TI-84)

For calculations, your graphing calculator has built-in functions:

*   **`geometpdf(p, k)`**: Calculates $P(X=k)$ (probability of first success on the $k$-th trial).
*   **`geometcdf(p, k)`**: Calculates $P(X \le k)$ (probability of first success on or before the $k$-th trial).

## [[Expected Counts in Two-Way Tables|Example Application]]

Imagine you are a basketball player with a 30% free throw percentage ($p=0.3$).

1.  **What is the probability that your first successful free throw occurs on your 3rd attempt?**
    This is $P(X=3)$.
    $P(X=3) = (1-0.3)^{3-1} (0.3) = (0.7)^2 (0.3) = 0.49 \times 0.3 = 0.147$.
    Using calculator: `geometpdf(0.3, 3) = 0.147`.

2.  **What is the expected number of free throws you will take until your first success?**
    $E(X) = \frac{1}{p} = \frac{1}{0.3} \approx 3.33$ attempts.

3.  **What is the probability that it takes you more than 5 attempts to make your first free throw?**
    This is $P(X > 5)$.
    $P(X > 5) = (1-0.3)^5 = (0.7)^5 = 0.16807$.

4.  **What is the probability that your first success occurs on or before your 4th attempt?**
    This is $P(X \le 4)$.
    $P(X \le 4) = 1 - (1-0.3)^4 = 1 - (0.7)^4 = 1 - 0.2401 = 0.7599$.
    Using calculator: `geometcdf(0.3, 4) = 0.7599`.