# [[Python 1 Home]]
# Context Managers

Context managers in Python provide a clean and efficient way to manage resources.  They ensure that resources are properly acquired and released, even in the presence of exceptions.  The most common way to use a context manager is with the `with` statement.

```python
with open("my_file.txt", "r") as f:
    file_contents = f.read()
    # ... process file_contents ...

# File automatically closed here, even if exceptions occur.
```

The `with` statement implicitly calls the context manager's `__enter__` method (to acquire the resource) and `__exit__` method (to release the resource).


[[Custom Context Managers]]  //Need to create this note


The `contextlib` module provides tools for creating custom context managers:

*   `contextlib.contextmanager`: A decorator that simplifies creating context managers.


```python
from contextlib import contextmanager

@contextmanager
def my_context_manager(arg):
    print(f"Entering context with arg: {arg}")
    try:
        yield arg  # The code within the 'with' block runs here
    except Exception as e:
        print(f"Exception in context: {e}")
        # Handle the exception, perhaps log it
    finally:
        print("Exiting context")

with my_context_manager(10) as value:
    print(f"Value inside context: {value}")
    # raise Exception("Something went wrong")

```

This is equivalent to a class-based approach but much more concise.


Related Notes:

* [[Exception Handling]]
* [[File Handling]]

