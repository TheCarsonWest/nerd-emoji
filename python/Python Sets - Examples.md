# [[Python Sets]]
# [[Python Sets - Examples]] 
This note covers examples of using [[Python Sets]].  Remember to consult [[Python Sets - Basics]] for foundational information.

**Creating Sets:**

Sets can be created in a few ways:

* Using curly braces `{}`:

```python
my_set = {[[1, 2, 3, 4}
print(my_set)  # Output: {[[1, 2, 3, 4}

empty_set = set() #This is the only way to create an empty set, {} creates an empty dictionary
print(empty_set) #Output: set()

another_set = {[[1, 2, "hello", 3.14} #Sets can contain different data types, but must be immutable(can't change once created)
print(another_set)
```

* Using the `set()` constructor:

```python
my_list = [[1, 2, 2, 3, 4, 4, 4  #Duplicates will be removed when converting to a set
my_set = set(my_list)
print(my_set)  # Output: {[[1, 2, 3, 4}

my_tuple = ([[1,2,3)
my_set = set(my_tuple)
print(my_set)
```

*[[Set Operations]]*

```python
set1 = {[[1, 2, 3}
set2 = {3, 4, 5}

# Union: combines elements from both sets.
union_set = set1 | set2  # Or: set1.union(set2)
print(f"Union: {union_set}")  # Output: {[[1, 2, 3, 4, 5}

# Intersection: returns common elements.
intersection_set = set1 & set2  # Or: set1.intersection(set2)
print(f"Intersection: {intersection_set}")  # Output: {3}

# Difference: elements in set1 but not in set2.
difference_set = set1 - set2  # Or: set1.difference(set2)
print(f"Difference (set1 - set2): {difference_set}")  # Output: {[[1, 2}

# Symmetric Difference: elements in either set, but not both.
symmetric_difference_set = set1 ^ set2  # Or: set1.symmetric_difference(set2)
print(f"Symmetric Difference: {symmetric_difference_set}")  # Output: {[[1, 2, 4, 5}

#Checking for subset and superset
set3 = {[[1,2}
print(f"Is set3 a subset of set1? {set3.issubset(set1)}") #True
print(f"Is set1 a superset of set3? {set1.issuperset(set3)}") #True

```


**Other Set Methods:**

```python
my_set = {[[1, 2, 3}
my_set.add(4)  # Adds an element.
print(my_set)  # Output: {[[1, 2, 3, 4}

my_set.remove(2)  # Removes an element; raises KeyError if not found.
print(my_set)  # Output: {[[1, 3, 4}

my_set.discard(5) #Removes an element if present, does not raise an error if not present
print(my_set)

my_set.pop() #Removes an arbitrary element, raises KeyError if set is empty
print(my_set)

my_set.clear() #Removes all elements from the set
print(my_set) #Output: set()
```

Remember to check out [[Python Sets - Advanced Techniques]] for more complex examples and applications.
