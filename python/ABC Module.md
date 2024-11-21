# [[Abstract Classes]]
# Python Notes: ABC Module

**Current String:** `ABC Module`

**Full List:** `['ABC Module']`


The `ABC` module in Python stands for **Abstract Base Classes**.  It's used to define interfaces for classes.  This means you specify *what* methods a class *must* have, without specifying *how* those methods are implemented.

Key Concepts:

* **Abstract Base Classes (ABCs):**  These are classes that cannot be instantiated directly. They serve as blueprints for other classes.  They define a common interface that subclasses must adhere to.

* **`abstractmethod`:** A decorator used to mark methods within an ABC as abstract.  Subclasses *must* provide implementations for these methods.  If they don't, a `TypeError` is raised at runtime.


Example:

```python
from abc import ABC, abstractmethod

class Shape(ABC): # Declare Shape as an abstract base class
    @abstractmethod
    def area(self):
        pass  # Abstract method - no implementation needed here

    @abstractmethod
    def perimeter(self):
        pass # Abstract method - no implementation needed here

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self,width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)

#This will raise a TypeError because Shape is an abstract class
#shape = Shape()

circle = Circle(5)
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")

rectangle = Rectangle(4,6)
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

```

Related Notes:

* [[Abstract Methods]]
* [[Decorators]]
* [[Inheritance]]


Further points to consider:

*   Error Handling:  How to handle situations where subclasses fail to implement required abstract methods.
*   Benefits of using ABCs:  Improved code organization, maintainability, and extensibility.  Enforcing a consistent interface across different classes.
*   Use Cases:  Examples of when using ABCs is particularly beneficial (e.g., designing APIs, working with polymorphic behavior).


