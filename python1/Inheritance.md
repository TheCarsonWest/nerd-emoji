## [[Inheritance]] in Python

### What is [[Inheritance]]?
 [[Inheritance]] is a fundamental concept in object-oriented programming that allows a new class (child class) to inherit properties and methods from an existing class (parent class). It enhances code reusability, reduces redundancy, and promotes the principles of "has-a" and "is-a" relationships between objects.

### How to Use [[Inheritance]]
To create a child class that inherits from a parent class, use the following syntax:

```python
class ChildClass(ParentClass):
 # Child class definition
```

**Note:**
- The `ChildClass` inherits all the attributes and methods defined in the `ParentClass`.
- The `ChildClass` can define additional attributes and methods specific to it.

### Code Example
```python
# Parent class: Animal
class Animal:
 def __init__(self, name):
 self.name = name

 def make_sound(self):
 print("Generic animal sound")

# Child class: Dog, inherits from Animal
class Dog(Animal):
 def bark(self):
 print("Woof!")

# Create a Dog object
my_dog = Dog("Buddy")

# Access inherited attribute
print(my_dog.name) # Output: Buddy

# Call inherited method
my_dog.make_sound() # Output: Generic animal sound

# Call child class method
my_dog.bark() # Output: Woof!
```

### Related Python Concepts

- [[Classes and Objects]]: [[Inheritance]] extends the functionality of existing classes by creating subclasses.
- [[Polymorphism]]: Child classes can override methods from the parent class, allowing different behaviors for objects of the same type.
- [[Encapsulation]]: [[Inheritance]] enables the reuse of protected and public attributes and methods, providing a level of abstraction and data hiding.
- [[Modules and Packages]]: [[Inheritance]] can be used to organize and structure code modules by creating hierarchies of related classes.
- [[Abstract Classes]]: Abstract classes can be used as parent classes to define common interfaces that child classes must implement.
# [[Python 1 Home]]