# Python [[Function Overloading]]

## What is [[Function Overloading]]?

Function overloading is a feature that allows multiple functions with the same name to exist in the same scope, but with different parameters. It enables the use of a single function name for different sets of input arguments, with each function performing a specific task based on the types and number of arguments passed.

## How to Use [[Function Overloading]]

Python does not directly support function overloading. However, there are ways to mimic its behavior:

- ** [[Default Parameters]]**: Using default parameters allows for variation in the number of input arguments.
 - Example:
 ```python
 def calculate_area(length, width=1):
 return length * width
 ```

- **Variable-Length Arguments**: The `*args` and `**kwargs` notation can be used to handle an arbitrary number of input arguments.
 - Example:
 ```python
 def sum_numbers(*numbers):
 return sum(numbers)
 ```

## Code Examples

```python
# Using default parameters
def greet(name, greeting="Hello"):
 return f"{greeting}, {name}!"

print(greet("John")) # Hello, John!
print(greet("Mary", "Good morning")) # Good morning, Mary!

# Using variable-length arguments
def calculate_average(*numbers):
 return sum(numbers) / len(numbers)

print(calculate_average(10, 20, 30)) # 20.0
```

## Related Python Concepts

- [[Functions]]: Function overloading mimics the behavior of multiple functions with the same name.
- [[Default Parameters]]: Default parameters permitem functions to have optional input arguments.
- [[Function Parameters]]: Overloaded functions require different sets of parameters.
- [[Variable and Data Types]]: Overloaded functions may accept different types of input arguments.
- [[Polymorphism]]: Function overloading can be seen as a form of polymorphism.
# [[Python 1 Home]]