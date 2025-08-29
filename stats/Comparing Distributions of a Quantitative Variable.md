# [[AP Stats Home]]
# Comparing Distributions of a Quantitative Variable

When analyzing quantitative data, it is often necessary to compare the distributions of a variable across two or more groups. This allows us to identify similarities, differences, and draw conclusions about the populations from which the samples were drawn. The key to effective comparison lies in a systematic approach, often summarized by acronyms like SOCS (Shape, Outliers, Center, Spread) or CUSS (Center, Unusual Features, Shape, Spread).

## 1. Visualizing Comparisons

The first step in comparing distributions is to create appropriate graphical displays for each group on the same scale. This enables a direct visual comparison. Common graphs for quantitative variables include:
*   [[Representing a Quantitative Variable with Graphs|Dot plots]]
*   [[Representing a Quantitative Variable with Graphs|Stem-and-leaf plots]]
*   [[Graphical Representations of Summary Statistics|Box plots]] (especially good for multiple groups as they are compact)
*   [[Representing a Quantitative Variable with Graphs|Histograms]] (ensure consistent bin widths across groups)

Side-by-side box plots are particularly useful for comparing multiple distributions because they clearly show the median, quartiles, and potential outliers for each group, making it easy to compare center and spread.

## 2. Comparing Key Features (SOCS/CUSS)

When comparing distributions, you must discuss *all four* key aspects in context, explicitly using comparative language (e.g., "Group A's median is higher than Group B's," "Group C's spread is wider than Group D's").

### 2.1. Shape

Describe the overall pattern of each distribution.
*   **Symmetry/Skewness**: Is the distribution roughly symmetric, skewed left, or skewed right?
*   **Modality**: Is it unimodal (one peak), bimodal (two peaks), or uniform?
*   **Other features**: Are there any gaps or clusters?
    *   *Example Comparison*: "Both distributions are roughly symmetric, but Distribution A appears to have a slight skew to the left, while Distribution B is more symmetric."

### 2.2. Outliers / Unusual Features

Identify any individual data points that fall far from the overall pattern of the distribution. These are often highlighted by box plots (as individual dots) or noticeable in histograms/dot plots as values isolated from the main body of data.
*   **Identifying Outliers**: For a box plot, points beyond the fences are considered outliers.
    *   Lower Fence: $Q_1 - 1.5 \times IQR$
    *   Upper Fence: $Q_3 + 1.5 \times IQR$
    *   *Example Comparison*: "Distribution A has no apparent outliers, whereas Distribution B has one high outlier at approximately 150."

### 2.3. Center

Compare the typical value of each distribution.
*   **Median**: Use the median when distributions are skewed or contain outliers, as it is resistant to extreme values.
*   **Mean**: Use the mean when distributions are roughly symmetric and do not have significant outliers.
*   *Example Comparison*: "The median value for Group X (approx. 75) is substantially higher than the median for Group Y (approx. 60)."

### 2.4. Spread

Compare the variability or dispersion of data within each distribution.
*   **Range**: Max - Min. (Sensitive to outliers)
*   **Interquartile Range (IQR)**: $Q_3 - Q_1$. (Resistant to outliers, good for skewed data)
*   **Standard Deviation**: Use when distributions are roughly symmetric and without outliers.
    *   The formula for sample standard deviation is $s = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2}$.
*   *Example Comparison*: "The spread of Distribution P (IQR = 20) is much wider than Distribution Q (IQR = 10), indicating more variability in P."

## 3. Summary Table for Comparison

A table can summarize the [[Summary Statistics for a Quantitative Variable|summary statistics]] for each group, making direct comparison of numerical values easier, but remember to still provide descriptive commentary.

| Feature       | Group 1 (e.g., Males) | Group 2 (e.g., Females) |
| :------------ | :-------------------- | :---------------------- |
| Shape         | Skewed Right          | Roughly Symmetric       |
| Outliers      | None                  | One high outlier (125)  |
| Center (Median) | 45                    | 58                      |
| Spread (IQR)  | 20                    | 15                      |

## 4. Context is Key

Always ensure your comparisons are made in the context of the problem. State what the variables represent and what the groups are. Your conclusions should relate back to the original question. When drawing comparisons, use phrases like "Distribution A tends to have higher values than Distribution B," or "There is more consistency in Group X's data than in Group Y's."