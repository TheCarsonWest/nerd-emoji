# [[Function Overloading]]
# [[Default Arguments]] 
Default arguments allow you to specify a default value for a function parameter. If the caller doesn't provide a value for that parameter, the default value is used.

```python
def greet(name, greeting="Hello"):
  print(f"{greeting}, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob", "Good morning")  # Output: Good morning, Bob!
```

**Important Considerations:**

* **Order Matters:** Default arguments must come *after* non-default arguments in the function definition.  This is because Python matches arguments based on their position.

```python
# Correct
def func(a, b=[[2]]):
    pass

# Incorrect - will raise a SyntaxError
def func(a=[[1]], b):
    pass
```

* **Mutability:** Be cautious when using mutable objects (like lists or dictionaries) as default arguments. The default value is created *only once* when the function is defined. Subsequent calls will modify the *same* object. [[Mutable Default Arguments]]

* **None as a Default:**  `None` is a good choice as a default for parameters that might not always be needed, avoiding the mutability issues mentioned above.

```python
def process_data(data=None):
  if data is None:
      data = [] #Create a new list if none is provided
  # ... process data ...
```


**Related Notes:**

* [[Function Definitions]]
* [[Function Calls]]

