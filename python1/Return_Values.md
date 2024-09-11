**Python Return Values**

**Explanation:**

* A return statement in Python allows a function to send back a value to the calling code.
* The return value can be of any data type, including None.
* If a return statement is not used, the function automatically returns None.

**Parameters:**

* The return statement takes an optional expression as a parameter.
* This expression can be any valid Python expression, such as a variable, literal, or function call.

**Code Examples:**

```python
# Function to return the square of a number
def square(x):
    return x * x

# Call the function and store the return value in a variable
result = square(5)
print(result)  # Output: 25
```

```python
# Function to return the maximum of two numbers
def max(a, b):
    if a > b:
        return a
    else:
        return b

# Call the function with two arguments
maximum = max(3, 7)
print(maximum)  # Output: 7
```

**Linked Python Concepts:**

* **Function Definitions:** Functions that return values are defined using the `def` keyword.
* **Variables:** The return value can be stored in a variable using the assignment operator (=).
* **Data Types:** The return value can be of any valid Python data type.
* **None:** If no return statement is used, the function automatically returns None.
* **Lambdas:** Lambdas can be used to create anonymous functions that return values.
* **Generators:** Generators can be used to return a sequence of values one at a time.
[[Python 1 Home]]