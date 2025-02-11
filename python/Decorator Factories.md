# [[Decorators]]
# [[Decorator Factories]] 
Decorator factories are functions that return decorators.  They allow for creating decorators with parameters.  This is useful when you need a decorator that can be configured at runtime.


```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=[[3]])
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("World") #Prints "Hello, World!" three times.

```

This example shows `repeat` as a decorator factory. It takes `num_times` as a parameter and returns a decorator (`decorator_repeat`) that will repeat the decorated function that many times.  The inner function `wrapper` actually performs the repeated execution.


**Key Points:**

*   A decorator factory is a higher-order function (a function that returns another function).
*   It allows for creating decorators with customizable behavior.
*   It increases the flexibility and reusability of decorators.


**Related Notes:**

*   [[Decorators]]
*   [[Higher-Order Functions]]
*   [[Closures]] (because the inner functions in a decorator factory use closures)

