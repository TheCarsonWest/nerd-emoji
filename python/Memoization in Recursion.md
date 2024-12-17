# [[Recursion]]
# [[Memoization in Recursion]] 
Memoization is an optimization technique used to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.  This is particularly useful in recursive functions where the same subproblems are calculated repeatedly.

**How it works:**

A memoized function maintains a cache (usually a dictionary) to store the results of previous calls. Before computing a result, it checks the cache:

* **Cache Hit:** If the input is already in the cache, the stored result is returned directly.
* **Cache Miss:** If the input is not in the cache, the function computes the result, stores it in the cache, and then returns it.


**Example:**

Let's consider a recursive Fibonacci sequence calculation:

```python
def fibonacci_recursive(n):
  if n <= 1:
    return n
  else:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

```

This is inefficient because it recalculates many Fibonacci numbers multiple times.  A memoized version would be:

```python
cache = {}  # Initialize cache

def fibonacci_memoized(n):
  if n in cache:
    return cache[n]  # Cache hit
  else:
    if n <= 1:
      result = n
    else:
      result = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
    cache[n] = result  # Cache miss, store result
    return result

```

`fibonacci_memoized` significantly improves performance for larger values of `n`.


**[[Python Dictionaries]]**  (Note: This needs its own explanation about Python dictionaries and their use in caching.)

**[[Recursive Function Design]]** (Note:  This note should cover best practices for writing efficient recursive functions.)


**Advantages of Memoization:**

* **Improved Performance:**  Significantly reduces computation time for repeated subproblems.
* **Reduced Redundancy:** Avoids unnecessary recalculations.

**Disadvantages of Memoization:**

* **Increased Memory Usage:** The cache consumes memory to store results.  This can be a concern for very large inputs or complex functions.
* **Implementation Complexity:** Requires additional code to manage the cache.  Not always worth the effort for simple functions or cases where the performance gain is small.


**When to use Memoization:**

Memoization is most beneficial when:

* The function is recursive.
* The same subproblems are computed multiple times.
* The function's inputs are relatively small and the outputs are relatively large.
* The cost of computation is high and/or the number of repeated subproblems is significant.
