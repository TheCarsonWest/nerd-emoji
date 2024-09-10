**Python Dictionaries**

**Explanation:**
A dictionary in Python is an unordered collection of key-value pairs, where each key is unique and points to a corresponding value. Dictionaries are mutable, meaning their content can be modified. They are commonly used to store data in a structured manner, especially when key-based access is required.

**Parameters:**

- **Key:** A unique identifier for each entry. Can be any immutable type (e.g., string, integer, tuple).
- **Value:** The data associated with the key. Can be any type of object.

**Code Examples:**

```python
# Create a dictionary
my_dict = {"name": "John Doe", "age": 30, "city": "New York"}

# Access a value by key
print(my_dict["name"])  # Output: John Doe

# Add a new key-value pair
my_dict["job"] = "Software Engineer"

# Iterate over the dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Check if a key exists
if "email" in my_dict:
    print("Email key exists")
else:
    print("Email key does not exist")
```

**Linked Concepts:**

- **Lists:** Lists are ordered collections of elements. Dictionaries differ from lists in that they use unique keys for access, while lists use indices.
- **Tuples:** Tuples are immutable sequences of elements. They can be used as keys in dictionaries because they are hashable (i.e., they can be converted to unique identifiers).
- **Sets:** Sets are unordered collections of unique elements. They are often used as keys in dictionaries when uniqueness is required.
- **JSON:** JSON (JavaScript Object Notation) is a data format that represents objects as key-value pairs. Dictionaries can be easily converted to and from JSON using the `json` module.