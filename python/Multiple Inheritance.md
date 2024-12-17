# [[Classes and Objects]]
# [[Multiple Inheritance]] 
Multiple inheritance in Python allows a class to inherit from multiple parent classes.  This means a child class can gain attributes and methods from several different sources.

**Example:**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)  # Call the parent class's constructor
        self.fur_color = fur_color

    def give_birth(self):
        print("Giving birth to live young")


class Flyer:
    def fly(self):
        print("Flying")


class Bat(Mammal, Flyer): #Inherits from Mammal and Flyer
    def __init__(self, name, fur_color):
        super().__init__(name, fur_color)

    def speak(self): #Method overriding
        print("Squeak!")


my_bat = Bat("Batman", "Black")
my_bat.speak()  # Output: Squeak!
my_bat.give_birth() # Output: Giving birth to live young
my_bat.fly() #Output: Flying
```

**Method Resolution Order (MRO):** [[MRO]]  This determines the order in which methods are searched for when a method call is made. Python uses the C3 linearization algorithm to determine the MRO.  Understanding MRO is crucial to avoid ambiguity and unexpected behavior in multiple inheritance scenarios.

**Diamond Problem:** [[Diamond Problem]] A classic problem in multiple inheritance where two parent classes have a common ancestor, and the child class inherits from both.  This can lead to conflicts if both parents implement the same method.


**Advantages:**

* Code Reusability:  Avoids repeating code in multiple classes.
* Flexibility: Allows creation of complex class hierarchies.


**Disadvantages:**

* Complexity: Can make code harder to understand and maintain.
* Ambiguity: Potential for conflicts if parent classes have methods with the same name (see Diamond Problem).


**When to use:**

Multiple inheritance should be used cautiously.  It's powerful, but adds significant complexity.  Favor composition over inheritance whenever possible.  Only use multiple inheritance when it clearly simplifies the design and avoids unnecessary complexity.  Consider if a simpler alternative using single inheritance or composition could achieve similar functionality.
