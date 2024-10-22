## [[Metaclasses]]

### What are [[Metaclasses]]?
 [[Metaclasses]] are classes that create other classes. They provide a way to modify the behavior of classes at the time of their creation. This allows for advanced customization and control over the creation and behavior of objects.

### How to Use [[Metaclasses]]
 [[Metaclasses]] are defined using the `type` keyword, followed by the metaclass name, the tuple of base classes, and the class body. The body of a metaclass typically contains methods that modify the behavior of the class being created.

```python
class MyMetaclass(type):
 def __new__(cls, name, bases, attrs):
 # modify the class being created
 return super().__new__(cls, name, bases, attrs)
```

The `__new__` method is the most commonly overridden method in metaclasses. It is called when a new class is created and provides an opportunity to modify the class before it is returned.

### Code Examples
```python
class MyMetaclass(type):
 def __new__(cls, name, bases, attrs):
 attrs['foo'] = 'bar'
 return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMetaclass):
 pass

obj = MyClass()
print(obj.foo) # prints 'bar'
```

### Related Python Concepts

- [[Classes and Objects]]: [[Metaclasses]] provide a way to customize the behavior of classes and objects.
- [[Inheritance]]: [[Metaclasses]] can be used to create new classes that inherit from existing classes.
- [[Polymorphism]]: [[Metaclasses]] can be used to change the behavior of methods and properties based on the class of an object.
- [[Encapsulation]]: [[Metaclasses]] can be used to restrict access to attributes and methods of a class.
- [[Modules and Packages]]: [[Metaclasses]] can be used to create modular and reusable code for creating and customizing classes.
# [[Python 1 Home]]