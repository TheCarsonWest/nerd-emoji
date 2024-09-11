**Python Inheritance**

**Concept:**

Inheritance is a fundamental object-oriented programming (OOP) mechanism that allows classes to inherit properties and behavior from other classes. It enables code reusability and facilitates code organization by establishing hierarchical relationships between classes.

**Parameters:**

* **Superclass (Parent Class):** The class from which the subclass inherits.
* **Subclass (Child Class):** The class that inherits from the superclass.
* **Inheritance Type:** Defines the scope of inheritance. Python supports four types:
    * Single inheritance: A subclass inherits from a single superclass.
    * Multiple inheritance: A subclass inherits from multiple superclasses.
* **Method Overriding:** Occurs when a method with the same name is defined in both the superclass and the subclass. The subclass method overrides the superclass method.
* **Method Overloading:** Occurs when a method with the same name is defined in a subclass with different parameters.

**Code Examples:**

**Single Inheritance:**

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Fido", "German Shepherd")
print(dog.name)  # Fido
print(dog.breed)  # German Shepherd
```

In this example, `Dog` inherits from the `Animal` class. `Dog` has its own `__init__` method that extends the `__init__` method of `Animal`.

**Multiple Inheritance:**

```python
class Animal:
    def __init__(self, name):
        self.name = name

class CanFly:
    def __init__(self, speed):
        self.speed = speed

class Bird(Animal, CanFly):
    def __init__(self, name, speed):
        super().__init__(name)
        super().__init__(speed)

bird = Bird("Eagle", 100)
print(bird.name)  # Eagle
print(bird.speed)  # 100
```

In this example, `Bird` inherits from both `Animal` and `CanFly`. `Bird` has its own `__init__` method that calls the `__init__` methods of both superclasses.

**Method Overriding:**

```python
class Animal:
    def eat(self):
        print("Animal eating")

class Dog(Animal):
    def eat(self):
        print("Dog eating")

dog = Dog()
dog.eat()  # Dog eating
```

In this example, the `eat` method is overridden in the `Dog` class. When `eat()` is called on an instance of `Dog`, the subclass method is executed instead of the superclass method.

**Other Related Concepts:**

* **Polymorphism:** Ability of objects of different subclasses to be treated as objects of the superclass.
* **Abstract Classes:** Classes that cannot be instantiated directly and serve as base classes for other classes.
* **Encapsulation:** Restricting access to data and methods of an object.
* **Composition:** Alternative to inheritance where objects contain other objects to achieve the desired functionality.
[[Python 1 Home]]