# [[Data Type Conversions]]
# [[Type Hinting]] in Python

Type hinting in Python allows you to specify the expected [[Data Types]] of variables, function arguments, and [[Return Values]].  This improves code readability, helps catch errors during development (using tools like MyPy), and aids in better code understanding and maintainability.

**Basic Syntax:**

```python
# Variable annotation
age: int = 30
name: str = "Alice"

# Function annotation
def greet(name: str) -> str:
    return f"Hello, {name}!"

# List annotation
numbers: list[int] = [1, 2, 3]

# Dictionary annotation
data: dict[str, int] = {"a": 1, "b": 2}
```

**Benefits:**

* **Improved Readability:** Makes code easier to understand by explicitly stating the expected types.
* **Early Error Detection:** Static type checkers (like MyPy) can identify type errors before runtime.
* **Better Code Maintainability:** Easier to refactor and modify code with clear type information.
* **Enhanced IDE Support:** IDEs can leverage type hints for better autocompletion, code navigation, and refactoring.


**Limitations:**

* Type hinting is *optional* in Python; it doesn't enforce types at runtime (unless you use a runtime type checker).
*  Can add some overhead to writing code.
*  [[Type hinting complexities]] (separate note needed)  -  dealing with complex types like unions, generics, etc. requires understanding advanced concepts.


**Related Notes:**

* [[MyPy Usage]] (separate note needed) - How to use the MyPy static type checker.
* [[Type Aliases]] (separate note needed) - Defining custom type names for improved readability.
* [[Optional Types]] (separate note needed) - Using the `Optional` type to handle cases where a variable might be `None`.

**Example with MyPy:**

```bash
# Install MyPy: pip install mypy
# Run MyPy: mypy your_script.py
```

MyPy will then report any type errors found in your code.


**Advanced Features:**

* **Type Unions:**  Specify multiple possible types for a variable.  Example: `x: int | str`
* **Generics:**  Define types that can work with different underlying types. Example: `List[T]` (where `T` is a type parameter)
* **Type Var:** Define type variables used in generics.
* [[Type Checking Decorators]] (separate note needed) – Using [[Decorators]] to enforce type checking at runtime

This concludes the basic overview of type hinting in python. Remember to consult the official python documentation for the most up-to-date and thorough explanation.
