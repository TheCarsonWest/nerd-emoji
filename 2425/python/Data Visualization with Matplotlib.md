# [[Libraries like Pandas]]
# [[Data Visualization with Matplotlib]] 
This note covers the basics of data visualization using the Matplotlib library in Python.

Key aspects to cover:

* **Basic Plotting:**
    * `matplotlib.pyplot.plot()` function:  Creating line plots.  Experiment with different line styles, markers, and colors.
    ```python
    import matplotlib.pyplot as plt
    plt.plot(1, 2, 3, 4, 5, 6, 7, 8)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Simple Line Plot")
    plt.show()
    ```
    * Scatter plots using `matplotlib.pyplot.scatter()`: Show relationships between two variables.  Example with color-coding.
    ```python
    plt.scatter(1, 2, 3, 4, 5, 6, 7, 8, c=['red', 'green', 'blue', 'yellow']])
    plt.show()
    ```
    * Bar charts and Histograms using `matplotlib.pyplot.bar()` and `matplotlib.pyplot.hist()`: Visualizing categorical and numerical data distributions.

* **Customizing Plots:**
    * Adding titles, labels, legends, and annotations.
    * Adjusting plot size, aspect ratio, and fonts.
    * Working with different colormaps.
    * Using `plt.subplots()` for creating multiple subplots within a single figure.

* **More Advanced Plotting:**
    * [[Matplotlib Subplots]] -  Detailed explanation of creating and customizing subplots.
    * [[Matplotlib Styling]] -  Advanced customization options, including stylesheets and rcParams.
    * 3D plotting with `mpl_toolkits.mplot3d`: Creating 3D visualizations (requires extra import).
    * [[Working with Images in Matplotlib]] - Importing and displaying images.  Examples using `imread` and `imshow`.


* **Saving Plots:**
    * Saving plots in various formats (e.g., PNG, JPG, PDF) using `plt.savefig()`.


* **Useful Resources:**
    * Matplotlib official documentation: [https://matplotlib.org/](https://matplotlib.org/)
    * Matplotlib tutorials and examples: [Numerous online tutorials available](Search online for "Matplotlib tutorials")

* **Related Notes:** [[Data Wrangling with Pandas]] (for preparing data for visualization)


