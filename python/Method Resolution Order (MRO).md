# [[Classes and Objects]]
# [[Method Resolution Order (MRO)]] 
Python's [[MRO]] determines the order in which methods are searched for during inheritance.  It's crucial for avoiding ambiguity when a class inherits from multiple parent classes that might define the same method. Python uses the C3 linearization algorithm to ensure a consistent and predictable [[MRO]].

The `mro()` method provides a way to inspect the [[MRO]] of a class.

```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):
    pass

print(D.mro()) # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
d = D()
d.method() # Output: B (because B is listed before C in the [[MRO]])

```

**Key aspects to remember:**

*   **Depth-First, Left-to-Right:**  The algorithm prioritizes the inheritance chain from left to right.  It exhausts all parent classes of a branch before moving to the next.
*   **Linearization:**  The C3 algorithm ensures that the [[MRO]] is a linear sequence, eliminating any ambiguity in method lookup.
*   **Diamond Problem:** The [[MRO]] elegantly solves the "diamond problem," where a class inherits from two classes that share a common ancestor, avoiding duplicated method calls in the way that some other multiple inheritance schemes might cause.  [[Diamond Problem Example]]

**Related Notes:**

* [[Inheritance in Python]]
* [[Multiple Inheritance in Python]]
* [[C3 Linearization Algorithm]]

**Example demonstrating the Diamond Problem solution**

```python
class A:
    def method(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

print(D.mro()) # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

d = D()
d.method() # Prints 'A', as it's resolved correctly in the [[MRO]] ```
