# [[Python Functions]]
# [[Python Decorators]] 
Python decorators are a powerful and expressive feature that allows you to modify or enhance functions and methods in a clean and readable way.  They use the `@` symbol followed by the decorator function name, placed above the function definition.

**Basic Syntax:**

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

This code shows a simple decorator. `my_decorator` takes a function (`func`) as input, creates a wrapper function that executes code before and after `func`, and returns the wrapper. The `@my_decorator` syntax is equivalent to `say_hello = my_decorator(say_hello)`.


**Decorator with Arguments:**
 [[Decorators]] can also accept arguments.  This requires a bit more complexity:

```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("World")
```

Here, `repeat` is a decorator factory – it returns a decorator.  The inner function `decorator_repeat` takes the function to be decorated, and the innermost `wrapper` handles the actual repetition.


**Use Cases:**

* **Logging:**  Track function calls and their arguments/return values. [[Logging with Decorators]]
* **Timing:** Measure the execution time of functions. [[Timing Functions]]
* **Access Control:** Restrict access to certain functions based on user roles or permissions. [[Access Control Decorators]]
* **Caching:** Store the results of expensive function calls to avoid redundant computations. [[Caching Decorators]]


**Advanced Topics:**

* **Class [[Decorators]]:** [[Decorators]] can also be applied to classes. [[Class Decorators]]
* **Decorator Arguments and Order:** Understanding how arguments are passed and the order of multiple decorators is crucial. [[Decorator Arguments and Order]]

**Further Reading:**

* Python's official documentation on decorators.


**Related Notes:**

* [[Function Arguments and Keyword Arguments]]
* [[Closures in Python]]  ([[Decorators]] heavily rely on closures.)
