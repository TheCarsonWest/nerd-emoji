## [[Context Managers]]

### What are [[Context Managers]]?
Context managers are a way to define a scope where certain resources are managed automatically. They are used to ensure that resources are properly acquired, used, and released, even in the presence of exceptions.

### How to Use [[Context Managers]]
A context manager is defined using the `with` statement. The resource to be managed is assigned to a variable within the `with` block. The context manager's `__enter__()` and `__exit__()` methods are called automatically when entering and exiting the block.

```python
with context_manager as resource:
 # code using the resource
```

The `__enter__()` method is called before the code block is executed and returns the resource that should be used within the block. The `__exit__()` method is called after the code block is executed, regardless of whether any exceptions occur.

### Code Examples
```python
# open a file for writing
with open("myfile.txt", "w") as file:
 file.write("Hello world!")
```

```python
# create a temporary directory using the `with` statement
from tempfile import TemporaryDirectory

with TemporaryDirectory() as tmp_dir:
 # do something with the temporary directory
 pass
```

### Related Python Concepts

- [[File Handling]]: Context managers are commonly used for file handling operations.
- [[Exception Handling]]: Context managers can be used to handle exceptions within a specific scope.
- [[Generators]]: Context managers can be implemented using generators.
- [[Decorators]]: Context managers can be implemented using decorators.
- [[Custom [[Context Managers]]: You can create your own custom context managers to manage your resources.
# [[Python 1 Home]]