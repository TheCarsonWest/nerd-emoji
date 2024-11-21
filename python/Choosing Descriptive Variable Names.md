# [[Variable Naming Conventions]]
# Choosing Descriptive Variable Names

This note covers best practices for choosing descriptive variable names in Python.  The goal is to write code that is readable and maintainable.

**Key Principles:**

* **Clarity over brevity:**  A slightly longer, descriptive name is far better than a short, cryptic one.  For example, `customer_total_price` is superior to `ctp`.

* **Reflect the data:** The name should accurately reflect the type and purpose of the data stored in the variable.  If a variable holds a list of user IDs, `user_ids` is a better choice than `data` or `items`.

* **Consistency:**  Use a consistent naming style throughout your code.  Python's standard style guide (PEP 8) recommends `snake_case` (all lowercase with underscores separating words).

* **Avoid reserved keywords:** Don't use Python keywords (e.g., `if`, `else`, `for`, `while`, `class`, `def`, etc.) as variable names.

* **Meaningful prefixes/suffixes:**  In some cases, prefixes or suffixes can improve readability, especially when dealing with collections or specific data types.  For example: `user_count`, `product_list`, `is_active`.


**Examples:**

**Good:**

```python
customer_name = "Alice Smith"
order_total = 150.50
product_prices = [10.99, 25.00, 5.75]
is_logged_in = True
```

**Bad:**

```python
n = "Alice Smith"  # What does 'n' represent?
t = 150.50        # Too cryptic
p = [10.99, 25.00, 5.75] #What is p?
l = True         # What does 'l' mean?
```


**Further Considerations:**

* [[Data Types in Python]] - Understanding different data types helps choose appropriately descriptive names.
* [[Python Style Guide (PEP 8)]] -  Provides detailed guidance on naming conventions and other style recommendations.
* [[Working with Lists in Python]] -  Shows how descriptive names can improve readability when working with lists.

