## Python Sets

### Definition

A Python set is an unordered collection of unique and immutable objects. It is a mutable data structure, meaning its contents can be modified after creation.

### Parameters

Sets have no parameters. You can create an empty set using the `set()` constructor or by using curly braces `{}`.

### Operations

#### Creation

```python
my_set = set()  # Creates an empty set
my_set = {1, 2, 3}  # Creates a set with three elements
```

#### Adding Elements

```python
my_set.add(4)  # Adds 4 to the set
my_set.update([5, 6, 7])  # Adds multiple elements from a list
```

#### Removing Elements

```python
my_set.remove(3)  # Removes 3 from the set
my_set.discard(4)  # Removes 4 from the set if it exists (no error)
```

#### Mathematical Operations

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Union (combines both sets, removing duplicates)
set1.union(set2)  # {1, 2, 3, 4}

# Intersection (elements common to both sets)
set1.intersection(set2)  # {2, 3}

# Difference (elements in set1 not in set2)
set1.difference(set2)  # {1}
```

#### Other Operations

```python
# Check if an element is in the set
my_set.__contains__(1)  # True

# Get the number of elements in the set
len(my_set)  # 3

# Convert to a list
list(my_set)  # [1, 2, 3]
```

### Linked Concepts

* **Dictionaries:** Sets can be used as keys in dictionaries.
* **Lists:** Sets can be used to remove duplicates from lists.
* **Tuples:** Sets can be used to create frozen sets, which are immutable.