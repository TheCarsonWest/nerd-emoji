# [[Python [[1]] Home]]
# [[Encapsulation]]  [[Encapsulation]] is one of the fundamental principles of object-oriented programming (OOP).  It's all about bundling data (attributes) and methods (functions) that operate on that data within a single unit – a class.  The goal is to protect the data from outside access and misuse, and to control how that data is modified.

This is achieved primarily through access modifiers (although Python doesn't have strict private/public keywords like Java or C++).  We use naming conventions to indicate the intended level of access:

* **Public members:**  Accessible from anywhere (no special naming).
* **Protected members:**  Intended for internal use within the class and its subclasses.  Indicated by a single leading underscore (`_`).
* **Private members:**  Intended for exclusive use within the class itself. Indicated by a double leading underscore (`__`).  (Note:  Even "private" members in Python can still be accessed with name mangling, but it's discouraged).

```python
class MyClass:
    def __init__(self, value):
        self.public_var = value  # Public
        self._protected_var = value * [[2]] # Protected
        self.__private_var = value * [[3]] # Private

    def get_private_var(self):
        return self.__private_var

my_instance = MyClass([[5]])
print(my_instance.public_var)       # Accessing public member - OK
print(my_instance._protected_var)   # Accessing protected member - Generally OK, but discouraged from outside the class
print(my_instance.get_private_var()) # Accessing private member through a getter method - Recommended
#print(my_instance.__private_var)  # Direct access to private member - will result in AttributeError
```

[[Classes and Objects]]  [[Private and Protected Members]]
