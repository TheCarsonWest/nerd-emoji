# [[Libraries like NumPy]]
# [[NumPy Random Number Generation]] 
NumPy's `random` module (now deprecated; use `numpy.random` directly) provides functions for generating various random numbers and distributions.  It's significantly faster than Python's built-in `random` module, especially for large arrays.


**Key Functions & Concepts:**

* **`numpy.random.rand(d0, d1, ..., dn)`:** Creates an array of the given shape and fills it with random floats sampled from a uniform distribution over `[0, [[1)`.

```python
import numpy as np

# 3x3 array of random floats between 0 and [[1
random_array = np.random.rand(3, 3)
print(random_array)
```

* **`numpy.random.randn(d0, d1, ..., dn)`:** Creates an array of the given shape and fills it with random floats sampled from a standard normal (Gaussian) distribution (mean=0, standard deviation=[[1).

```python
# 2x2 array of random floats from a standard normal distribution
normal_array = np.random.randn(2, 2)
print(normal_array)
```

* **`numpy.random.randint(low, high=None, size=None, dtype=int)`:** Returns random integers from `low` (inclusive) to `high` (exclusive).  If `high` is `None`, then results are from 0 to `low`.

```python
# 5 random integers between [[1 and 10 (inclusive)
random_integers = np.random.randint([[1, 11, 5) # 11 is exclusive
print(random_integers)
```

* **`numpy.random.choice(a, size=None, replace=True, p=None)`:** Generates a random sample from a given array `a`.  `replace=True` allows sampling with replacement (same element can be selected multiple times). `p` specifies probabilities for each element in `a`.

```python
# Sample 3 elements from an array with replacement
my_array = np.array([[1, 2, 3, 4, 5)
sample = np.random.choice(my_array, size=3, replace=True)
print(sample)


# Sample with probabilities
probabilities = np.array([0.[[1, 0.2, 0.3, 0.2, 0.2) # must sum to [[1
weighted_sample = np.random.choice(my_array, size=3, replace=True, p=probabilities)
print(weighted_sample)
```

* **`numpy.random.seed(seed)`:** Sets the seed for the random number generator. Using the same seed will produce the same sequence of random numbers.  This is crucial for reproducibility.

```python
np.random.seed(42) # set seed to 42
print(np.random.rand(2))
np.random.seed(42) # setting it again produces the same results
print(np.random.rand(2))
```

* **Other Distributions:** NumPy provides functions for generating random numbers from many other probability distributions, including binomial, exponential, Poisson, etc.  Refer to the NumPy documentation for a complete list.  ([[NumPy Distributions]])


* **Generating Random Matrices:**  NumPy offers convenient ways to create random matrices with specific properties (e.g., symmetric, orthogonal, etc.).([[Random Matrix Generation]])


**Deprecated `random` Module:**

The top-level `numpy.random` module is now preferred over the older `np.random` module.  While the older module might still work in some cases, it is recommended to transition to the newer approach for better compatibility and future-proofing.


**Note:**  For more advanced random number generation and statistical simulations, consider using libraries like SciPy.([[SciPy Statistical Functions]])
