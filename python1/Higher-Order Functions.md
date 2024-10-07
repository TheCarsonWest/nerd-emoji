## Higher-Order [[Functions]]

### Explanation
Higher-Order [[Functions]] (HOFs) are functions that can take other functions as arguments or return functions as their results. They allow for a powerful level of abstraction and code reuse by enabling the passing of behavior as data.

### How to Use Higher-Order [[Functions]]
When using HOFs, there are two main scenarios:

- **Passing a function as an argument:** This is achieved by assigning a function to a variable and passing it to the HOF.
- **Returning a function as a result:** The HOF generates and returns a new function based on its input arguments.

### Code Examples
**Passing a function as an argument:**

```python
def apply_operation(numbers, operation):
 return [operation(num) for num in numbers]

def square(num):
 return num ** 2

# apply the square operation to a list of numbers
result = apply_operation([1, 2, 3], square)
print(result) # [1, 4, 9]
```

**Returning a function as a result:**

```python
def create_adder(value):
 def adder(arg):
 return arg + value
 return adder

# create an adder function that adds 5
adder = create_adder(5)

# use the adder function to add 10
result = adder(10)
print(result) # 15
```

### Related Python Concepts

- [[Lambda [[Functions]]: Lambda functions are anonymous functions that can be used within HOFs.
- [[Functions]]: HOFs utilize functions as arguments or return values.
- [[Map, Filter, and Reduce]]: These are built-in HOFs that perform common operations on iterables.
- [[Closures]]: [[Closures]] allow HOFs to retain access to variables outside their scope.
- [[Decorators]]: [[Decorators]] are HOFs that modify the behavior of other functions.
# [[Python 1 Home]]