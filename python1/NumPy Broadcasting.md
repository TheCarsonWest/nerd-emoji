## [[NumPy Broadcasting]]

### What is Broadcasting?
Broadcasting is a mechanism in NumPy that allows arrays of different shapes to perform operations as if they were of the same shape. It automatically aligns and replicates elements of arrays to facilitate element-wise calculations.

### How to Use Broadcasting
Broadcasting occurs when arrays with compatible dimensions are passed to an arithmetic operation (e.g., +, -, *, /). NumPy automatically adjusts the shape of the smaller array to match the shape of the larger array, ensuring that the dimensions match and the operation can be performed element-wise. Dimensions that do not match are broadcast one element at a time.

### Code Examples
```python
# Add two arrays of different shapes
a = np.array([1, 2, 3])
b = np.array([[4, 5], [6, 7]])
result = a + b
# Broadcast result: [[5 7] [7 9]]
```

```python
# Multiply a scalar by an array
c = 2
result = c * b
# Broadcast result: [[ 8 10] [12 14]]
```

### Related Python Concepts

- [[Operators]]: Broadcasting is used during arithmetic operations such as addition and multiplication.
- [[Arrays in NumPy]]: Broadcasting assumes that the arrays involved are NumPy arrays.
- [[Vectorization]]: Broadcasting enables the efficient execution of element-wise operations on arrays.
- [[Slicing in NumPy]]: Broadcasting can be used in conjunction with slicing to perform operations on specific subsets of arrays.
- [[DataFrames in Pandas]]: Pandas DataFrames also support broadcasting operations, allowing for efficient dataframe manipulations.
# [[Python 1 Home]]