# [[Namespaces and Scope]]
# Global vs Local Variables

**Scope:**  The scope of a variable determines where in your code that variable is accessible.

* **Global Variables:** Declared outside of any function. Accessible from anywhere in the program *after* its declaration.

```python
global_var = 10

def my_function():
  print(global_var)  # Accessing global variable inside a function

my_function()  # Output: 10
print(global_var) # Output: 10
```

* **Local Variables:** Declared inside a function. Only accessible within that function.  

```python
def my_function():
  local_var = 5
  print(local_var)  # Accessing local variable

my_function()  # Output: 5
#print(local_var) # This will cause a NameError because local_var is not accessible here.
```

**Modifying Global Variables within Functions:**

To modify a global variable from within a function, you *must* use the `global` keyword:

```python
global_var = 10

def modify_global():
  global global_var  # Declare that we are modifying the global variable
  global_var = 20

modify_global()
print(global_var)  # Output: 20
```

Without the `global` keyword, a new local variable with the same name would be created.

**Potential Issues:**

* **Name clashes:** Using the same name for global and local variables can lead to confusion and unexpected behavior.  It's generally good practice to avoid this.
* **Readability:** Overuse of global variables can make code harder to understand and maintain, as it becomes difficult to track where a variable's value might be changed.  [[Variable Naming Conventions]]  It's generally better to pass data as arguments and return values.


**Related Notes:**

* [[Variable Scope and Lifetime]]
* [[Namespaces in Python]]

