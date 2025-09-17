# [[AP Stats Home]]
# Introduction to the Binomial Distribution

The binomial distribution is a discrete probability distribution that models the number of successes in a fixed number of independent trials, each with only two possible outcomes (success or failure), and where the probability of success is constant for each trial. It is a fundamental concept in statistics, often used to analyze situations where we're counting "hits" or "misses" in a series of identical opportunities.

## Binomial Setting (BINS)

For a random variable $X$ to follow a binomial distribution, four specific conditions must be met. These are often remembered by the acronym **BINS**:

| Condition       | Description                                                                                                                                                                                                                                                                                                                                                     |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **B**inary      | Each trial must have only two possible outcomes, typically labeled "success" or "failure." For example, flipping a coin (heads/tails), a product being defective or not, or a patient recovering or not.                                                                                                                                                             |
| **I**ndependent | The outcome of one trial must not influence the outcome of any other trial. This means that the trials are independent. If sampling without replacement, the sample size should be less than 10% of the population size to ensure approximate independence ([[Random Sampling and a Collection]] and [[Potential Problems with Sampling]]).                         |
| **N**umber      | The number of trials, denoted by $n$, must be fixed in advance. You know exactly how many times the experiment will be repeated. For instance, flipping a coin 10 times, or inspecting 50 items from a production line. This distinguishes it from the [[The Geometric Distribution]], where the number of trials is not fixed.                                     |
| **S**uccess     | The probability of success, denoted by $p$, must be the same for each trial. This probability remains constant throughout the entire series of $n$ trials. The probability of failure, $q$, is then $1-p$.                                                                                                                                                         |

## Notation

If a random variable $X$ follows a binomial distribution, we denote it as $X \sim B(n, p)$, where:
*   $n$ is the fixed number of trials.
*   $p$ is the probability of success on any given trial.

$X$ represents the count of successes in $n$ trials. Possible values for $X$ are $0, 1, 2, \dots, n$. This makes $X$ a [[Introduction to Random Variables and Probability Distributions|discrete random variable]].

## Binomial Probability Formula (PMF)

The probability of obtaining exactly $k$ successes in $n$ trials for a binomial distribution is given by the following formula:

$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$

Where:
*   $P(X=k)$ is the probability of getting exactly $k$ successes.
*   $\binom{n}{k}$ is the binomial coefficient, read as "n choose k," which represents the number of ways to choose $k$ successes from $n$ trials. It is calculated as:
    $$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$
    where $!$ denotes the factorial (e.g., $5! = 5 \times 4 \times 3 \times 2 \times 1$).
*   $p^k$ is the probability of getting $k$ successes.
*   $(1-p)^{n-k}$ is the probability of getting $n-k$ failures.

## Example

Suppose a fair coin is tossed 5 times. What is the probability of getting exactly 3 heads?

1.  **BINS Check:**
    *   **B**inary: Yes, Heads or Tails.
    *   **I**ndependent: Yes, each toss is independent.
    *   **N**umber: Yes, $n=5$ (fixed number of trials).
    *   **S**uccess: Yes, $p=0.5$ for heads on each toss.
2.  **Parameters:** $X \sim B(n=5, p=0.5)$, and we want to find $P(X=3)$.
3.  **Calculation:**
    *   $\binom{5}{3} = \frac{5!}{3!(5-3)!} = \frac{5!}{3!2!} = \frac{5 \times 4}{2 \times 1} = 10$
    *   $P(X=3) = \binom{5}{3} (0.5)^3 (1-0.5)^{5-3}$
    *   $P(X=3) = 10 \times (0.5)^3 \times (0.5)^2$
    *   $P(X=3) = 10 \times 0.125 \times 0.25 = 0.3125$

So, the probability of getting exactly 3 heads in 5 tosses is 0.3125.

For a deeper dive into the properties, including the mean and standard deviation of a binomial distribution, refer to [[Parameters for a Binomial Distribution]].