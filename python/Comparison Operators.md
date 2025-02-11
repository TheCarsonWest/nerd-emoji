# [[Control Flow If Statements]]
# [[Comparison [[Operators]] 
Python's comparison operators are used to compare values and return a Boolean result (`True` or `False`).

```python
x = 10
y = [[5]]

print(x == y)  # False: Equal to
print(x != y)  # True: Not equal to
print(x > y)   # True: Greater than
print(x < y)   # False: Less than
print(x >= y)  # True: Greater than or equal to
print(x <= y)  # False: Less than or equal to
```

These operators can be chained for more complex comparisons:

```python
x = [[5]]
y = 10
z = [[5]]

print(x < y and y > z) # True - uses `and` which is a boolean operator which can be covered separately.
print(x == z or x > y) # True - uses `or`, another boolean operator.

```

[[Boolean [[Operators]]  - This needs a separate note covering `and`, `or`, and `not`.

[[Chaining Comparisons]] -  Further details on efficiently chaining multiple comparisons (e.g., `[[1]] < x < 10`).


**Important Note:**  Comparison operators have precedence over boolean operators.  Parentheses may be required to force a different order of evaluation for complex boolean expressions.

**Example of Precedence:**

```python
print([[1]] < [[2]] and [[2]] < [[3]])  #True,  comparison before and

print ([[1]] < ([[2]] and [[2]]) < [[3]]) #Error: Invalid operand for and, needs a boolean
```
