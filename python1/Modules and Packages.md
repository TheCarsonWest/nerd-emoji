## [[Modules and Packages]]

### What are [[Modules and Packages]]?

**Modules:**
- Self-contained Python code stored in a file (`*.py`).
- Contain functions, classes, or variables that can be imported and used in other Python scripts.
- Used to organize and reuse code.

**Packages:**
- A collection of related modules organized within a directory structure.
- Packages provide a way to group and distribute modules logically.
- Can contain subpackages and modules within subdirectories.

### How to Use [[Modules and Packages]]

** [[Importing Modules]]:**
```python
import module_name
```
Imports the specified module, allowing access to its contents.

**Importing Specific Elements from a Module:**
```python
from module_name import element1, element2
```
Imports specific elements (e.g., functions, classes) from a module.

**Importing a Package:**
```python
import package_name
```
Imports the entire package, providing access to all its modules and subpackages.

### Code Examples

**Importing and Using a Module:**
```python
import mymodule

mymodule.my_function()
```

**Importing and Using a Specific Element from a Module:**
```python
from mymodule import my_function

my_function()
```

**Importing and Using a Package:**
```python
import mypackage

subpackage = mypackage.subpackage
subpackage.my_function()
```

### Related Python Concepts

- [[Functions]]: Modules and packages provide a way to organize and reuse functions.
- [[Importing Modules]]: The import statement is used to import modules and packages.
- [[Libraries like NumPy]]: NumPy is a package that provides scientific computing capabilities.
- [[Libraries like Pandas]]: Pandas is a package that provides data analysis and manipulation tools.
- [[Libraries like Matplotlib]]: Matplotlib is a package that provides data visualization capabilities. [[Dynamic Importing]]
- [[Functions]]
- [[Python Package Index (PyPI) Publishing]]
- [[Virtual Environments]]

# [[Python 1 Home]]