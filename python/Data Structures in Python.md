# [[Mutable vs Immutable Types]]
# [[Data Structures in Python]] 
This note covers the fundamental data structures in Python.  I'll need to expand on several of these in separate notes.

**[[1. Built-in Data Structures:**

Python offers several built-in data structures:

* **[[Lists]]:** Ordered, mutable (changeable) sequences of items.  Allow duplicate elements.

```python
my_list = [[1, 2, "hello", 3.14, True]]
```

* **[[Tuples]]:** Ordered, immutable (unchangeable) sequences of items. Allow duplicate elements.  Useful for representing fixed collections of data.

```python
my_tuple = ([[1, 2, "hello", 3.14, True)
```

* **Sets:** Unordered collections of unique items.  Useful for membership testing and eliminating duplicates.

```python
my_set = {[[1, 2, 3, 3, 4} # {[[1, 2, 3, 4}
```

* **[[Dictionaries]]:**  Unordered collections of key-value pairs.  Keys must be immutable (e.g., strings, numbers, tuples), values can be any data type.  Provides efficient lookups by key.

```python
my_dict = {"name": "Alice", "age": 30, "city": "[[New York]]"}
```


**2.  Data Structure Operations:**

Each data structure has its own set of operations (methods):

* **[[Lists]]:**  `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `index()`, `count()` etc.  ([[List Methods]])
* **[[Tuples]]:**  Limited operations due to immutability.  `index()`, `count()`. ([[Tuple Methods]])
* **Sets:** `add()`, `remove()`, `union()`, `intersection()`, `difference()` etc. ([[Set Methods]])
* **[[Dictionaries]]:** `get()`, `items()`, `keys()`, `values()`, `update()`, `pop()`, `popitem()` etc. ([[Dictionary Methods]])


**3. Choosing the Right Data Structure:**

The choice of data structure depends on the specific needs of your program:

* Use lists when you need an ordered, mutable sequence.
* Use tuples when you need an ordered, immutable sequence.
* Use sets when you need to store unique items and perform set operations.
* Use dictionaries when you need to store data in key-value pairs for efficient lookups.


**4.  More Advanced Data Structures ([[Advanced Data Structures]])**

This section will cover more advanced data structures, like:

* **Deque (double-ended queue):**  Efficient for adding and removing elements from both ends.
* **Namedtuple:**  Similar to tuples, but with named fields for better readability.
* **Counter:**  A dictionary subclass for counting hashable objects.
* **OrderedDict (deprecated in Python 3.7+):**  Maintained order of insertion. (Use `collections.OrderedDict` if needed for older Python versions).


**5.  Further Reading:**

* Python documentation on built-in types.
* Relevant chapters in a Python textbook.


**Linked Notes:** [[List Methods]], [[Tuple Methods]], [[Set Methods]], [[Dictionary Methods]], [[Advanced Data Structures]]
