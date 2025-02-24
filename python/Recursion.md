# [[Python 1 Home]]
# [[Recursion]]

[[Recursion in Python]] involves a function calling itself within its own definition.  This allows for elegant solutions to problems that can be broken down into smaller, self-similar subproblems.

**Key Concepts:**

* **Base Case:**  A condition that stops the recursion. Without a base case, the function will call itself infinitely, leading to a `RecursionError`.
* **Recursive Step:** The part of the function where it calls itself, typically with a modified input that moves closer to the base case.


**Example: Factorial Calculation**

```python
def factorial(n):
  """
  Calculates the factorial of a non-negative integer using recursion.
  """
  if n == 0:  # Base case
    return 1
  else:
    return n * factorial(n - 1)  # Recursive step

print(factorial(5))  # Output: 120
```

**Potential Issues:**

* **Stack Overflow:**  If the recursion depth becomes too large, it can exceed the Python interpreter's stack limit, resulting in a `RecursionError`.  This is more likely with deeply nested recursive calls.
* **Inefficiency:**  Recursive solutions can sometimes be less efficient than iterative ones, especially for problems that can be easily solved iteratively.


**Related Notes:**

* [[Function Parameters]]
* [[Return Values]]
* [[Memoization in Recursion]]  (This will explain how to optimize recursive functions for performance)


**Example: Fibonacci Sequence (Illustrating potential inefficiency)**

```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(6)) # Output: 8 (but slow for larger n)
```

This recursive Fibonacci solution is inefficient because it recalculates many values multiple times.  An iterative approach would be significantly faster for larger values of `n`.
