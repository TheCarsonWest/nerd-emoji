**Python For Loops**

**Explanation:**

A for loop is a control flow statement used in Python to iterate over a sequence (list, tuple, string, etc.) and execute a set of statements for each element in the sequence.

**Parameters:**

* **Iterable (required):** The sequence (list, tuple, string, etc.) to iterate over.
* **Variable (required):** A variable to hold the current element of the iterable.
* **Range of Numbers (optional):** Specifies a range of numbers to iterate over using the syntax `range(start, stop, step)`.
* ** else:** An optional clause that executes after the loop has completed.

**Code Examples:**

**Iterating over a List:**

```python
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)
```

**Iterating over a Tuple:**

```python
my_tuple = (1, 2, 3, 4, 5)

for item in my_tuple:
    print(item)
```

**Iterating over a String:**

```python
my_string = "Hello World"

for char in my_string:
    print(char)
```

**Iterating over a Range of Numbers:**

```python
for i in range(1, 6):
    print(i)
```

**Using the else Clause:**

```python
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)
else:
    print("Loop completed successfully.")
```

**Other Python Concepts Linked to For Loops:**

* **Iterables:** Objects that can be iterated over, such as lists, tuples, strings, and ranges.
* **Control Flow:** Statements that control the flow of execution, such as if-else statements and while loops.
* **Ranges:** Objects that generate consecutive numbers, used to iterate over a specific range.
* **List Comprehensions:** A compact way to create new lists by iterating over an iterable.
[[Python 1 Home]]