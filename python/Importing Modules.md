# [[Python 1 Home]]
# [[Importing Modules]] 
This note covers importing modules in Python.

Modules are files containing Python definitions and statements.  They provide a way to organize and reuse code.

**Ways to Import:**

*   `import module_name`: Imports the entire module. Access members using `module_name.member`.
*   `from module_name import member_name`: Imports a specific member (function, class, variable).  Access directly using `member_name`.
*   `from module_name import member1, member2`: Imports multiple specific members.
*   `from module_name import *`: Imports all members.  Generally discouraged due to potential naming conflicts.  ([[Namespaces and Scope]])

**Example:**

```python
import math

print(math.sqrt(25))  # Output: 5.0

from random import randint

print(randint([[1, 10)) # Output: A random integer between [[1 and 10 (inclusive)

from os import path, getcwd

print(getcwd()) #Prints current working directory.  
```

**[[Module Search Path]]:**

Python searches for modules in a specific order:

1.  The current directory.
2.  Locations specified by the `PYTHONPATH` environment variable.
3.  Standard library directories.
4.  Installation-specific directories (site-packages).

([[PYTHONPATH Environment Variable]])

**Packages:**

Packages are a way to organize modules into directories. A package directory must contain an `__init__.py` file (can be empty).

```python
# mypackage/
#  __init__.py
#  module1.py
#  module2.py

import mypackage.module1
import mypackage.module2 
from mypackage import module1, module2
```

([[Packages and __init__.py]])


**Relative Imports:**

Within a package, you can import modules relative to the current module's location.  Use leading dots to specify the relative path.


```python
# mypackage/module1.py
from .module2 import my_function # Imports my_function from module2 within mypackage
```

([[Relative Imports]])

**Built-in Modules:**

Python comes with many built-in modules (e.g., `math`, `os`, `random`, `sys`).  These are always available without needing to install them.


([[Standard Library Modules]])
