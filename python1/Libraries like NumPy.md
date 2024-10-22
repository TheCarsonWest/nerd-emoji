## [[Libraries like NumPy]]

### What is NumPy?
NumPy (Numerical Python) is a powerful Python library for scientific computing that provides a comprehensive collection of functions and data structures for numerical operations and linear algebra. It enables efficient handling of multidimensional arrays and offers a wide range of mathematical functions for numerical computations.

### How to Use NumPy
To use NumPy in your Python programs, you first need to import the library using the following statement:

```python
import numpy as np
```

Once imported, you can access the functions and classes provided by NumPy.

**Creating Arrays:**
- `np.array(object)`: Converts a Python object to a NumPy array.
- `np.zeros(shape)`: Creates a new array filled with zeros.
- `np.ones(shape)`: Creates a new array filled with ones.
- `np.random.rand(shape)`: Creates a new array filled with random values between 0 and 1.

**Array Operations:**
- `arr.shape`: Returns the shape of an array.
- `arr.dtype`: Returns the data type of an array.
- `arr + arr2`: Element-wise addition of two arrays.
- `arr * arr2`: Element-wise multiplication of two arrays.
- `np.sum(arr)`: Computes the sum of all elements in an array.

**Mathematical [[Functions]]:**
- `np.sin(x)`: Computes the sine of x.
- `np.cos(x)`: Computes the cosine of x.
- `np.log(x)`: Computes the natural logarithm of x.
- `np.sqrt(x)`: Computes the square root of x.

### Code Examples
```python
# Create a 3x3 array of zeros
arr = np.zeros((3, 3))
print(arr)
```

```python
# Compute the element-wise product of two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = arr1 * arr2
print(result)
```

```python
# Compute the sum of all elements in an array
arr = np.array([1, 2, 3, 4, 5])
total = np.sum(arr)
print(total)
```

### Related Python Concepts
- [[Variables and Data Types]]: NumPy arrays are stored using NumPy's own data types.
- [[Operators]]: NumPy provides operators for array operations like element-wise addition and multiplication.
- [[Functions]]: NumPy provides a rich set of mathematical functions for numerical computations.
- [[Lists]]: NumPy arrays can be converted to and from Python lists.
- [[Modules and Packages]]: NumPy is a third-party library that is installed as a package.
# [[Python 1 Home]]