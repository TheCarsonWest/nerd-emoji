# [[AP Stats Home]]
# Least Squares Regression

## Introduction to Least Squares Regression

When analyzing the relationship between two [[Representing the Relationship Between Two Quantitative Variables|quantitative variables]], a [[Linear Regression Models|linear regression model]] aims to describe this relationship with a straight line. The **Least Squares Regression Line (LSRL)** is the specific line that best fits the data by minimizing the sum of the squared vertical distances (residuals) from each data point to the line. This method provides the most commonly used linear model for prediction.

The primary goal of least squares regression is to make predictions about a response variable ($y$) based on an explanatory variable ($x$).

## The Least Squares Regression Line (LSRL)

The equation of the Least Squares Regression Line is given by:
$$\hat{y} = a + bx$$
Where:
*   $\hat{y}$ (read as "y-hat") is the predicted value of the response variable for a given $x$.
*   $a$ is the y-intercept, the predicted value of $y$ when $x=0$.
*   $b$ is the slope, the predicted change in $y$ for every one-unit increase in $x$.

### How the LSRL is Determined

The "least squares" part refers to the mathematical criterion used to find this "best-fit" line. The LSRL is the unique line that minimizes the **Sum of Squared Residuals (SSR)**.

$$SSR = \sum(y_i - \hat{y}_i)^2$$
Where $y_i$ is the observed value of the response variable and $\hat{y}_i$ is the predicted value from the regression line for the $i$-th data point. This minimization process makes the LSRL sensitive to extreme values or [[Analyzing Departures from Linearity|outliers]].

### Formulas for Slope and Y-intercept

The slope ($b$) and y-intercept ($a$) of the LSRL can be calculated using the following formulas:

$$b = r \frac{s_y}{s_x}$$
$$a = \bar{y} - b\bar{x}$$

Where:
*   $r$ is the [[Correlation|correlation coefficient]] between $x$ and $y$.
*   $s_y$ is the standard deviation of the response variable $y$.
*   $s_x$ is the standard deviation of the explanatory variable $x$.
*   $\bar{y}$ is the mean of the response variable $y$.
*   $\bar{x}$ is the mean of the explanatory variable $x$.

### Properties of the LSRL

1.  **Passes Through the Means**: The LSRL always passes through the point $(\bar{x}, \bar{y})$. This means if you substitute $\bar{x}$ into the equation, you will get $\bar{y}$ as the predicted value.
2.  **Role of Correlation**: The square of the [[Correlation|correlation coefficient]], $r^2$, known as the **[[Coefficient of Determination ($r^2$)]]**, provides the proportion of the variation in the response variable ($y$) that is explained by the linear relationship with the explanatory variable ($x$).
3.  **Interpolation vs. Extrapolation**: Using the LSRL to make predictions within the range of the observed $x$ values (interpolation) is generally reliable. Making predictions outside this range (extrapolation) is risky and may not be accurate, as the linear relationship may not hold.

## Key Terminology

| Term               | Symbol     | Description                                                                                             |
| :----------------- | :--------- | :------------------------------------------------------------------------------------------------------ |
| Observed Response  | $y$        | The actual value of the response variable for a given data point.                                       |
| Predicted Response | $\hat{y}$  | The value of the response variable predicted by the LSRL for a given $x$.                               |
| Residual           | $e = y-\hat{y}$ | The difference between an observed value and its predicted value ([[Residuals|Residuals]]). |
| Slope              | $b$        | Predicted change in $y$ for a one-unit increase in $x$.                                                 |
| Y-intercept        | $a$        | Predicted value of $y$ when $x=0$. Often not interpretable in context.                                  |
| Correlation        | $r$        | Measures the strength and direction of the linear relationship between $x$ and $y$.                     |
| Coefficient of Determination | $r^2$      | Proportion of the variation in $y$ that is explained by the linear relationship with $x$.               |

## Cautions and Considerations

*   **Outliers and Influential Points**: The LSRL is sensitive to [[Analyzing Departures from Linearity|outliers]], especially those that are extreme in the x-direction. Such points can significantly affect the slope and y-intercept.
*   **Correlation is Not Causation**: Even a strong linear relationship does not imply that changes in $x$ cause changes in $y$. There might be [[Lurking and Confounding Variables|lurking variables]] or other factors at play.
*   **Linearity**: Always inspect a [[Scatterplot]] to confirm that a linear model is appropriate for the data before applying least squares regression. [[Residual plots]] are also crucial for checking the appropriateness of the linear model.