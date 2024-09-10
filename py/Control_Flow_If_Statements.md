**Python Control Flow: If Statements**

**What is an If Statement?**

An if statement is a conditional statement that allows you to control the execution of code based on the evaluation of a boolean expression.

**Syntax:**

```python
if condition:
    code_block_1
elif condition_2:
    code_block_2
...
else:
    code_block_n
```

**Parameters:**

* **Condition:** A boolean expression that determines whether the corresponding code block will be executed.
* **Code block:** The code that will be executed if the condition evaluates to `True`.
* **Elif (else if):** Optional statements that provide additional conditions and corresponding code blocks.
* **Else:** An optional statement that provides a default code block if none of the previous conditions were met.

**Code Examples:**

```python
# Check if a number is greater than 10
if num > 10:
    print("Number is greater than 10")

# Check if a string is equal to "Hello"
if string == "Hello":
    print("String is equal to 'Hello'")

# Check if multiple conditions are met
if name != "" and age > 18:
    print("User has provided a name and is over 18")
```

**Other Python Concepts Linked to If Statements:**

* **Boolean [[operators]]:** Used to create boolean expressions (e.g., `and`, `or`, `not`).
* **Comparison operators:** Used to compare values and produce boolean values (e.g., `==`, `<`, `>`).
* **Nested if statements:** Multiple if statements can be nested within each other to create complex conditions.
* **Ternary operators:** Provide a concise way to write simple if-else statements (e.g., `x = y if condition else z`).

**Tips for Using If Statements:**

* Keep conditions simple and easy to understand.
* Use elif statements to handle multiple conditions without redundant code.
* Consider using boolean operators and comparison operators to create more complex conditions.
* Nest if statements only when necessary to avoid unreadable code.
* Use ternary operators sparingly for brevity.