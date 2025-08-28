# [[AP Stats Home]]
# Representing the Relationship Between Two Quantitative Variables

When we have two quantitative variables measured on the same individuals, we often want to understand if there's a relationship between them and, if so, describe its nature. This involves both graphical and numerical summaries.

## [[Scatterplots]]

A **scatterplot** is the most effective graphical tool for displaying the relationship between two quantitative variables. Each individual in the data is represented as a point on the graph.

*   **Explanatory Variable (Independent Variable):** Plotted on the horizontal ($x$) axis. This variable is thought to explain or cause changes in the response variable.
*   **Response Variable (Dependent Variable):** Plotted on the vertical ($y$) axis. This variable measures an outcome of a study.

**Example:** If we're studying how the number of hours studied relates to exam scores, hours studied would likely be the explanatory variable, and exam scores the response variable.

## Describing a Scatterplot (DOFS)

When analyzing a scatterplot, we look for four key characteristics:

1.  **Direction:**
    *   **Positive Association:** As the explanatory variable increases, the response variable tends to increase. The points trend upwards from left to right.
    *   **Negative Association:** As the explanatory variable increases, the response variable tends to decrease. The points trend downwards from left to right.
    *   **No Association:** There is no clear upward or downward trend. The points appear randomly scattered.

2.  **[[Outliers]]**: Individual points that fall outside the overall pattern of the relationship. These points can significantly influence numerical summaries and models.

3.  **Form:** The general shape of the relationship.
    *   **Linear:** The points cluster around a straight line. This is the most common form we study in AP Statistics.
    *   **Non-linear (Curved):** The points follow a curved pattern (e.g., parabolic, exponential).
    *   **No Clear Form:** The points show no discernible pattern.

4.  **Strength:** How closely the points follow the form.
    *   **Strong:** The points are tightly clustered around the form.
    *   **Moderate:** The points show a clear form but with some scatter.
    *   **Weak:** The points are widely scattered, but a form might still be discernible.

### Example of DOFS Description

"The scatterplot shows a **strong, positive, linear relationship** between hours studied and exam scores, with **no obvious outliers**."

## Choosing Appropriate Variables

It's crucial to correctly identify the explanatory and response variables based on the context of the problem.

| Context                 | Explanatory Variable (x) | Response Variable (y) |
| :---------------------- | :----------------------- | :-------------------- |
| Hours of exercise vs. weight loss | Hours of exercise        | Weight loss           |
| Temperature vs. ice cream sales | Temperature              | Ice cream sales       |
| Age vs. reaction time   | Age                      | Reaction time         |

## [[Correlation]]

While scatterplots provide a visual description, the **correlation coefficient** (denoted by $r$) is a numerical measure that quantifies the **strength** and **direction** of a *linear* relationship between two quantitative variables.

*   **Range:** $r$ always falls between -1 and 1, inclusive ($-1 \le r \le 1$).
*   **Direction:**
    *   $r > 0$: Positive linear association.
    *   $r < 0$: Negative linear association.
    *   $r \approx 0$: Very weak or no linear association.
*   **Strength:**
    *   Values close to $\pm 1$ indicate a strong linear relationship.
    *   Values close to $0$ indicate a weak linear relationship.
    *   $r = \pm 1$ means a perfect linear relationship (all points fall exactly on a straight line).

**Formula for Correlation Coefficient:**
$$ r = \frac{1}{n-1} \sum \left( \frac{x_i - \bar{x}}{s_x} \right) \left( \frac{y_i - \bar{y}}{s_y} \right) $$
Where:
*   $n$ is the number of observations.
*   $x_i$ and $y_i$ are individual data points.
*   $\bar{x}$ and $\bar{y}$ are the means of $x$ and $y$.
*   $s_x$ and $s_y$ are the standard deviations of $x$ and $y$.

**Important Notes about Correlation:**
*   **Correlation does not imply causation.** A strong correlation between two variables does not mean one causes the other. There might be [[Lurking Variables]] involved.
*   **Correlation only measures linear relationships.** A strong non-linear relationship might have a correlation close to 0.
*   **Correlation is not resistant to outliers.** Outliers can significantly affect the value of $r$.
*   **Changing units of measurement does not change $r$.** If you change from feet to meters, $r$ remains the same.