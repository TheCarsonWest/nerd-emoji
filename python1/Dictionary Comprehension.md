## Python [[Dictionary Comprehension]]

### What is [[Dictionary Comprehension]]?
Dictionary comprehension is a concise syntax in Python that allows for the creation of dictionaries from iterable sequences. It provides a convenient way to generate dictionaries where the keys and values are derived from the input iterables.

### How to Use [[Dictionary Comprehension]]
Dictionary comprehension is expressed in the following format:

```python
{key: value for key, value in iterable}
```

- `key`: Represents the key for each item in the resulting dictionary.
- `value`: Represents the value associated with each key.
- `iterable`: An iterable sequence that provides values for both the key and value.

### Code Examples
```python
# create a dictionary with square numbers as keys and squares as values
squares = {x: x * x for x in range(1, 6)}

# create a dictionary with names and ages from a list of tuples
data = [('John', 25), ('Mary', 30), ('Bob', 28)]
ages = {name: age for name, age in data}
```

### Related Python Concepts
- [[List Comprehension]]: Similar to dictionary comprehension, but used for creating lists.
- [[Generators]]: Can be used to create iterables for dictionary comprehension.
- [[Functions]]: Lambda functions can be used as expressions for keys and values.
- [[For Loops]]: Dictionary comprehension can be seen as a concise form of a for loop.
- [[Operators]]: Conditional and mathematical operators can be used in the key or value expressions.
# [[Python 1 Home]]