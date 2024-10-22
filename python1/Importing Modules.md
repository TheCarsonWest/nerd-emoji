## [[Importing Modules]]

### What is [[Importing Modules]]?

Importing modules in Python allows you to access and reuse code written in other files. Modules are individual Python files with a `.py` extension that contain defined functions, classes, and variables. Importing modules enables code reusability, modularity, and organization in larger projects.

### How to Use [[Importing Modules]]

To import a module, use the `import` statement followed by the module name:

```python
import module_name
```

You can also import specific elements from a module using the `from` statement:

```python
from module_name import specific_element
```

### Code Examples

```python
# import the entire `math` module
import math

# print the value of pi from the `math` module
print(math.pi)
```

```python
# import the `sqrt` function from the `math` module
from math import sqrt

# calculate the square root of a number
result = sqrt(16)
```

### Related Python Concepts

- [[Modules and Packages]]: Modules are the building blocks of packages, which group related modules together.
- [[Functions]]: Modules can define custom functions that can be imported and used in other modules.
- [[Classes and Objects]]: Modules can define classes and objects that can be imported and reused across programs.
- [[File Handling]]: Modules can be used to interact with files and manage file operations.
- [[Dynamic Importing]]: Modules can be imported dynamically during runtime using the `importlib` module.
# [[Python 1 Home]]