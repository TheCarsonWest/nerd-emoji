# [[AP Stats Home]]
# Residuals

Residuals are fundamental to understanding the accuracy and appropriateness of a [[Linear Regression Models]] when fitting data. They represent the "leftover" variation in the dependent variable after accounting for the linear relationship with the independent variable.

## Definition and Purpose

A **residual** is the difference between an observed value of the response variable ($y$) and the value predicted by the regression model ($\hat{y}$). In essence, it tells us how far off our prediction was for a specific data point.

*   **Observed Value ($y$)**: The actual value from the dataset.
*   **Predicted Value ($\hat{y}$)**: The value estimated by the [[Least Squares Regression]] line for a given x-value.

The primary purpose of residuals is to help us assess how well a regression model fits the data and to identify any patterns or issues that the linear model might not be capturing.

## Calculating Residuals

The formula for a residual ($e$) is straightforward:

$$
e = y - \hat{y}
$$

Where:
*   $e$ is the residual
*   $y$ is the observed value of the response variable
*   $\hat{y}$ is the predicted value of the response variable from the regression line.

**Example:**
If the actual weight of a dog is 25 kg, and our regression model predicts 22 kg for a dog of that size, the residual would be $e = 25 - 22 = 3$ kg. A positive residual means the model *underpredicted* the actual value, while a negative residual means the model *overpredicted* it.

## Residual Plots

A [[Residuals]] plot (or residual plot) is a scatterplot of the residuals against the explanatory variable (x) or the predicted values ($\hat{y}$). These plots are crucial for assessing the appropriateness of a linear model.

### How to Construct a Residual Plot

1.  Calculate the residuals for each data point using the formula $e = y - \hat{y}$.
2.  Plot the residuals ($e$) on the y-axis against the corresponding explanatory variable ($x$) or predicted value ($\hat{y}$) on the x-axis. A horizontal line at $y=0$ is usually added to the plot.

### Interpreting Residual Plots

When examining a residual plot, we look for two main characteristics:

1.  **No Obvious Pattern**:
    *   **Good Fit (Random Scatter)**: If the points in the residual plot are randomly scattered around the horizontal line at 0 with no discernible pattern, it suggests that a linear model is appropriate for the data. This indicates that the linear model has captured most of the systematic relationship between the variables.
    *   **Bad Fit (Presence of a Pattern)**: If there is a clear pattern (e.g., a curved shape, fanning out, or clustering) in the residual plot, it indicates that the linear model is not the best fit for the data. This means a nonlinear relationship might exist, or other variables might be influencing the relationship. [[Analyzing Departures from Linearity]] often involves examining residual plots for patterns.

    | Pattern Type       | Implication for Linear Model                                   |
    | :----------------- | :------------------------------------------------------------- |
    | Random Scatter     | Linear model is appropriate.                                   |
    | Curved Pattern     | A non-linear model might be more appropriate.                  |
    | "Cone" Shape       | Variability in residuals changes with x; assumptions violated. |
    | Horizontal Bands   | May indicate categorical explanatory variable or other issues. |

2.  **Constant Variability (Homoscedasticity)**:
    *   **Consistent Spread**: The spread of the residuals should be roughly the same across all values of $x$ (or $\hat{y}$). This is known as **homoscedasticity**.
    *   **Varying Spread (Heteroscedasticity)**: If the spread of the residuals increases or decreases as $x$ (or $\hat{y}$) increases (often appearing as a "cone" or "fan" shape), this indicates **heteroscedasticity**. This violates an important assumption of linear regression and suggests that the precision of our predictions varies across the range of the explanatory variable.

## Properties of Residuals in Least Squares Regression

For a [[Least Squares Regression]] line:

*   The sum of the residuals is always zero: $\sum e_i = \sum (y_i - \hat{y}_i) = 0$.
*   The mean of the residuals is also zero.

These properties are a direct consequence of how the least squares line is determined, minimizing the sum of squared residuals.