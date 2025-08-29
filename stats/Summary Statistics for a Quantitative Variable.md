# [[AP Stats Home]]
# Summary Statistics for a Quantitative Variable

Summary statistics provide a concise numerical description of the main features of a distribution of a quantitative variable. They help us understand the center, spread, and shape of the data without having to look at every single data point. When describing a distribution, we often focus on these key characteristics.

## Measures of Center

Measures of center indicate the "typical" value of a dataset.

### Mean ($\bar{x}$)
The arithmetic mean, often simply called the mean, is the sum of all values divided by the number of values. It's the most common measure of center.

$$ \bar{x} = \frac{\sum x_i}{n} $$

*   **Interpretation:** The mean is the balancing point of the distribution.
*   **Sensitivity to Outliers:** The mean is **not resistant** to outliers. Extreme values can significantly pull the mean towards them.
*   **Appropriate Use:** Best for approximately symmetric distributions without outliers.

### Median (M)
The median is the midpoint of an ordered distribution. Half of the observations are smaller than the median, and half are larger.

*   **Calculation:**
    *   Order the data from smallest to largest.
    *   If $n$ is odd, the median is the middle observation. Its position is $\frac{n+1}{2}$.
    *   If $n$ is even, the median is the average of the two middle observations.
*   **Resistance to Outliers:** The median **is resistant** to outliers. Extreme values have little effect on its value.
*   **Appropriate Use:** Best for skewed distributions or distributions with strong outliers.

### Comparing Mean and Median
*   **Symmetric Distribution:** Mean $\approx$ Median
*   **Skewed Right Distribution:** Mean $>$ Median (The mean is pulled towards the longer tail)
*   **Skewed Left Distribution:** Mean $<$ Median (The mean is pulled towards the longer tail)

## Measures of Spread (Variability)

Measures of spread describe how much the data values vary from each other.

### Range
The range is the difference between the maximum and minimum values in a dataset.

$$ \text{Range} = \text{Maximum value} - \text{Minimum value} $$

*   **Limitation:** It is highly sensitive to outliers as it only considers the two most extreme values.

### [[Interquartile Range (IQR)]]
The IQR is the range of the middle 50% of the data. It's the difference between the third quartile (Q3) and the first quartile (Q1).

$$ IQR = Q_3 - Q_1 $$

*   **Quartiles:**
    *   $Q_1$ (First Quartile): The median of the lower half of the data. 25% of the data falls below $Q_1$.
    *   $Q_3$ (Third Quartile): The median of the upper half of the data. 75% of the data falls below $Q_3$.
*   **Resistance to Outliers:** The IQR **is resistant** to outliers.
*   **Appropriate Use:** Best for skewed distributions or distributions with strong outliers.

### Standard Deviation ($s_x$)
The standard deviation measures the typical distance of an observation from the mean. It's the square root of the variance.

$$ s_x = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}} $$

*   **Interpretation:** A larger standard deviation indicates greater variability in the data.
*   **Sensitivity to Outliers:** The standard deviation is **not resistant** to outliers.
*   **Properties:**
    *   $s_x \ge 0$. $s_x = 0$ only when all observations are the same.
    *   Like the mean, $s_x$ is strongly affected by outliers.
*   **Appropriate Use:** Best for approximately symmetric distributions without outliers.

### Variance ($s_x^2$)
The variance is the average of the squared deviations from the mean. It is the square of the standard deviation.

$$ s_x^2 = \frac{\sum (x_i - \bar{x})^2}{n-1} $$

*   **Units:** The units of variance are the square of the units of the original data, which makes it less intuitive to interpret than standard deviation.

## The Five-Number Summary

The five-number summary provides a robust numerical description of a distribution and consists of:

1.  Minimum value
2.  First Quartile ($Q_1$)
3.  Median (M)
4.  Third Quartile ($Q_3$)
5.  Maximum value

This summary is the basis for constructing [[Graphical Representations of Summary Statistics#Boxplots]].

## Identifying Outliers

Outliers are observations that fall outside the overall pattern of the distribution. A common rule for identifying potential outliers using the IQR is:

*   An observation is a **low outlier** if it falls below $Q_1 - 1.5 \times IQR$.
*   An observation is a **high outlier** if it falls above $Q_3 + 1.5 \times IQR$.

These summary statistics are fundamental tools for [[Describing the Distribution of a Quantitative Variable]].