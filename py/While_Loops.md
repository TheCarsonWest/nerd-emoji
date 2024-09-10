**Python While Loops**

**What is a While Loop?**

A while loop in Python is a control flow statement that repeatedly executes a block of code as long as a specified condition remains true.

**Parameters**

The syntax of a while loop is:

```python
while condition:
    # Code block to be executed
```

* **condition:** A Boolean expression that evaluates to True or False. The loop continues to execute as long as the condition is True.

**Code Examples**

```python
# Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1
```

```python
# Read input until the user enters "quit"
while True:
    user_input = input("Enter something (or 'quit' to exit): ")
    if user_input == "quit":
        break
```

```python
# Iterate over a list while modifying it
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        numbers[i] *= 2
    i += 1
print(numbers)  # Output: [2, 4, 3, 4, 5]
```

**Related Python Concepts**

* **For Loops:** Iterate over a sequence of items.
* **Break Statement:** Exits the loop prematurely.
* **Continue Statement:** Skips the rest of the loop body and continues to the next iteration.
* **Conditional Statements:** Used to evaluate the condition that controls the loop.