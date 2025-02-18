# [[Exception Handling]]
# [[Exception Handling Examples]] 
This note covers examples of exception handling in Python.  The core concept is using `try...except` blocks to gracefully handle errors that might occur during program execution.  Refer to [[Python Exceptions]] for a comprehensive list of built-in exceptions.

**Example 1: Handling `FileNotFoundError`**

```python
try:
    with open("myfile.txt", "r") as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    print("File not found!")
except Exception as e: #Generic Exception handler.  Always keep as last except block
    print(f"An unexpected error occurred: {e}")

```

**Example 2: Handling `ZeroDivisionError`**

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

**Example 3: Handling `TypeError`**

```python
try:
    result = "hello" + 5
except TypeError:
    print("Cannot concatenate string and integer")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```

**Example 4: Using `else` and `finally` clauses**

The `else` block executes if no exception occurs in the `try` block. The `finally` block *always* executes, regardless of whether an exception occurred or not. This is often used for cleanup actions (e.g., closing files).

```python
try:
    with open("myfile.txt", "r") as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully!")
finally:
    print("This always executes.")

```

**Example 5: Raising custom exceptions**

You can define your own exceptions by creating classes that inherit from the `Exception` class or one of its subclasses. [[Custom Exceptions]]

```python
class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("Something went wrong!")
except MyCustomError as e:
    print(f"Caught a custom exception: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```


**Further Reading:**

* [[Python Error Handling Best Practices]]
* [[Context Managers]] (for more elegant resource management)


