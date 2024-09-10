## Python Function Parameters

**Definition:**

Function parameters are variables that receive values when the function is called. They allow us to pass data to functions and use them within their code.

### Types of Parameters:

**Required Parameters:**

* **Positional parameters:** Parameters that must be passed to the function in a specific order.
* **Keyword parameters:** Parameters that can be passed in any order by specifying their names.

Example: 
```python
def add_numbers(num1, num2):
    return num1 + num2

add_numbers(10, 20)  # Positional parameters
add_numbers(num2=20, num1=10)  # Keyword parameters
```

**Optional Parameters:**

* **Default parameters:** Parameters that have a default value if no value is passed.
* **Variable-length arguments:** Parameters that can be passed any number of arguments.

Example:
```python
def greet(name, age=20):
    print("Hello", name, ", you are", age, "years old.")

greet("John")  # Default parameter
greet("Jane", 30)  # Override default parameter
```

**Arbitrary Keyword Arguments:**

* ****kwargs:** A special parameter that allows us to pass an arbitrary number of keyword arguments.

Example:
```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="John", age=30, city="New York")
```

### Other Python Concepts Related to Parameters:

* **Variable Argument Lists:** For variable-length arguments and arbitrary keyword arguments.
* **Function Annotations:** To provide type hints for parameters and return values.
* **Lambdas:** Anonymous functions that can receive parameters.