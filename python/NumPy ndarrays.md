# [[Libraries like NumPy]]
# [[NumPy ndarrays]] 
NumPy's core data structure is the ndarray (N-dimensional array).  It's a powerful tool for numerical computation because it provides efficient storage and manipulation of large arrays of homogeneous data.

Key features:

* **Homogeneous data type:** All elements within a single ndarray must be of the same data type (e.g., `int32`, `float64`, etc.).  This allows for optimized memory usage and vectorized operations.

* **N-dimensional:**  ndarrays can represent data in any number of dimensions (1D vectors, 2D matrices, 3D tensors, and beyond).

* **Vectorized operations:**  NumPy allows for performing operations on entire arrays at once, rather than iterating element by element. This significantly improves performance.

* **Broadcasting:**  NumPy's broadcasting rules allow for operations between arrays of different shapes under certain conditions, simplifying code and improving efficiency. [[Broadcasting in NumPy]]

* **Slicing and indexing:**  Powerful slicing and indexing mechanisms enable accessing and manipulating portions of ndarrays efficiently. [[NumPy Array Indexing and Slicing]]

* **Memory efficiency:** ndarrays store data in contiguous memory locations, improving performance and reducing memory overhead compared to Python lists.

**Example:**

```python
import numpy as np

# Creating a 2D array
arr = np.array([[1]], [[2]], [[3]]], [[[4]], [[5]], [[6]])

# Accessing elements
print(arr[0, [[1]]])  # Output: [[2]]

# Performing vectorized operations
print(arr * [[2]])  # Output: [[ 2]]  [[4]]  [[6]]], [ 8 10 12]]

# Array shape
print(arr.shape)  # Output: ([[2]], [[3]])

# Array data type
print(arr.dtype)  # Output: int64 (or similar, depending on your system)
```

**Related Notes:**

* [[NumPy Array Creation]]
* [[NumPy Array Manipulation]]
* [[NumPy Linear Algebra]]


