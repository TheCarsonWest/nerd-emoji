# [[Namespaces and Scope]]
# [[Nested Functions]] 
Nested functions are functions defined inside other functions.  They have access to the variables in their enclosing scope (the outer function's scope), even after the outer function has finished executing (closure). This is a powerful feature for creating specialized functions or encapsulating logic.


```python
def outer_function(x):
  """This is the outer function."""
  y = 5  # Variable in outer function's scope

  def inner_function(z):
    """This is the nested function."""
    return x + y + z

  return inner_function

# Example usage:
my_function = outer_function(2)  #Creates a closure
result = my_function(3)  #inner_function accesses x and y from the outer function even after outer_function has completed
print(result)  # Output: 10

```

[[Closures]]  -  This needs a seperate explanation on how the inner function retains access to the outer function's variables even after the outer function has completed.

[[Scope and Lifetime of Variables]] - Needs further explanation on how variable scope and lifetime relate to nested functions.

[[Decorators]] -  Nested functions are a key part of how decorators work in Python.  This is a related topic.

[[Lambda Functions]] - While not strictly nested, lambda functions can be used within nested functions and share similar scoping rules.
