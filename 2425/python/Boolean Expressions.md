# [[Control Flow If Statements]]
# [[Boolean Expressions]] 
Boolean expressions are expressions that evaluate to either `True` or `False`.  They are fundamental to controlling the flow of execution in Python programs through conditional statements (`if`, `elif`, `else`) and loops.

**Key Components:**

* **Boolean Values:** `True` and `False` (case-sensitive).
* **[[Comparison Operators]]:**
    * `==` (equal to)
    * `!=` (not equal to)
    * `>` (greater than)
    * `<` (less than)
    * `>=` (greater than or equal to)
    * `<=` (less than or equal to)
* **Logical [[Operators]]:**
    * `and` (both operands must be True)
    * `or` (at least one operand must be True)
    * `not` (inverts the boolean value)
* **Membership [[Operators]]:**
    * `in` (checks if a value is present in a sequence)
    * `not in` (checks if a value is not present in a sequence)
* **[[Identity]] [[Operators]]:**
    * `is` (checks if two variables refer to the same object in memory)
    * `is not` (checks if two variables refer to different objects)


**Examples:**

```python
x = 10
y = 5

print(x > y)  # Output: True
print(x == y)  # Output: False
print(x > 5 and y < 10) # Output: True
print(x < 5 or y > 10) # Output: False
print(not (x == y)) # Output: True
print(x in [10, 20, 30]]) #Output: True
print(x is y) #Output: False
```

**Important Considerations:**

* [[Operator Precedence]]:  Logical operators have a specific order of operations ( `not`, then `and`, then `or`). Parentheses can be used to change the order of evaluation. [[Operator Precedence]]
* Short-circuiting:  Python uses short-circuiting evaluation for `and` and `or`.  For `x and y`, if `x` is `False`, `y` is not evaluated.  For `x or y`, if `x` is `True`, `y` is not evaluated.

**Related Notes:**

* [[Conditional Statements]]
* [[Loops]]
* [[Truthiness and Falsiness]]


