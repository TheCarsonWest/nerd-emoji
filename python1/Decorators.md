**Python Decorators**

**What are Python Decorators?**

Python decorators are a powerful tool that allows you to modify the behavior of a function or class without modifying its source code. They are implemented as functions that take another function as an argument and return a modified version of that function.

**Parameters of a Decorator**

The parameters of a decorator function depend on its specific purpose. However, the following parameters are commonly used:

* **func:** The function that the decorator is being applied to.
* **args:** The positional arguments passed to the decorated function.
* **kwargs:** The keyword arguments passed to the decorated function.

**Code Examples of Decorators**

**Example 1: Simple Logging Decorator**

This decorator logs the arguments and return value of a function:

```python
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@logging_decorator
def add(a, b):
    return a + b

add(1, 2)
```

**Example 2: Caching Decorator**

This decorator caches the results of a function call to avoid repeated computations:

```python
import functools

def cache_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in wrapper.cache:
            wrapper.cache[key] = func(*args, **kwargs)
        return wrapper.cache[key]
    wrapper.cache = {}
    return wrapper

@cache_decorator
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(5)
```

**Other Python Concepts Related to Decorators**

* **Metaclasses:** Decorators can be implemented using metaclasses.
* **Metaprogramming:** Decorators are a form of metaprogramming, which allows you to write code that manipulates other code.
* **Function Annotations:** Decorators can be used to add type hints to functions.
* **Property Decorators:** Decorators can be used to define property getters and setters.
* **Classmethod Decorators:** Decorators can be used to create classmethods.

[[Python 1 Home]]