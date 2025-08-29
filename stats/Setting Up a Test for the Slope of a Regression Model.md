# [[AP Stats Home]]
# Setting Up a Test for the Slope of a Regression Model

When we believe a linear relationship exists between two quantitative variables, we often use a [[Linear Regression Models]] to model this relationship. However, the observed slope from a sample ($\hat{b}$) might just be due to random chance, even if there's no true linear relationship in the population. A hypothesis test for the slope of a regression model allows us to determine if there is statistically significant evidence of a linear relationship between the two variables in the population.

## Purpose of the Test

The primary goal of this test is to assess whether the explanatory variable ($x$) has a statistically significant linear association with the response variable ($y$) in the population. If the true population slope ($\beta$) is zero, it implies that there is no linear relationship between $x$ and $y$.

## Hypotheses

The hypotheses for testing the slope of a regression model are stated in terms of the population regression slope, $\beta$.

*   **Null Hypothesis ($H_0$)**: There is no linear relationship between the explanatory variable ($x$) and the response variable ($y$) in the population.
    $$H_0: \beta = 0$$
    This means that the true slope of the population regression line is zero.
*   **Alternative Hypothesis ($H_a$)**: There is a linear relationship between the explanatory variable ($x$) and the response variable ($y$) in the population. The alternative hypothesis can be one-sided or two-sided, depending on the research question.
    *   Two-sided: The slope is not zero.
        $$H_a: \beta \neq 0$$
    *   One-sided (positive relationship): The slope is greater than zero.
        $$H_a: \beta > 0$$
    *   One-sided (negative relationship): The slope is less than zero.
        $$H_a: \beta < 0$$

## Conditions for Inference

Before carrying out a test for the slope of a regression model, several conditions must be met to ensure the validity of the results. These are often remembered by the acronym **LINER**:

| Condition | Description | How to Check |
| :-------- | :---------- | :----------- |
| **L**inear | The true relationship between $x$ and $y$ is linear. | Examine the [[Representing the Relationship Between Two Quantitative Variables|scatterplot]] of the data for linearity. A [[Residuals|residual plot]] should show no obvious pattern. |
| **I**ndependent | Individual observations are independent of each other. | This is usually ensured by [[Random Sampling and a Collection|random sampling]] or [[Introduction to Experimental Design|random assignment]]. If sampling without replacement, check the $10\%$ condition: sample size $n \le 0.10 \times$ population size. |
| **N**ormal | For any fixed value of $x$, the response $y$ varies normally around the true regression line. | Examine a histogram or normal probability plot of the [[Residuals|residuals]]. It should appear approximately normal. Large sample sizes can sometimes mitigate minor departures due to the [[The Central Limit Theorem|Central Limit Theorem]]. |
| **E**qual Variance | The standard deviation of the response $y$ is the same for all values of $x$. | Examine the [[Residuals|residual plot]]. The spread of the residuals should be roughly constant across all predicted values ($\hat{y}$) or values of $x$. |
| **R**andom | The data come from a well-designed [[Introduction to Planning a Study|random sample]] or [[Introduction to Experimental Design|randomized experiment]]. | State how the data were collected and confirm it was random. |

If these conditions are not reasonably met, the inference procedure for the slope may not be appropriate, and the conclusions drawn could be unreliable.

## Test Statistic

The test statistic for the slope of a regression model is a $t$-statistic. It measures how many standard errors the observed sample slope ($\hat{b}$) is away from the hypothesized population slope (typically 0).

The formula for the test statistic is:

$$t = \frac{\hat{b} - \beta_0}{SE_{\hat{b}}}$$

Where:
*   $\hat{b}$ is the sample slope (estimate of $\beta$).
*   $\beta_0$ is the hypothesized population slope (usually 0 under $H_0$).
*   $SE_{\hat{b}}$ is the standard error of the slope. This value is typically provided in the regression output from statistical software.

The degrees of freedom for this $t$-distribution are $df = n - 2$, where $n$ is the number of observations in the sample.

This test is often referred to as a $t$-test for the slope. Once the test statistic is calculated, it can be used to find the [[Interpreting p-Values|p-value]] to make a decision regarding the null hypothesis, as outlined in [[Carrying Out a Test for the Slope of a Regression Model]].