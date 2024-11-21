# [[Operators]]
# Short-circuiting in Logical Operators

Python's logical [[Operators]] (`and`, `or`) employ short-circuiting.  This means that the evaluation of the expression stops as soon as the final outcome is known.

* **`and`:**  If the left operand is falsy (evaluates to `False`), the entire expression is falsy, and the right operand is *not* evaluated.

```python
x = 0
y = 1/0  # This will cause an error if executed

result = x and y 
print(result) # Output: 0 (no ZeroDivisionError)
```

* **`or`:** If the left operand is truthy (evaluates to `True`), the entire expression is truthy, and the right operand is *not* evaluated.

```python
x = 1
y = 1/0 # This will cause an error if executed

result = x or y
print(result) # Output: 1 (no ZeroDivisionError)
```

**Practical Implications:**

* **Avoiding Errors:** Short-circuiting is crucial for preventing errors like the `ZeroDivisionError` shown above.  We can use it to check for valid conditions before attempting operations that might fail.

* **Improved Efficiency:**  If the right operand is computationally expensive, short-circuiting avoids unnecessary calculations.


**[[Truthy and Falsy Values]]**  ([[Error Handling in Python]])
