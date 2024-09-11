## Python While Loops

### Overview

A while loop is a control flow statement that repeatedly executes a block of code as long as a specified condition remains True.

### Parameters

* **while (condition):** The condition to evaluate. If True, the loop body will execute. If False, the loop terminates.

### Code Examples

```python
# Example 1: Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# Example 2: Read user input until they enter "quit"
while True:
    user_input = input("Enter a command (or 'quit' to exit): ")
    if user_input == "quit":
        break
    else:
        # Process the user input
```

### Usage and Considerations

* **Initialization:** Before entering the loop, the variables used in the condition and body should be initialized.
* **Condition:** The condition is evaluated at the beginning of each iteration. If it becomes False, the loop terminates.
* **Body:** The code within the loop body executes as long as the condition remains True.
* **Loop Control:** Use statements like `break` and `continue` to control the flow within the loop. `break` exits the loop, and `continue` skips the remaining code in the current iteration.

### Related Python Concepts

* **For Loops:** For loops iterate over a sequence of elements, while while loops execute based on a condition.
* **Conditional Statements:** While loops use a conditional statement (the `while` condition) to determine whether to execute the loop body.
* **Iterators:** Iterators provide a way to iterate over elements in a loop.
* **Generators:** Generators can be used to create sequences of values on-the-fly, which can be iterated over in a while loop.
[[Python 1 Home]]