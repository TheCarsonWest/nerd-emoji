# [[ndarray Explained]]
# [[Array Creation Methods]] 
Different ways to create arrays in Python, focusing primarily on NumPy arrays which are the most common type of array used for numerical computation.  Standard Python lists are less efficient for numerical operations.

[[NumPy Arrays]] -  A separate note dedicated to explaining NumPy arrays in detail.  This will cover data types, dimensions, and other core concepts.

**Methods:**

[[1. **Using `numpy.array()`:** This is the most straightforward method.  It takes an iterable (like a list or tuple) as input.

```python
import numpy as np

# From a list
my_array = np.array([[1, [[2], [[3], [[4], [[5]])
print(my_array)

# From a tuple
my_array = np.array(([[1, [[2], [[3], [[4], [[5]))
print(my_array)

# From a list of lists (creates a 2D array)
my_2d_array = np.array([[1, [[2]], [[3], [[4])
print(my_2d_array)

# Specifying the data type
my_array = np.array([[1, [[2], [[3]], dtype=float) #forces creation of a floating point array
print(my_array)
```

[[2]. **Using `numpy.arange()`:** Creates an array with evenly spaced values within a given interval. Similar to Python's `range()` function.

```python
import numpy as np

my_array = np.arange(10) # 0 to 9
print(my_array)

my_array = np.arange([[2], 10, [[2]) # [[2] to 8, step of [[2]
print(my_array)
```

[[3]. **Using `numpy.linspace()`:** Creates an array with evenly spaced numbers over a specified interval.  Useful for generating sequences for plotting or other applications.

```python
import numpy as np

my_array = np.linspace(0, [[1, [[5]) # [[5] evenly spaced numbers from 0 to [[1 (inclusive)
print(my_array)

my_array = np.linspace(0, 10, num=[[6]) # [[6] evenly spaced numbers from 0 to 10
print(my_array)

```

[[4]. **Using `numpy.zeros()` and `numpy.ones()`:** Creates arrays filled with zeros or ones, respectively.  Useful for initializing arrays before populating them with other data.  Specify shape as a tuple.

```python
import numpy as np

zeros_array = np.zeros(([[3], [[4])) # 3x4 array of zeros
print(zeros_array)

ones_array = np.ones(([[2],[[2])) # 2x2 array of ones
print(ones_array)

```

[[5]. **Using `numpy.full()`:** Creates an array filled with a specified value.

```python
import numpy as np

full_array = np.full(([[2], [[3]), [[7])  # 2x3 array filled with 7s
print(full_array)
```

[[6]. **Using `numpy.eye()`:** Creates an identity matrix (square matrix with ones on the diagonal and zeros elsewhere).

```python
import numpy as np

identity_matrix = np.eye([[3]) # 3x3 identity matrix
print(identity_matrix)
```

[[7]. **Using `numpy.random` functions:**  NumPy's `random` module provides various functions to create arrays with random numbers.  See [[NumPy Random Number Generation]] for more details.  Examples:


```python
import numpy as np

random_array = np.random.rand([[3],[[2]) # 3x2 array of random floats between 0 and [[1
print(random_array)

random_integers = np.random.randint(0,10, size=([[2],[[3])) # 2x3 array of random integers between 0 and 9
print(random_integers)
```

8.  [[Array Reshaping]] -  A separate note describing how to change the shape of an existing array using `reshape()`, `resize()`, and other methods.



These are the most common ways to create arrays in Python.  The choice of method depends on your specific needs and the data you're working with.  Remember that efficiency is often a key consideration, especially when dealing with large datasets. NumPy arrays are optimized for numerical operations compared to standard Python lists.
