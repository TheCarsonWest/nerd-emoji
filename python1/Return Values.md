## [[Return Values]]

### What are [[Return Values]]?
Return values are the output of a function or method. They allow functions to communicate back to the calling code and provide the result of their execution.

### How to Use [[Return Values]]
 [[Functions]] and methods can return values using the `return` statement. The `return` statement takes an expression or a variable as its argument, which represents the value to be returned.

### Code Examples
```python
def sum_numbers(a, b):
 return a + b

# call the function and store the return value in result
result = sum_numbers(5, 10)

# print the return value
print(result) # Output: 15
```

```python
class Person:
 def get_name(self):
 return "John Doe"

# create an instance of the Person class
person = Person()

# call the get_name method and store the return value in name
name = person.get_name()

# print the return value
print(name) # Output: John Doe
```

### Related Python Concepts

- [[Functions]]: Return values are the primary means of output from functions.
- [[Function Parameters]]: Return values are passed back from the function to the calling code.
- [[Default Parameters]]: Default parameters can be used to provide a default value for the return value if it is not explicitly specified.
- [[Recursion]]: Recursive functions can return values at each level of the recursion.
- [[Lambda [[Functions]]: Lambda functions always return a value, which is the expression on the right-hand side of the function definition.
# [[Python 1 Home]]