## [[Closures]]

### What is a Closure?
A closure in Python is a function that retains access to the variables in its enclosing scope, even after the enclosing function has returned. This allows the closed function to access and manipulate variables from the enclosing scope, making it a powerful tool for encapsulating state and creating flexible and reusable code.

### How to Use [[Closures]]
To create a closure, define a nested function inside another function. The inner function can access all the variables in the enclosing function's scope. The closure is created when the enclosing function returns the inner function as its result.

### Code Examples
```python
def outer_function(x):
 y = 10
 def inner_function():
 z = x + y
 print(z)
 return inner_function

# create a closure by returning the inner function
closure = outer_function(5)

# call the closure to access the variables from the enclosing scope
closure() # prints 15
```

### Related Python Concepts

- [[Functions]]: [[Closures]] are nested functions that retain access to the enclosing function's scope.
- [[Function Parameters]]: Parameters passed to the enclosing function can be accessed by the closure.
- [[Return Values]]: The closure is the return value of the enclosing function.
- [[Higher-Order [[Functions]]: [[Closures]] are examples of higher-order functions, which return other functions.
- [[Global and Nonlocal Variables]]: [[Closures]] access nonlocal variables from the enclosing scope, but not global variables.
# [[Python 1 Home]]