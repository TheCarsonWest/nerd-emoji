## Python List Comprehension

**What is List Comprehension?**

List comprehension is a concise way to create a new list from an existing one, transforming each element based on specified conditions. It is a powerful Python syntax that combines the functionality of loops and conditional statements into a single expression.

**Parameters of List Comprehension:**

- `[expression for item in iterable]`
- **expression:** The transformation or calculation to be performed on each item.
- **item:** The individual element from the iterable.
- **iterable:** The original list or sequence to be iterated over.

**Code Examples:**

**Basic List Comprehension:**

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

**Conditional List Comprehension:**

```python
numbers = [1, 2, 3, 4, 5]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)  # Output: [1, 3, 5]
```

**Nested List Comprehension:**

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [item for row in matrix for item in row]
print(flattened_matrix)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Other Python Concepts Linked to List Comprehension:**

- **Generators:** List comprehensions are similar to generators in that they produce values lazily, one at a time.
- **Lambda Functions:** Lambda functions can be used within list comprehensions to specify the transformation or calculation.
- **Map and Filter Functions:** List comprehensions can be used as concise alternatives to the `map()` and `filter()` functions.
[[Python 1 Home]]