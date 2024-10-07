## [[Global and Nonlocal Variables]]

### What are [[Global and Nonlocal Variables]]?
Global variables are declared outside of any function and are accessible throughout the program. 
Nonlocal variables are declared within a nested function and can access and modify variables in the enclosing scope, but not in the global scope.

### How to Use Global Variables
Global variables are declared using the `global` keyword. To access a global variable from within a function, you must declare it as global.

```python
my_global_var = 10

def my_function():
 global my_global_var
 my_global_var += 1
```

### How to Use Nonlocal Variables
Nonlocal variables are declared using the `nonlocal` keyword. To access a nonlocal variable from within a nested function, you must declare it as nonlocal.

```python
def outer_function():
 my_nonlocal_var = 10

 def inner_function():
 nonlocal my_nonlocal_var
 my_nonlocal_var += 1
```

### Code Examples
```python
# Declare a global variable
global_var = 10

# Define a function that modifies the global variable
def my_function():
 global global_var
 global_var += 1

print(global_var) # Output: 10
my_function()
print(global_var) # Output: 11
```

```python
# Declare a nonlocal variable
def outer_function():
 nonlocal_var = 10

 def inner_function():
 nonlocal nonlocal_var
 nonlocal_var += 1
 inner_function()

print(nonlocal_var) # Output: 11
```

### Related Python Concepts

- [[Variables and Data Types]]: Global and nonlocal variables are examples of variable scope in Python.
- [[Functions]]: Global and nonlocal variables are used within functions.
- [[Function Parameters]]: Global and nonlocal variables can interact with function parameters.
- [[Default Parameters]]: Global and nonlocal variables can be used as default values for function parameters.
- [[Closures]]: Global and nonlocal variables can be captured by closures.
# [[Python 1 Home]]