# [[Private and Protected Members]]
# [[Encapsulation in Python]] 
Encapsulation is one of the four fundamental principles of object-oriented programming (OOP).  It aims to bundle data (attributes) and the methods (functions) that operate on that data within a single unit (a class), protecting the data from outside access and misuse.  This is achieved primarily through access modifiers.

Python doesn't have strict access modifiers like `public`, `private`, and `protected` found in languages like Java or C++. However, it achieves a similar effect through naming conventions and techniques.

##  Achieving [[Encapsulation in Python]] 
* **Name Mangling:**  Prefixing attribute names with double underscores (`__`) signals to Python to "mangle" the name, making it harder (but not impossible) to access directly from outside the class. This is often used to simulate private attributes.

```python
class MyClass:
    def __init__(self, value):
        self.__private_var = value  # Name mangling

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value

my_obj = MyClass(10)
print(my_obj.get_private_var())  # Access via getter method
#print(my_obj.__private_var)  # Direct access attempts name mangling -  AttributeError
my_obj.set_private_var(20)
print(my_obj.get_private_var())

#Though this can be accessed with  _MyClass__private_var, still helps control access
print(my_obj._MyClass__private_var)
```

* **Getter and Setter Methods:** These methods provide controlled access to attributes.  Getters retrieve the value of an attribute, while setters modify it, allowing you to add validation or other logic.  This is a more explicit way to enforce encapsulation.  The example above demonstrates this.


* **Internal Methods:** Methods that are not intended for direct external use can simply be left without documentation or explanation, making their usage less likely and potentially more confusing.  While not strictly enforcement, this helps with encapsulation by suggesting usage patterns.



## [[Python Access Modifiers]]  (separate note)

## [[Object-Oriented Programming Principles]] (separate note)

## Related Notes:
* [[Python Classes and Objects]]
* [[Python Getter and Setter Methods]]

