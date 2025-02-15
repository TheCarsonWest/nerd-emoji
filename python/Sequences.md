# [[Iterables]]
# [[Sequences]] in Python
 [[Sequences]] are a fundamental data structure in Python.  They are ordered collections of items, meaning that the order in which items are added matters, and each item has a specific index.  Several built-in types in Python are sequences.

Key characteristics:

* **Ordered:** Items maintain their relative positions.
* **Iterable:** You can loop through the items using `for` loops.
* **Indexable:** You can access items using their index (starting from 0).
* **Slicable:** You can extract portions of the sequence using slicing.

**Common Sequence Types:**

* **[[Lists]]:** Mutable (changeable) sequences. `[[1, 2, 'a', True]]`
```python
my_list = [[1, 2, 3
my_list.append(4)  # Add an item
my_list[0]] = 10   # Change an item
```

* **[[Tuples]]:** Immutable (unchangeable) sequences. `([[1, 2, 'a', True)`
```python
my_tuple = ([[1, 2, 3)
# my_tuple.append(4)  # This would raise an error because tuples are immutable
```

* **Strings:** [[Sequences]] of characters. `"Hello, world!"`
```python
my_string = "Python"
my_string[0]]  # Accesses 'P'
```

* **Ranges:**  [[Sequences]] of numbers.  `range(10)` generates numbers 0-9.
```python
for i in range(5):
    print(i) # prints 0, [[1, 2, 3, 4
```

* **bytes** and **bytearrays**:  [[Sequences]] of bytes.

**Sequence Operations:**

Many operations work consistently across different sequence types:


* **Indexing:** Accessing individual elements using their index (e.g., `my_list2`).
* **Slicing:** Extracting a portion of the sequence (e.g., `my_list[[1:3`).  ([[Slicing]])
* **Concatenation:** Combining sequences using the `+` operator (e.g., `list1 + list2`).
* **Membership testing:** Checking if an item is present using `in` or `not in` (e.g., `'a' in my_string`).
* **Iteration:** Looping through the elements using a `for` loop.
* **Length:** Getting the number of items using `len()` (e.g., `len(my_list)`).


**Further Notes:**

* [[Mutability]]
* [[Immutability]]
* [[Iteration in Python]]


