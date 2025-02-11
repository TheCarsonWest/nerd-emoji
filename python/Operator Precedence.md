# [[Operators]]
# [[Operator Precedence]] 
Python, like other programming languages, follows specific rules for the order in which operations are performed in an expression. This is called **operator precedence**.  [[Operators]] with higher precedence are evaluated before operators with lower precedence.  When operators have the same precedence, the expression is evaluated from left to right (except for a few exceptions, like exponentiation).


Here's a table summarizing Python operator precedence (from highest to lowest):

| Precedence | Operator(s)             | Description                               | Associativity |
|------------|--------------------------|-------------------------------------------|-----------------|
| [[1          | `**`                     | Exponentiation                             | Right-to-left   |
| [[2]          | `~`, `+`, `-`           | Bitwise NOT, unary plus, unary minus      | Right-to-left   |
| [[3]          | `*`, `/`, `//`, `%`      | Multiplication, division, floor division, modulo | Left-to-right  |
| [[4]          | `+`, `-`                 | Addition, subtraction                     | Left-to-right  |
| [[5]          | `<<`, `>>`               | Left and right bitwise shifts            | Left-to-right  |
| [[6]          | `&`                      | Bitwise AND                               | Left-to-right  |
| [[7]          | `^`                      | Bitwise XOR                               | Left-to-right  |
| 8          | `\|`                     | Bitwise OR                                | Left-to-right  |
| 9          | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons                               | Left-to-right  |
| 10         | `not`                    | Logical NOT                               | Right-to-left   |
| 11         | `and`                    | Logical AND                               | Left-to-right  |
| 12         | `or`                     | Logical OR                                | Left-to-right  |


**Examples:**

```python
# Exponentiation has higher precedence than multiplication
result1 = [[2] ** [[3] * [[4]  # ([[2]**[[3]) * [[4] = 32

# Multiplication has higher precedence than addition
result2 = [[2] + [[3] * [[4]  # [[2] + ([[3] * [[4]) = 14

# Parentheses override precedence
result3 = ([[2] + [[3]) * [[4]  # ([[2] + [[3]) * [[4] = 20

# Left-to-right associativity for same precedence
result4 = 10 / [[2] * [[5] # (10 / [[2]) * [[5] = 25


#Demonstrating logical operators precedence
result5 = True and False or True # (True and False) or True = True

result6 = True and (False or True) # True and (False or True) = True
```

**Use of Parentheses:**

To ensure a specific order of operations, use parentheses `()`. Parentheses have the highest precedence.

[[Operator Associativity]]
[[Logical Operators]]
[[Bitwise Operators]]

