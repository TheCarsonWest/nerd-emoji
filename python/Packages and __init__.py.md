# [[Importing Modules]]
# Packages and `__init__.py`

Python packages are a way of organizing related modules into a hierarchical structure.  This helps manage complexity in larger projects.  The key to creating a package is the `__init__.py` file.

- **`__init__.py`:** This file (even if it's empty!) signals to Python that a directory should be treated as a package.  Without it, Python treats the directory as just a directory, not a package.  It can also contain initialization code for the package, for example, importing specific modules or defining variables to be used throughout the package.

```python
# mypackage/__init__.py
__all__ = ["module1", "module2"] # This line controls what gets imported with `from mypackage import *`

# Or, you can explicitly import modules to make them available:
from .module1 import *
from .module2 import some_function 
```

- **Structure:** A typical package structure looks like this:

```
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```

- **Importing from Packages:**

  -  Import specific modules: `import mypackage.module1`
  - Import specific items: `from mypackage.module1 import some_function`
  - Import all (using `__all__` in `__init__.py`): `from mypackage import *`  (generally discouraged, it can lead to name clashes)
  -  Using relative imports (within the package itself):  `from .module2 import another_function` (the `.` refers to the current package directory).

- **Nested Packages:** You can nest packages within packages to create a deeper, more organized hierarchy.  Each subpackage needs its own `__init__.py` file.

```
mypackage/
├── __init__.py
├── subpackage1/
│   ├── __init__.py
│   └── module3.py
└── subpackage2/
    └── __init__.py
    └── module4.py
```


- [[Namespaces and Scope]]  (Linked Note:  This would discuss how packages create their own namespaces.)
- [[Relative vs]]. Absolute Imports]] (Linked Note: This would compare and contrast these types of import statements.)
- [[Circular Imports]] (Linked Note: This is a common problem when working with packages - this note would describe them and offer solutions.)

