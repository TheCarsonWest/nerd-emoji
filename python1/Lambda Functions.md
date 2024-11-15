## Lambda [[Python Functions]]

### Explanation
Lambda [[Python Functions]] in Python are small, anonymous [[Python Functions]] that can be defined without using the `def` keyword. They are often used as inline [[Python Functions]] when passing a function as an argument to another function or as a way to quickly define a simple function.

### How to Use Lambda [[Python Functions]]
Lambda [[Python Functions]] take the following format:

```python
lambda arguments: expression
```

* **arguments**: The input parameters to the function.
* **expression**: The code to be executed when the function is called.

### Code Examples
```python
# define a lambda function to calculate the square of a number
square = lambda x: x ** 2

# call the lambda function
print(square(5)) # Output: 25
```
Lambda [[Python Functions]] are used as keys for sorting frequently
```python
# use a lambda function as an argument to the `sort` function
numbers = [5, 1, 3, 2, 4]
numbers.sort(key=lambda x: x % 2) # sort the numbers based on their remainder when divided by 2
print(numbers) # Output: [2, 4, 1, 3, 5]
```

### Related Python Concepts
- [[Python Functions]]: Lambda [[Python Functions]] are essentially simplified versions of regular [[Python Functions]].
- [[Function Parameters]]: Lambda [[Python Functions]] can receive arguments just like regular [[Python Functions]].
- [[Higher-Order [[Python Functions]]: Lambda [[Python Functions]] are often used as arguments to higher-order [[Python Functions]].
- [[Closures]]: Lambda [[Python Functions]] can access variables from the enclosing scope, creating closures.
- [[Map, Filter, and Reduce]]: Lambda [[Python Functions]] commonly appear in these built-in [[Python Functions]].
# [[Python 1 Home]]