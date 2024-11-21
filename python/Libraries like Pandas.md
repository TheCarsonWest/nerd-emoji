# [[Modules and Packages]]
# Python Note: Libraries like Pandas

The term "Libraries like Pandas" refers to powerful Python libraries that provide high-level data manipulation and analysis capabilities. Pandas, in particular, is a cornerstone of data science in Python.  This note will focus on Pandas, but the concept extends to other libraries with similar functionalities.

Key features of libraries like Pandas include:

* **Data Structures:**  Efficient storage and manipulation of data, primarily using `Series` (1D labeled arrays) and `DataFrames` (2D labeled data structures).  These are significantly more powerful than standard Python lists and dictionaries for data analysis tasks.

* **Data Cleaning & Preprocessing:** Functions for handling missing data (`fillna`, `dropna`), data transformation (e.g., converting data types), and data wrangling in general.

* **Data Analysis:** Tools for exploring and summarizing data – calculating statistics (mean, median, standard deviation), grouping data, applying functions to groups (`.groupby()`), etc.

* **Data Visualization:**  Integration with visualization libraries (like Matplotlib or Seaborn) to create charts and graphs from your data.  While Pandas itself doesn't handle all visualization, the DataFrame structure makes visualization significantly easier.

* **Data Input/Output:** Reading data from various file formats (CSV, Excel, SQL databases, etc.) using functions like `read_csv()`, `read_excel()`, etc., and writing data back to those formats.


**Example Pandas Code:**

```python
import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Calculate the average age
average_age = df['Age'].mean()
print(f"Average age: {average_age}")

# Filter for people older than 28
older_than_28 = df[df['Age'] > 28]
print(older_than_28)

# Group by city and calculate the average age for each city
grouped = df.groupby('City')['Age'].mean()
print(grouped)
```

[[Pandas Data Structures]]  ([[Pandas Data Manipulation]]) [[Data Visualization with Matplotlib]] [[Data Cleaning in Pandas]]
