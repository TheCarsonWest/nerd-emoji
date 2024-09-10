**Python Default Parameters**

**Definition:**

In Python, it is possible to define functions with default values for some of their parameters. These default values are used when the function is called without specifying a value for the corresponding parameter.

**Parameters:**

Default parameters can have the following parameters:

* **Name:** The name of the parameter to which the default value applies.
* **Default value:** The value that will be assigned to the parameter if no value is provided when the function is called.
* **Position:** Default parameters must be defined after all non-default parameters.

**Syntax:**

```python
def function_name(parameter1, parameter2=default_value):
    # Function body
```

**Code Examples:**

```python
# Example 1: Default value for a single parameter
def greet(name="John"):
    print("Hello, " + name + "!")

greet()  # Output: Hello, John!
greet("Mary")  # Output: Hello, Mary!

# Example 2: Default values for multiple parameters
def calculate_area(length=5, width=3):
    return length * width

print(calculate_area())  # Output: 15
print(calculate_area(10))  # Output: 30
print(calculate_area(10, 6))  # Output: 60
```

**Linked Python Concepts:**

* **Variable Assignment:** Default parameters are evaluated when the function is defined, not when the function is called.
* **Function Overloading:** Default parameters allow for overloaded functions, where the same function can accept different combinations of parameters with or without default values.
* **Immutable Data Types:** Default values for mutable data types (e.g., lists, dictionaries) can lead to unexpected behavior if the default value is modified within the function. It is recommended to use immutable data types for default values.