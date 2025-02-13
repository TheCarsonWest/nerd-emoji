# [[Multidimensional Lists]]
# [[NumPy Arrays]] 
NumPy arrays are the fundamental data structure for numerical computation in Python.  They provide efficient storage and manipulation of numerical data.  Key advantages over standard Python lists include:

* **Homogeneous data type:** All elements in a NumPy array must be of the same data type. This allows for optimized memory usage and faster computations.
* **Vectorized operations:** NumPy supports vectorized operations, meaning that operations are applied to the entire array at once, rather than element by element. This significantly speeds up calculations.
* **Broadcasting:**  A powerful feature that allows arithmetic operations between arrays of different shapes under certain conditions. [[Broadcasting in NumPy]]
* **Efficient memory layout:** NumPy arrays store data in contiguous memory locations, improving memory access speed.


**Creating [[NumPy Arrays]]:**

NumPy arrays are created using the `numpy.array()` function.

```python
import numpy as np

# From a list
arr1 = np.array([[1, 2, 3, 4, 5) 

# From a list of lists (creates a 2D array)
arr2 = np.array([[1, 2, 3, 4, 5, 6)

# Using other functions like arange, zeros, ones, etc.
arr3 = np.arange(10) # Creates an array from 0 to 9
arr4 = np.zeros((2,3)) # Creates a 2x3 array filled with zeros
arr5 = np.ones((3,2)) # Creates a 3x2 array filled with ones

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
```

**Array Attributes:**

NumPy arrays have several useful attributes:

```python
print(arr2.shape) # Returns the dimensions of the array
print(arr2.dtype) # Returns the data type of the array elements
print(arr2.size) # Returns the total number of elements in the array
print(arr2.ndim) # Returns the number of dimensions (axes) of the array
```

**Array Operations:**

NumPy provides a rich set of functions for array manipulation and computation:

```python
# Arithmetic operations
arr6 = arr1 + 2 # Adds 2 to each element
arr7 = arr1 * arr1 # Element-wise multiplication

# Array slicing
arr8 = arr2[:2, :2 # Selects a subarray

# Reshaping arrays
arr9 = arr1.reshape(5,[[1) # Reshapes arr1 into a 5x1 array

# Linear algebra operations ([[NumPy Linear Algebra]])
# ...

print(arr6)
print(arr7)
print(arr8)
print(arr9)
```


[[NumPy Indexing and Slicing]]
[[NumPy Data Types]]


