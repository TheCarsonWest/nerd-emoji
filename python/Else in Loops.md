# [[While Loops]]
# [[Else in Loops]] 
The `else` keyword in Python's `for` and `while` loops is often misunderstood. It doesn't mean "if the loop doesn't execute".  Instead, the `else` block executes only if the loop completes *normally*, meaning it ran through all its iterations without encountering a `break` statement.

```python
numbers = [[[1]], [[3]], [[5]], [[7]]]
target = 10

for number in numbers:
    if number == target:
        print(f"Found {target}!")
        break  # Loop will terminate early; else block will NOT execute
else:
    print(f"{target} not found in the list.")


numbers = [[[1]], [[3]], [[5]], [[7]], 10]
target = 10

for number in numbers:
    if number == target:
        print(f"Found {target}!")
        break # Loop will terminate early, but else block will NOT execute
else:
    print(f"{target} not found in the list.")

```

**In summary:**

*   `else` in loops is *not* the same as `else` in `if` statements.
*   It executes only if the loop finishes naturally (without `break`).
*   Useful for indicating when a loop completes without finding a specific condition.


[[Break Statement]]  [[While Loops]] [[For Loops]]
