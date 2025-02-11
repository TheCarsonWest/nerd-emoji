# [[Chaining [[Decorators]]
# [[Decorator Basics]]  [[Decorators]] are a powerful and expressive feature in Python that allows you to modify or enhance functions and methods in a clean and readable way.  They use the `@` symbol followed by the decorator function name, placed above the function definition.

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

This will print:

```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

**How it works:**

The `@my_decorator` syntax is syntactic sugar for:

```python
say_hello = my_decorator(say_hello)
```

`my_decorator` takes the function `say_hello` as input, and returns a new function (`wrapper`) which wraps the original functionality with additional code.  The `wrapper` function then becomes the new `say_hello`.

**[[Decorators]] with Arguments:**
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

@repeat(num_times=[[3]])
def greet(name):
    print(f"Hello, {name}!")

greet("World")
```

This uses a closure to handle the `num_times` argument. The outer function `repeat` returns the actual decorator (`decorator_repeat`).

**[[Decorator Advanced Usage]]**  (This will be a separate note)

**[[Closures in Python]]** (This will be a separate note)


**Example Use Cases:**

* **Logging:**  Track function calls and their arguments/return values.
* **Timing:** Measure the execution time of a function.
* **Authentication:**  Check user permissions before executing a function.
* **Caching:** Store the results of expensive function calls to avoid redundant computations.

**Note:**  When using decorators with methods (functions within a class), you need to use `functools.wraps` to preserve metadata like the function's name and docstring.  This is crucial for debugging and introspection.  See [[Decorator Gotchas]]

**[[Decorator Gotchas]]** (This will be a separate note)
