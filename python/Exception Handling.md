# [[Python 1 Home]]
# [[Exception Handling]]

Python uses `try`, `except`, `else`, and `finally` blocks to handle exceptions.

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Division by zero")
except Exception as e: # Catches any other exception
    print(f"An error occurred: {e}")
else:
    # Code to execute if no exception occurs
    print("Division successful:", result)
finally:
    # Code that always executes, regardless of exceptions
    print("This always runs")

```

[[Custom Exceptions]]  ([[Exception Handling Examples]])


**Common Exceptions:**

* `ZeroDivisionError`: Division by zero.
* `TypeError`:  Operation on incompatible types.
* `NameError`:  Using an undefined variable.
* `IndexError`: Accessing a list index out of range.
* `KeyError`: Accessing a dictionary key that doesn't exist.
* `FileNotFoundError`: Trying to open a non-existent file.
* `IOError`: General input/output error.


**Raising Exceptions:**

You can raise exceptions using the `raise` keyword:

```python
def my_function(x):
    if x < 0:
        raise ValueError("Input must be non-negative")
    return x * 2
```

**Exception Chaining:**

You can chain exceptions to provide more context when an exception is caught and re-raised.

```python
try:
    # some code that may raise an exception
    raise ValueError("Something went wrong")
except ValueError as e:
    raise RuntimeError("A ValueError occurred") from e
```

[[File IO Modes]]  [[Handling Binary Files]]
