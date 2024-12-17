# [[Python 1 Home]]
# [[Polymorphism]]  [[Polymorphism]] allows objects of different classes to be treated as objects of a common type.  This is particularly useful when dealing with inheritance.

* **Example:**  Consider a scenario where you have different shapes (circle, square, triangle) each with an `area()` method.  [[Polymorphism]] allows you to call `area()` on any shape object without needing to know its specific type.

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(shape.area()) # Polymorphic call to area()
```

[[Inheritance]]  (This needs its own note)

[[Classes and Objects]] (This needs its own note)


Related notes:

- [[Method Resolution Order (MRO)]]
- [[Abstract Classes]] (This note should explain abstract base classes and their use in polymorphism)

