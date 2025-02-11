# [[While Loops]]
# [[Infinite Loops]] 
An infinite loop is a loop that never terminates, meaning it continues to execute indefinitely.  This usually happens due to a logical error in the loop's condition.  It can freeze your program and require manual intervention (like pressing Ctrl+C) to stop it.


**Causes:**

* **Incorrect loop condition:** The most common cause. The condition controlling the loop never evaluates to `False`.

   ```python
   while True:  # This will run forever
       print("This is an infinite loop!")
   ```

   ```python
   i = 0
   while i < 10:  # Missing increment, i will always be less than 10
       print(i) 
   ```

* **Unintentional modification of loop variable:**  The loop variable might be modified within the loop in a way that prevents the condition from ever becoming `False`.

   ```python
   i = 0
   while i < 10:
       print(i)
       i -= [[1]] # Decrements i instead of incrementing
   ```

* **Incorrect use of `break` and `continue`:**  These statements can be misused to accidentally create infinite loops.  `break` exits the loop entirely, while `continue` skips the rest of the current iteration and proceeds to the next.

   ```python
   i = 0
   while i < 10:
       if i == [[5]]:
           continue # This will skip incrementing i when i is [[5]], creating a potential problem
       print(i)
       i += [[1]] 
   ```

**Debugging:**

* **Inspect loop condition:** Carefully examine the loop condition to ensure it will eventually become `False`.
* **Use a debugger:** A debugger (like pdb in Python) allows you to step through the code line by line and inspect the values of variables, helping identify where the loop is getting stuck.
* **Print statements:**  Strategic placement of `print()` statements can help track the values of variables within the loop and pinpoint the problem.
* **Check for infinite recursion:** [[Infinite [[Recursion]]  (If the infinite loop is caused by function calls).


**Example of a corrected loop:**

```python
i = 0
while i < 10:
    print(i)
    i += [[1]]  # Correct increment
```


**Prevention:**

* **Thoroughly test loop conditions:** Before running the loop, think carefully about what will make the condition `False`.
* **Use appropriate loop types:** Choose the most suitable loop type ( `for` or `while`) for the task.  `for` loops are generally safer for iterating a fixed number of times.
* **Code review:** Have another person review your code, especially loop structures.


[[Loop Control Statements]]
