# [[Control Flow If Statements]]
# Python [[Operators]] 
This note covers Python operators.  Further notes will be needed for subtopics.

**Types of Operators:**

* **Arithmetic Operators:**  These perform mathematical calculations.

```python
x = 10
y = 5

print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x // y) # Floor Division (integer division)
print(x % y)  # Modulus (remainder)
print(x ** y) # Exponentiation
```

* **Comparison Operators:** These compare two values and return a Boolean (True or False).

```python
x = 10
y = 5

print(x == y) # Equal to
print(x != y) # Not equal to
print(x > y)  # Greater than
print(x < y)  # Less than
print(x >= y) # Greater than or equal to
print(x <= y) # Less than or equal to
```

* **Logical Operators:** These combine or modify Boolean expressions.

```python
x = True
y = False

print(x and y) # Logical AND
print(x or y)  # Logical OR
print(not x)   # Logical NOT
```

* **Assignment Operators:** These assign values to variables.

```python
x = 10         # Simple assignment
x += 5         # x = x + 5
x -= 5         # x = x - 5
x *= 5         # x = x * 5
x /= 5         # x = x / 5
x %= 5         # x = x % 5
x **= 5        # x = x ** 5
x //= 5        # x = x // 5

```

* **Bitwise Operators:** These operate on individual bits of integers. [[Bitwise Operators]]

* **Membership Operators:** These test for membership in sequences (e.g., lists, tuples, strings).

```python
my_list = [1, 2, 3]
print(1 in my_list)  # True
print(4 in my_list)  # False
print(1 not in my_list) # False

```

* **Identity Operators:** These test for object identity (whether two variables refer to the same object in memory).

```python
x = [1,2,3]
y = [1,2,3]
z = x

print(x is y) # False (different objects)
print(x is z) # True (same object)
print(x == y) # True (same values)


```

**Operator Precedence:**  The order in which operators are evaluated.  [[Operator Precedence]]


**Further Notes:**

* [[Operator Overloading]] (How operators behave differently with different data types.)
* [[Short-circuiting in Logical Operators]] (How `and` and `or` can sometimes avoid evaluating all operands.)

