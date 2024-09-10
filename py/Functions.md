## Python Functions

**Definition:**

A function in Python is a block of code designed to perform a specific task and return a value. It allows you to organize code into reusable modules, making programs easier to read, understand, and maintain.

### Parameters:

* **Required parameters:** These parameters are mandatory and must be provided when calling the function.
* **Optional parameters (default parameters):** These parameters have default values and can be omitted when calling the function.
* **Variable-length parameters (*args):** These parameters can accept any number of additional arguments.
* **Keyword-only parameters:** These parameters must be specified by name when calling the function.

### Syntax:

```python
def function_name(parameters):
    # Code to be executed
    return value
```

### Examples:

**Example 1: Simple Function**

```python
def add_numbers(a, b):
    return a + b
```

**Example 2: Function with Optional Parameter**

```python
def print_name(name="John Doe"):
    print("Hello, " + name)
```

**Example 3: Function with Variable-Length Parameters**

```python
def sum_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total
```

**Example 4: Function with Keyword-Only Parameter**

```python
def calculate_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)
```

### Related Python Concepts:

* **Modules:** Functions can be organized into modules, which can be imported into other programs.
* **Objects and Classes:** Functions can be defined as methods of objects and classes.
* **Lambda Functions:** These are anonymous functions that can be defined using a concise syntax.
* **Decorators:** These allow you to modify the behavior of other functions.
* **Higher-Order Functions:** These functions can take other functions as arguments or return functions.