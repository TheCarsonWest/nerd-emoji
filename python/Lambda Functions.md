# [[Python 1 Home]]
# Lambda Functions

Lambda functions are small, anonymous functions defined using the `lambda` keyword.  They are useful for short, simple operations that don't require a full function definition.

```python
square = lambda x: x**2
print(square(5))  # Output: 25

add = lambda x, y: x + y
print(add(3, 4))  # Output: 7
```

Lambda functions are often used with higher-order functions like `map`, `filter`, and `reduce`. [[Higher-Order Functions]]

**Example with `map`:**

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

**Example with `filter`:**

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

Lambda functions can only contain a single expression, which is implicitly returned.  They cannot have multiple statements or complex logic.  For more complex operations, a regular function definition is preferred. [[Python Functions]]


