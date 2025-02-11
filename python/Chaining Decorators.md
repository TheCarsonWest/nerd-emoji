# [[Decorators]]
# [[Chaining [[Decorators]] 
Chaining decorators in Python means applying multiple decorators to a single function.  The order of application matters, as decorators are applied from the inside out (bottom to top).

```python
def my_decorator_1(func):
  def wrapper():
    print("Decorator [[1]] before")
    func()
    print("Decorator [[1]] after")
  return wrapper

def my_decorator_2(func):
  def wrapper():
    print("Decorator [[2]] before")
    func()
    print("Decorator [[2]] after")
  return wrapper

@my_decorator_1
@my_decorator_2
def say_hello():
  print("Hello!")

say_hello()
```

This will output:

```
Decorator [[1]] before
Decorator [[2]] before
Hello!
Decorator [[2]] after
Decorator [[1]] after
```

Notice how `my_decorator_2` is executed first, then `my_decorator_1`.  This is because the `@` syntax applies decorators from bottom to top.


[[Decorator Basics]]  ([[Function Wrappers]])

The above example only shows decorators without arguments.  [[Decorators]] with Arguments]]  handle more complex scenarios.  Remember to also review [[Function Scope and Closures]] as they are fundamental to understanding how decorators work.
