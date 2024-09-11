**Variables and Data Types in Python**

**What is a Variable?**

A variable is a named location in memory that stores a value. It allows us to store, retrieve, and modify data during program execution.

**Parameters of a Variable**

**Variable Name:**
* A unique identifier for the variable.
* Must start with a letter or underscore and can include letters, numbers, and underscores.
* Cannot be a reserved keyword.

**Variable Value:**
* The data stored in the variable.
* Can be any valid data type in Python.

**Variable Scope:**
* The portion of the program where the variable is accessible.
* Can be local (within a function), global (within the program), or nonlocal (within a nested function).

**Data Types in Python**

Python supports various data types, each representing a different kind of data. Some common data types include:

* **Numeric Types:**
    * Integer (int): Whole numbers, e.g., 10, 500
    * Float (float): Decimal numbers, e.g., 3.14, 5.6
    * Complex (complex): Complex numbers, e.g., 1+2j, 5-3j
* **String Types:**
    * String (str): A sequence of characters, e.g., "Hello", 'Python'
* **Sequence Types:**
    * List (list): An ordered collection of items, e.g., [1, 2, 3, 4]
    * Tuple (tuple): An immutable ordered collection of items, e.g., (1, 2, 3, 4)
* **Mapping Types:**
    * Dictionary (dict): A collection of key-value pairs, e.g., {"name": "John", "age": 30}
* **Set Types:**
    * Set (set): A collection of unique elements, e.g., {1, 2, 3, 4}
* **Boolean Type:**
    * Boolean (bool): A type representing True or False

**Creating Variables and Assigning Values**

We can create a variable by assigning it a value:

```python
my_name = "John"
age = 30
```

**Type Conversion**

Python can automatically convert between data types when necessary:

```python
x = 10  # int
y = 3.14  # float
z = str(x) + str(y)  # z becomes the string "103.14"
```

**Linking to Other Python Concepts**

* **Functions:** Variables can be passed as arguments to functions and returned as results.
* **Data Structures:** Variables can store references to data structures such as lists, dictionaries, and sets.
* **Object-Oriented Programming:** Variables can refer to objects created from classes.
* **Error Handling:** Variables can be used to store error messages and error codes.
[[Python 1 Home]]