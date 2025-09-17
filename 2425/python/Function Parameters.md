# [[Python 1 Home]]
# [[Function Parameters]] 
Python function parameters allow you to pass data into functions, making them reusable and flexible.  There are several types of parameters:

* **Positional Parameters:**  These are matched based on their position in the function definition and the function call.

```python
def greet(name, greeting):
  print(f"{greeting}, {name}!")

greet("Alice", "Hello") # Output: Hello, Alice!
```

* **Keyword Parameters:** These are specified by name in the function call, allowing you to pass arguments in any order.

```python
greet(greeting="Good morning", name="Bob") # Output: Good morning, Bob!
```

* **[[Default Parameters]]:** These assign a default value to a parameter if no value is provided during the function call.

```python
def greet(name, greeting="Hello"):
  print(f"{greeting}, {name}!")

greet("Charlie") # Output: Hello, Charlie!
greet("Dave", "Hi") # Output: Hi, Dave!
```
[[Default Parameters]]

* **Variable-length Positional Arguments (`*args`):**  Allows a function to accept any number of positional arguments. These are packed into a tuple.

```python
def sum_all(*args):
  total = 0
  for num in args:
    total += num
  return total

print(sum_all(1, 2, 3)) # Output: 6
print(sum_all(10, 20, 30, 40)) # Output: 100
```

* **Variable-length Keyword Arguments (`**kwargs`):** Allows a function to accept any number of keyword arguments. These are packed into a dictionary.

```python
def print_kwargs(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_kwargs(name="Eve", age=30, city="[[New York]]")
```

* **Combining Parameter Types:** You can combine different parameter types in a single function definition, but positional parameters must come before keyword parameters and `*args` before `**kwargs`.

```python
def my_function(a, b, *args, c=5, **kwargs):
  print(f"a: {a}, b: {b}, args: {args}, c: {c}, kwargs: {kwargs}")

my_function(1, 2, 3, 4, c=10, d=20)
```

* **Parameter Annotations:** These are optional and provide type hints for better code readability and static analysis. They don't enforce type checking at runtime.

```python
def annotated_function(name: str, age: int) -> str:
  return f"{name} is {age} years old."
```
[[Type Hinting]]


Related Notes: [[Python Functions]], [[Return Values]]
