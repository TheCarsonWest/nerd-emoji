**[[Python]] Polymorphism**

**[[Definition]]:**

[[Polymorphism]] allows different objects to respond to the same operation in different ways. It's a fundamental concept in [[OOP]] that enables code reusability, flexibility, and maintainability.

**[[Parameters]]:**

* **Method Overloading:** Defining multiple methods with the same name but different parameters.
* **Method Overriding:** Redefining methods in subclasses to provide different functionality.
* **Duck Typing:** Assigning objects to variables based on their attributes and behaviors rather than their class.

**Code Examples:**

**Method Overloading:**

```python
class Shape:
    def area(self, length=None, width=None, radius=None):
        if length and width:
            return length * width
        elif radius:
            return math.pi * radius ** 2
```

**Method Overriding:**

```python
class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    def speak(self):
        print("Woof!")
```

**Duck Typing:**

```python
def get_area(object):
    if hasattr(object, "area"):
        return object.area()
```

**Other [[Python]] Concepts Related to [[Polymorphism]]:**

* [[Inheritance]]: [[Polymorphism]] is built upon [[Inheritance]], which allows subclasses to inherit methods and attributes from parent classes.
* [[Abstraction]]: [[Polymorphism]] enables the creation of abstract classes and interfaces that define common method signatures, allowing subclasses to implement their own specific behavior.
* [[Data Encapsulation]]: [[Polymorphism]] supports [[Data Encapsulation]] by providing a consistent interface for accessing and manipulating data, regardless of the underlying implementation.
* [[Design Patterns]]: [[Polymorphism]] plays a crucial role in design patterns such as Strategy and Visitor, which provide flexible and extensible solutions to common programming problems.****