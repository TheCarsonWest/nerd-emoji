# [[Source Analysis Techniques]]
# [[Data Visualization Techniques]]

This document outlines various data visualization techniques.  I'll need to expand on several of these with dedicated notes.

**I. Choosing the Right Visualization:**

The choice of visualization depends heavily on the type of data and the message you want to convey.  Consider:

* **Data Type:**  Categorical, numerical, temporal, geographical.
* **Question Being Asked:** What story are you trying to tell?  What insights are you highlighting?
* **Audience:**  Who is the intended recipient of this visualization?  Adjust complexity accordingly.

**II.  Types of Visualizations:**

* **A. For Showing Distributions:**
    * **Histograms:**  Good for showing the distribution of a single numerical variable.  ([[Histograms]])
    * **Density Plots:**  A smoother version of a histogram. [[Density Plots]]
    * **Box Plots:** Show the median, quartiles, and outliers of a numerical variable. Useful for comparing distributions across groups. [[Box Plots]]
    * **Violin Plots:** Combine a box plot with a kernel density estimation.  [[Violin Plots]]

* **B. For Showing Relationships:**
    * **Scatter Plots:** Show the relationship between two numerical variables.  ([[Scatter Plots]])
    * **Line Charts:** Show trends over time or other continuous variables. [[Line Charts]]
    * **Heatmaps:** Show the relationship between two categorical variables or a numerical variable across two categorical variables. [[Heatmaps]]
    * **Correlation Matrix:**  Visual representation of correlation coefficients between multiple variables.  ([[Correlation Matrix]])

* **C. For Showing Composition:**
    * **Pie Charts:** Show the proportion of different categories within a whole.  Use sparingly, as they can be difficult to interpret for many categories.  ([[Pie Charts]])
    * **Bar Charts:** Show the comparison of different categories.  [[Bar Charts]]
    * **Stacked Bar Charts:**  Show the composition of categories within different groups. [[Stacked Bar Charts]]
    * **Treemaps:** Show hierarchical data using nested rectangles. [[Treemaps]]

* **D. For Showing Geographic Data:**
    * **Maps:**  Various types exist, depending on the data and desired emphasis (choropleth, dot density, etc.). [[Geographic Data Visualization]]


**III.  Key Considerations:**

* **Clear and Concise Labels:** Axes, titles, legends should be clear and unambiguous.
* **Appropriate Scale and Range:** Choose scales that accurately represent the data without distorting the message.
* **Color Palette:** Use a color palette that is both visually appealing and accessible (consider colorblindness).
* **Avoid Chartjunk:** Remove unnecessary elements that distract from the data.

**IV.  Software and Tools:**

* Python (Matplotlib, Seaborn, Plotly)
* R (ggplot2)
* Tableau
* Power BI


**V. Equations (Example):**

* Linear Regression:  $y = mx + b$
* Standard Deviation:  $\sigma = \sqrt{\frac{[[1]]}{N} \sum_{i=[[1]]}^{N}(x_i - \mu)^[[2]]}$

## $$ \text{Mean} = \frac{\sum_{i=[[1]]}^{n} x_i}{n} $$

This is a basic framework.  I need to flesh out the individual visualization types with more detail in the linked notes.
