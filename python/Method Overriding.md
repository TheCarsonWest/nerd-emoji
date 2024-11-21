# [[Abstract Classes]]
# Method Overriding

Method overriding in Python occurs when a subclass provides a specific implementation for a method that is already defined in its superclass.  This allows subclasses to modify or extend the behavior of inherited methods.  Unlike some other languages (like Java), Python doesn't have explicit keywords like `override` to denote overriding.  It's purely based on inheritance and method signature matching.

**Key points:**

* **Inheritance:**  Method overriding relies on inheritance. A subclass must inherit from a superclass. [[Inheritance]]
* **Method Signature:** The overriding method in the subclass must have the *exact same* name and parameter list as the method in the superclass.  If the parameters differ, it's not overriding, but rather method overloading (which Python doesn't directly support in the same way as some other languages). [[Method Overloading (Python's Approach)]]
* **Dynamic Dispatch:**  Python uses dynamic dispatch (also known as runtime polymorphism) to determine which method to call at runtime.  The actual method called depends on the type of the object the method is invoked on.
* **`super()` function:** The `super()` function is often used within the overriding method to call the superclass's implementation. This allows the subclass to extend, rather than completely replace, the superclass's behavior.

**Example:**

```python
class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()  # Output: Generic animal sound
dog.speak()     # Output: Woof!
cat.speak()     # Output: Meow!
```

In this example, `Dog` and `Cat` override the `speak` method from the `Animal` class.

**Using `super()`:**

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        super().speak() #Calls the superclass's speak method.
        print("Woof!")

my_dog = Dog("Buddy")
my_dog.speak() # Output: Buddy makes a sound.  Woof!
```

**Potential Issues:**

* **Accidental Overriding:**  It's easy to accidentally override a method without intending to, especially in larger projects.  Careful consideration of method names and inheritance is crucial.


[[Polymorphism]]
