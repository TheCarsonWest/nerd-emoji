## [[Nested Loops]]

### What are [[Nested Loops]]?
Nested loops are a sequence of loops, where one or more loops are contained within another loop. They enable the execution of a nested block of code a specified number of times, depending on the conditions of the outer and inner loops.

### How to Use [[Nested Loops]]
To create nested loops, use one or more for loops (or while loops) nested within another for loop (or while loop). The syntax is as follows:

```python
for outer_variable in outer_sequence:
 for inner_variable in inner_sequence:
 # code block to be executed for each iteration of the inner loop
```

### Code Examples
```python
# print a multiplication table for numbers from 1 to 5
for i in range(1, 6):
 for j in range(1, 6):
 print(i * j, end=" ")
 print()
```

```python
# check if a number is prime
for i in range(2, number):
 if number % i == 0:
 break
else:
 print("Number is prime")
```

### Related Python Concepts

- [[For Loops]]: Nested loops are built using multiple for loops (or while loops).
- [[Variables]]: The variables used in the nested loops represent the counters or iterators used to control the flow of execution.
- [[Control Flow If Statements]]: Nested loops can be used in conjunction with if statements to conditionally execute code blocks.
- [[Functions]]: Nested loops can be used to iterate over the elements of a list or dictionary passed as a parameter to a function.
- [[List Comprehension]]: Nested loops can be used to create multi-dimensional lists using list comprehension.
# [[Python 1 Home]]