# [[Function Parameters]]
# [[Iterable Unpacking]] 
Iterable unpacking is a powerful Python feature that allows you to assign elements of an iterable (like a list, tuple, or string) to multiple variables in a single line of code.  This is particularly useful for:

* **Simplifying code:**  Avoids the need for explicit indexing or iteration.
* **Improving readability:** Makes code cleaner and easier to understand.
* **Working with functions that return multiple values:**  Many functions return tuples of values; unpacking makes accessing these values straightforward.


**Basic Syntax:**

```python
my_list = [10, 20, 30]
a, b, c = my_list  # Unpacks the list into three variables
print(a, b, c)  # Output: 10 20 30
```

**Extended Unpacking with the Asterisk Operator (`*`):**

This is used when you don't know the exact number of elements in the iterable or want to collect remaining items into a single variable.

```python
my_list = [1, 2, 3, 4, 5]
first, *rest = my_list  # first gets 1, rest gets [2, 3, 4, 5]
print(first)  # Output: 1
print(rest)  # Output: [2, 3, 4, 5]

*head, tail = my_list # head gets [1,2,3,4], tail gets 5
print(head) # Output: [1,2,3,4]
print(tail) # Output: 5

first, *middle, last = my_list #first gets 1, last gets 5, middle gets [2,3,4]
print(first) #Output: 1
print(middle) #Output: [2,3,4]
print(last) #Output: 5

```


**Unpacking in Function Arguments:**

```python
def my_function(x, y, z):
  print(f"x: {x}, y: {y}, z: {z}")

my_tuple = (100, 200, 300)
my_function(*my_tuple) # Output: x: 100, y: 200, z: 300
```

**Error Handling:**

If the number of variables on the left-hand side doesn't match the number of elements in the iterable, you'll get a `ValueError`.

```python
my_list = [1, 2]
a, b, c = my_list  # ValueError: too many values to unpack (expected 3)
```


**Related Notes:**

* [[Iterators]]
* [[Generators]]
* [[Tuples]]
* [[Lists]]


