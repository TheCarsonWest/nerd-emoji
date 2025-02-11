# [[Context Managers]]
# [[Custom [[Context Managers]] 
Context managers are a powerful feature in Python that allows you to manage resources efficiently and gracefully.  The `with` statement is the syntax used to work with them.  Built-in context managers like `open()` for files handle opening and closing automatically.  Custom context managers allow you to create your own resource management logic.

There are two primary ways to define custom context managers:

**[[1]]. Using the `contextlib.contextmanager` decorator:**

This is generally the preferred and more concise approach for simpler context managers.

```python
from contextlib import contextmanager

@contextmanager
def my_context_manager(arg1, arg2):
    """Example context manager."""
    print(f"Entering context manager with {arg1}, {arg2}")
    try:
        yield  # The yield keyword signifies where the context's 'body' will execute
    except Exception as e:
        print(f"Exception in context manager: {e}")
        # Handle exceptions here, if needed
    finally:
        print("Exiting context manager")

with my_context_manager("value1", "value2") as result:
    print("Inside the context manager")
    # Do something here
    # result will be None here unless you yield something
    # a value from within the with block.
    # If a value is yielded, it is returned in 'result'
```


**[[2]]. Using a class that implements the context management protocol (__enter__ and __exit__):**

This approach offers more control and flexibility, especially when dealing with complex resource management scenarios or cleanup that requires more than simple `try...finally` logic.


```python
class MyCustomContextManager:
    def __init__(self, resource):
        self.resource = resource
        print(f"Initializing context manager with {resource}")

    def __enter__(self):
        # Acquire the resource
        print("Acquiring resource")
        return self.resource  # or any other value you want to make accessible inside with block

    def __exit__(self, exc_type, exc_value, traceback):
        # Release the resource, handle exceptions
        print("Releasing resource")
        if exc_type:
            print(f"Exception handled: {exc_type}, {exc_value}")
        return False #False means exceptions are propagated, True means suppressed.

with MyCustomContextManager("my_resource") as resource:
    print(f"Using resource: {resource}")
    # potentially some code that might throw an exception

```

[[Exception Handling]]  
[[Resource Management]]

Note: Both methods achieve similar outcomes; the choice depends on complexity and preference.  The `@contextmanager` decorator is often simpler for straightforward scenarios.  The class-based approach provides more control, particularly for handling exceptions within `__exit__`.
