# [[Importing Modules]]
# [[Module Search Path]] 
The Python interpreter searches for modules in a specific order, defined by the `sys.path` variable.  This is crucial for importing modules correctly.

`sys.path` is a list of strings, each representing a directory.  The interpreter searches these directories in order until it finds the module being imported.

```python
import sys
print(sys.path) 
```

The `sys.path` list typically includes:

[[1]]. The directory containing the script being run (or the current directory if no script is specified).
[[2]]. The directories specified by the `PYTHONPATH` environment variable (if set).
[[3]]. Installation-dependent default locations (e.g., site-packages directories).


[[PYTHONPATH Environment Variable]]

[[Site-packages Directories]]

If a module is not found in any of these directories, an `ImportError` is raised.


**Modifying `sys.path`:**

You can modify `sys.path` programmatically to add or remove directories from the search path.  This is useful for:

* Importing modules from custom locations.
* Managing different versions of modules.

Example: adding a custom directory:

```python
import sys
sys.path.append('/path/to/my/modules') # replace with your path
import my_module  # now you can import your module
```

**Important Considerations:**

* **Order Matters:** The order of directories in `sys.path` is significant.  The interpreter will find the *first* occurrence of the module.
* **Namespace Conflicts:** Modifying `sys.path` can lead to namespace conflicts if you have multiple modules with the same name in different directories.
* **Security:**  Avoid arbitrarily adding directories to `sys.path` from untrusted sources, as this could expose your system to malicious code.  Be especially cautious with dynamically constructed paths.


[[Module Importing in Python]]
[[Error Handling: ImportError]]

