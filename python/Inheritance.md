# [[Python 1 Home]]
# Inheritance

Inheritance is a powerful mechanism in object-oriented programming (OOP) that allows you to create new classes (child classes or subclasses) based on existing classes (parent classes or superclasses).  The child class inherits the attributes (variables) and methods (functions) of the parent class, and can also add its own unique attributes and methods, or override existing ones.

**Benefits of Inheritance:**

* **Code Reusability:** Avoids redundant code by reusing existing functionality.
* **Extensibility:** Easily extend the functionality of existing classes without modifying them.
* **Maintainability:**  Changes to the parent class are automatically reflected in the child classes.
* **Polymorphism:** Enables objects of different classes to be treated as objects of a common type. (See [[Polymorphism]])

**Example:**

```python
class Animal:  # Parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):  # Child class inheriting from Animal
    def speak(self):
        print("Woof!")

class Cat(Animal): # Child class inheriting from Animal
    def speak(self):
        print("Meow!")

my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

my_dog.speak()  # Output: Woof!
my_cat.speak()  # Output: Meow!
print(my_dog.name) # Output: Buddy (inherited from Animal)

```

**Types of Inheritance:**

* **Single Inheritance:** A class inherits from only one parent class.  (Example above)
* [[Multiple Inheritance]]: A class inherits from multiple parent classes.
* **Multilevel Inheritance:** A class inherits from another class, which in turn inherits from another class.
* **Hierarchical Inheritance:** Multiple classes inherit from a single parent class.


**Method Overriding:**  As shown in the example, the `Dog` and `Cat` classes override the `speak()` method from the `Animal` class. This allows child classes to provide their own specific implementations.

**Super() Function:** The `super()` function is used to call methods of the parent class from within the child class.  This is particularly useful when you want to extend, rather than replace, the functionality of a parent class method.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Calls the parent class's __init__ method
        self.breed = breed

    def speak(self):
        print(f"Woof! My name is {self.name}, and I'm a {self.breed}.")

```

[[Classes and Objects]]
[[Method Resolution Order (MRO)]]
