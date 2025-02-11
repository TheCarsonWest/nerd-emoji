# [[Control Flow If Statements]]
# [[Nested If Statements]] 
Nested if statements are if statements placed inside other if statements.  They're used to create complex conditional logic.  The inner `if` statement only executes if the outer `if` statement's condition is true.

```python
x = 10
y = [[5]]

if x > [[5]]:
    if y < 10:
        print("x is greater than [[5]] and y is less than 10")
    else:
        print("x is greater than [[5]] but y is not less than 10")
else:
    print("x is not greater than [[5]]")

```

This example shows a simple nested `if` structure.  More complex scenarios can involve multiple levels of nesting and `elif` (else if) statements within the nested structure.  However, deeply nested `if` statements can become difficult to read and understand. It's often better to refactor complex conditional logic into functions or use other control flow structures like loops or dictionaries to improve readability and maintainability.


[[If-elif-else Statements]]  --  This would explain the basics of `if`, `elif`, and `else` in more detail, which is fundamental to understanding nested ifs.

[[Code Readability and Refactoring]] --  This would cover best practices for writing clean and understandable Python code,  especially for complex conditional logic.  It will discuss refactoring techniques.
