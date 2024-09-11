**Python Recursion**

**What is Recursion?**

Recursion occurs when a function calls itself within its own code. It is a powerful technique used to solve problems with recursive structure, such as binary trees, linked lists, and solving complex mathematical puzzles.

**Parameters**

A recursive function typically has one or more parameters that control its behavior:

* **Base Case:** A condition that stops the recursion and returns a result.
* **Recursive Case:** The part of the function that calls itself with modified parameters.
* **Parameter Modification:** The way in which the parameters change with each recursive call.

**Code Examples**

**Factorial Calculation:**

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

* Base Case: When `n == 0`, the function returns 1.
* Recursive Case: The function calls itself with `n-1`.
* Parameter Modification: The parameter decrements by 1 with each recursive call.

**Fibonacci Sequence:**

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

* Base Case: When `n` is 0 or 1, the function returns 1.
* Recursive Case: The function calls itself with `n-1` and `n-2`.
* Parameter Modification: The parameter decrements by 1 and 2 with each recursive call.

**Other Python Concepts Related to Recursion**

* **Recursion Limit:** Python has a default recursion limit of 1000. This can be increased using the `sys.setrecursionlimit()` function.
* **Stack Overflow:** Recursion can lead to a stack overflow error if the function calls itself too many times without reaching a base case.
* **Memoization:** A technique used to store the results of recursive calls to avoid redundant calculations.
* **Dynamic Programming:** Another technique that uses recursion to solve problems by breaking them down into smaller subproblems and storing their solutions.
[[Python 1 Home]]