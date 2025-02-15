# [[While Loops]]
# [[Break and Continue Statements]] 
These statements alter the flow of control within loops ( `for` and `while`).

* **`break`:** Terminates the loop entirely.  Execution jumps to the statement immediately following the loop.

```python
for i in range([[1, 6):
    if i == 3:
        break
    print(i)  # Output: [[1 2
```

* **`continue`:** Skips the rest of the current iteration and proceeds to the next iteration.

```python
for i in range([[1, 6):
    if i == 3:
        continue
    print(i)  # Output: [[1 2 4 5
```

**Nested Loops and `break`/`continue`:**

`break` and `continue` only affect the *innermost* loop they are contained within.

```python
for i in range([[1,3):
    for j in range([[1,3):
        if i == j:
            continue # only affects inner loop
        print(f"({i},{j})")
    if i == [[1:
        break # only affects outer loop

#Output: ([[1,2)
#       (2,[[1)
#       (2,2)
```

[[Loop Control Flow]]  ([[Break statement]]) [[Continue statement]]
