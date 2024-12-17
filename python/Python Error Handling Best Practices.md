# [[Exception Handling Examples]]
# [[Python [[Error Handling]] Best Practices]] 
These notes cover best practices for handling errors in Python.  The goal is to write robust and user-friendly code that gracefully handles unexpected situations.

**Key Concepts:**

* **`try...except` blocks:** The fundamental mechanism for handling exceptions.

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except TypeError:
    print("Error: Invalid data type.")
except Exception as e: #Catch all other exceptions
    print(f"An unexpected error occurred: {e}")
else: #Executes if no exception is raised
    print(f"Result: {result}")
finally: #Always executes, regardless of exceptions
    print("This always runs.")

```

* **Specific vs. General Exceptions:**  It's best to catch specific exceptions first, then use a general `Exception` clause to catch anything you haven't explicitly handled.  This improves code readability and helps pinpoint the source of errors.  Avoid bare `except:` blocks, as they can mask unexpected problems.


* **Logging Errors:**  Instead of just printing error messages to the console (which might be missed or unhelpful in production environments), use a logging library (like the built-in `logging` module) to record errors with timestamps, severity levels, and other relevant information. [[Python Logging]]

* **Raising Custom Exceptions:** Create custom exceptions to handle application-specific error conditions.  This improves code clarity and maintainability.

```python
class InvalidInputError(Exception):
    pass

def process_data(data):
    if not isinstance(data, int):
        raise InvalidInputError("Input must be an integer.")
    # ... rest of the function ...
```

* **Context Managers (`with` statement):**  Useful for managing resources that need to be properly released (e.g., files, network connections).  The `with` statement ensures that resources are cleaned up even if exceptions occur.

```python
with open("myfile.txt", "r") as f:
    contents = f.read()
    # Process file contents
```

* **Defensive Programming:** Write code that anticipates potential problems and handles them gracefully.  This includes input validation, checking for null values, and handling edge cases.


* **Testing:** Thorough testing is crucial for identifying and addressing potential error handling issues.  Unit tests should include scenarios that trigger various exceptions to ensure your error handling logic works as expected. [[Python Unit Testing]]


**Related Notes:**

* [[Python Exception Hierarchy]]
* [[Common Python Exceptions]]



