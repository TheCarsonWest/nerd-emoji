# [[For Loop Examples]]
# [[Loop Control Statements]] 
Loop control statements in Python alter the flow of execution within loops (primarily `for` and `while` loops).  They allow you to skip iterations, terminate the loop prematurely, or jump to a specific point within the loop.

The key loop control statements are:

* **`break`:** Terminates the loop entirely and transfers control to the statement immediately following the loop.

```python
for i in range(1, 11):
    if i == 5:
        break  # Exit loop when i is 5
    print(i) 
```

* **`continue`:** Skips the rest of the current iteration and proceeds to the next iteration of the loop.

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```

* **`pass`:** Acts as a placeholder. It does nothing.  Often used where syntactically a statement is required, but you don't want any action to be performed.  Useful in defining empty functions or loops which you intend to implement later.

```python
for i in range(1, 11):
    if i % 2 == 0:
        pass  # Do nothing for even numbers
    else:
        print(i)
```

* **`else` clause in loops:** The `else` block is executed only if the loop completes normally (without encountering a `break` statement).

```python
for i in range(1, 11):
    if i == 15: #this condition will never be met
        break
    print(i)
else:
    print("Loop completed normally") #This will always print

for i in range(1, 11):
    if i == 5:
        break
    print(i)
else:
    print("Loop completed normally") #This will not print

```

[[Nested Loops]]  
[[Break and Continue Statements Detailed]]
[[For Loop Syntax]]
[[While Loop Syntax]]

