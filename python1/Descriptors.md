## [[Descriptors]]

### What are [[Descriptors]]?
 [[Descriptors]] are a mechanism in Python that provide a way to define custom behavior for object attributes. They allow attributes to be accessed, set, and deleted in a controlled manner, providing more flexibility and control over object properties.

### How to Use [[Descriptors]]
 [[Descriptors]] are defined as classes with special methods:

- **__get__(self, instance, owner)**: Invoked when the attribute is accessed.
- **__set__(self, instance, value)**: Invoked when the attribute is assigned a new value.
- **__delete__(self, instance)**: Invoked when the attribute is deleted.

The first parameter (`self`) represents the descriptor instance, the second (`instance`) is the object instance the attribute belongs to, and the third (`owner`) is the class that owns the attribute (may be different from `instance` in inheritance scenarios).

### Code Examples
```python
# Descriptor to convert attribute access to uppercase
class UppercaseDescriptor:
 def __get__(self, instance, owner):
 return instance._value.upper()

 def __set__(self, instance, value):
 instance._value = value

# Example class using the descriptor
class Example:
 name = UppercaseDescriptor()

 def __init__(self, name):
 self._value = name

e = Example("John Doe")
print(e.name) # Output: "JOHN DOE"
```

### Other Python Concepts Closely Related to [[Descriptors]]

- [[Metaclasses]]: [[Descriptors]] can be used with metaclasses to modify the behavior of classes themselves.
- [[Properties]]: Properties provide a way to define getter, setter, and deleter methods for object attributes, similar to descriptors.
- [[Decorators]]: [[Decorators]] can also be used to modify object attributes, although descriptors offer more flexibility and control.
- [[Class and Objects]]: [[Descriptors]] operate on object attributes, providing a means to define custom behavior for these attributes.
- [[Inheritance]]: [[Descriptors]] can be inherited by subclasses, allowing for reusable attribute customization across multiple classes.
# [[Python 1 Home]]