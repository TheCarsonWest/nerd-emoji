**Variables and Data Types in Python**

**What is a [[Variable]]?**

A [[Variable]] is a named location in memory that stores a value. It allows us to store, retrieve, and modify data during Functions.

**Parameters of a [[Variable]]**

**[[Variable Name]]:**
* A unique identifier for the [[Variable]].
* Must start with a letter or underscore and can include letters, numbers, and underscores.
* Cannot be a reserved keyword.

**[[Variable Value]]:**
* The data stored in the [[Variable]].
* Can be any valid Data Types in Python.

**[[Variable Scope]]:**
* The portion of the program where the [[Variable]] is accessible.
* Can be local (within a function), global (within the program), or nonlocal (within a nested function).

**Data Types in Python**

Python supports various Data Types in Python, each representing a different kind of data. Some common Data Types include:

* **Numeric Types:**
    * Integer (Integers): Whole numbers, e.g., 10, 500
    * Float (Floats): Decimal numbers, e.g., 3.14, 5.6
    * Complex (Complexes): Complex numbers, e.g., 1+2j, 5-3j
* **String Types:**
    * String (Strings): A sequence of characters, e.g., "Hello", 'Python'
* **Sequence Types:**
    * [[Lists]] (Lists): An ordered collection of items, e.g., 1, 2, 3, 4
    * [[Tuples]] (Tuples): An immutable ordered collection of items, e.g., (1, 2, 3, 4)
* **Mapping Types:**
    * [[Dictionaries]] (Dictionaries): A collection of key-value pairs, e.g., {"name": "John", "age": 30}
* **Set Types:**
    * Sets (Sets): A collection of unique elements, e.g., {1, 2, 3, 4}
* **Boolean Type:**
    * Boolean (Booleans): A Type representing True or False

**Creating Variables and Assigning Values**

We can create a [[Variable]] by assigning it a Value:

```python
my_name = "John"
age = 30
```

**Type Conversion**

Python can automatically convert between Data Types when necessary:

```python
x = 10  # int
y = 3.14  # float
z = str(x) + str(y)  # z becomes the string "103.14"
```