**Python For Loops**

**Concept:**

A `for` loop is a control flow statement used to iterate over a sequence of items, such as a list, tuple, or string. It allows you to execute a block of code for each item in the sequence.

**Parameters:**

* **Iterable Sequence:** The sequence of items to iterate over.
* **Item Variable:** The variable used to store the current item in the sequence.

**Syntax:**

```python
for item_variable in iterable_sequence:
    # Block of code to execute for each item
```

**Code Examples:**

```python
# Iterate over a list
my_list = [1, 2, 3]
for number in my_list:
    print(number)  # Output: 1, 2, 3

# Iterate over a tuple
my_tuple = (1, 2, 3)
for number in my_tuple:
    print(number)  # Output: 1, 2, 3

# Iterate over a string
my_string = "Hello World"
for character in my_string:
    print(character)  # Output: H, e, l, l, o,  , W, o, r, l, d
```

**Other Python Concepts:**

* **Range Function:** The `range()` function generates a sequence of numbers that can be used as the iterable sequence in a `for` loop.
* **Enumerate Function:** The `enumerate()` function returns a tuple of the index and the item for each element in the sequence, which can be useful in some loop scenarios.
* **Iterables:** A concept in Python that refers to objects that can be iterated over, such as lists, tuples, and strings.
* **Iterable Unpacking:** The ability to unpack multiple items from an iterable into separate variables within a `for` loop.