# [[AP Stats Home]]
# Representing a Quantitative Variable with Graphs

When analyzing data in AP Statistics, it's crucial to distinguish between different types of variables. A **quantitative variable** takes numerical values for which it makes sense to find an average. These values typically represent counts or measurements. Graphical representations are powerful tools for visualizing the [[Describing the Distribution of a Quantitative Variable]] of a quantitative variable, helping us identify patterns, shape, center, spread, and potential outliers.

## Types of Graphs for Quantitative Variables

Several types of graphs are specifically designed to display the distribution of a single quantitative variable. Each has its strengths and is suitable for different scenarios.

### [[Dotplots]]

A dotplot is one of the simplest graphs for displaying a quantitative variable.
*   **Construction**: Draw a horizontal axis and label it with the variable name. Mark a dot above the appropriate value on the axis for each observation. If there are multiple occurrences of a value, stack the dots vertically.
*   **Best Use**: Ideal for small to moderate-sized datasets. They clearly show individual data points, clusters, gaps, and outliers.
*   **Example**: To display the number of siblings for 10 students: 1, 2, 0, 3, 1, 2, 1, 0, 4, 2.

```
      *   *
  *   *   *
* * * * * *
---.---.---.---.---
   0   1   2   3   4
  Number of Siblings
```

### [[Stemplots (Stem-and-Leaf Plots)]]

Stemplots are another way to display the distribution of a quantitative variable, especially for small to moderate datasets. They are unique in that they retain the individual data values.
*   **Construction**: Separate each observation into a **stem** (all but the final digit) and a **leaf** (the final digit). Write the stems in a vertical column, then draw a vertical line to their right. Write each leaf in the row next to its stem, in increasing order away from the stem. Include a **key** to explain what the stems and leaves represent.
*   **Best Use**: Good for showing the shape of the distribution while preserving the actual data values. Useful for comparing two related distributions (back-to-back stemplot).
*   **Example**: Test scores (out of 100): 65, 72, 78, 81, 83, 85, 85, 89, 90, 92, 95.

```
6 | 5
7 | 2 8
8 | 1 3 5 5 9
9 | 0 2 5

Key: 8|1 represents a score of 81
```

### [[Histograms]]

Histograms are the most common type of graph for visualizing the distribution of a quantitative variable for larger datasets.
*   **Construction**:
    1.  Divide the range of the data into classes of equal width. These are called "bins" or "intervals."
    2.  Count the number of observations (frequency) or the proportion of observations (relative frequency) in each class.
    3.  Draw bars for each class. The height of the bar represents the frequency (or relative frequency) of observations in that class. The bars should touch each other to emphasize that the data is continuous.
*   **Best Use**: Excellent for large datasets. They clearly show the overall pattern and shape of the distribution (e.g., symmetric, skewed, unimodal, bimodal). They do not show individual data points.
*   **Important**: The choice of bin width can significantly affect the appearance of the histogram.
*   **Formula for relative frequency**:
    $$ \text{Relative Frequency} = \frac{\text{Frequency of Class}}{\text{Total Number of Observations}} $$

## Choosing the Right Graph

The choice of graph depends on the size of the dataset and the specific information you want to convey:
*   **Dotplots**: Best for small datasets to see individual values and simple patterns.
*   **Stemplots**: Good for small to moderate datasets when preserving individual data values and showing shape is important.
*   **Histograms**: Preferred for larger datasets to visualize the overall shape, center, and spread without needing individual values.

Regardless of the graph type, always remember to:
*   **Label axes**: Clearly indicate what each axis represents, including units if applicable.
*   **Provide a title**: A clear, concise title summarizing the graph's content.
*   **Scale axes appropriately**: Ensure the chosen scale allows for a clear representation of the data without being misleading.

These graphical representations are the first step in [[Describing the Distribution of a Quantitative Variable]], which then leads to calculating [[Summary Statistics for a Quantitative Variable]] for a more formal analysis.