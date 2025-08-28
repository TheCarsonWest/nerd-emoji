# [[AP Stats Home]]
# Describing the Distribution of a Quantitative Variable

When analyzing a single quantitative variable, it's crucial to describe its overall pattern and any striking deviations from that pattern. We often use a visual display like a histogram, stemplot, or boxplot (which can be found in [[Representing a Quantitative Variable with Graphs]]) to aid in this description. A common mnemonic for a complete description is **SOCS**: **S**hape, **O**utliers, **C**enter, and **S**pread.

## Shape

The shape of a distribution describes its overall form.

*   **Symmetry/Skewness:**
    *   **Symmetric:** The left and right sides of the graph are approximately mirror images. The mean and median will be close. A special case of a symmetric distribution is the [[The Normal Distribution]].
    *   **Skewed Right (Positively Skewed):** The tail extends further to the right. The mean will typically be greater than the median.
    *   **Skewed Left (Negatively Skewed):** The tail extends further to the left. The mean will typically be less than the median.
*   **Modality:**
    *   **Unimodal:** Has one distinct peak (mode).
    *   **Bimodal:** Has two distinct peaks.
    *   **Multimodal:** Has more than two distinct peaks.
    *   **Uniform:** No distinct peaks; all values appear with roughly the same frequency.

## Outliers

Outliers are individual values that fall outside the overall pattern of the distribution. They can be due to natural variability, measurement errors, or data entry mistakes. When describing a distribution, you should always mention any apparent outliers and investigate them further.

### [[Identifying Outliers]]
*   **1.5 IQR Rule:** A common method to formally identify potential outliers is the 1.5 IQR rule. A value is considered a potential outlier if it falls below $Q_1 - 1.5 \times IQR$ or above $Q_3 + 1.5 \times IQR$. Here, $Q_1$ is the first quartile, $Q_3$ is the third quartile, and $IQR = Q_3 - Q_1$.

## Center

The center of a distribution provides a typical or central value.

*   **Mean ($\bar{x}$ or $\mu$):** The arithmetic average of all the values. It is sensitive to outliers and skewness.
    $$ \bar{x} = \frac{\sum x_i}{n} $$
    where $x_i$ are the individual data points and $n$ is the number of data points.
*   **Median (M):** The midpoint of the ordered data. Half the observations are smaller, and half are larger. It is resistant to outliers and skewness.

For more on calculating these values, refer to [[Summary Statistics for a Quantitative Variable]].

## Spread

The spread (or variability) describes how much the data values vary from each other.

*   **Range:** The difference between the maximum and minimum values ($Max - Min$). It is highly affected by outliers.
*   **Interquartile Range (IQR):** The range of the middle 50% of the data ($IQR = Q_3 - Q_1$). It is resistant to outliers.
*   **Standard Deviation ($s$ or $\sigma$):** A measure of the typical distance of the observations from the mean. It is sensitive to outliers.
    $$ s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}} $$
    where $x_i$ are the individual data points, $\bar{x}$ is the sample mean, and $n$ is the sample size.

For a summary of resistance to outliers:

| Statistic        | Resistant to Outliers? |
| :--------------- | :--------------------- |
| Mean             | No                     |
| Median           | Yes                    |
| Range            | No                     |
| Interquartile Range (IQR) | Yes                    |
| Standard Deviation | No                     |

Choosing between mean/standard deviation vs. median/IQR depends on the shape:
*   Use **mean and standard deviation** for reasonably symmetric distributions without outliers.
*   Use **median and IQR** for skewed distributions or those with significant outliers.

Remember to always describe a quantitative variable in terms of its SOCS!