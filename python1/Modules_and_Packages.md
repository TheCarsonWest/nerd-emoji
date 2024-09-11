## Python Modules and Packages

### Definition
A module in Python is a file consisting of Python code containing functions, classes, or variables defined in it. Packages, on the other hand, are a collection of related modules organized into a hierarchal structure.

### Parameters
- **Name:** Unique name identifying the module or package.
- **Path:** Location of the module or package file on the file system.
- **Contents:** Code contained within the module or package file.
- **Dependencies:** Other modules or packages that the module or package requires to function properly.

### Code Examples

#### Creating a Module
```python
# mymodule.py
def greet(name):
    print("Hello, {}!".format(name))
```

#### Importing a Module
```python
import mymodule

# Call function from imported module
mymodule.greet("John")
```

#### Creating a Package
```python
# mypackage/__init__.py
from .module1 import *
from .module2 import *
```

```python
mypackage/
    __init__.py
    module1.py
    module2.py
```

#### Importing a Package
```python
import mypackage
from mypackage import module1

# Call function from imported module
module1.greet("Mary")
```

### Related Python Concepts

- **Namespace:** A Python module creates its own namespace where its variables and functions are defined.
- **Path:** Modules and packages are organized in a file system hierarchy, and Python uses the PYTHONPATH environment variable to search for them.
- **Importing:** The `import` statement allows you to import modules or packages into your code.
- **Submodules:** A module can contain other modules, known as submodules, allowing for organization and code reusability.
- **Packages and Directories:** Packages are represented by directories on the file system, and the `__init__.py` file in each directory acts as an initialization file for the package.
[[Python 1 Home]]