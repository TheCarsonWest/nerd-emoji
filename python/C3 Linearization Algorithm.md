# [[Method Resolution Order (MRO)]]
# [[C3 Linearization Algorithm]] 
This note covers the C3 linearization algorithm used in Python's method resolution order (MRO) for resolving conflicts in multiple inheritance.

The core goal is to maintain a consistent and predictable order for attribute lookup in classes with multiple inheritance, avoiding ambiguities and ensuring that the intended superclass methods are called.  The algorithm is designed to be:

* **Consistent:**  Always produces the same [[MRO]] for a given class hierarchy.
* **Intuitive:** The resulting [[MRO]] generally reflects a programmer's intuitive expectations (though edge cases can exist).
* **Correct:** Prevents conflicts and ensures that the desired superclass methods are called in the appropriate order.


The algorithm itself is complex, but can be understood through its principles:

1. **Depth-First Search:**  It starts with the class itself, and then traverses the inheritance tree in a depth-first manner.


2. **Linearization:** It aims to create a linear order of superclasses, ensuring that all parents are visited in a consistent manner.


3. **Merging:** When encountering multiple inheritance, the algorithm carefully merges the MROs of the parent classes to avoid conflicts.  It uses a sophisticated approach to ensure that the linearization is consistent across different inheritance paths.


4. **C3 Algorithm's "Monotonicity" Property:** A key aspect of C3 is its guarantee of monotonicity. This property ensures that, if a class B is listed before C in the linearization of A, B will always appear before C in the linearization of any subclass of A.


Example illustrating the C3 algorithm:

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

In this case, the C3 algorithm produces the [[MRO]] `<D, B, C, A, object>`.


[[Python MRO]]  ([[Multiple [[Inheritance]] in Python]]) [[Depth-First Search]]


The C3 algorithm is crucial for understanding Python's sophisticated approach to multiple inheritance. While the algorithm's implementation details are intricate, the core principles of depth-first traversal and the careful merging of MROs ensure consistent and predictable behavior.  Understanding the intricacies allows for effective use and avoidance of unexpected behaviors in complex inheritance scenarios.
