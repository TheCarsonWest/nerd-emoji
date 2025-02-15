# [[Python 1 Home]]
# [[Default Parameters]] 
Default parameters allow you to specify default values for function arguments.  If a caller doesn't provide a value for an argument with a default, the default value is used.

```python
def greet(name, greeting="Hello"):
  print(f"{greeting}, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob", "Hi")  # Output: Hi, Bob!
```

**Important Considerations:**

* **Order Matters:** Default parameters must come *after* non-default parameters in the function definition.

```python
# Correct
def func(a, b=2):
    pass

# Incorrect - will raise a SyntaxError
def func(a=[[1, b):
    pass
```

* **Mutable [[Default Arguments]]:** Be cautious when using mutable objects (like lists or dictionaries) as default parameters.  The default is created *once* when the function is defined, not each time it's called. This can lead to unexpected behavior.

```python
def add_to_list(item, my_list=1):
  my_list.append(item)
  return my_list

print(add_to_list([[1))  # Output: 1
print(add_to_list(2))  # Output: [[1, 2  <-- Unexpected!  The list persists between calls.
```

To avoid this, use `None` as the default and create the list inside the function:

```python
def add_to_list(item, my_list=None):
  if my_list is None:
    my_list = 1
  my_list.append(item)
  return my_list

print(add_to_list([[1))  # Output: 1
print(add_to_list(2))  # Output: 2
```

[[Function Parameters]]
[[Python Functions]]

