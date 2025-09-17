# [[AP Stats Home]]
# Introduction to Random Variables and Probability Distributions

This note page introduces the fundamental concepts of random variables and their associated probability distributions, crucial for understanding statistical inference.

## What is a Random Variable?
A **random variable** is a numerical outcome of a random phenomenon. It's a variable whose value is a numerical outcome of a random process. Unlike the variables you might have encountered in algebra, the value of a random variable is not fixed; it depends on the outcome of a chance event.
Random variables are typically denoted by capital letters, such as $X$ or $Y$. The specific values a random variable can take are denoted by lowercase letters, such as $x$ or $y$.

For example, if you flip a coin three times, the number of heads is a random variable. The specific outcomes (HHH, HHT, HTH, THH, HTT, THT, TTH, TTT) are mapped to numerical values (3, 2, 2, 2, 1, 1, 1, 0).

## Types of Random Variables

There are two main types of random variables:

### Discrete Random Variables
A **discrete random variable** is a random variable that can take on a countable number of distinct values. These values are often integers, but not always. They usually result from counting.

**Examples:**
*   The number of heads in 4 coin flips (0, 1, 2, 3, 4)
*   The number of cars passing a certain point in an hour
*   The number of students absent from class

#### Probability Distribution for a Discrete Random Variable
The **probability distribution** of a discrete random variable lists all possible values the variable can take and the probability of each of those values occurring. This is sometimes called a Probability Mass Function (PMF).

**Properties of a Discrete Probability Distribution:**
1.  For any possible value $x_i$, $0 \le P(X=x_i) \le 1$.
2.  The sum of the probabilities for all possible values must equal 1: $\sum P(X=x_i) = 1$.

**Example: Number of Heads in Two Coin Flips**

| $X$ (Number of Heads) | $P(X=x)$ |
| :-------------------- | :------- |
| 0                     | 0.25     |
| 1                     | 0.50     |
| 2                     | 0.25     |
| **Total**             | **1.00** |

We can also calculate probabilities for events involving multiple outcomes, for instance, $P(X \ge 1) = P(X=1) + P(X=2) = 0.50 + 0.25 = 0.75$.

To learn more about the specific characteristics of these distributions, refer to [[Mean and Standard Deviation of Random Variables]] and [[Combining Random Variables]]. Specific types of discrete distributions include [[Introduction to the Binomial Distribution]] and [[The Geometric Distribution]].

### Continuous Random Variables
A **continuous random variable** is a random variable that can take on any value within a given interval. These values usually result from measuring.

**Examples:**
*   The height of a randomly selected student
*   The time it takes to complete a task
*   The amount of rainfall in a month

#### Probability Distribution for a Continuous Random Variable
For a continuous random variable, we cannot list all possible values because there are infinitely many. Instead, we describe its probability distribution using a **probability density curve (or function, PDF)**.

**Properties of a Continuous Probability Distribution:**
1.  The curve is always on or above the horizontal axis.
2.  The total area under the curve is exactly 1.
3.  The probability of the variable falling within any specific range is the area under the curve above that range.
4.  The probability of a continuous random variable taking on any *exact* single value is 0. That is, $P(X=x) = 0$. This implies that $P(X < x) = P(X \le x)$.

**Visualizing Continuous Distributions:**
A common continuous distribution is [[The Normal Distribution]]. Its density curve is bell-shaped and symmetric. Probabilities correspond to areas under this curve.

For an in-depth understanding of how to estimate probabilities using simulations for either type of random variable, refer to [[Estimating Probabilities Using Simulation]]. For foundational probability concepts, see [[Introduction to Probability]].