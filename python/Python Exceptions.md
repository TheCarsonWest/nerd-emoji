# [[Exception Handling Examples]]
# [[Python Exceptions]]  [[Python Exceptions]] are events that occur during the execution of a program that disrupt the normal flow of instructions.  They are a way for Python to signal that something unexpected or erroneous has happened.  Handling exceptions gracefully is crucial for writing robust and reliable code.

Key Concepts:

* **`try...except` block:** This is the fundamental construct for handling exceptions.

```python
try:
  # Code that might raise an exception
  result = 10 / 0  
except ZeroDivisionError:
  # Code to handle the specific exception
  print("Error: Division by zero!")
except Exception as e: #Catches any other exception.  Should be used cautiously.
    print(f"An unexpected error occurred: {e}")
else: #Optional block that executes only if no exception occurred.
    print(f"Result: {result}")
finally: #Optional block that ALWAYS executes, regardless of exceptions.  Good for cleanup.
    print("This always runs.")

```

* **Types of Exceptions:** Python has a rich hierarchy of built-in exceptions.  Some common ones include:
    * `ZeroDivisionError`: Division by zero.
    * `TypeError`:  Operation on incompatible types.
    * `ValueError`:  Incorrect value passed to a function.
    * `FileNotFoundError`:  Attempting to open a non-existent file.
    * `IndexError`: Accessing an index outside the bounds of a sequence.
    * `KeyError`: Accessing a non-existent key in a dictionary.
    * `NameError`: Referencing an undefined variable.  


* **Raising Exceptions:** You can explicitly raise exceptions using the `raise` keyword. This is useful for signaling errors in your own functions.

```python
def validate_age(age):
  if age < 0:
    raise ValueError("Age cannot be negative")
  # ... rest of the function ...
```

* **Custom Exceptions:** You can create your own exception classes by inheriting from the built-in `Exception` class or its subclasses. This allows you to define specific exception types for your application's needs.  ([[Custom Exception Classes]])


* **Exception Handling Best Practices:**
    * Be specific in your `except` blocks. Catch only the exceptions you expect and know how to handle. Avoid a bare `except:` clause unless absolutely necessary.
    * Use `try...except...finally` to ensure cleanup actions (like closing files) are always performed.
    * Log exceptions for debugging purposes.  ([[Logging in Python]])
    * Don't catch exceptions silently unless you have a very good reason (e.g., handling minor issues that the user doesn't need to see).


Related Notes:

* [[Custom Exception Classes]]
* [[Logging in Python]]
* [[Error Handling Strategies]]


