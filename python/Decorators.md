# [[Python 1 Home]]
# [[Decorators]]  [[Decorators]] are a powerful and expressive feature in Python that allows you to modify or enhance functions and methods in a clean and readable way.  They use the `@` symbol followed by the decorator function name placed above the function definition.

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

This example shows a simple decorator that prints messages before and after the decorated function (`say_hello`) is executed.  The `my_decorator` function takes the function to be decorated as an argument, and returns a new function (`wrapper`) that includes the additional functionality.  The `@` syntax is just syntactic sugar for:

```python
say_hello = my_decorator(say_hello)
```

**Arguments to [[Decorators]]:**
 [[Decorators]] can also accept arguments. This requires a more complex structure:

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

Here, `repeat` is a decorator factory – it returns a decorator.


**[[Decorator Factories]]**

**[[Chaining Decorators]]**


**Class [[Decorators]]:**
 [[Decorators]] can also be classes:


```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += [[1
        print(f"Call count: {self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def my_function():
    print("This function is being counted!")

my_function()
my_function()
```


This uses the `__call__` method to make the class behave like a function.


**Use Cases:**

* Logging:  Record function calls and their arguments/return values.
* Timing: Measure the execution time of a function.
* Access Control: Restrict access to a function based on certain conditions.
* Caching: Store the results of expensive function calls to avoid redundant computations.
* Input Validation: Check the validity of function arguments.


Related notes: [[Closures]], [[Higher-Order Functions]]
