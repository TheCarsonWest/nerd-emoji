## Python Libraries like [[NumPy]]

### What is [[NumPy]]?

[[NumPy]] (Numerical Python) is a powerful Python library for scientific computing. It provides a high-performance multidimensional array object, and tools for working with these arrays.

### Parameters

**Array Creation:**

* `ndim`: Number of dimensions in the array
* `dtype`: Data type of the array elements
* `shape`: Tuple of integers representing the dimensions of the array

**Array Indexing and Slicing:**

* `i` or `:, i`: Index to access a single element or slice
* `start:stop:step` or `:, start:stop:step`: Slice to access a range of elements
* `arr.reshape(new_shape)`: Reshape the array to a new shape

**Array Operations:**

* Arithmetic operations (+, -, *, /, **, etc.)
* Comparison operations (==, !=, <, >, <=, >=)
* Boolean operations (logical_and, logical_or, logical_not)
* Element-wise functions (exp, sin, cos, etc.)

### Code Examples

```python
import numpy as np

# Create a 2D array of zeros
arr = np.zeros((3, 4))

# Create a 1D array of random numbers
arr = np.random.rand(10)

# Access a single element
print(arr0, 1)

# Slice an array
print(arr:, 1:3)

# Perform an element-wise operation
print(np.sin(arr))
```

### Related Python Concepts

* [[Pandas]]: [[Pandas]] ([[DataFrames]]) are similar to [[NumPy]] arrays, but they have additional features such as row and column labels.
* **Lists and Tuples**: Lists and tuples can also hold collections of data, but they are less efficient for numerical operations.
* [[Matplotlib]]: [[Matplotlib]] is a Python library for data visualization that can work with [[NumPy]] arrays.
* [[Pandas]]: [[Pandas]] is a Python library for data manipulation and analysis that heavily utilizes [[NumPy]] arrays.
**(Python 1 Home)**