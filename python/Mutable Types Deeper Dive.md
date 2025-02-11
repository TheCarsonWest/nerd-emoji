# [[Mutable vs Immutable Types]]
# Mutable Types: Deeper Dive

[[Mutable Objects in Python]] are those whose internal state can be changed after creation.  This contrasts with immutable objects, where the value remains constant throughout its lifetime.  Understanding mutability is crucial for avoiding unexpected behavior and writing efficient code.

Key Mutable Types:

* **[[Lists]]:**  `1`
    ```python
    my_list = [[1, [[2], [[3]]
    my_list.append([[4])  # Modifies the list in place
    print(my_list)  # Output: [[1, [[2], [[3], [[4]]
    ```

* **[[Dictionaries]]:** `{}`
    ```python
    my_dict = {"a": [[1, "b": [[2]}
    my_dict["c"] = [[3]  # Adds a new key-value pair
    print(my_dict)  # Output: {'a': [[1, 'b': [[2], 'c': [[3]}
    ```

* **Sets:** `set()`
    ```python
    my_set = {[[1, [[2], [[3]}
    my_set.add([[4])  # Adds an element to the set
    print(my_set)  # Output: {[[1, [[2], [[3], [[4]}
    ```

* [[List Comprehensions]] -  A concise way to create [[Lists]], often involving manipulation of mutable objects.


* [[Dictionary Comprehensions]] - Similar to [[List Comprehensions]], but for [[Dictionaries]].


* [[Set Comprehensions]] -  Similar to list and dictionary comprehensions, but for sets.


**Implications of Mutability:**

* **Aliasing:** When you assign a mutable object to a new variable, both variables point to the *same* object in memory. Modifying the object through one variable affects the other.

    ```python
    list1 = [[1, [[2], [[3]]
    list2 = list1
    list2.append([[4])
    print(list1)  # Output: [[1, [[2], [[3], [[4]]  list1 is also modified!
    ```

* **Function Side Effects:**  Functions that modify mutable objects passed as arguments can have unintended consequences if you are not aware of the mutability.  Consider using copies to avoid this, which will be discussed in [[Shallow vs. Deep Copy]].

* **Memory Management:**  Modifying mutable objects in place is generally more efficient than creating entirely new objects.


**Example of unexpected behavior (due to mutability):**

```python
def modify_list(my_list):
    my_list.append([[4])

my_list = [[1,[[2],[[3]]
modify_list(my_list)
print(my_list) # Output: [[1,[[2],[[3],[[4]]. The original list is changed!
```

[[Immutable Types]] - A comparison to help solidify the concept of mutability.  This will cover strings, [[Tuples]], numbers, etc.

[[Copying Objects]] -  Methods for creating independent copies of mutable objects to avoid aliasing problems.
