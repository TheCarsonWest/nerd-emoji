## [[DataFrames in Pandas]]

### What are DataFrames?
DataFrames are a data structure in the Pandas library that represents tabular data with rows and columns. They are a powerful tool for manipulating and analyzing structured data, similar to tables in relational databases.

### How to Use DataFrames
To create a DataFrame, you can use the `pandas.DataFrame()` constructor. The constructor takes a variety of arguments, including:

- `data`: A two-dimensional array, list of dictionaries, or another DataFrame.
- `index`: An array-like object to use as the index (row labels).
- `columns`: An array-like object to use as the columns (column labels).

### Code Examples
```python
# create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Carol'], 'Age': [20, 25, 30]}
df = pd.DataFrame(data)

# create a DataFrame from a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(arr)
```

### Related Python Concepts
- [[NumPy]]: DataFrames rely on NumPy arrays for data storage.
- [[Lists]]: DataFrames can be created from lists of dictionaries.
- [[Dictionaries]]: DataFrames can be created from dictionaries.
- [[Functions]]: Methods on DataFrames are essentially functions that operate on the data in the DataFrame.
- [[Modules and Packages]]: Pandas is a module that provides the DataFrame data structure.
# [[Python 1 Home]]