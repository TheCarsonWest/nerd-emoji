## Python [[List_Comprehension]]

**What is [[List_Comprehension]]?**

[[List_Comprehension]] is a concise way to create a new list from an existing one, transforming each element based on specified conditions. It is a powerful Python syntax that combines the functionality of loops and conditional statements into a single expression.

**Parameters of [[List_Comprehension]]:**

- `expression for item in iterable`
- **expression:** The transformation or calculation to be performed on each item.
- **item:** The individual element from the iterable.
- **iterable:** The original list or sequence to be iterated over.

**Code Examples:**

**Basic [[List_Comprehension]]:**

```python
numbers = 1, 2, 3, 4, 5
squared_numbers = x**2 for x in numbers
print(squared_numbers)  # Output: 1, 4, 9, 16, 25
```

**Conditional [[List_Comprehension]]:**

```python
numbers = 1, 2, 3, 4, 5
odd_numbers = x for x in numbers if x % 2 != 0
print(odd_numbers)  # Output: 1, 3, 5
```

**Nested [[List_Comprehension]]:**

```python
matrix = 1, 2, 3], 4, 5, 6, [7, 8, 9
flattened_matrix = item for row in matrix for item in row
print(flattened_matrix)  # Output: 1, 2, 3, 4, 5, 6, 7, 8, 9
```

**Other Python Concepts Linked to [[List_Comprehension]]:**

- [[Generators]]
- [[Lambda_Functions]]
- [[Map and Filter Functions]]