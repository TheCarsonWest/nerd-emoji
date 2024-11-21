# [[Chaining Decorators]]
# Decorators with Arguments

Decorators are a powerful and expressive feature in Python that allows you to modify or enhance functions and methods in a clean and readable way.  Standard decorators work by taking a function as input and returning a modified version. However, sometimes you need to pass arguments to the decorator itself to customize its behavior. This is where decorators with arguments come in.

Instead of a simple decorator function, you create a decorator *factory* – a function that *returns* a decorator function.  This factory function accepts the arguments you need and uses them to create a tailored decorator.

```python
def my_decorator(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator arguments: {arg1}, {arg2}")
            result = func(*args, **kwargs)
            print("After function execution")
            return result
        return wrapper
    return decorator

@my_decorator("hello", 123)
def say_hello(name):
    print(f"Hello, {name}!")
    return "Returned from say_hello"


result = say_hello("World")
print(f"Result: {result}")

```

This demonstrates a decorator factory `my_decorator` which takes `arg1` and `arg2`.  It returns the actual decorator `decorator`, which in turn returns the `wrapper` function.  The `wrapper` function performs actions before and after the decorated function (`say_hello`).

**Key Points:**

* **Decorator Factory:** The outer function (`my_decorator`) is the factory.
* **Nested Functions:**  The structure uses nested functions (`decorator` and `wrapper`).
* **Argument Passing:** Arguments are passed to the factory, and these arguments are accessible within the `wrapper` function (via closure).


[[Decorator Basics]]  ([[Closure in Python]])
