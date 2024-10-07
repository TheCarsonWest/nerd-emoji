## [[Recursion]]

### Explanation
 [[Recursion]] is a programming technique where a function calls itself inside its own body. It is used to break down a problem into smaller subproblems, each of which is a simpler instance of the original problem.

### How to use [[Recursion]]
When implementing recursion, it is important to:

- Define a base case: This is the stopping condition that prevents the function from recursing indefinitely.
- Recursively call the function with simpler subproblems: The subproblems should have smaller inputs and gradually move towards the base case.
- Return values from the recursive calls: The function returns values that are aggregated or used to calculate the final result.

### Code Examples

**Factorial Calculation:**
```python
def factorial(n):
 # Base case: factorial of 0 is 1
 if n == 0:
 return 1
 # Recursive call: multiply n by the factorial of n-1
 else:
 return n * factorial(n-1)
```

**Fibonacci Sequence Generator:**
```python
def fibonacci(n):
 # Base case: first two Fibonacci numbers
 if n < 2:
 return n
 # Recursive calls: sum of two previous Fibonacci numbers
 else:
 return fibonacci(n-1) + fibonacci(n-2)
```

### Related Python Concepts

- [[Functions]]: [[Recursion]] is a special case of function calls where the function calls itself.
- [[Function Parameters]]: Recursive functions often use parameters to pass smaller subproblems to the recursive calls.
- [[Return Values]]: Recursive functions return values that are used to calculate the final result.
- [[Memoization in [[Recursion]]: Memoization techniques can optimize recursive functions by caching previously calculated results.
- [[Higher-Order [[Functions]]: [[Recursion]] can be used to implement higher-order functions that accept and return other functions.
# [[Python 1 Home]]