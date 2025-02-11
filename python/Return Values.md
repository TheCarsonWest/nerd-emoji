# [[Python 1 Home]]
# [[Return Values]] 
Return values are the data sent back by a function after it has completed its execution.  A function can return any data type, including `None` (if no explicit return statement is used).

```python
def add(x, y):
  """This function adds two numbers and returns the sum."""
  return x + y

result = add([[5]], [[3]])  # result will be 8
print(result)

def greet(name):
  """This function greets the person passed in as a parameter and returns a string"""
  return f"Hello, {name}!"

greeting = greet("Alice") # greeting will be "Hello, Alice!"
print(greeting)

def no_return():
    print("This function does not return a value.")

returned_value = no_return() #returned_value will be None
print(returned_value)

```

[[Python Functions]]  (link to a note about the general concept of [[Python Functions]])
[[Function Parameters]] (link to a note about [[Function Parameters]])

The `return` statement immediately exits the function and sends the specified value back to the caller.  If a function doesn't have a `return` statement, it implicitly returns `None`.  Multiple return values are possible using [[Tuples]]:

```python
def multiple_returns(a, b):
  return a, b*[[2]]

x, y = multiple_returns([[5]], [[3]])  # x will be [[5]], y will be [[6]]
print(x, y)

```

[[Tuples]] (link to a note on [[Tuples]])
