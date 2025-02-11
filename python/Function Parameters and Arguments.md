# [[Python Functions]]
# [[Function Parameters and Arguments]] 
Python functions utilize parameters to receive input and arguments to provide that input during function calls.  There's a subtle but important distinction.

* **Parameters:** These are defined within the function's definition. They act as placeholders for the values that will be passed in.

* **Arguments:** These are the actual values passed to the function when it's called.


```python
def greet(name, greeting="Hello"): # 'name' and 'greeting' are parameters
    print(f"{greeting}, {name}!")

greet("Alice") # "Alice" is an argument for 'name', "Hello" is the default argument for 'greeting'
greet("Bob", "Good morning") # "Bob" and "Good morning" are arguments
```

**Types of Parameters:**

* **Positional Parameters:**  The order matters.  Arguments are matched to parameters based on their position in the function call.

* **Keyword Arguments:**  Arguments are explicitly assigned to parameters using the parameter name. Order doesn't matter.

```python
greet(greeting="Hi", name="Charlie") #Keyword Arguments
```

* **[[Default Parameters]]:**  Parameters can have default values. If an argument isn't provided for a parameter with a default, the default is used.  Default parameters must come after non-default parameters in the function definition.

* **[[Variable-Length Arguments]] (Arbitrary Arguments):**
    * `*args`:  Collects any number of positional arguments into a tuple.
    * `**kwargs`: Collects any number of keyword arguments into a dictionary.

```python
def my_function(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

my_function([[1, [[2], [[3], [[4], [[5], name="Alice", age=30)
```

[[Variable-Length Arguments]]

**Argument Passing:**

Python uses pass-by-object-reference.  This means that when you pass a mutable object (like a list or dictionary) to a function, the function can modify the original object.  If you pass an immutable object (like an integer or string), the original object is not modified within the function.

[[Pass-by-Object-Reference]]


**Scope and Lifetime of Variables:**  Parameters have local scope within the function.  [[Scope and Lifetime of Variables]]

**Example illustrating mutability and immutability in argument passing:**

```python
def modify_list(my_list):
    my_list.append([[4])

my_list = [[1, [[2], [[3]]
modify_list(my_list)
print(my_list)  # Output: [[1, [[2], [[3], [[4]]  (List modified)


def modify_string(my_string):
    my_string += "!"

my_string = "hello"
modify_string(my_string)
print(my_string)  # Output: hello (String not modified in place)
```
