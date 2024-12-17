# [[Python 1 Home]]
# [[Dictionaries]]  [[Dictionaries]] are unordered collections of key-value pairs.  Keys must be immutable (like strings, numbers, or tuples), while values can be of any data type.

```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"])  # Accessing values using keys
```

Accessing a non-existent key raises a `KeyError`.  Use the `get()` method for safer access:

```python
print(my_dict.get("country", "Unknown")) # Returns "Unknown" if "country" is not found
```

Adding and modifying entries:

```python
my_dict["occupation"] = "Engineer"
my_dict["age"] = 31
```

Iterating through dictionaries:

```python
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)
```

Other useful methods:

* `keys()`: Returns a view object containing keys.
* `values()`: Returns a view object containing values.
* `items()`: Returns a view object containing key-value pairs as tuples.
* `pop(key)`: Removes and returns the value associated with the key.
* `popitem()`: Removes and returns an arbitrary key-value pair.
* `clear()`: Removes all items.
* `copy()`: Creates a shallow copy.


[[Dictionary Comprehension]], [[Mutable vs Immutable Types]]
