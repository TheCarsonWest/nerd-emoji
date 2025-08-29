# [[Python Functions]]
# [[Variable Scope and Lifetime]] 
Python's variable scope determines where a variable is accessible within your code.  A variable's lifetime is how long it exists in memory.  These two concepts are closely related.


**Scope:**

* **Local Scope:** Variables defined inside a function are only accessible within that function.  Their lifetime is tied to the function's execution.

```python
def my_function():
  x = 10  # x is local to my_function
  print(x)

my_function() # prints 10
print(x) # This will cause a NameError because x is not defined in the global scope.
```

* **Global Scope:** Variables defined outside any function are accessible from anywhere in the program after their definition.  Their lifetime lasts until the program terminates.

```python
y = 20 # y is global

def another_function():
  print(y) # Accessing the global variable y

another_function() # prints 20
print(y) # prints 20
```

* **Enclosing Function Locals ([[Nested Functions]]):**  If you have [[Nested Functions]], inner functions can access variables from their enclosing (outer) functions, but not vice-versa.  This is called *closure*.

```python
def outer_function():
  z = 30
  def inner_function():
    print(z) # inner_function can access z from outer_function
  inner_function()

outer_function() # prints 30
#print(z) # This will cause a NameError because z is not accessible here.

```

* **Built-in Scope:**  Python has a built-in scope containing pre-defined functions and constants (e.g., `print`, `len`, `True`, etc.). These are accessible from anywhere.

* **`global` keyword:** To modify a global variable from within a function, you must use the `global` keyword.

```python
global_var = 50

def modify_global():
  global global_var # Declare that we are modifying the global variable
  global_var = 100

modify_global()
print(global_var)  # Output: 100
```

* **`nonlocal` keyword:** Similar to `global`, but for variables in enclosing functions ([[Nested Functions]]).


```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)  # Output: 20

outer()
```

**Lifetime:**

A variable's lifetime is directly related to its scope. A variable's lifetime begins when it is created (assigned a value) and ends when it's no longer referenced and garbage collected. In local scope, this happens when the function completes.  In global scope, it's at program termination.


[[Garbage Collection]]


[[LEGB Rule]] (This will explain the order of scope searching: Local, Enclosing function locals, Global, Built-in)
