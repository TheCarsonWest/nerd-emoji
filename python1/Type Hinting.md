## [[Type Hinting]]

### What is [[Type Hinting]]?
Type hinting is a feature of Python that allows developers to include type annotations in their code to specify the expected data types of variables, function parameters, and return values. It is a non-enforced form of type checking that helps improve code readability, consistency, and the potential to detect errors early on.

### How to Use [[Type Hinting]]
Type hints are added using type annotations, which are special comments written with a colon (:) at the end of a line of code.

#### [[Functions]]
**Parameters:**
```python
def add_numbers(a: int, b: int) -> int:
 """
 Adds two numbers and returns the result.

 Args:
 a (int): The first number to add.
 b (int): The second number to add.

 Returns:
 int: The sum of the two numbers.
 """
 return a + b
```

** [[Return Values]]:**
```python
def get_max(a: int, b: int) -> int:
 """
 Returns the maximum of two numbers.

 Args:
 a (int): The first number.
 b (int): The second number.

 Returns:
 int: The maximum of the two numbers.
 """
 if a > b:
 return a
 else:
 return b
```

#### Variables
```python
name: str = "John Doe"
age: int = 30
```

### Code Examples
```python
# specify the expected data type for the 'result' variable
result: int
# assign an integer value to 'result'
result = 42
```

```python
# specify the expected data type of the 'names' list
names: list[str] = ["John", "Jane", "Mike"]
```

### Related Python Concepts

- [[Variables and Data Types]]: Type hints explicitly specify the expected data types.
- [[Functions]]: Type hints describe the data types of function arguments and return values.
- [[Function Parameters]]: Type hints provide type information for function parameters.
- [[Return Values]]: Type hints indicate the expected return type of functions.
- [[Mutable vs Immutable Types]]: Type hints can help distinguish between mutable and immutable types.
# [[Python 1 Home]]