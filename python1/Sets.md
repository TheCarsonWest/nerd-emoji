## Python [[Sets]]

### Explanation

[[Sets]] are a data structure in Python that store unique and unordered collections of elements. They are similar to [[Lists]], but they only allow each element to appear once. [[Sets]] are defined using curly braces {}, and their elements can be of any type.

### Parameters

[[Sets]] have the following parameters:

- **elements:** The elements of the set, enclosed in curly braces {}.
- **mutable:** [[Sets]] are mutable, meaning their elements can be added, removed, or modified.

### Code Examples

#### Creating a [[Set]]

```python
# Create a set of numbers
numbers = {1, 2, 3, 4, 5}

# Create a set of strings
fruits = {"apple", "banana", "cherry"}

# Create a set from a list
languages = [[set]]("Python", "Java", "C++")
```

#### Accessing Elements

[[Sets]] are unordered, so there is no way to access elements by index. However, you can use the `in` operator to check if an element is in the set.

```python
# Check if 3 is in the numbers set
print(3 in numbers)  # True

# Check if "apple" is in the fruits set
print("apple" in fruits)  # True
```

#### Adding Elements

To add an element to a [[Set]], use the `add` method.

```python
# Add 6 to the numbers set
numbers.add(6)

# Add "grape" to the fruits set
fruits.add("grape")
```

#### Removing Elements

To remove an element from a [[Set]], use the `remove` method.

```python
# Remove 3 from the numbers set
numbers.remove(3)

# Remove "banana" from the fruits set
fruits.remove("banana")
```

#### Other Python Concepts that Link Back to [[Sets]]

- **[[Lists]]**: [[Sets]] can be created from [[Lists]] using the `[[set]]` function.
- **[[Dictionaries]]**: [[Sets]] can be used as keys in [[Dictionaries]].
- **[[Tuples]]**: [[Sets]] can be converted to [[Tuples]] using the `[[tuple]]` function.
