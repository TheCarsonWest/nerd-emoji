# [[Namespaces and Scope]]
# [[Modules and Packages]] 
Python's modularity is a key strength.  It allows for code reusability and organization.

* **Modules:**  A single Python file (`.py`) containing functions, classes, and variables.  Think of it as a toolbox with specific tools.

```python
# my_module.py
def my_function(x):
  return x * 2

my_variable = 10
```

To use `my_function` and `my_variable`, you import the module:

```python
import my_module

result = my_module.my_function(5)  # result will be 10
print(my_module.my_variable)       # prints 10
```

You can also import specific elements:

```python
from my_module import my_function, my_variable

result = my_function(5) # result will be 10
print(my_variable)      # prints 10
```

Or rename things during import:

```python
from my_module import my_function as func, my_variable as var

result = func(5) # result will be 10
print(var)      # prints 10
```


* **Packages:** A collection of modules organized in a directory hierarchy.  The directory must contain an `__init__.py` file (can be empty), which signals to Python that it's a package.  Packages help structure larger projects.

```
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```

Importing from a package:

```python
import mypackage.module1

mypackage.module1.some_function()

from mypackage.module2 import some_other_function
some_other_function()
```

[[Import Statements]]

[[Standard Library Modules]]

[[Creating Your Own Modules and Packages]]

[[Namespaces and Scope]]


[[The `__init__.py` File]]  (Explains the purpose and functionality of `__init__.py` in more detail.)

[[Package Management with pip]] (How to install and manage external packages using pip)
