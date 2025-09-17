# [[AP Stats Home]]
# Confidence Intervals for the Slope of a Regression Model

When we fit a [[Linear Regression Models]] to a sample of data, we obtain a sample regression line with a slope, $\hat{b}$. This sample slope is a point estimate for the true, unknown slope $\beta$ of the population regression line. A confidence interval for $\beta$ provides a range of plausible values for the true slope, allowing us to make inferences about the relationship between two quantitative variables in the population.

## Purpose

The primary purpose of constructing a confidence interval for the slope of a regression model is to estimate the true slope $\beta$ of the population regression line with a certain level of confidence. This helps us understand how the dependent variable ($y$) changes, on average, for each unit increase in the independent variable ($x$), across the entire population.

## Formula

The general formula for a confidence interval for the slope of a regression line is:

$$
\hat{b} \pm t^* \cdot SE_{\hat{b}}
$$

Where:
*   $\hat{b}$ is the sample slope (our point estimate for $\beta$).
*   $t^*$ is the critical $t$-value for the desired confidence level and degrees of freedom.
*   $SE_{\hat{b}}$ is the standard error of the slope.

## Conditions for Inference

Before constructing a confidence interval, certain conditions must be met to ensure the validity of the inference. These are often remembered by the acronym **LINER**:

| Condition | Description | How to Check |
| :-------- | :---------- | :----------- |
| **L**inear | The true relationship between $x$ and $y$ is linear. | Examine a scatterplot of the data for linearity. A [[Residuals]] plot should show no obvious pattern. |
| **I**ndependent | Individual observations are independent of each other. | Check the experimental design. If sampling without replacement, the population size should be at least 10 times the sample size ($N \ge 10n$). |
| **N**ormal | For any fixed value of $x$, the response $y$ varies according to a Normal distribution around the true regression line. | Examine a histogram or Normal probability plot of the [[Residuals]] to check for approximate normality and absence of strong skewness or outliers. |
| **E**qual Standard Deviation (Equal Variance) | The standard deviation of $y$ about the true regression line is the same for all values of $x$. | Examine the [[Residuals]] plot for a consistent spread of points around the residual = 0 line (no fanning out or in). |
| **R**andom | The data come from a well-designed random sample or randomized experiment. | State how the data were collected. |

## Degrees of Freedom

The degrees of freedom (df) for inference about the slope of a regression line are given by:

$$
df = n - 2
$$

where $n$ is the number of data points (observations). We subtract 2 because we are estimating two parameters from the data: the slope ($\beta$) and the y-intercept ($\alpha$).

## Standard Error of the Slope ($SE_{\hat{b}}$)

The standard error of the slope, $SE_{\hat{b}}$, measures the typical distance between the sample slopes ($\hat{b}$) from repeated samples and the true population slope ($\beta$). It quantifies the variability of the sample slope.

The formula for $SE_{\hat{b}}$ is:

$$
SE_{\hat{b}} = \frac{s_e}{\sqrt{(n-1)s_x^2}} = \frac{s_e}{s_x\sqrt{n-1}}
$$

Where:
*   $s_e$ is the standard deviation of the residuals (also known as the residual standard error), which estimates the common standard deviation $\sigma$ of the responses about the true regression line.
*   $s_x$ is the standard deviation of the independent variable $x$.
*   $n$ is the sample size.

Often, $SE_{\hat{b}}$ is provided directly in computer output for regression analysis.

## Interpretation

A confidence interval for the slope $\beta$ can be interpreted as follows:

"We are [Confidence Level]% confident that the interval from [Lower Bound] to [Upper Bound] captures the true slope of the population regression line relating [explanatory variable] to [response variable]."

For example, a 95% confidence interval of (0.8, 1.2) for the slope might be interpreted as: "We are 95% confident that for every one-unit increase in [explanatory variable], the [response variable] increases by an average of between 0.8 and 1.2 units."

## Relationship to Hypothesis Testing

A confidence interval for the slope is closely related to a [[Setting Up a Test for the Slope of a Regression Model]] for the slope. If a confidence interval for $\beta$ does *not* contain a hypothesized value (e.g., 0 for a test of no linear relationship), then we would reject the null hypothesis at the corresponding significance level. Conversely, if it *does* contain the hypothesized value, we would fail to reject the null hypothesis. This concept is explored further in [[Justifying a Claim About the Slope of a Regression Model Based on a Confidence Interval]].