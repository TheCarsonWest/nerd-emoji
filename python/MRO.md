# [[Multiple Inheritance]]
# [[MRO]] Notes

**[[MRO]]:** Method Resolution Order.  Determines the order in which methods are searched for during inheritance in Python.  Python uses the C3 linearization algorithm for its [[MRO]].

Crucial for understanding how inheritance works, especially with multiple inheritance.  Incorrect [[MRO]] can lead to unexpected behavior.

[[C3 Linearization]]  (This will be a separate note explaining the C3 algorithm)

Example:

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

d = D()
d.method() # Output: B (because of [[MRO]])

print(D.__mro__) # Shows the [[MRO]]: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

```

Things to explore further:

*   Diamond problem (and how Python's [[MRO]] solves it) [[Diamond Problem]]
*   Impact of [[MRO]] on super() [[super()]]
*   [[MRO]] in different Python versions (though unlikely to change significantly)

Related Notes:
* [[Inheritance]]
* [[Multiple Inheritance]]

