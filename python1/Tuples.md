## Python Tuples

### Introduction

A tuple is an ordered collection of immutable objects in Python. It is similar to a list, but cannot be changed once created. Tuples are often used to store data that should not be modified, such as coordinates or dates.

### Parameters

* **Ordered:** Tuples are ordered, meaning that the elements in a tuple are accessed by their index.
* **Immutable:** Tuples are immutable, meaning that they cannot be modified once created.
* **Heterogeneous:** Tuples can store elements of different data types.
* **Tuple Size:** Tuples can be of any size.

### Creation

Tuples can be created using the tuple() function or by enclosing elements in parentheses.

```python
# Using the tuple() function
my_tuple = tuple([1, 2, 3])

# Using parentheses
my_tuple = (1, 2, 3)
```

### Accessing Elements

Elements in a tuple can be accessed using their index.

```python
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1
```

### Slicing

Tuples can be sliced to obtain a subtuple.

```python
my_tuple = (1, 2, 3, 4, 5)
sub_tuple = my_tuple[1:3]  # Output: (2, 3)
```

### Concatenation

Tuples can be concatenated using the + operator.

```python
my_tuple1 = (1, 2, 3)
my_tuple2 = (4, 5, 6)
new_tuple = my_tuple1 + my_tuple2  # Output: (1, 2, 3, 4, 5, 6)
```

### Other Python Concepts

* **Lists:** Lists are similar to tuples, but can be modified.
* **Sets:** Sets are unordered collections of unique elements.
* **Dictionaries:** Dictionaries are collections of key-value pairs.
[[Python 1 Home]]