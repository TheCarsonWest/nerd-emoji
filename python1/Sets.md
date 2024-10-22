## Python [[Sets]]

### What are [[Sets]]?
 [[Sets]] are an unordered collection of unique, immutable elements that can be used in various situations where you need to work with unique values and perform set operations like union, intersection, and difference. They are mutable, meaning that elements can be added or removed, but the order of elements is not guaranteed, and duplicate values are not allowed.

### How to Create a Set
 [[Sets]] can be created using curly braces ({}) or the `set()` constructor.

```python
# creating a set from a list
my_set = {"apple", "banana", "cherry"}

# creating an empty set
empty_set = set()
```

### Operations on [[Sets]]

 [[Sets]] support various operations, including:

- **Union (|):** Combines two sets and returns a new set containing all unique elements from both sets.
- **Intersection (&):** Returns a new set containing only the elements that are common to both sets.
- **Difference (-):** Returns a new set containing the elements that are in the first set but not in the second set.
- **Symmetric Difference (^):** Returns a new set containing the elements that are in either set but not in both sets.

### Code Examples

```python
# create two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# union
set3 = set1 | set2
print(set3) # output: {'apple', 'banana', 'cherry', 'google', 'microsoft'}

# intersection
set4 = set1 & set2
print(set4) # output: {'apple'}

# difference
set5 = set1 - set2
print(set5) # output: {'banana', 'cherry'}

# symmetric difference
set6 = set1 ^ set2
print(set6) # output: {'banana', 'cherry', 'google', 'microsoft'}
```

### Related Python Concepts

- [[Lists]]: Similar to sets, lists are also a collection of elements, but they allow duplicates and maintain the order of insertion.
- [[Tuples]]: [[Tuples]] are immutable collections similar to sets but with a fixed order of elements.
- [[Dictionaries]]: [[Dictionaries]] are mappings that associate keys to values, and they do not allow duplicate keys.
- [[Frozen [[Sets]]: Frozen sets are immutable versions of sets, meaning their elements cannot be modified.
- [[Set Comprehension]]: Set comprehension provides a concise way to create sets using a similar syntax to list comprehension.
# [[Python 1 Home]]