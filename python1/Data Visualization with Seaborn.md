## [[Data Visualization with Seaborn]]

### Introduction
Seaborn is a Python library for data visualization based on Matplotlib that provides a high-level interface for creating statistical graphics. It simplifies the process of generating visually appealing and informative charts and plots.

### How to Use Seaborn
To use Seaborn, follow these steps:
1. Import the Seaborn library:
```python
import seaborn as sns
```
2. Load and prepare your data.
3. Choose the type of plot you want to create (e.g., line plot, scatter plot, histogram).
4. Use the appropriate Seaborn function to create the plot. (See below for specific functions and parameters.)
5. Customize the plot as needed (e.g., add labels, set colors).

### [[Functions]] and Parameters
Seaborn provides various functions for different types of plots, each with its own set of parameters. Some commonly used functions include:

- **relplot()**: Create scatter plots, line plots, and bar plots with customizable relationships (e.g., hue, size).
 - `data`: The data to plot.
 - `x`, `y`: The data columns to plot on the x and y axes.
 - `hue`, `size`: Categorical variables to encode as color and size.
- **histplot()**: Create histograms.
 - `data`: The data to plot.
 - `x`, `y`: The data columns to plot on the x and y axes.
 - `hue`: Categorical variable to encode as color.
- **scatterplot()**: Create scatter plots.
 - `data`: The data to plot.
 - `x`, `y`: The data columns to plot on the x and y axes.
 - `hue`: Categorical variable to encode as color.
- **lineplot()**: Create line plots.
 - `data`: The data to plot.
 - `x`, `y`: The data columns to plot on the x and y axes.
 - `hue`: Categorical variable to encode as color.

### Code Examples
```python
# Line plot
sns.relplot(data=df, x="x", y="y")

# Scatter plot
sns.scatterplot(data=df, x="x", y="y", hue="category")

# Histogram
sns.histplot(data=df, x="x")
```

### Related Python Concepts

- [[Libraries like Matplotlib]]: Seaborn is built on top of Matplotlib and provides an easier-to-use interface.
- [[DataFrames in Pandas]]: Pandas DataFrames are commonly used as input data for Seaborn plots.
- [[Plot Customization in Matplotlib]]: Seaborn plots can be further customized using Matplotlib functions.
- [[Mutable vs Immutable Types]]: Seaborn plots are mutable and can be modified after creation.
# [[Python 1 Home]]