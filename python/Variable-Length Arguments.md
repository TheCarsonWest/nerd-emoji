# [[Function Overloading]]
# Variable-Length Arguments in Python

Python offers flexibility in function definitions by allowing variable-length arguments. This means you can define functions that accept a varying number of arguments, without needing to specify the exact number beforehand.  There are two main ways to achieve this:

* **`*args` (Arbitrary Positional Arguments):**

  This syntax allows a function to accept any number of positional arguments. These arguments are collected into a tuple named `args` (though you can use any valid variable name,  `args` is a convention).

```python
def my_sum(*args):
  total = 0
  for num in args:
    total += num
  return total

print(my_sum(1, 2, 3))  # Output: 6
print(my_sum(10, 20, 30, 40)) # Output: 100
print(my_sum()) # Output: 0
```

* **`**kwargs` (Arbitrary Keyword Arguments):**

  This syntax allows a function to accept any number of keyword arguments. These arguments are collected into a dictionary named `kwargs` (again, the name is a convention).  The keys of the dictionary are the argument names, and the values are their corresponding values.

```python
def print_details(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")
```

Output:

```
name: Alice
age: 30
city: New York
```

* **Combining `*args` and `**kwargs`:**

  You can combine both `*args` and `**kwargs` in a single function definition.  The order matters: `*args` must come before `**kwargs`.

```python
def combined_example(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

combined_example(1, 2, 3, name="Bob", age=25)
```

Output:

```
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Bob', 'age': 25}
```


[[Tuple Unpacking]]
[[Dictionary Manipulation]]

These are essential for understanding how to fully utilize `*args` and `**kwargs`.
