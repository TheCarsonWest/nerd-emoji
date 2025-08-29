# [[Nested If Statements]]
# [[If-elif-else Statements]] 
Python's `if-elif-else` statements provide a way to control the flow of execution based on multiple conditions.  They're an extension of the basic `if` statement, allowing for more complex decision-making.

**Basic Syntax:**

```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition1 is False and condition2 is True
elif condition3:
    # Code to execute if condition1 and condition2 are False, and condition3 is True
else:
    # Code to execute if all previous conditions are False
```

**Important Points:**

*   Conditions are evaluated sequentially.  The first condition that evaluates to `True` will have its corresponding code block executed.  The rest are skipped.
*   The `else` block is optional. If it's omitted and no previous condition is met, nothing happens.
*   Conditions can be any expression that evaluates to a boolean value (`True` or `False`).
*   Indentation is crucial in Python.  The code within each block must be properly indented.


**Example:**

```python
x = 10

if x > 20:
    print("x is greater than 20")
elif x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

```

**Nested `if-elif-else`:**

You can nest `if-elif-else` statements within each other to create more complex logic.  However, excessive nesting can make code harder to read and maintain. [[Nested Conditional Statements]]

**Short-circuiting:**

Python uses short-circuiting evaluation for boolean operators (`and`, `or`). This means that if the outcome of the expression can be determined from evaluating only the first part, the second part won't be evaluated.  This can be useful for optimization and avoiding errors. [[Boolean Operators]]

**Common Mistakes:**

*   Incorrect indentation leading to `IndentationError`
*   Forgetting colons (`:`) at the end of each conditional statement
*   Using assignment (`=`) instead of comparison (`==`) in conditions.


**Related Notes:**

* [[Boolean Logic]]
* [[Conditional Expressions (Ternary Operator)]]

