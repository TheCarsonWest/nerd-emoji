## [[Function Parameters]]

### Definition
Function parameters are arguments that are passed into a function when it is called. They allow functions to receive data from the caller and use it within their execution.

### How to Use [[Function Parameters]]
Function parameters are defined within the parentheses of the function definition. Each parameter is assigned a name and a type annotation (optional). When the function is called, the actual arguments are passed in the same order as the parameters defined in the function signature.

### Code Examples
```python
def add_numbers(num1, num2):
 return num1 + num2

# call the function with actual arguments
result = add_numbers(5, 10)
```

```python
def greet_person(name: str, age: int):
 print(f"Hello, {name}. You are {age} years old.")

# call the function with named arguments (optional)
greet_person(age=25, name="John")
```

### Related Python Concepts

- [[Functions]]: Function parameters are an integral part of defining and using functions.
- [[Return Values]]: Parameters enable functions to receive input and return meaningful values.
- [[Default Parameters]]: Default parameters can be specified to provide default values for optional parameters.
- [[Variable Scope]]: Parameters introduce variables that are local to the function's scope.
- [[Recursion]]: [[Functions]] can have parameters that refer to themselves, enabling recursive execution.
# [[Python 1 Home]]