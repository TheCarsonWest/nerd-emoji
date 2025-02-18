# [[Variables and Data Types]]
# [[Variable Naming Conventions]] 
Python's variable naming follows specific conventions for readability and maintainability.  Inconsistent naming can lead to errors and make code harder to understand.


**Key Principles:**

* **Use descriptive names:** Names should clearly indicate the variable's purpose.  `user_age` is better than `x` or `a`.

* **Lowercase with underscores:**  For variables, use lowercase letters separated by underscores (`snake_case`).  e.g., `total_price`, `customer_name`.

* **Constants:** For constants (values that don't change), use all uppercase with underscores.  e.g., `MAX_VALUE`, `PI`.

* **Avoid reserved keywords:** Don't use Python's reserved keywords (e.g., `if`, `else`, `for`, `while`, `import`, `def`) as variable names.

* **Be consistent:** Maintain a consistent style throughout your code.


**Examples:**

```python
# Good examples
user_name = "Alice"
product_price = 99.99
is_active = True
MAX_ATTEMPTS = 3

# Bad examples
usrnm = "Bob"       # Too short and cryptic
productPrice = 10  # Inconsistent casing
2items = 2        # Starts with a number (invalid)
if = 1             # Uses a reserved keyword (invalid)

```

**Further Notes:**

* [[Data Types]]  (Understanding [[Data Types]] helps in choosing appropriate variable names.)
* [[Code Style Guides]] (PEP 8 provides detailed guidelines on Python style, including variable naming.)

**Example of referencing another note:**

For a more in-depth explanation on how to choose effective variable names, refer to [[Choosing Descriptive Variable Names]].

