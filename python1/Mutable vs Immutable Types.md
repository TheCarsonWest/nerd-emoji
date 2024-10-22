## [[Mutable vs Immutable Types]]

### Explanation
In Python, data types can be categorized as either mutable or immutable. Mutability refers to whether the value of a variable can be changed once it is created.

- **Mutable Types:** Allow modification of their values after creation, such as lists, dictionaries, and sets.
- **Immutable Types:** Do not allow modification of their values after creation, such as strings, tuples, and numbers (integers, floats, etc.).

### How to Use It
The mutability of a type is determined by its class. For example, `list()` is a mutable class, while `str()` is an immutable class.

### Code Examples
```python
# Mutable: list value can be modified
my_list = [1, 2, 3]
my_list[0] = 4

# Immutable: string value cannot be modified
my_string = "Hello"
# my_string[0] = 'W' # TypeError: 'str' object does not support item assignment
```

### Related Python Concepts
- [[Variables and Data Types]]: Mutable and immutable types are fundamental data types in Python.
- [[Lists]]: [[Lists]] are mutable sequences that can be modified in place.
- [[Tuples]]: [[Tuples]] are immutable sequences that cannot be modified.
- [[Dictionaries]]: [[Dictionaries]] are mutable mappings that can be modified in place.
- [[Sets]]: [[Sets]] are mutable collections that can be modified in place.
# [[Python 1 Home]]