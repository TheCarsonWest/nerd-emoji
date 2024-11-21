# [[Mutable vs Immutable Types]]
# Common Pitfalls with Mutability and Immutability

Mutable vs. Immutable types:  A core concept in Python. Understanding this is crucial to avoid unexpected behavior.

* **Immutable:**  These objects cannot be changed after creation.  Changes create a *new* object. Examples include:
    * `int`, `float`, `bool`, `str`, `tuple`
    * `frozenset`

* **Mutable:** These objects *can* be modified in place. Examples include:
    * `list`, `dict`, `set`

**Pitfalls:**

1. **Modifying lists within loops:**
    ```python
    my_list = [[1, 2], [3, 4]]
    for sublist in my_list:
        sublist.append(5)  # Modifies the original list in place!
    print(my_list)  # Output: [[1, 2, 5], [3, 4, 5]]
    ```

    This is often unexpected.  If you need to create new lists, use list comprehension or a loop that creates new objects:
    ```python
    my_list = [[1, 2], [3, 4]]
    new_list = [sublist + [5] for sublist in my_list]  # Creates new sublists
    print(new_list) #Output: [[1, 2, 5], [3, 4, 5]]
    print(my_list) #Output: [[1, 2], [3, 4]]
    ```

2. **Default mutable arguments in functions:**

    ```python
    def add_to_list(item, my_list=[]): # Default argument is a mutable list!
        my_list.append(item)
        return my_list

    print(add_to_list(1))  # Output: [1]
    print(add_to_list(2))  # Output: [1, 2]  Unexpected!  The list persists across calls.
    ```

    The default list is created *only once* when the function is defined.  To fix this, use `None` as the default and create a new list inside the function:

    ```python
    def add_to_list(item, my_list=None):
        if my_list is None:
            my_list = []
        my_list.append(item)
        return my_list

    print(add_to_list(1))  # Output: [1]
    print(add_to_list(2))  # Output: [2]
    ```

3. **Shallow vs. Deep Copying:** [[Shallow vs Deep Copy]]  This is especially relevant when dealing with nested mutable objects.  A shallow copy only copies the references, not the objects themselves. A deep copy creates entirely new copies.

4. **Tuple containing mutable objects:**

    Tuples themselves are immutable, but they can contain mutable objects.  Modifying the contained mutable object still changes the tuple's content (because the tuple only holds a reference to the object).

    ```python
    my_tuple = ([1, 2], 3)
    my_tuple[0].append(3) # Modifies the list *inside* the tuple
    print(my_tuple) #Output: ([1, 2, 3], 3)
    ```


5. **Aliasing:** When two variables refer to the same object (especially a mutable object), changes through one variable affect the other.


[[List Comprehensions]]
[[Function Arguments]]
