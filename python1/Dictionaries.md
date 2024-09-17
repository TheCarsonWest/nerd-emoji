**Python Dictionaries**

**Definition:**

A Dictionary in Python is an unordered collection of key-value pairs. Each key is associated with a value, and the key-value pairs are enclosed in curly braces.

**Parameters:**

* ** Keys:** Unique and immutable objects of any type (e.g., number, string, tuple).
* **Values:** Any type of object (e.g., number, string, [[Lists]]).
* **Order:** Dictionaries are unordered; elements are not stored or accessed in any specific sequence.

**Code Examples:**

**Creation:**

```python
my_dict = {
    "name": "John Doe",
    "age": 30,
    "occupation": "Software Engineer"
}
```

**Access:**

* **By key:** Use square brackets to access the value associated with a specific key.

```python
print(my_dict"name")  # Output: John Doe
```

* **Using get() method:** Returns the value associated with a key or None if the key doesn't exist.

```python
print(my_dict.get("email", "N/A"))  # Output: N/A
```

**Addition:**

```python
my_dict"email" = "john.doe@example.com"
```

**Iteration:**

* **Keys:** Use a for loop to iterate through the keys of a Dictionary.

```python
for key in my_dict:
    print(key)
```

* **Key-value pairs:** Use the items() method to iterate through key-value pairs as tuples.

```python
for key, value in my_dict.items():
    print(key, value)
```

**Other Python Concepts:**

* **[[Sets]]******: [[Sets]] are unordered collections of unique elements, similar to Dictionary keys.
* **[[Lists]]****: [[Lists]] are ordered collections of elements, unlike Dictionaries.
* **Nesting:** Dictionaries can be nested within other Dictionaries or [[Lists]], creating a hierarchical data structure.

**Advantages:**

* Efficient lookup and retrieval of data by key.
* Easily extendable and modifiable.
* Can be used to represent complex data structures.

**Disadvantages:**

* Not ordered, so elements cannot be accessed in a specific sequence.
* Keys must be unique and immutable, which can limit flexibility in some cases.

Python 1 HomeHere is a list of the other topics in this course:**