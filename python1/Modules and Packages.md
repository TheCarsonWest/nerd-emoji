## [[Modules and Packages]]

### Definition
A [[Module]] in Python is a file consisting of Python code containing [[Functions]], [[Classes]], or [[Variables]] defined in it. [[Packages]], on the other hand, are a collection of related [[Modules]] organized into a hierarchal structure.

### Parameters
- **Name:** Unique name identifying the [[Module]] or [[Package]].
- **Path:** Location of the [[Module]] or [[Package]] file on the file system.
- **Contents:** Code contained within the [[Module]] or [[Package]] file.
- **Dependencies:** Other [[Modules]] or [[Packages]] that the [[Module]] or [[Package]] requires to function properly.

### Code Examples

#### Creating a [[Module]]
```python
# mymodule.py
def greet(name):
    print("Hello, {}!".format(name))
```

#### Importing a [[Module]]
```python
import mymodule

# Call [[Function]] from imported [[Module]]
mymodule.greet("John")
```

#### Creating a [[Package]]
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

#### Importing a [[Package]]
```python
import mypackage
from mypackage import module1

# Call [[Function]] from imported [[Module]]
module1.greet("Mary")
```

### Related Python Concepts

- **[[Namespace]]**: A Python [[Module]] creates its own [[Namespace]] where its [[Variables]] and [[Functions]] are defined.
- **[[Path]]**: [[Modules]] and [[Packages]] are organized in a file system hierarchy, and Python uses the PYTHONPATH environment variable to search for them.
- **[[Importing]]**: The `import` statement allows you to import [[Modules]] or [[Packages]] into your code.
- **[[Submodules]]**: A [[Module]] can contain other [[Modules]], known as [[Submodules]], allowing for organization and code reusability.
- **[[Packages]] and [[Directories]]**: [[Packages]] are represented by [[Directories]] on the file system, and the `__init__.py` file in each [[Directory]] acts as an initialization file for the [[Package]].