# [[Method Resolution Order (MRO)]]
# [[Diamond Problem Example]] 
The diamond problem arises in multiple inheritance when a class inherits from two classes that have a common ancestor, and both ancestor and descendant classes implement the same method.  This creates ambiguity: which version of the method should the inheriting class use?

Python resolves this using Method Resolution Order ([[MRO]]).

```python
class A:
    def method(self):
        print("A's method")

class B(A):
    def method(self):
        print("B's method")

class C(A):
    def method(self):
        print("C's method")

class D(B, C):
    pass

d = D()
d.method()  # Output: B's method
```

In this example, `D` inherits from `B` and `C`, both of which inherit from `A`. All three classes have a `method`.  Python's [[MRO]] determines the order in which methods are searched (Depth-First, Left-to-Right).  Because `B` is listed before `C` in `D`'s inheritance, `B`'s version of `method` is used.

To understand this fully, you need to grasp:

- [[Method Resolution Order (MRO)]]
- [[Multiple Inheritance in Python]]


You can check the [[MRO]] using `D.__mro__` or `help(D)`:

```python
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

This shows the order in which Python will search for methods in class `D`.  It follows the Depth-First, Left-to-Right rule from the inheritance declaration.  Understanding this order is key to avoiding unexpected behavior in multiple inheritance scenarios.
