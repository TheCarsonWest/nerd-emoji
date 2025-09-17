# [[AP Stats Home]]
# Linear Regression Models

Linear regression models are a fundamental tool in AP Statistics used to describe the relationship between two quantitative variables when a scatterplot suggests a linear association. The primary goal is to predict the value of one variable (the response variable) from the value of another (the explanatory variable). This topic builds upon understanding [[Representing the Relationship Between Two Quantitative Variables]] and [[Correlation]].

## The Least-Squares Regression Line (LSRL)

The most common method for fitting a line to a set of data is the **Least-Squares Regression Line (LSRL)**. This line minimizes the sum of the squared vertical distances (residuals) between the observed data points and the line itself. The equation of the LSRL is:

$$ \hat{y} = a + bx $$

Where:
*   $\hat{y}$ (read as "y-hat") is the predicted value of the response variable for a given $x$.
*   $a$ is the **y-intercept**, the predicted value of $y$ when $x=0$.
*   $b$ is the **slope**, which represents the predicted change in $y$ for every one-unit increase in $x$.
*   $x$ is the value of the explanatory variable.

For a deeper dive into its calculation, refer to [[Least Squares Regression]].

### Interpreting Slope and Y-intercept

Interpreting the slope and y-intercept in context is crucial:

*   **Slope ($b$):** For every one-unit increase in the explanatory variable ($x$), the response variable ($y$) is predicted to change by $b$ units, on average.
*   **Y-intercept ($a$):** When the explanatory variable ($x$) is 0, the predicted value of the response variable ($y$) is $a$. (Be cautious: sometimes $x=0$ is not a meaningful value in context).

### Formulas for Slope and Y-intercept

The slope ($b$) and y-intercept ($a$) can be calculated using the following formulas:

$$ b = r \frac{s_y}{s_x} $$
$$ a = \bar{y} - b\bar{x} $$

Where:
*   $r$ is the [[Correlation]] coefficient between $x$ and $y$.
*   $s_y$ is the standard deviation of the response variable $y$.
*   $s_x$ is the standard deviation of the explanatory variable $x$.
*   $\bar{y}$ is the mean of the response variable $y$.
*   $\bar{x}$ is the mean of the explanatory variable $x$.

## Residuals

[[Residuals]] are the differences between the observed values of the response variable and the values predicted by the regression line. They represent the "error" in the prediction for each data point.

$$ \text{Residual} = \text{Observed } y - \text{Predicted } y = y - \hat{y} $$

A **residual plot** is a scatterplot of the residuals against the explanatory variable (or predicted values $\hat{y}$). A good linear model will show no obvious pattern in the residual plot (a random scatter around zero). Patterns in a residual plot indicate that a linear model might not be appropriate, suggesting [[Analyzing Departures from Linearity]].

## Coefficient of Determination ($R^2$)

The **coefficient of determination**, denoted as $R^2$, is a measure that tells us how well the regression line fits the data. It is the square of the correlation coefficient ($r$).

$$ R^2 = r^2 $$

### Interpretation of $R^2$

$R^2$ represents the proportion (or percentage, if multiplied by 100) of the variation in the response variable ($y$) that can be explained by the linear relationship with the explanatory variable ($x$). A higher $R^2$ indicates that the model explains more of the variability in the response variable.

**Example:** If $R^2 = 0.75$, it means that 75% of the variation in $y$ can be explained by the linear relationship with $x$. The remaining 25% of the variation is due to other factors or random chance.

## Standard Deviation of the Residuals ($s_e$ or $s$)

The standard deviation of the residuals, often denoted as $s$ or $s_e$, measures the typical distance between the observed $y$ values and the predicted $\hat{y}$ values (the typical size of a residual).

$$ s = \sqrt{\frac{\sum(y_i - \hat{y}_i)^2}{n-2}} $$

Where $n$ is the number of data points.

### Interpretation of $s$

$s$ estimates the standard deviation of the errors (residuals) and tells us the typical prediction error using the LSRL. A smaller value of $s$ indicates that the observed $y$ values generally fall closer to the regression line, meaning the model makes more precise predictions.

## Extrapolation

[[Extrapolation]] is the use of a regression line to predict values of the response variable ($y$) for values of the explanatory variable ($x$) that are outside the range of the observed data. This is generally not recommended because the linear relationship observed within the data range may not continue outside that range. The further you extrapolate, the less reliable your prediction becomes.

## Outliers and Influential Points

Points that lie far from the overall pattern of the data are considered [[Outliers and Influential Points]]. An **outlier** in regression is a point that has a large residual (far from the line in the y-direction). An **influential point** is an outlier in the x-direction that, if removed, would significantly change the slope or y-intercept of the regression line. It's important to identify and assess the impact of such points.