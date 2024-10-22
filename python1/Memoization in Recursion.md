## [[Memoization in [[Recursion]]

### What is Memoization?
Memoization is a technique used in recursion to optimize performance by storing the results of function calls in a cache. This prevents the function from recomputing the same values multiple times, resulting in significantly faster execution times.

### How to Use Memoization
Memoization can be implemented using a decorator function, which wraps the original function and checks the cache for existing results before executing the function again.

The decorator typically has a parameter `cache` to store the cached results. If the result for the current function call is not present in the cache, the function is executed and the result is added to the cache before being returned.

### Code Examples
```python
# memoization decorator
def memoize(cache=None):
 if cache is None:
 cache = {}

 def wrapper(func):
 def memoized_func(*args):
 key = args
 if key not in cache:
 cache[key] = func(*args)
 return cache[key]
 return memoized_func
 return wrapper

# example function to calculate the Fibonacci number
@memoize
def fibonacci(n):
 if n < 2:
 return n
 else:
 return fibonacci(n-1) + fibonacci(n-2)
```

### Related Python Concepts

- [[Recursion]]: Memoization is directly related to recursion, as it optimizes recursive function calls.
- [[Caches]]: Memoization involves the use of a cache to store the results of function calls.
- [[Decorators]]: Memoization is implemented using a decorator function.
- [[Dynamic Programming]]: Memoization is a key technique in dynamic programming, which optimizes recursive solutions by storing intermediate results.
- [[Optimizations]]: Memoization is a method of optimizing the performance of recursive functions.
# [[Python 1 Home]]