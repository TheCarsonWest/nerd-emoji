## [[Exception Handling]]

### What is [[Exception Handling]]?
Exception handling is a crucial mechanism in Python that allows programmers to gracefully handle errors and exceptions that may occur during program execution. It enables the detection and handling of unexpected or exceptional conditions, preventing the program from crashing or terminating abruptly.

### How to Use [[Exception Handling]]
Exception handling is typically achieved using `try` and `except` blocks. The `try` block contains the code that may potentially raise exceptions, while the `except` block is responsible for catching and handling those exceptions. The syntax for exception handling is:

```python
try:
 # code that may raise an exception
except ExceptionType1 as e1:
 # code to handle ExceptionType1
except ExceptionType2 as e2:
 # code to handle ExceptionType2
```
- `try`: The `try` block contains the code that may raise an exception. If an exception occurs within this block, control is transferred to the corresponding `except` block.
- `except`: The `except` block is used to handle the specific exceptions raised within the `try` block. You can specify multiple `except` blocks to handle different types of exceptions.
- `ExceptionType`: This is the type of exception being handled. It can be a specific exception class or a parent class like `Exception`.
- `as`: The `as` keyword is used to bind the exception to a variable (`e1` or `e2` in the example). This allows you to access the exception object for further processing or error reporting.

### Code Examples
```python
try:
 x = int(input("Enter a number: "))
except ValueError:
 print("Invalid number entered.")
```

```python
try:
 with open("myfile.txt", "r") as f:
 data = f.read()
except FileNotFoundError:
 print("File not found.")
```

### Related Python Concepts

- [[Variables and Data Types]]: Exception handling involves identifying and managing exceptions, which are objects that represent errors.
- [[Operators]]: The `try` and `except` blocks are control flow constructs used for error handling.
- [[Functions]]: Exception handling is often used in conjunction with functions to handle errors that occur during function calls.
- [[For Loops]]: Exception handling can be used to detect and handle errors that occur within loops.
- [[While Loops]]: Similar to for loops, exception handling can be used to handle errors in while loops.
# [[Python 1 Home]]