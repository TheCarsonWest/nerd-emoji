# [[Python Functions]]
# [[Variable Length Arguments in Python]] 
Python offers flexibility in defining functions that can accept a variable number of arguments. This is achieved using two special syntaxes: `*args` and `**kwargs`.

*   `*args`:  This allows a function to accept a variable number of positional arguments. These arguments are collected into a tuple.

```python
def my_sum(*args):
  total = 0
  for num in args:
    total += num
  return total

print(my_sum([[1, [[2], [[3]))  # Output: [[6]
print(my_sum(10, 20, 30, 40)) # Output: 100
print(my_sum()) # Output: 0
```

*   `**kwargs`: This allows a function to accept a variable number of keyword arguments.  These arguments are collected into a dictionary.

```python
def print_details(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_details(name="Alice", age=30, city="[[New York]]")
```

Output:

```
name: Alice
age: 30
city: [[New York]] ```

You can combine `*args` and `**kwargs` in a single function definition:

```python
def combined_example(*args, **kwargs):
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

combined_example([[1, [[2], [[3], name="Bob", age=25)
```

Output:

```
Positional arguments: ([[1, [[2], [[3])
Keyword arguments: {'name': 'Bob', 'age': 25}
```

**Important Considerations:**

*   The order matters:  `*args` must come before `**kwargs` in the function definition.
*   `args` and `kwargs` are just conventions; you can use other names (e.g., `*numbers`, `**params`), but sticking to the convention improves readability.


[[Tuple Unpacking]]
[[Dictionary Manipulation]]
[[Function Definitions]]

