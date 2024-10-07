## [[List Comprehension]]

### What is [[List Comprehension]]?
List comprehension is a concise and readable syntax in Python that allows you to create a new list based on the elements of an existing list. It combines a for loop and a conditional statement into a single line of code.

### How to Use [[List Comprehension]]
The syntax of a list comprehension is:

```python
[expression for item in iterable if condition]
```

- `expression`: The expression to evaluate for each item in the iterable.
- `item`: The variable that represents each item in the iterable.
- `iterable`: The sequence or collection to iterate over.
- `condition` (optional): The condition to filter the elements of the iterable.

### Code Examples
```python
# create a new list with the squares of the numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]

# create a new list with the positive numbers from a list
positive_numbers = [x for x in numbers if x > 0]
```

### Related Python Concepts

- [[Lists]]: List comprehension creates new lists.
- [[For Loops]]: List comprehension uses a for loop syntax.
- [[Conditional Statements]]: List comprehension uses a conditional statement to filter elements.
- [[Functions]]: List comprehension can be used inside functions to create and return new lists.
- [[Map, Filter, and Reduce]]: List comprehension is similar to the map and filter functions.
# [[Python 1 Home]]