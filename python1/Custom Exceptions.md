## [[Custom Exceptions]]

### What are [[Custom Exceptions]]?
Custom exceptions are classes designed to handle specific errors or exceptional conditions encountered during program execution. They extend the built-in `Exception` class and allow developers to create specialized exceptions that can provide more context and tailored handling.

### How to Use [[Custom Exceptions]]
To create a custom exception, define a class that inherits from the `Exception` class and optionally provides additional attributes for storing error information. Typically, a custom exception class is defined as follows:

```python
class CustomException(Exception):
 def __init__(self, message):
 super().__init__(message)
```

Where:

- `CustomException` is the name of the custom exception class.
- `__init__()` is the constructor that takes a custom message as an argument.
- `super().__init__(message)` calls the constructor of the parent `Exception` class and sets the error message.

### Code Examples
```python
# define a custom exception for invalid input
class InvalidInputException(Exception):
 def __init__(self, message):
 super().__init__(message)

# raise the custom exception when invalid input is encountered
if input_value < 0:
 raise InvalidInputException("Invalid input: Input value cannot be negative")
```

```python
# define a custom exception for file not found
class FileNotFoundException(Exception):
 def __init__(self, message):
 super().__init__(message)

# raise the custom exception when trying to access a non-existent file
try:
 with open("non-existent-file.txt", "r") as f:
 # code to read the file
except FileNotFoundException as e:
 print(f"Error: File not found - {e}")
```

### Related Python Concepts

- [[Exception Handling]]: Custom exceptions are part of the exception handling mechanism that allows catching and handling specific exceptions.
- [[Classes and Objects]]: Custom exceptions are defined as classes and can have custom attributes and methods.
- [[Inheritance]]: Custom exceptions inherit from the `Exception` base class to gain its functionality.
- [[Function Parameters]]: The constructor of a custom exception class can take additional parameters for error handling.
- [[Return Values]]: Custom exceptions can return error messages or other relevant information.
# [[Python 1 Home]]