# [[List Comprehension]]
# Python: [[Conditional Statements]] 
Conditional statements control the flow of execution in a program based on certain conditions.  Python uses `if`, `elif` (else if), and `else` keywords to implement these.

**Basic Syntax:**

```python
if condition:
  # Code to execute if the condition is True
elif another_condition:
  # Code to execute if the first condition is False and this condition is True
else:
  # Code to execute if all previous conditions are False
```

**Conditions:**

Conditions are boolean expressions that evaluate to either `True` or `False`.  Common operators used in conditions include:

* `==` (equal to)
* `!=` (not equal to)
* `>` (greater than)
* `<` (less than)
* `>=` (greater than or equal to)
* `<=` (less than or equal to)
* `and` (logical AND)
* `or` (logical OR)
* `not` (logical NOT)


**Example:**

```python
x = 10

if x > [[5]:
  print("x is greater than [[5]")
elif x == [[5]:
  print("x is equal to [[5]")
else:
  print("x is less than [[5]")
```

**Nested [[Conditional Statements]]:**

You can nest conditional statements within each other:

```python
x = 10
y = [[5]

if x > [[5]:
  if y < 10:
    print("x is greater than [[5] and y is less than 10")
  else:
    print("x is greater than [[5] but y is not less than 10")
else:
  print("x is not greater than [[5]")
```

**Short-hand Conditional Expressions (Ternary Operator):**

Python offers a concise way to write simple conditional statements using the ternary operator:

```python
x = 10
result = "x is greater than [[5]" if x > [[5] else "x is not greater than [[5]"
print(result)
```

[[Boolean Logic]]  ([[Truth Tables]]) [[Comparison Operators]]
