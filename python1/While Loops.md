## [[While Loops]]

### What are [[While Loops]]?
While loops are a control flow construct that allows the execution of a code block repeatedly as long as a specified condition remains True. They provide a way to iterate through a sequence of operations or execute a block of code an indefinite number of times.

### How to Use [[While Loops]]
The syntax of a while loop in Python is:

```python
while condition:
 # code block to be executed while condition is True
```

The `condition` is typically a comparison expression that evaluates to either True or False. As long as the condition remains True, the code block under the while loop will continue to execute. Once the condition becomes False, the execution will proceed to the next statement after the while loop.

### Code Examples
```python
# print numbers from 1 to 10
i = 1
while i <= 10:
 print(i)
 i += 1
```

```python
# read input from the user until they enter "quit"
while True:
 user_input = input("Enter a command (or 'quit' to exit): ")
 if user_input == "quit":
 break
```

### Other Python Concepts Related to [[While Loops]]

- [[Variables and Data Types]]: Variables are used to store and manipulate data within while loops.
- [[Operators]]: Comparison operators like `>` and `==` are used to create conditions in while loops.
- [[Control Flow If Statements]]: If statements can be used to control the flow of execution within while loops.
- [[For Loops]]: While loops can be used to implement the same functionality as for loops, but they provide more flexibility in controlling the iteration.
- [[Recursion]]: While loops can be used as the base case in recursive functions.
# [[Python 1 Home]]