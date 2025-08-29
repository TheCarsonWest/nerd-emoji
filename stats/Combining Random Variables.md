# [[AP Stats Home]]
# Combining Random Variables

Understanding how to combine random variables is crucial for analyzing situations involving multiple sources of variation. This topic builds upon [[Introduction to Random Variables and Probability Distributions]] and [[Mean and Standard Deviation of Random Variables]]. When we combine random variables, we are often interested in the mean and standard deviation of the resulting new random variable.

## Combining Means of Random Variables

The mean (or expected value) of a sum or difference of random variables is straightforward and follows simple arithmetic, regardless of whether the variables are independent or not.

If $X$ and $Y$ are random variables, then:

*   **Sum of Means:** The mean of the sum of two random variables is the sum of their individual means.
    $$E(X+Y) = E(X) + E(Y)$$
*   **Difference of Means:** The mean of the difference of two random variables is the difference of their individual means.
    $$E(X-Y) = E(X) - E(Y)$$

These rules also extend to linear transformations:

*   **Linear Transformation:** For constants $a$ and $b$, the mean of $aX + b$ is:
    $$E(aX + b) = aE(X) + b$$

**Example:** If the average time to complete Task A is $E(A) = 10$ minutes and Task B is $E(B) = 15$ minutes, then the average total time to complete both tasks is $E(A+B) = 10 + 15 = 25$ minutes.

## Combining Variances of Random Variables

Combining variances is slightly more complex than combining means, as it requires the assumption of independence between the random variables.

### [[Independent Random Variables]]

Two random variables are **independent** if the outcome of one does not affect the outcome of the other. This condition is critical for combining variances.

*   **Variance of a Sum (Independent Variables):** If $X$ and $Y$ are independent random variables, the variance of their sum is the sum of their individual variances.
    $$\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$$
*   **Variance of a Difference (Independent Variables):** If $X$ and $Y$ are independent random variables, the variance of their difference is also the sum of their individual variances.
    $$\text{Var}(X-Y) = \text{Var}(X) + \text{Var}(Y)$$
    *Important Note:* Variances *always add* when combining independent random variables, even when taking the difference. This is because variance measures the spread or variability, and combining variables, whether by addition or subtraction, generally increases the overall variability.

*   **Variance of a Linear Transformation:** For constants $a$ and $b$, the variance of $aX + b$ is:
    $$\text{Var}(aX + b) = a^2\text{Var}(X)$$
    Note that adding a constant $b$ does not affect the spread, so it does not change the variance. Multiplying by $a$ multiplies the standard deviation by $|a|$, and thus the variance by $a^2$.

### Combining Standard Deviations

Since standard deviation is the square root of variance, you cannot simply add or subtract standard deviations. You must convert them to variances, combine the variances, and then take the square root to find the new standard deviation.

*   If $X$ and $Y$ are independent random variables, then:
    $$\sigma_{X+Y} = \sqrt{\sigma_X^2 + \sigma_Y^2}$$
    $$\sigma_{X-Y} = \sqrt{\sigma_X^2 + \sigma_Y^2}$$

## Summary Table

Let $X$ and $Y$ be random variables, and $a, b$ be constants.

| Operation       | Mean $E(\cdot)$             | Variance $\text{Var}(\cdot)$ (if $X,Y$ are independent) | Standard Deviation $\sigma(\cdot)$ (if $X,Y$ are independent) |
| :-------------- | :-------------------------- | :------------------------------------------------------- | :---------------------------------------------------------- |
| $X+Y$           | $E(X) + E(Y)$               | $\text{Var}(X) + \text{Var}(Y)$                         | $\sqrt{\sigma_X^2 + \sigma_Y^2}$                            |
| $X-Y$           | $E(X) - E(Y)$               | $\text{Var}(X) + \text{Var}(Y)$                         | $\sqrt{\sigma_X^2 + \sigma_Y^2}$                            |
| $aX+b$          | $aE(X) + b$                 | $a^2\text{Var}(X)$                                       | $|a|\sigma_X$                                                |
| $X_1 + X_2 + \dots + X_n$ (all independent) | $E(X_1) + \dots + E(X_n)$ | $\text{Var}(X_1) + \dots + \text{Var}(X_n)$ | $\sqrt{\text{Var}(X_1) + \dots + \text{Var}(X_n)}$ |

## Shape of the Distribution

If the original random variables $X$ and $Y$ are [[The Normal Distribution|Normally distributed]], then any linear combination of $X$ and $Y$ (e.g., $X+Y$, $X-Y$, $aX+bY$) will also be Normally distributed. This property is very useful for performing inferential procedures later on. If the variables are not Normally distributed, the shape of their sum or difference may become approximately Normal, especially if there are many variables, due to the [[The Central Limit Theorem]].