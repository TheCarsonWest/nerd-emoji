# [[AP Stats Home]]
# Representing a Categorical Variable with Graphs

Categorical variables categorize individuals into groups or categories. Unlike quantitative variables, which take numerical values that can be ordered and measured, categorical variables deal with labels. Visualizing these variables through graphs is crucial for understanding the distribution of data within each category and for identifying patterns or differences. This note page focuses on the primary graphical methods for displaying a single categorical variable.

## Introduction to Graphing Categorical Data

When we have data for a categorical variable, we are interested in how many observations fall into each category, or what proportion of the total observations each category represents. These counts and proportions are often summarized first in a [[Representing a Categorical Variable with Tables]]. Graphs then provide a visual summary, making it easier to compare categories and spot trends.

## Bar Charts

[[Bar Charts]] are the most common and often the most appropriate way to display the distribution of a categorical variable.

### What is a Bar Chart?
A bar chart displays the categories of a categorical variable on one axis (usually the horizontal axis) and the counts or proportions (percentages) of observations in each category on the other axis (usually the vertical axis). Each category is represented by a bar, and the height of the bar corresponds to the count or proportion for that category.

### Constructing a Bar Chart
1.  **Label Axes**: The horizontal axis (x-axis) lists the categories of the variable. The vertical axis (y-axis) is labeled with "Count," "Frequency," "Relative Frequency," or "Percent."
2.  **Scale Vertical Axis**: Choose an appropriate scale for the vertical axis, starting from 0.
3.  **Draw Bars**: For each category, draw a bar whose height matches its count or percentage.
4.  **Separate Bars**: Leave spaces between the bars to indicate that the categories are distinct and not on a continuous scale. This is a key distinction from [[Representing a Quantitative Variable with Graphs#Histograms|Histograms]], where bars touch.

### Example: Preferred Pet
Let's consider the distribution of preferred pets among a sample of 20 students.

| Preferred Pet | Count | Relative Frequency |
| :------------ | :---- | :----------------- |
| Dog           | 8     | 0.40               |
| Cat           | 6     | 0.30               |
| Fish          | 3     | 0.15               |
| Bird          | 2     | 0.10               |
| Other         | 1     | 0.05               |
| **Total**     | **20**| **1.00**           |

A bar chart for this data would have "Preferred Pet" on the x-axis and "Count" or "Relative Frequency" on the y-axis, with separate bars for each pet type.

## Pie Charts

[[Pie Charts]] are another common way to display the distribution of a categorical variable, but they are often less effective than bar charts, especially when comparing categories.

### What is a Pie Chart?
A pie chart shows the distribution of a categorical variable as "slices" of a circular "pie." Each slice represents a category, and the size of the slice (both in area and central angle) is proportional to the percentage of observations in that category.

### Constructing a Pie Chart
1.  **Calculate Proportions**: Determine the proportion or percentage of the total for each category.
2.  **Calculate Angles**: Multiply each proportion by $360^{\circ}$ to find the central angle for each slice.
    $$ \text{Angle for Category } i = (\text{Proportion of Category } i) \times 360^{\circ} $$
3.  **Draw and Label**: Draw a circle and divide it into slices according to the calculated angles. Label each slice with its category and percentage.

### Example: Preferred Pet (continued)
Using the "Preferred Pet" data:

| Preferred Pet | Proportion | Angle ($360^{\circ} \times \text{Proportion}$) |
| :------------ | :--------- | :--------------------------------------------- |
| Dog           | 0.40       | $0.40 \times 360^{\circ} = 144^{\circ}$        |
| Cat           | 0.30       | $0.30 \times 360^{\circ} = 108^{\circ}$        |
| Fish          | 0.15       | $0.15 \times 360^{\circ} = 54^{\circ}$         |
| Bird          | 0.10       | $0.10 \times 360^{\circ} = 36^{\circ}$         |
| Other         | 0.05       | $0.05 \times 360^{\circ} = 18^{\circ}$         |
| **Total**     | **1.00**   | **$360^{\circ}$**                               |

### When to Use Pie Charts
Pie charts are best used when you want to show how a whole is divided into parts, and when there are a small number of categories (typically 2-5). They become difficult to read and compare when there are too many categories or when the proportions are very similar. In most cases, a bar chart provides a clearer comparison of category sizes.

## Key Considerations for Graphing Categorical Data

*   **Labels and Titles**: Always include clear titles and axis labels to ensure the graph is easily understandable.
*   **Source**: If the data comes from a specific source, include that information.
*   **Avoid Misleading Graphs**: Be wary of [[Potential Problems with Sampling#Bias|biased]] or misleading graphical representations. For example, 3D bar charts or pie charts can distort the perception of proportions.
*   **Order of Categories**: In bar charts, categories can be ordered alphabetically, by size (ascending or descending), or by some other logical criterion. For pie charts, the order typically doesn't convey additional information beyond the labels themselves.