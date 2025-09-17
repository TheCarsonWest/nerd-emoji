# [[AP Stats Home]]
# Analyzing Departures from Linearity

When we fit a [[Linear Regression Models|linear regression model]] to a set of bivariate data, we assume that the relationship between the two quantitative variables, $x$ (explanatory) and $y$ (response), is linear. However, real-world data doesn't always conform to this assumption. Analyzing departures from linearity is crucial to ensure that our chosen model is appropriate and that our predictions and inferences are valid.

## Why Assess Linearity?

A linear regression model is built on the premise of a linear relationship. If this assumption is violated, the model's predictions may be systematically biased, and interpretations of the slope and intercept can be misleading. It's a key condition to check for the validity of statistical inference based on regression.

## Detecting Departures from Linearity

The primary tool for detecting departures from linearity is the **residual plot**.

### [[Residuals]]

A residual is the difference between the observed value of the response variable and the value predicted by the regression model. It quantifies how much the model "misses" the actual data point.

$$
e = y - \hat{y}
$$

Where:
*   $e$ is the residual
*   $y$ is the observed value of the response variable
*   $\hat{y}$ is the predicted value of the response variable from the regression line

### Residual Plots

A residual plot is a scatterplot of the residuals ($e$) against the explanatory variable ($x$) or the predicted values ($\hat{y}$). It helps visualize the appropriateness of the linear model.

**What to Look For in a Residual Plot:**

| Pattern in Residual Plot       | Implication                                                                                                      |
| :----------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **Random Scatter**             | No obvious pattern, residuals are spread randomly above and below $y=0$. This is ideal.                          |
| **Curved Pattern**             | Indicates a non-linear relationship between $x$ and $y$. A linear model is not appropriate.                      |
| **Fanning Out/In (Heteroscedasticity)** | The spread of residuals changes across the range of $x$. This violates the assumption of constant variance.    |
| **Outliers**                   | Points that lie far away from the bulk of the residuals. These may be influential points or data errors.           |

#### Interpreting Patterns

*   **No Pattern (Random Scatter):** If the residual plot shows a random scatter of points above and below the horizontal line at $y=0$, it suggests that a linear model is a good fit for the data. The residuals show no systematic pattern, meaning the linear model captures the relationship well.

    *Example:*
    ```
    .   .
    .     .
      .   .   .
    ----------------- (y=0)
    .   .   .
      .     .
    .   .
    ```

*   **Curved Pattern:** If the residual plot exhibits a distinct curved pattern (e.g., a "U" shape or an inverted "U" shape), it indicates that the relationship between $x$ and $y$ is non-linear. The linear model is systematically underestimating or overestimating $y$ for certain ranges of $x$. In this case, a transformation of one or both variables, or a non-linear regression model, might be more appropriate.

    *Example of a "U" shape:*
    ```
      .   .
    .         .
    ------------- (y=0)
        .   .
    ```
    *Example of an inverted "U" shape:*
    ```
        .   .
    ------------- (y=0)
    .         .
      .   .
    ```

## Addressing Departures from Linearity

If a residual plot reveals a non-linear pattern, several approaches can be considered:

1.  **[[Transforming Data to Achieve Linearity]]:** This is a common method. Applying a mathematical transformation (e.g., logarithm, square root, reciprocal) to either the explanatory variable ($x$), the response variable ($y$), or both, can sometimes linearize the relationship.
    *   **Concave Up (increasing rate of change):** Try $log(y)$, $\sqrt{y}$, or $1/y$.
    *   **Concave Down (decreasing rate of change):** Try $x^2$, $e^x$, $log(x)$, $\sqrt{x}$.
    *   Choosing the correct transformation often involves trial and error and re-examining residual plots after each transformation.

2.  **Using a Non-Linear Regression Model:** For more complex relationships, a non-linear regression model (e.g., quadratic, exponential, power model) might be directly fitted to the data. This goes beyond the scope of basic AP Statistics, which primarily focuses on linear models.

## Conclusion

Always construct a residual plot when performing [[Least Squares Regression|least-squares regression]]. It is a vital diagnostic tool to verify the appropriateness of a linear model. A random scatter of residuals around zero is the goal, indicating that the linear model adequately describes the relationship between the variables. If a pattern is present, the model may be inappropriate, and further analysis (like data transformation) is needed.