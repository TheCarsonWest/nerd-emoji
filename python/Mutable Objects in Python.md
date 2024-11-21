# [[Default Parameters]]
# Mutable Objects in Python

Mutable objects in Python are objects whose internal state can be changed after they are created.  This means you can modify their contents without creating a new object.  In contrast, immutable objects cannot be changed after creation; any operation that appears to modify them actually creates a new object.

Key characteristics of mutable objects:

* **Modifiable:**  Their values can be altered in place.
* **Methods that change state:** They often have methods that modify their contents (e.g., `append()` for lists, `insert()` for lists, `update()` for dictionaries).
* **Impact on references:** Changes to a mutable object are reflected in all references to that object.


Examples of Mutable Objects:

* **Lists:**

```python
my_list = [1, 2, 3]
my_list.append(4)  # Modifies the original list
print(my_list)  # Output: [1, 2, 3, 4]
```

* **Dictionaries:**

```python
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3  # Modifies the original dictionary
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

* **Sets:**

```python
my_set = {1, 2, 3}
my_set.add(4) # Modifies the original set
print(my_set) # Output: {1, 2, 3, 4}
```

* [[Sets in Python]] (Note: This will be a seperate note)

* **User-defined classes (if implemented to be mutable):**  You can create your own mutable objects by defining classes.  The use of instance variables and methods is typically how you will make these modifications

Important Considerations:

* **Aliasing:** When you assign a mutable object to multiple variables, they all refer to the same object in memory. Changes made through one variable are visible through all others.

```python
list1 = [1, 2, 3]
list2 = list1  # list2 is an alias for list1
list1.append(4)
print(list2)  # Output: [1, 2, 3, 4]  (list2 is also modified)
```

* **Copying:** To avoid unintended side effects from aliasing, you can create a copy of a mutable object using techniques like slicing (`[:]`) for lists or the `copy()` method for more complex objects.  See [[Shallow vs Deep Copying]] for more details.


[[Immutable Objects in Python]] (Note: This will be a seperate note)

[[Shallow vs Deep Copying]] (Note: This will be a seperate note)
