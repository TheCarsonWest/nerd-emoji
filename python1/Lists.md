## Python [[Lists]]

### What are [[Lists]]?
 [[Lists]] are one of the most versatile data structures in Python. They are ordered collections of elements that can be accessed and modified by index. [[Lists]] are mutable, which means their contents can be changed during program execution.

### How to Use [[Lists]]
 [[Lists]] can be created using square brackets `[]`. The elements of a list are separated by commas.

```python
my_list = [1, 2, 3, 4, 5]
```

 [[Lists]] can also be created from other iterables, such as tuples and strings.

```python
my_list = list((1, 2, 3, 4, 5))
my_list = list("Python")
```

**Accessing List Elements:**
Individual elements of a list can be accessed by index. The index of the first element is 0, and the index of the last element is the length of the list minus 1.

```python
print(my_list[0]) # 1
print(my_list[-1]) # 5
```

**Modifying List Elements:**
Elements of a list can be modified by assigning a new value to the corresponding index.

```python
my_list[0] = 10
```

### Code Examples
```python
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Add an element to the end of the list
numbers.append(6)

# Remove an element from the list by index
del numbers[2]

# Sort the list in ascending order
numbers.sort()
```

### Related Python Concepts
- [[Variables and Data Types]]: [[Lists]] are a type of data structure that can store multiple values.
- [[Mutable vs Immutable Types]]: [[Lists]] are mutable, meaning their contents can be modified.
- [[For Loops]]: For loops can be used to iterate over the elements of a list.
- [[List Comprehension]]: List comprehensions provide a concise way to create new lists based on existing lists.
- [[Multidimensional [[Lists]]: [[Lists]] can be nested to create multidimensional data structures.
# [[Python 1 Home]]