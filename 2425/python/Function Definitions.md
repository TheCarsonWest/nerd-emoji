# [[Return Values]]
# [[Function Definitions]] 
Python functions are defined using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`.  The function body is indented.

```python
def my_function(param1, param2):
  """This is a docstring describing the function."""
  # Function body
  result = param1 + param2
  return result

# Calling the function
output = my_function(5, 3) 
print(output)  # Output: 8
```

* **Parameters and Arguments:**  `param1` and `param2` are parameters.  When you call the function, you provide arguments (e.g., `5` and `3`).

* **Return Value:** The `return` statement specifies the value the function sends back.  If no `return` statement is present, the function implicitly returns `None`.

* **Docstrings:** The triple-quoted string (`"""Docstring"""`) is a docstring. It's used to document what the function does.  It's good practice to always include docstrings.

* **[[Default Arguments]]:** You can specify default values for parameters.

```python
def greet(name, greeting="Hello"):
  print(f"{greeting}, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob", "Good morning")  # Output: Good morning, Bob!
```

* **Variable Scope:** Variables defined inside a function are local to that function.  Variables defined outside are global. [[Variable Scope]]

* **Keyword Arguments:** Arguments can be passed by keyword (name=value), making the order less important.

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
```

* **Arbitrary Number of Arguments:** Use `*args` for a variable number of positional arguments and `**kwargs` for a variable number of keyword arguments. [[Arbitrary Arguments]]

* **Recursive Functions:**  Functions can call themselves. [[Recursion]]

* **[[Lambda Functions]]:**  Anonymous, small functions defined using the `lambda` keyword. [[Lambda Functions]]

* **Function Annotations:**  (Optional) Add type hints to parameters and return values for better readability and static analysis.  [[Type Hinting]]


