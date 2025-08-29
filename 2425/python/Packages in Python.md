# [[Importing Modules]]
# [[Packages in Python]] 
Packages are a way of organizing related modules into a directory hierarchy.  This helps to avoid naming conflicts and makes it easier to manage large collections of code.

A package is essentially a directory containing an `__init__.py` file (can be empty, but it's required to tell Python that the directory is a package) and other modules (`.py` files).

**Example:**

Let's say we have a package called `mypackage` with the following structure:

```
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```

* `__init__.py`:  This file can contain initialization code for the package, or it can be left empty.
* `module1.py` and `module2.py`: These are the modules that contain the actual code.


**Importing from Packages:**

To import modules from a package, you use the dot notation:

```python
import mypackage.module1
import mypackage.module2

from mypackage import module1, module2 #this can also be done

# Accessing functions/classes within the modules:
mypackage.module1.my_function()
module1.my_function() #After using from mypackage import module1, module2
module2.another_function()
```

**Nested Packages:**

Packages can be nested within other packages to create a more complex organizational structure.  For instance:

```
myproject/
├── mypackage/
│   ├── __init__.py
│   ├── subpackage1/
│   │   ├── __init__.py
│   │   └── module3.py
│   └── module1.py
└── another_package/
    └── __init__.py

```

Importing from nested packages:

```python
import myproject.mypackage.subpackage1.module3
from myproject.mypackage.subpackage1 import module3

myproject.mypackage.subpackage1.module3.my_nested_function()
module3.my_nested_function()
```

**Installing Packages ([[Python Package Management]]):**

This is a crucial step to using external packages.  It involves using tools like `pip`.


**`__init__.py` - further details:**

The `__init__.py` file can be used to control what gets imported when you import the package itself:

```python
# mypackage/__init__.py
from .module1 import my_function as my_package_function

# Now, importing mypackage will also make my_package_function available:
import mypackage
mypackage.my_package_function()
```

[[Relative Imports]]: This is a special way of importing modules within a package itself.


[[Namespaces in Python]]:  Understanding namespaces is essential for comprehending how packages work.  They help organize and manage symbols to avoid conflicts.
