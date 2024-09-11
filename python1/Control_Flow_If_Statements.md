**Python Control Flow: If Statements**

**Explanation**

If statements allow for conditional execution of code blocks in Python. They enable you to control the flow of your program based on whether a certain condition is true or false.

**Parameters**

- **if** clause: The condition that determines whether the code block will be executed.
- **colon**: Marks the end of the if clause and the beginning of the code block.
- **indentation**: Indent the code block to indicate that it belongs to the if statement.

**Code Examples**

```python
# Check if a number is positive
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")

# Check if a string is empty
s = "Hello World"
if not s:
    print("The string is empty.")
```

**Variations**

- **elif** (else if): Used to check additional conditions.
- **else**: Used to execute code if none of the if/elif conditions are met.

**Code Examples**

```python
# Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

**Linked Concepts**

- **Boolean operators**: Used to create conditions in if statements (e.g., and, or, not).
- **Comparison operators**: Used to compare values in conditions (e.g., ==, !=, <, >).
- **Loops**: Can be used in conjunction with if statements for more complex conditional execution (e.g., for loops, while loops).
- **Functions**: Can return values that can be used as conditions in if statements.
[[Python 1 Home]]