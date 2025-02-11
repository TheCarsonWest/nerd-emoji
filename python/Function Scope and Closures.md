# [[Chaining Decorators]]
# [[Function Scope and Closures]] 
Python's scope rules determine where a variable is accessible within your code.  Understanding this is crucial for writing clean and predictable functions.

* **LEGB Rule:** Python uses the LEGB rule to search for a variable:

    [[1. **L**ocal: Inside the current function or block of code.
    [[2]. **E**nclosing function locals: If the variable isn't found locally, Python searches the local scope of any enclosing functions. This is relevant for nested functions.
    [[3]. **G**lobal: Variables declared at the module level (outside any function).
    [[4]. **B**uilt-in: Predefined functions and constants available in Python (e.g., `len`, `print`).


* **Example illustrating LEGB:**

```python
x = 10  # Global scope

def outer_function():
    y = 20  # Enclosing function scope
    def inner_function():
        z = 30  # Local scope
        print(x, y, z)  # Accesses x, y, and z
    inner_function()

outer_function() # Output: 10 20 30

print(x) # Output: 10
#print(y) # NameError: name 'y' is not defined (y is not in global scope)
```


* **`global` keyword:** To modify a global variable from within a function, you must use the `global` keyword:

```python
global_var = [[5]

def modify_global():
    global global_var  # Declare that we are modifying the global variable
    global_var = 10

modify_global()
print(global_var)  # Output: 10
```


* **`nonlocal` keyword:**  Similar to `global`, but for modifying variables in enclosing functions:

```python
def outer():
    enclosing_var = [[5]
    def inner():
        nonlocal enclosing_var #Declare that we are modifying a variable in the enclosing scope
        enclosing_var = 10
    inner()
    print(enclosing_var) # Output: 10

outer()
```

* **Closures:** A closure is an inner function that remembers and has access to variables in its local scope, even after the outer function has finished executing.  This is because the inner function "closes over" the outer function's variables.


* **Closure Example:**

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function([[5])  # 'closure' now holds a reference to 'inner_function' with x=[[5]
result = closure([[3])  # result will be [[5] + [[3] = 8
print(result)  # Output: 8
```


[[Nested Functions]]
[[Variable Scope]]

