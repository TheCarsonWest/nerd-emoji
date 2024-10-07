## [[Duck Typing]]

### Definition
Duck typing is a concept in Python that allows objects to be used based on their behavior rather than their type. In other words, if an object can "quack" like a duck and "swim" like a duck, it can be treated as a duck, even if it is not an instance of the `Duck` class.

### Usage
Duck typing works by checking if an object has the necessary attributes or methods to perform a specific task. This is done dynamically at runtime, without relying on static type checking.

### Code Examples
```python
class Duck:
 def quack(self):
 print("Quack!")

class Swan:
 def quack(self):
 print("Honk!")

# create a list of objects that can quack
animals = [Duck(), Swan()]

# iterate over the list and call the quack() method on each object
for animal in animals:
 animal.quack()
```

Output:
```
Quack!
Honk!
```

In this example, the `animals` list contains both a `Duck` instance and a `Swan` instance. However, since both objects have the `quack()` method, they can be treated as ducks and their `quack()` methods can be called.

### Related Python Concepts

- [[Variables and Data Types]]: Duck typing heavily relies on dynamic type checking at runtime, rather than static type checking.
- [[Classes and Objects]]: Duck typing allows objects to be used interchangeably as long as they have similar behaviors, regardless of their class hierarchy.
- [[Inheritance]]: Duck typing can be used in place of inheritance to create polymorphic behavior.
- [[Polymorphism]]: Duck typing enables objects to respond differently to the same method calls, based on their actual behavior.
- [[Encapsulation]]: Duck typing emphasizes the behavior of objects rather than their internal implementation, promoting a level of encapsulation.
# [[Python 1 Home]]