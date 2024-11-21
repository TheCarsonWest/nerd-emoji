# [[Classes and Objects]]
# Abstract Classes

Abstract classes are classes that cannot be instantiated directly.  They serve as blueprints for other classes (subclasses).  They often contain one or more abstract methods, which are methods without a concrete implementation. Subclasses *must* provide implementations for these abstract methods.

Key features:

* **Abstract Methods:** Defined using the `@abstractmethod` decorator from the `abc` (Abstract Base Classes) module.  They have a signature but no body (or just a `pass` statement).

* **`abc.ABC`:**  The base class for creating abstract classes.  Your abstract class should inherit from `abc.ABC`.

* **Enforcing Implementation:** Abstract classes ensure that subclasses implement specific methods, promoting code consistency and preventing errors.


```python
from abc import ABC, abstractmethod

class Shape(ABC):  # Inherits from abc.ABC, making it an abstract class
    @abstractmethod
    def area(self):
        pass  # No implementation in the abstract class

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

#Trying to instantiate Shape will raise an error
#my_shape = Shape() #TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

my_circle = Circle(5)
print(my_circle.area())
my_square = Square(4)
print(my_square.perimeter())

```

[[ABC Module]]  ([[Method Overriding]]) [[Polymorphism]]
