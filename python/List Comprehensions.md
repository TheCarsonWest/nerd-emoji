# [[For Loop Examples]]
# [[List Comprehensions]] 
List comprehensions provide a concise way to create lists in Python.  They're essentially a shorthand for a `for` loop combined with an optional conditional statement.

**Basic Syntax:**

```python
new_list = [expression for item in iterable if condition]] 
```

* `expression`:  What you want to do with each `item`.  This can be a simple transformation or a more complex calculation.
* `item`: A variable representing each element in the `iterable`.
* `iterable`:  Something you can iterate over (like a list, tuple, range, etc.).
* `if condition`: (Optional) A filter to include only items that meet a specific criteria.


**Examples:**

[[1. **Squaring numbers:**

```python
numbers = [[1, 2, 3, 4, 5
squares = [x**2 for x in numbers]]  # Output: [[1, 4, 9, 16, 25
```

2. **Filtering even numbers:**

```python
numbers = [[1, 2, 3, 4, 5, 6
even_numbers = [x for x in numbers if x % 2 == 0]] # Output: 2, 4, 6
```

3. **String manipulation:**

```python
words = ["hello", "world", "python"]]
uppercase_words = [word.upper() for word in words]] # Output: ['HELLO', 'WORLD', 'PYTHON']]
```

4. **Nested [[List Comprehension]] ([[Nested Loops]])**:  Creating a matrix:

```python
matrix = [[i*j for j in range(3]])]] for i in range(3)]] # Output: [[0, 0, 0]], [0, [[1, 2, [0, 2, 4
```


**Advantages:**

* **Readability:** Often more concise and easier to read than equivalent `for` loops.
* **Efficiency:**  Can be slightly faster than traditional loops in some cases, especially for simple operations.


**When NOT to use [[List Comprehensions]]:**

* **Complex logic:** If your logic involves multiple nested loops or very complex conditional statements, a traditional `for` loop might be clearer.
* **Side effects:** Avoid using list comprehensions if you need to perform actions that have side effects (like modifying external variables) within the comprehension.  This can lead to less readable and less maintainable code.


[[Iterable Objects]]
