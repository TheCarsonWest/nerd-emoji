## [[Libraries like Pandas]]

### What is Pandas?
Pandas is an open-source Python library that provides high-performance, data manipulation and analysis tools. It is designed to work with "tabular data," which is data organized in columns and rows. Pandas data structures are called DataFrames, which are similar to tables in relational databases or spreadsheets.

### How to Use Pandas

Pandas provides a wide range of functions and methods for manipulating and analyzing data. Some of the most commonly used functions include:

- `read_csv()`: Reads a Comma-Separated Values (CSV) file into a DataFrame.
- `head()`: Displays the first few rows of a DataFrame.
- `tail()`: Displays the last few rows of a DataFrame.
- `info()`: Provides information about the DataFrame, such as the number of rows, columns, and data types.
- `sort_values()`: Sorts the DataFrame by one or more columns.
- `groupby()`: Groups the DataFrame by one or more columns.

### Code Examples

```python
# Read a CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
df.head()
```

```python
# Sort the DataFrame by the 'age' column
df.sort_values('age')
```

### Related Python Concepts

- [[Lists]]: DataFrames are a specialized type of list that holds data in a tabular format.
- [[Dictionaries]]: DataFrames can be created from dictionaries, where the keys become column names and the values become rows.
- [[File Handling]]: Pandas functions like `read_csv()` and `to_csv()` allow for reading and writing data from and to files.
- [[DataFrames in Pandas]]: DataFrames are the primary data structure used in Pandas for representing and manipulating tabular data.
- [[NumPy Broadcasting]]: Pandas leverages NumPy for efficient data manipulation and numerical operations.
# [[Python 1 Home]]