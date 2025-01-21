# [[Python Sets - Examples]]
# [[Python Sets - Advanced Techniques]] 
This note covers advanced techniques related to [[Python Sets]] beyond basic creation and operations.  We'll assume basic set understanding (see [[Python Sets - Basics]]).

## Set Comprehensions

Similar to [[List Comprehensions]], set comprehensions provide a concise way to create sets.

```python
# Create a set of squares of even numbers
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0, 4, 16, 36, 64}

# Create a set from a string, removing duplicates
unique_chars = {char for char in "abracadabra"}
print(unique_chars)  # Output: {'a', 'b', 'r', 'c', 'd'}
```

## [[Set Operations]] on Multiple Sets

Python supports efficient operations on multiple sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

# Union: combines all elements from all sets
union_set = set1 | set2 | set3  # or set1.union(set2, set3)
print(f"Union: {union_set}") # Output: {1, 2, 3, 4, 5, 6, 7}

# Intersection: elements common to all sets
intersection_set = set1 & set2 & set3 # or set1.intersection(set2, set3)
print(f"Intersection: {intersection_set}") # Output: set()

# Difference: elements in set1 but not in set2
difference_set = set1 - set2 # or set1.difference(set2)
print(f"Difference (set1 - set2): {difference_set}") # Output: {1, 2}

# Symmetric Difference: elements in either set1 or set2, but not both
symmetric_difference_set = set1 ^ set2 # or set1.symmetric_difference(set2)
print(f"Symmetric Difference: {symmetric_difference_set}") # Output: {1, 2, 4, 5}
```


## [[Frozen Sets]] 
[[Frozen Sets]] are immutable versions of sets.  Once created, their elements cannot be added or removed.  Useful when a set needs to be used as a key in a dictionary or as an element in another set.

```python
frozen_set1 = frozenset({1, 2, 3})
# frozen_set1.add(4)  # This will raise an AttributeError

dictionary = {frozen_set1: "value"} #  Can be used as dictionary keys
```

##  Set Methods for Advanced Manipulation

Explore the following methods for more complex set manipulations (refer to Python documentation for detailed explanations):


* `set.issubset()`: Checks if one set is a subset of another.
* `set.issuperset()`: Checks if one set is a superset of another.
* `set.discard()`: Removes an element if it exists (doesn't raise an error if not present).
* `set.remove()`: Removes an element; raises an error if not present.
* `set.pop()`: Removes and returns an arbitrary element. Raises KeyError if set is empty.
* `set.clear()`: Removes all elements from the set.
* `set.copy()`: Creates a shallow copy of the set.


[[Python Sets - Basics]]

