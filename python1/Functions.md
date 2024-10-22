# [[Functions]]

## What are [[Functions]]?
 [[Functions]] in Python are reusable blocks of code that are defined once and can be called multiple times. They encapsulate specific tasks or functionality and provide a way to organize and structure code, making it more maintainable and modular.

## How to Use [[Functions]]
 [[Functions]] are defined using the `def` keyword, followed by the function name and parentheses containing any required parameters. The function body is indented below the function declaration and contains the statements to be executed when the function is called.

```python
def function_name(parameters):
 """Function documentation (optional)"""
 # Function body
```

### [[Function Parameters]]
Parameters are optional input values that are passed to a function when it is called. They allow functions to be flexible and accept different values each time they are invoked. Parameters are defined within the parentheses of the function declaration.

```python
def greet_person(name):
 print(f"Hello, {name}!")
```

## Code Examples
```python
# Define a function to calculate the area of a circle
def calculate_area_circle(radius):
 area = math.pi * radius ** 2
 return area

# Call the function to calculate the area of a circle with radius 5
area = calculate_area_circle(5)
print(area)
```

## Related Python Concepts

- [[Modules and Packages]]: [[Functions]] can be grouped into modules and packages to organize and reuse code.
- [[Default Parameters]]: Default values can be specified for parameters to handle cases when they are not provided during function calls.
- [[Return Values]]: [[Functions]] can return values using the `return` statement, allowing them to pass data back to the calling code.
- [[Lambda Functions]]: Lambda functions are anonymous functions that provide a concise way to define one-line functions.
- [[Higher-Order Functions]]: [[Functions]] can accept other functions as arguments or return functions as values.
# [[Python 1 Home]]