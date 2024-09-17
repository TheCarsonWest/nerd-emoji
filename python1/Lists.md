## [[Lists]]

**What it is:**

* A [[Lists]] is an ordered sequence of elements enclosed in square brackets ().
* Elements can be of any data type, including other [[Lists]].

**Parameters:**

* **len(list):** Returns the number of elements in the [[Lists]].
* **listindex:** Accesses an element at a specified index.
* **liststart:end**:** Slices the [[Lists]] and returns a new [[Lists]] containing elements from the start index (inclusive) to the end index (exclusive).

**Code Examples:**

**Creating a [[Lists]]:**
```python
my_list = 1, 2, 3, 4
```

**Accessing Elements:**
```python
print(my_list0)  # Output: 1
```

**Modifying Elements:**
```python
my_list2 = 5
print(my_list)  # Output: 1, 2, 5, 4
```

**Adding and Removing Elements:**

**append(element):** Adds an element to the end of the [[Lists]].
```python
my_list.append(6)
print(my_list)  # Output: 1, 2, 5, 4, 6
```

**insert(index, element):** Inserts an element at a specified index.
```python
my_list.insert(0, 0)
print(my_list)  # Output: 0, 1, 2, 5, 4, 6
```

**pop(index):** Removes an element at a specified index and returns it.
```python
removed_element = my_list.pop(2)
print(removed_element)  # Output: 2
print(my_list)  # Output: 0, 1, 5, 4, 6
```

**Other [[Python]] Concepts that Link to [[Lists]]:**

* [[Tuples]]: Immutable sequences of elements.
* [[Sets]]: Unordered collections of unique elements.
* [[Dictionaries]]: Unordered collections of key-value pairs.
* [[Iterations]]: Using `for` loops or [[List Comprehension]] to iterate through [[Lists]].