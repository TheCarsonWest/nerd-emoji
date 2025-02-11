# [[Mutable vs Immutable Types]]
# [[Immutable Types]]: Deeper Dive

This note expands on the concept of immutability in Python.  Key [[Immutable Types]] include:

* `int` (integers)
* `float` (floating-point numbers)**
* `bool` (booleans)
* `str` (strings)
* `tuple` ([[Tuples]])
* `frozenset` ([[Frozen Sets]])


**What does immutability mean?**

It means that once an immutable object is created, its value cannot be changed.  Any operation that *appears* to modify an immutable object actually creates a *new* object with the modified value.

**Example (Strings):**

```python
my_string = "hello"
my_string += " world"  # This doesn't modify my_string in place.
print(id(my_string)) # print memory location of original string
my_string2 = my_string # assigning the same value to another variable.
print(id(my_string2)) # shows that it is the same memory location as my_string.
print(my_string)  # Output: hello world
print(id(my_string)) # shows a new memory location, because we created a new string.
```

**Example ([[Tuples]]):**

```python
my_tuple = ([[1, [[2], [[3])
# my_tuple[0] = [[4]  # This will raise a TypeError: 'tuple' object does not support item assignment.
new_tuple = my_tuple + ([[4],) # creates a new tuple with value [[4] concatenated.
print(new_tuple) # Output: ([[1, [[2], [[3], [[4])
```

**Implications of Immutability:**

* **Thread safety:** Immutable objects can be safely shared between multiple threads without the risk of data corruption. [[Thread Safety]]
* **Data integrity:**  You can be confident that the value of an immutable object will not change unexpectedly.
* **Hashing:**  Immutable objects can be used as keys in [[Dictionaries]] because their hash value remains constant. [[Hashing in Python]]
* **Performance:** While creating new objects might seem inefficient, Python's memory management often optimizes this.  However, frequent modifications to large immutable objects can impact performance.


**Contrast with Mutable Types:**

Mutable types, like [[Lists]] and [[Dictionaries]], *can* be modified in place.  This allows for more flexibility but also introduces potential risks related to concurrency and unintended side effects. [[Mutable Types in Python]]


**Further Exploration:**

* Deep vs. shallow copying with immutable and mutable objects. [[Deep vs. Shallow Copy]]
* Understanding how Python's garbage collector handles immutable objects. [[Python Garbage Collection]]

