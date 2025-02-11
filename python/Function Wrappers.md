# [[Chaining Decorators]]
# [[Function Wrappers]] 
Function wrappers are a powerful technique in Python that allows you to extend or modify the behavior of a function without modifying its core functionality.  This is achieved by creating a new function that wraps around the original function, executing additional code before or after the original function's execution.

Key aspects:

* **Mechanism:**  A wrapper function takes the original function as an argument and returns a new function that incorporates the wrapper's logic.

* **`@decorator` syntax:** This is the most common and readable way to implement wrappers in Python.  It uses the `@` symbol followed by the wrapper function name above the function being wrapped.

```python
def my_wrapper(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

@my_wrapper
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("World")
```

This will print:

```
Before function execution
Hello, World!
After function execution
```

* **Use Cases:**
    * **Logging:**  Record function calls, arguments, and return values. [[Logging in Python]]
    * **Timing:** Measure the execution time of a function. [[Performance Measurement]]
    * **Input Validation:** Check if the input arguments are valid before executing the function. [[Input Validation Techniques]]
    * **Authentication/Authorization:**  Add security checks before allowing the function to run. [[Security in Python]]
    * **Caching:** Store the results of expensive function calls to speed up subsequent calls. [[Caching Mechanisms]]


* **`functools.wraps`:** This decorator is crucial when creating wrappers. It helps preserve the metadata (like `__name__`, `__doc__`) of the original function, preventing issues with introspection and documentation.

```python
from functools import wraps

def my_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # ...wrapper logic...
        return func(*args, **kwargs)
    return wrapper

```

Without `wraps`, the decorated function might lose its original name and docstring.


* **Decorator Arguments:**  Wrappers can also accept arguments.  This allows for configurable wrapper behavior.  This requires a higher-order decorator.

```python
def repeat(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=[[3]])
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```


This example shows a decorator factory `repeat` that takes `num_times` as an argument.


* **Class [[Decorators]]:** It's also possible to create decorators using classes. This can be particularly useful for more complex scenarios. [[Class Decorators]]

Remember to consult the official Python documentation for more advanced details and examples.
