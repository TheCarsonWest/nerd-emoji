## [[Nested If Statements]]

### What are [[Nested If Statements]]?
Nested if statements involve embedding one or more if statements within another if statement. They enable complex decision-making scenarios and allow for specific code blocks to be executed based on multiple conditions.

### How to Use [[Nested If Statements]]
The syntax of nested if statements is:

```python
if outer_condition:
 # code block to be executed if outer_condition is True
 if inner_condition1:
 # code block to be executed if inner_condition1 is True
 elif inner_condition2:
 # code block to be executed if inner_condition2 is True
 else:
 # code block to be executed if none of the inner conditions are True
```

The outer_condition is the condition of the outer if statement. If it evaluates to True, the execution proceeds to the inner if statements. The inner_condition1 and inner_condition2 are the conditions of the inner if statements. If any of these inner conditions evaluate to True, the corresponding code block will be executed. If none of the inner conditions are True, the else block (if present) will be executed.

### Code Examples
```python
# check if the number is positive and even
if number > 0:
 if number % 2 == 0:
 print("The number is positive and even")
```

```python
# decide on a discount based on customer type and purchase amount
if customer_type == "member":
 if purchase_amount >= 100:
 discount = 15
 else:
 discount = 10
else:
 if purchase_amount >= 150:
 discount = 5
 else:
 discount = 0
```

### Other Related Python Concepts

- [[Control Flow If Statements]]: Nested if statements are an extension of regular if statements.
- [[For Loops]]: Nested if statements can be used within for loops to make decisions based on looped elements.
- [[While Loops]]: Similarly, nested if statements can be used within while loops to control loop execution.
- [[Functions]]: Nested if statements can be used to conditionally call functions or determine function behavior.
- [[Boolean Logic]]: Nested if statements rely on Boolean logic operators (e.g., and, or, not) for conditional evaluations.
# [[Python 1 Home]]