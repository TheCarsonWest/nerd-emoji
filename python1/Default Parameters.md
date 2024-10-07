## [[Default Parameters]]

### What are [[Default Parameters]]?
Default parameters are a way to give a value to a function parameter if no argument is passed when calling the function. This helps in providing more flexibility and simplifying the function call.

### How to Use [[Default Parameters]]
To define a default parameter in a function, assign a value to the parameter in the function definition. For example:

```python
def greet(name="World"):
 print(f"Hello, {name}!")
```

In the above function, `name` is a parameter with a default value of "World". If no argument is passed to the `greet` function, the value of `name` will be "World".

### Code Examples
```python
# greet the user with the provided name, or "World" if no name is given
greet()
greet("John")
```

### Other Related Python Concepts

- [[Function Parameters]]: Default parameters extend the functionality of function parameters.
- [[Variables and Data Types]]: Default parameter values can be of any data type.
- [[Control Flow If Statements]]: Default parameters can help simplify conditional statements in some cases.
- [[For Loops]]: Default parameters can reduce the need for explicit checks before entering loops.
- [[While Loops]]: Default parameters can be used to initialize loop conditions.
# [[Python 1 Home]]