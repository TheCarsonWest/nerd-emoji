# [[Packages and __init__.py]]
# [[Relative vs. Absolute Imports]] 
These notes cover the differences and best practices for using relative and absolute imports in Python.

**Absolute Imports:**

These imports specify the full path to a module from the root of your project.  They are generally preferred for their clarity and avoid ambiguity.

```python
import mypackage.moduleA
from mypackage.moduleB import functionB
```

Advantages:

*   **Clearer and more readable:**  The import path explicitly shows the module's location within the project.
*   **Less prone to errors:**  Avoids confusion caused by relative path changes.
*   **Easier refactoring:**  Module restructuring is less likely to break absolute imports.

Disadvantages:

*   Can be slightly more verbose, especially for deeply nested modules.


**Relative Imports:**

These imports specify the module's location relative to the current module's location.  They use a dot (`.`) to indicate the relative position.

```python
from .moduleC import functionC  # Imports moduleC from the same directory
from ..moduleD import functionD # Imports moduleD from the parent directory
```

Advantages:

*   Can be more concise for modules within the same package.

Disadvantages:

*   More prone to errors as the relative path is dependent on the current file's location.
*   Can become confusing and difficult to maintain in larger projects.  
*   Can break easily if the project structure changes.


**Best Practices:**

*   Generally prefer absolute imports for better readability and maintainability, especially in larger projects.
*   Use relative imports sparingly and only when absolutely necessary, often within the same package.
*   Avoid using too many levels of relative imports (`.`, `..`, `...`).
*   Always consider the clarity and maintainability of your imports.  Choosing clarity is generally superior to brevity.


[[Package Structure]]  ([[Circular Imports]])
