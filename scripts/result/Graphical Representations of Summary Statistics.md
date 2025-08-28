# [[AP Stats Home]]
# Graphical Representations of Summary Statistics

Graphical representations of summary statistics provide powerful visual tools to understand and compare distributions of quantitative variables. While [[Summary Statistics for a Quantitative Variable]] give us numerical values for center, spread, and shape, graphs allow for quick, intuitive interpretation and identification of patterns, skewness, and outliers. They are especially useful when comparing multiple groups or understanding the overall structure of a dataset.

## Box Plots (Box-and-Whisker Plots)

Box plots are a highly effective way to visualize the [[Summary Statistics for a Quantitative Variable]] for a quantitative variable, particularly the five-number summary. They are excellent for comparing distributions across different categories.

### Components of a Box Plot

A standard box plot displays:
*   **Median (Q2)**: The line inside the box.
*   **First Quartile (Q1)**: The bottom (or left) edge of the box. 25% of the data falls below this value.
*   **Third Quartile (Q3)**: The top (or right) edge of the box. 75% of the data falls below this value.
*   **Interquartile Range (IQR)**: The length of the box, calculated as $IQR = Q3 - Q1$. This represents the middle 50% of the data.
*   **Whiskers**: Lines extending from the box to the minimum and maximum values within 1.5 times the IQR from the quartiles.
    *   Upper Fence: $Q3 + 1.5 \times IQR$
    *   Lower Fence: $Q1 - 1.5 \times IQR$
*   **Outliers**: Individual points beyond the whiskers, indicated by dots, asterisks, or other symbols. These are values that fall outside the fences. [[Identifying Outliers]] is crucial for understanding unusual observations.

### Interpreting Box Plots

Box plots allow us to quickly assess:
*   **Center**: The median line shows the central tendency.
*   **Spread**: The length of the box (IQR) shows the spread of the middle 50%. The total length of the whiskers and box shows the overall range (excluding outliers).
*   **Shape**:
    *   **Symmetric**: If the median is roughly in the middle of the box, and the whiskers are roughly equal in length, the distribution is approximately symmetric.
    *   **Skewed Right (Positively Skewed)**: If the median is closer to Q1, and the upper whisker is longer, the data has a tail to the right.
    *   **Skewed Left (Negatively Skewed)**: If the median is closer to Q3, and the lower whisker is longer, the data has a tail to the left.
*   **Outliers**: Clearly visible as individual points.

Consider the following example:

| Summary Statistic | Value |
| :---------------- | :---- |
| Minimum           | 10    |
| Q1                | 25    |
| Median            | 40    |
| Q3                | 60    |
| Maximum           | 95    |

From these statistics:
*   $IQR = Q3 - Q1 = 60 - 25 = 35$
*   Lower Fence = $25 - 1.5 \times 35 = 25 - 52.5 = -27.5$
*   Upper Fence = $60 + 1.5 \times 35 = 60 + 52.5 = 112.5$
Any data points below -27.5 or above 112.5 would be considered outliers.

## Histograms with Summary Statistics

While [[Representing a Quantitative Variable with Graphs#Histograms]] show the frequency distribution of raw data, summary statistics like the mean ($\mu$ or $\bar{x}$) and standard deviation ($\sigma$ or $s$) can be overlaid or inferred to provide additional context.

*   **Mean**: Often represented by a vertical line, especially on symmetric or approximately normal distributions.
*   **Standard Deviation**: Can be shown by adding shaded regions or additional vertical lines at $\bar{x} \pm s$, $\bar{x} \pm 2s$, etc., to illustrate the spread around the mean. This is particularly useful for [[The Normal Distribution]].

$$
\text{Approximate range of data (for unimodal, symmetric distributions): } \bar{x} \pm 3s
$$

However, it's crucial to remember that the mean and standard deviation are sensitive to skewness and outliers, making them less robust for highly skewed distributions compared to the median and IQR.

## Dot Plots and Stem-and-Leaf Plots

[[Representing a Quantitative Variable with Graphs#Dot Plots]] and [[Representing a Quantitative Variable with Graphs#Stem-and-Leaf Plots]] also allow for a visual assessment of summary statistics, though less directly than box plots for the five-number summary. You can easily pinpoint the minimum, maximum, and visually estimate the median, quartiles, and modes from these plots. They are best for smaller datasets where individual data points are important to display.