## Python Libraries like Matplotlib

### Overview

Matplotlib is a powerful Python library for creating static, animated, and interactive visualizations. It provides a wide range of plotting options, including 2D and 3D graphs, histograms, scatter plots, and more.

### Key Parameters

* **figure:** A container for a set of axes.
* **subplot:** A region within a figure that contains a single plot.
* **axis:** A set of lines that represent the axes of the plot.
* **x/y-axis:** The axis that measures the horizontal or vertical position of data points.
* **ticks:** Markers along the axes that indicate the values of data points.
* **labels:** Text labels that identify the axes and data points.
* **title:** The title of the plot.
* **legend:** A list of labels that identifies the data series in the plot.

### Usage Examples

**Creating a Simple Line Plot:**

```python
import matplotlib.pyplot as plt

# Generate data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and subplot
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Set the title, labels, and legend
ax.set_title("Line Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend(["Line"])

# Display the plot
plt.show()
```

**Creating a Bar Chart:**

```python
import matplotlib.pyplot as plt

# Generate data
data = [5, 10, 15, 20, 25]

# Create a figure and subplot
fig, ax = plt.subplots()

# Create a bar chart
ax.bar(data)

# Set the title, labels, and legend
ax.set_title("Bar Chart")
ax.set_xlabel("Bars")
ax.set_ylabel("Values")
ax.legend(["Data"])

# Display the plot
plt.show()
```

**Creating a 3D Scatter Plot:**

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
z = [11, 12, 13, 14, 15]

# Create a figure and subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data
ax.scatter(x, y, z)

# Set the title, labels, and legend
ax.set_title("3D Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend(["Data"])

# Display the plot
plt.show()
```

### Related Python Concepts

* **NumPy:** Used for numerical operations and data manipulation.
* **Pandas:** Used for data analysis and manipulation.
* **Seaborn:** A higher-level interface for creating visualizations with Matplotlib.
* **Bokeh:** A library for creating interactive visualizations.
[[Python 1 Home]]