# [[For Loop Examples]]
# [[Range Function]] 
The `range()` function in Python is a built-in function that generates a sequence of numbers.  It's commonly used in loops to iterate a specific number of times.

**Syntax:**

```python
range(stop)
range(start, stop[, step]])
```

* `stop`:  The ending number (exclusive).  The sequence will go up to, but not include, this number.  This is the *only* required argument.
* `start`: The starting number (inclusive). Defaults to 0 if not specified.
* `step`: The increment between each number. Defaults to 1 if not specified.  Can be negative for reverse iteration.


**Examples:**

```python
# Basic usage:
for i in range(5):  # iterates 0, 1, 2, 3, 4
    print(i)

# Specifying start and stop:
for i in range(2, 7): # iterates 2, 3, 4, 5, 6
    print(i)

# Specifying start, stop, and step:
for i in range(1, 10, 2): # iterates 1, 3, 5, 7, 9
    print(i)

# Negative step:
for i in range(10, 0, -1): # iterates 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    print(i)

#Creating a list from range:
my_list = list(range(1,6)) # Creates 1, 2, 3, 4, 5
print(my_list)
```

**Important Considerations:**

* `range()` returns a *range object*, not a list.  This is a memory-efficient way to represent a sequence of numbers, especially when dealing with large ranges.  To get a list, you need to explicitly convert it using `list()`.
* The `stop` value is *always* exclusive.  This is a common source of off-by-one errors.


[[Range Object]]  ([[Iteration in Python]])
