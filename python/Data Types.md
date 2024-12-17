# [[Variable Naming Conventions]]
# [[Data Types]] 
Python has several built-in data types.  Here's a breakdown:

* **Numeric Types:**
    * `int`: Integers (e.g., 10, -5, 0)
    * `float`: Floating-point numbers (e.g., 3.14, -2.5, 0.0)
    * `complex`: Complex numbers (e.g., 2+3j)

* **Text Type:**
    * `str`: Strings (e.g., "hello", 'Python', """multiline string""")

* **Sequence Types:**
    * `list`: Ordered, mutable sequence of items (e.g., `[1, 2, "apple", 3.14]`)
    * `tuple`: Ordered, immutable sequence of items (e.g., `(1, 2, "apple", 3.14)`)
    * `range`: Represents a sequence of numbers (e.g., `range(10)`)

* **Mapping Type:**
    * `dict`: Unordered collection of key-value pairs (e.g., `{"name": "Alice", "age": 30}`)

* **Set Types:**
    * `set`: Unordered collection of unique items (e.g., `{1, 2, 3}`)
    * `frozenset`: Immutable set (e.g., `frozenset({1, 2, 3})`)

* **Boolean Type:**
    * `bool`: Represents truth values (`True` or `False`)

* **Binary Types:**
    * `bytes`: Immutable sequence of bytes
    * `bytearray`: Mutable sequence of bytes
    * `memoryview`: Allows access to the internal data of an object without copying


**Example Code:**

```python
my_int = 10
my_float = 3.14
my_string = "Hello, world!"
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_dict = {"a": 1, "b": 2}
my_set = {1, 2, 3}
my_bool = True
```

**Type Conversion:**

Python allows type conversion (casting) between data types using functions like `int()`, `float()`, `str()`, etc.  However, not all conversions are possible (e.g., converting a string containing letters to an integer will raise an error).

```python
x = 10  # int
y = float(x)  # convert to float
z = str(x)   # convert to string
```

[[Type Conversion]]  [[Mutability]]  [[Immutability]] [[Sequence Types in Detail]] [[Dictionary Methods]]
