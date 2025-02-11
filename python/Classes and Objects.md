# [[Python [[1]] Home]]
# [[Classes and Objects]] 
Python uses classes to create user-defined data types.  A class is a blueprint for creating objects.  Objects are instances of a class.

```python
class Dog:
    def __init__(self, name, breed): #Constructor
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy", "Golden Retriever")  #Creating an object (instance of Dog class)
print(my_dog.name) # Accessing attributes
my_dog.bark() # Calling a method
```

[[Constructors]]
[[Methods]]
[[Attributes]]

Classes have:

* **Attributes:**  These are variables that hold data associated with an object (e.g., `my_dog.name`, `my_dog.breed`).
* **Methods:** These are functions that operate on the object's data (e.g., `my_dog.bark()`).  Methods always take `self` as their first parameter, which refers to the instance of the class.

**Key Concepts:**

* **`__init__` method:** This is a special method called the constructor. It's automatically called when you create a new object.  It's used to initialize the object's attributes.
* **`self` parameter:**  Refers to the instance of the class.  It allows methods to access and modify the object's attributes.


Related Notes:
* [[Inheritance]]
* [[Polymorphism]]
* [[Encapsulation]]
* [[Abstract Classes]]
* [[Multiple [[Inheritance]]
* [[Method Resolution Order ([[MRO]])]]
* [[Private and Protected Members]]

