# [[Importing Modules]]
# [[Namespaces and Scope]] 
Namespaces are basically containers that hold names (variables, functions, classes, etc.).  They help prevent naming conflicts.  Python uses namespaces to manage the organization of names, ensuring that names are unique and accessible within their intended context.

There are several types of namespaces:

* **Built-in:** Contains pre-defined functions and constants (e.g., `print`, `len`).  This is created when the Python interpreter starts.
* **Global:** Contains names defined at the top level of a module (a `.py` file).
* **Local:** Contains names defined within a function or block of code (e.g., inside an `if` statement or a loop).
* **Enclosing function locals:** If a nested function references a variable not in its local namespace, Python searches the namespaces of enclosing functions.

Scope determines the accessibility of names.  It's the region of code where a particular name is visible and can be accessed.  Python uses the LEGB rule to search for names:

[[1. **L**ocal: The innermost scope, where the name is defined.
2. **E**nclosing function locals:  If not found locally, Python searches outwards to enclosing functions.
3. **G**lobal:  The module's namespace.
4. **B**uilt-in: The namespace containing pre-defined functions and constants.


Example:

```python
x = 10  # Global scope

def my_function():
    x = 5  # Local scope
    print(f"Inside function: x = {x}")

my_function()  # Output: Inside function: x = 5
print(f"Outside function: x = {x}")  # Output: Outside function: x = 10

```

In this example, the `x` inside the function is different from the global `x`.

[[Nested Functions]]


Example with nested functions:

```python
x = 10 #Global scope

def outer_function():
    x = 5 #Enclosing function locals
    def inner_function():
        x = [[1 #Local scope
        print(f"Inner: x = {x}")

    inner_function()
    print(f"Outer: x = {x}")

outer_function()
print(f"Global: x = {x}")
```

[[Modules and Packages]]

The `global` keyword can be used to modify a global variable from within a function.  However, it's generally best to avoid modifying global variables directly inside functions to improve code readability and maintainability.


```python
global_var = 0

def modify_global():
    global global_var #Declare that we are modifying the global variable
    global_var = 10

modify_global()
print(global_var) #Output: 10

```

[[Global vs Local Variables]]
