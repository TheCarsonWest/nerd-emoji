# [[Classes and Objects]]
# Constructors

Python doesn't have constructors in the same way as languages like Java or C++.  Instead, we use the `__init__` method.

*   `__init__` is a special method (a "dunder" method because of the double underscores) that gets called automatically when you create an instance of a class.

*   It's used to initialize the object's attributes.


```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)  # Output: Buddy
my_dog.bark()       # Output: Woof!
```

The `self` parameter represents the instance of the class being created.  It's how you refer to the object's attributes within the `__init__` method.


[[Special Methods]]  <!--This would link to another note about special methods in python -->

[[Object Instantiation]] <!--This would link to a note about creating objects in python-->
