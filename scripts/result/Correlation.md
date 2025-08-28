# [[AP Stats Home]]
# Correlation

Correlation is a statistical measure that quantifies the **strength** and **direction** of the **linear relationship** between two [[Quantitative Variable]]. It's a key component in understanding how two variables move together. Before delving into correlation, it's essential to visualize the relationship between two quantitative variables using a [[Representing the Relationship Between Two Quantitative Variables|scatterplot]].

## The Correlation Coefficient ($r$)

The most common measure of correlation is the Pearson product-moment correlation coefficient, denoted by $r$.

### Formula for $r$

The correlation coefficient $r$ for a set of $n$ paired observations $(x_i, y_i)$ is calculated as:

$$
r = \frac{1}{n-1} \sum_{i=1}^{n} \left(\frac{x_i - \bar{x}}{s_x}\right) \left(\frac{y_i - \bar{y}}{s_y}\right)
$$

Where:
*   $n$ is the number of data points.
*   $x_i$ and $y_i$ are individual data points.
*   $\bar{x}$ and $\bar{y}$ are the means of the $x$ and $y$ variables, respectively.
*   $s_x$ and $s_y$ are the standard deviations of the $x$ and $y$ variables, respectively.
*   The terms $\left(\frac{x_i - \bar{x}}{s_x}\right)$ and $\left(\frac{y_i - \bar{y}}{s_y}\right)$ are the standardized scores (z-scores) for each observation. This formula essentially averages the product of the z-scores for $x$ and $y$.

### Properties of $r$

Understanding the properties of the correlation coefficient is crucial for correct interpretation:

*   **Range:** $r$ always falls between -1 and 1, inclusive ($-1 \le r \le 1$).
    *   $r = 1$: Perfect positive linear relationship.
    *   $r = -1$: Perfect negative linear relationship.
    *   $r = 0$: No linear relationship (variables may still have a non-linear relationship).
*   **Direction:** The sign of $r$ indicates the direction of the linear relationship.
    *   Positive $r$ (e.g., $r = 0.75$): As one variable increases, the other tends to increase.
    *   Negative $r$ (e.g., $r = -0.60$): As one variable increases, the other tends to decrease.
*   **Strength:** The absolute value of $r$ indicates the strength of the linear relationship. Values closer to 1 or -1 indicate stronger linear relationships. Values closer to 0 indicate weaker linear relationships.
    *   Generally, absolute values above 0.7 are considered strong, between 0.3 and 0.7 moderate, and below 0.3 weak. These are guidelines, not strict rules.
*   **Units:** $r$ is a unitless measure. It's not affected by changes in the units of measurement for $x$ or $y$. For example, converting height from inches to centimeters won't change $r$.
*   **Symmetry:** The correlation between $x$ and $y$ is the same as the correlation between $y$ and $x$. $r_{xy} = r_{yx}$.
*   **Sensitivity to Outliers:** The correlation coefficient is **not resistant** to outliers. Outliers can significantly affect the value of $r$, potentially making a weak correlation appear strong, or vice versa. Always inspect a [[Representing the Relationship Between Two Quantitative Variables|scatterplot]] for outliers.
*   **Linearity:** $r$ only measures the strength of a *linear* relationship. A strong non-linear relationship (e.g., a curve) might have an $r$ value close to 0, which would incorrectly suggest no relationship if not observed on a scatterplot.

### Interpreting $r$ Values

Here's a general guide for interpreting the strength of the linear relationship based on $r$:

| Value of $r$ (absolute) | Strength of Linear Relationship |
| :---------------------- | :------------------------------ |
| $0.90 \le |r| \le 1.00$  | Very Strong                     |
| $0.70 \le |r| < 0.90$   | Strong                          |
| $0.50 \le |r| < 0.70$   | Moderate                        |
| $0.30 \le |r| < 0.50$   | Weak                            |
| $0.00 \le |r| < 0.30$   | Very Weak or None               |

## [[Correlation Does Not Imply Causation]]

One of the most critical concepts in statistics, often misunderstood, is that **correlation does not imply causation**. Just because two variables are strongly correlated does not mean that one causes the other. There might be:
*   **Confounding variables**: A third, unobserved variable affecting both.
*   **Common response**: Both variables respond to a third, lurking variable.
*   **Coincidence**: The relationship is purely by chance.

For example, the number of ice cream sales and the number of drownings might be strongly positively correlated. This doesn't mean eating ice cream causes drowning, nor that drowning causes ice cream sales. Both are influenced by a lurking variable: hot weather.

Always be cautious when drawing conclusions about cause-and-effect from correlational studies. Experimental studies are generally needed to establish causation, as discussed in [[Introduction to Experimental Design]].

## When to Use Correlation

Correlation is appropriate for describing the relationship between two [[Quantitative Variable]]. It's most meaningful when the scatterplot shows a roughly linear pattern. If the pattern is clearly curved, correlation is not an appropriate measure of the relationship, and other methods like [[Analyzing Departures from Linearity]] may be needed.