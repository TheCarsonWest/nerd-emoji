# [[Python Sets]]
# [[Frozen Sets]] 
Frozen sets are immutable versions of Python's built-in `set` type.  This means once a frozen set is created, its elements cannot be added or removed.  They are hashable, unlike regular sets, which makes them suitable as keys in dictionaries or elements of other sets.

**Key Characteristics:**

* **Immutability:**  The defining characteristic.  No changes after creation.
* **Hashability:** Allows use as dictionary keys or set elements.
* **Membership Testing:**  `in` and `not in` operators work efficiently.
* **[[Set Operations]]:**  Standard set operations (union, intersection, difference, etc.) are supported, but always return *new* frozen sets.

**Creation:**

Frozen sets are created using the `frozenset()` constructor:

```python
my_set = {1, 2, 3}
frozen_set = frozenset(my_set)  # Create a frozen set from a regular set

empty_frozen_set = frozenset() # Create an empty frozen set

another_frozen_set = frozenset(4,5,6) #from a list

```

**Operations:**

```python
set1 = frozenset({1, 2, 3})
set2 = frozenset({3, 4, 5})

union_set = set1 | set2  # Union
intersection_set = set1 & set2 # Intersection
difference_set = set1 - set2  # Difference
symmetric_difference_set = set1 ^ set2 #Symmetric Difference

print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference (set1 - set2): {difference_set}")
print(f"Symmetric Difference: {symmetric_difference_set}")

#Membership testing
print(f"Is 3 in set1? {3 in set1}")

#Attempting to modify (will raise an error)
# set1.add(4) # AttributeError: 'frozenset' object has no attribute 'add'

```

**Use Cases:**

*   Dictionary keys:  Because they are hashable.
*   Representing constant collections of data where immutability is desired.
*   Data structures that require elements to be unique and unchanging.


[[Set Operations]]  ([[Python Sets]])
