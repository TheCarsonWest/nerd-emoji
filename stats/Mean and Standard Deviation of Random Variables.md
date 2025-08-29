# [[AP Stats Home]]
# Mean and Standard Deviation of Random Variables

This note page expands on the concepts introduced in [[Introduction to Random Variables and Probability Distributions]], focusing specifically on quantifying the center and spread of a random variable's distribution.

## Expected Value (Mean) of a Discrete Random Variable

The **expected value** or **mean** of a discrete random variable $X$, denoted as $E(X)$ or $\mu_X$, represents the long-run average value of the variable over many repetitions of the random process. It is a measure of the center of the probability distribution.

To calculate the expected value of a discrete random variable, you multiply each possible value of the variable by its corresponding probability and then sum these products.

$$
\mu_X = E(X) = \sum x_i p_i
$$

Where:
*   $x_i$ are the individual values the random variable $X$ can take.
*   $p_i$ are the probabilities associated with each $x_i$.

### Example: Expected Value
Consider a game where you roll a fair six-sided die. If you roll a 6, you win \$5. If you roll a 1 or 2, you lose \$2. Otherwise, you neither win nor lose. Let $X$ be the amount of money you win/lose.

| $x_i$ (Outcome) | $p_i$ (Probability) |
| :-------------- | :------------------ |
| \$5             | $1/6$               |
| -\$2            | $2/6$               |
| \$0             | $3/6$               |

The expected value is:
$$
E(X) = (5 \times \frac{1}{6}) + (-2 \times \frac{2}{6}) + (0 \times \frac{3}{6}) \\
E(X) = \frac{5}{6} - \frac{4}{6} + 0 = \frac{1}{6} \approx \$0.17
$$
On average, you can expect to win about \$0.17 per game in the long run.

## Standard Deviation of a Discrete Random Variable

The **standard deviation** of a random variable, denoted as $\sigma_X$, measures the typical distance of the values of the variable from the mean. It quantifies the spread or variability of the distribution. A larger standard deviation indicates greater spread.

Before calculating the standard deviation, we first find the **variance**, denoted as $Var(X)$ or $\sigma_X^2$. The variance is the expected value of the squared deviations from the mean.

$$
\sigma_X^2 = Var(X) = \sum (x_i - \mu_X)^2 p_i
$$

The standard deviation is simply the square root of the variance:

$$
\sigma_X = \sqrt{\sum (x_i - \mu_X)^2 p_i}
$$

### Example: Standard Deviation
Using the previous die roll example, where $\mu_X = 1/6$:

| $x_i$ | $p_i$ | $(x_i - \mu_X)$ | $(x_i - \mu_X)^2$ | $(x_i - \mu_X)^2 p_i$ |
| :---- | :---- | :-------------- | :---------------- | :-------------------- |
| \$5   | $1/6$ | $5 - 1/6 = 29/6$ | $(29/6)^2 = 841/36$ | $(841/36) \times 1/6 = 841/216$ |
| -\$2  | $2/6$ | $-2 - 1/6 = -13/6$ | $(-13/6)^2 = 169/36$ | $(169/36) \times 2/6 = 338/216$ |
| \$0   | $3/6$ | $0 - 1/6 = -1/6$ | $(-1/6)^2 = 1/36$ | $(1/36) \times 3/6 = 3/216$ |

Summing the last column gives the variance:
$$
Var(X) = \frac{841}{216} + \frac{338}{216} + \frac{3}{216} = \frac{1182}{216} \approx 5.472
$$
The standard deviation is:
$$
\sigma_X = \sqrt{\frac{1182}{216}} \approx \sqrt{5.472} \approx \$2.34
$$
This means that, on average, the amount won or lost per game typically varies by about \$2.34 from the expected win of \$0.17.

## [[Combining Random Variables]]
When dealing with multiple random variables, we often need to understand the mean and standard deviation of their sum or difference. This topic, known as [[Combining Random Variables]], covers rules for linear transformations of random variables ($Y = a + bX$) and for combining independent random variables (e.g., $W = X + Y$ or $D = X - Y$). Key principles include:
*   **Mean**: Means are additive for both sums and differences ($E(X \pm Y) = E(X) \pm E(Y)$).
*   **Variance**: Variances are additive for the sum or difference of *independent* random variables ($Var(X \pm Y) = Var(X) + Var(Y)$). Note that standard deviations are not directly additive.
*   **Independence**: The rule for adding variances only applies if the random variables are independent. If they are not independent, additional considerations related to covariance are needed.