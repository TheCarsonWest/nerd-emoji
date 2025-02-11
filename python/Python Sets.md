# [[Python [[1]] Home]]
# [[Python Sets]]

Python sets are unordered collections of unique elements.  They are defined using curly braces `{}` or the `set()` constructor.

```python
my_set = {[[1]], [[2]], [[3]], [[3]], [[4]]}  # Duplicates are automatically removed
print(my_set)  # Output: {[[1]], [[2]], [[3]], [[4]]}

another_set = set([[[5]], [[6]], [[7]]]) # Creating a set from a list
print(another_set) # Output: {[[5]], [[6]], [[7]]}

empty_set = set() #Creating an empty set.  Note: {} creates an empty dictionary.
print(empty_set) #Output: set()
```

**Key [[Set Operations]]:**

* **`union()` or `|`:** Combines elements from two sets.
```python
set1 = {[[1]], [[2]], [[3]]}
set2 = {[[3]], [[4]], [[5]]}
union_set = set1.union(set2) #or set1 | set2
print(union_set)  # Output: {[[1]], [[2]], [[3]], [[4]], [[5]]}
```

* **`intersection()` or `&`:** Returns common elements.
```python
intersection_set = set1.intersection(set2) #or set1 & set2
print(intersection_set)  # Output: {[[3]]}
```

* **`difference()` or `-`:** Returns elements in the first set but not the second.
```python
difference_set = set1.difference(set2) #or set1 - set2
print(difference_set)  # Output: {[[1]], [[2]]}
```

* **`symmetric_difference()` or `^`:** Returns elements in either set, but not both.
```python
symmetric_difference_set = set1.symmetric_difference(set2) #or set1 ^ set2
print(symmetric_difference_set)  # Output: {[[1]], [[2]], [[4]], [[5]]}
```

* **`add()`:** Adds an element.
```python
my_set.add([[5]])
print(my_set)
```

* **`remove()`:** Removes an element; raises KeyError if not present.
* **`discard()`:** Removes an element; does nothing if not present.
* **`pop()`:** Removes and returns an arbitrary element.
* **`clear()`:** Removes all elements.
* **`issubset()`:** Checks if one set is a subset of another.
* **`issuperset()`:** Checks if one set is a superset of another.
* **`isdisjoint()`:** Checks if two sets have no common elements.


[[Frozen Sets]]
[[Python Sets]] - Examples]]

**Set Comprehension:** Similar to [[List Comprehension]], but creates a set.

```python
squares = {x**[[2]] for x in range([[5]])}
print(squares)  # Output: {0, [[1]], [[4]], 9, 16}
```

