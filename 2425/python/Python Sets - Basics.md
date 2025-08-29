# [[Python Sets - Examples]]
# [[Python Sets - Basics]] 
Key Features:

* Unordered collections of unique elements.
* Defined using curly braces `{}` or the `set()` constructor.
* Mutable (can be changed after creation).
* Do not allow duplicate elements; attempting to add a duplicate has no effect.
* Support mathematical [[Set Operations]] (union, intersection, difference, etc.).


**Creating Sets:**

```python
# Using curly braces
my_set = {1, 2, 3, 4} 
print(my_set)  # Output: {1, 2, 3, 4} (order may vary)

# Using the set() constructor
my_set2 = set(5, 6, 7, 7)  # Duplicates are automatically removed
print(my_set2) # Output: {5, 6, 7}

my_set3 = set("hello") #creating a set from a string.
print(my_set3) # Output: {'h', 'e', 'l', 'o'}

empty_set = set() #creating an empty set.  (Note: {} creates an empty dictionary!)
```

**Basic Operations:**

```python
my_set = {1, 2, 3}
my_set.add(4) # Adds 4 to the set.
print(my_set) #Output: {1, 2, 3, 4}

my_set.remove(2) #removes 2 from the set, raises error if 2 isn't present.
print(my_set) #Output: {1, 3, 4}

my_set.discard(5) # removes 5 if it exists, doesn't raise an error otherwise.
print(my_set) #Output: {1, 3, 4}

my_set.pop() # Removes and returns an arbitrary element.  Sets are unordered, so the output is unpredictable
print(my_set)


my_set.clear() # Removes all elements.
print(my_set) #Output: set()

```

**[[Set Operations]]:**

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1 | set2 # or set1.union(set2)
print(f"Union: {union_set}") # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1 & set2 # or set1.intersection(set2)
print(f"Intersection: {intersection_set}") # Output: {3}

# Difference
difference_set = set1 - set2 # or set1.difference(set2)
print(f"Difference (set1 - set2): {difference_set}") # Output: {1, 2}

# Symmetric Difference
symmetric_difference_set = set1 ^ set2 # or set1.symmetric_difference(set2)
print(f"Symmetric Difference: {symmetric_difference_set}") # Output: {1, 2, 4, 5}

#Checking for Subsets and Supersets
set3 = {1,2}
print(f"Is set3 a subset of set1?: {set3.issubset(set1)}") #True
print(f"Is set1 a superset of set3?: {set1.issuperset(set3)}") #True

```

**Other Useful Methods:**

* `len(my_set)`: Returns the number of elements.
* `x in my_set`: Checks if `x` is an element of the set.
* `x not in my_set`: Checks if `x` is not an element of the set.

[[Set Comprehension]]
[[Frozen Sets]]
