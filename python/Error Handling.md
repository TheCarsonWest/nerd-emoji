# [[Data Type Conversions]]
# [[Error Handling]] 
Python uses `try-except` blocks to handle errors gracefully.  This prevents your program from crashing when unexpected situations occur.

```python
try:
    # Code that might raise an exception
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Division by zero")
except Exception as e: # Catches all other exceptions
    print(f"An unexpected error occurred: {e}")
else: #Executes if no exception occurs
    print(f"Result: {result}")
finally: # Always executes, regardless of exceptions
    print("This always runs")

```

[[Exception Handling]] Specifics]]  (This will be a separate note detailing different exception types, best practices, and custom exceptions)

Common Exceptions:

* `ZeroDivisionError`: Division by zero.
* `TypeError`:  Incompatible data types in an operation.
* `ValueError`:  Inappropriate value passed to a function.
* `FileNotFoundError`:  Attempting to open a non-existent file.
* `IndexError`: Accessing a list or tuple index out of bounds.
* `KeyError`: Accessing a dictionary key that doesn't exist.


Example of catching multiple exceptions:

```python
try:
  file = open("my_file.txt", "r")
  #Process file
  content = file.read()
  data = int(content)

except (FileNotFoundError, ValueError) as e:
    print(f"Error processing file: {e}")
finally:
  file.close() # important to close the file, regardless of success or failure

```


[[Custom Exceptions]] (This note will explain how to define your own exception classes to manage specific error conditions in your code)


Related Notes:

* [[File Handling]] (This will discuss file I/O operations and related error handling)

