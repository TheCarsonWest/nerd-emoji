# [[Operators]]
# [[Operator Overloading]] 
Operator overloading allows you to define the behavior of built-in operators (like `+`, `-`, `*`, `/`, etc.) for user-defined types (classes).  This makes your classes more intuitive and Pythonic.

**How it works:**

Operator overloading is achieved by defining special methods within your class.  These methods have double underscores (`__`) at the beginning and end of their names (also known as "dunder" methods).  For example:

```python
class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloads the '+' operator
        return MyVector(self.x + other.x, self.y + other.y)

    def __str__(self): #Overloads the str() function.
        return f"({self.x}, {self.y})"

v1 = MyVector(1, 2)
v2 = MyVector(3, 4)
v3 = v1 + v2  # Uses the __add__ method
print(v3) # prints (4,6)
print(str(v3)) #prints (4,6)

```

Here, `__add__` is overloaded to define the behavior of the `+` operator for `MyVector` objects.  The `+` operator now performs vector addition.


**Commonly Overloaded Operators and their corresponding methods:**

* `+`: `__add__`
* `-`: `__sub__`
* `*`: `__mul__`
* `/`: `__truediv__`
* `//`: `__floordiv__`
* `%`: `__mod__`
* `**`: `__pow__`
* `==`: `__eq__`
* `!=`: `__ne__`
* `>`, `<`, `>=`, `<=`: `__gt__`, `__lt__`, `__ge__`, `__le__`


**Important Considerations:**

* **Return Type:** The special methods should usually return an instance of the same class or a compatible type.
* **Error Handling:**  You should include error handling (e.g., `TypeError` for incompatible types) within your overloaded methods.
* **Readability:** While powerful, overuse can make your code harder to understand. Use operator overloading judiciously where it enhances clarity and usability.


[[Dunder Methods]]
[[Error Handling in Python]]
[[Magic Methods]]

