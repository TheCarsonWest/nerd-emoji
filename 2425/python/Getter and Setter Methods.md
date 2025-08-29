# [[Private and Protected Members]]
# [[Getter and Setter Methods]] 
These methods provide controlled access to an object's attributes.  They are crucial for encapsulation and data integrity.

**Why use them?**

* **[[Encapsulation]]:** Hide internal object state.  Prevent direct manipulation of attributes, which can lead to inconsistencies or errors.
* **Data Validation:**  Enforce constraints on attribute values before they are assigned.  This ensures data remains valid and prevents unexpected behavior.
* **Maintainability:** Makes it easier to modify internal implementation without affecting external code that uses the object.


**Example:**

```python
class Person:
    def __init__(self, age):
        self._age = age  # Using _age indicates a protected attribute (convention, not enforced)

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age cannot be negative")

person = Person(30)
print(person.get_age())  # Accessing age using getter

person.set_age(35)  # Modifying age using setter
print(person.get_age())

try:
    person.set_age(-5)
except ValueError as e:
    print(e) # Handles invalid age using error message
```

**Alternative using `@property` decorator (Pythonic way):**

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age cannot be negative")

person = Person(30)
print(person.age) # Access like a normal attribute

person.age = 35
print(person.age)

try:
    person.age = -5
except ValueError as e:
    print(e)
```

[[Property Decorator in Python]]  [[Encapsulation in OOP]] [[Error Handling in Python]]
