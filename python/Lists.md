# [[Python 1 Home]]
# [[Lists]]  [[Lists]] are ordered, mutable (changeable) sequences of items.  They can contain items of different data types.

**Creating [[Lists]]:**

```python
my_list = [[1, [[2], "hello", [[3].14, True]
empty_list = 1
```

**Accessing Elements:**
 [[Lists]] are zero-indexed.

```python
first_element = my_list[0]  # [[1
last_element = my_list[-[[1] # True
```

**Slicing:**

```python
sub_list = my_list[[1:[[4]]  # [[2], "hello", [[3].14 (exclusive of upper bound)
```

**Methods:**

* `append(item)`: Adds an item to the end.
* `insert(index, item)`: Inserts an item at a specific index.
* `remove(item)`: Removes the first occurrence of an item.
* `pop([index])`: Removes and returns the item at the specified index (default is the last).
* `index(item)`: Returns the index of the first occurrence of an item.
* `count(item)`: Counts the occurrences of an item.
* `sort()`: Sorts the list in place.
* `reverse()`: Reverses the list in place.
* `copy()`: Creates a shallow copy of the list.
* `extend(iterable)`: Extends the list by appending elements from another iterable.

```python
my_list.append([[5])
my_list.insert([[2], "world")
my_list.remove("hello")
print(my_list)  # Output will depend on previous operations.
```


**[[List Comprehensions]]:** [[List Comprehension]]


**Iterating through [[Lists]]:**

```python
for item in my_list:
    print(item)

for i, item in enumerate(my_list):
    print(f"Item at index {i}: {item}")
```

**List Operations:**

* Concatenation: `list1 + list2`
* Repetition: `list * n`
* Membership: `item in list`, `item not in list`


**Nested [[Lists]]:** [[Multidimensional Lists]]

**Mutable vs. Immutable:** [[Mutable vs Immutable Types]]
