**Python [[File Handling]]**

**What is [[File Handling]]?**

[[File Handling]] refers to the process of creating, reading, writing, and modifying files in a computer system using a programming language. In Python, [[File Handling]] capabilities are provided through the open() function.

**Parameters for open() Function:**

* **Filename:** The name of the file to be opened.
* **Mode:** This parameter specifies how the file is to be opened. Common modes include:
    * 'r': Open for reading (default)
    * 'w': Open for writing, overwriting any existing content
    * 'a': Open for appending content at the end
    * 'r+': Open for both reading and writing
    * 'w+': Open for writing and reading, overwriting any existing content
* **Buffering:** This parameter specifies how data is stored in memory before being written to the file. Common values are:
    * 'None': No buffering
    * '0': Unbuffered
    * '1': Line buffered
    * '2': Fully buffered

**Code Examples**

**Opening a File:**

```python
with open('myfile.txt', 'r') as file:
    # Perform operations on the file
```

**Reading from a File:**

```python
with open('myfile.txt', 'r') as file:
    data = file.read()
    print(data)
```

**Writing to a File:**

```python
with open('myfile.txt', 'w') as file:
    file.write("Hello, world!")
```

**Appending to a File:**

```python
with open('myfile.txt', 'a') as file:
    file.write("This is a new line.")
```

**Closing a File:**

It is important to close a file after performing operations on it to release system resources. The preferred method is to use the 'with' statement, which automatically closes the file when the block exits.

**Other Python Concepts Linked to [[File Handling]]:**

* [[File_Objects]]: Files opened using the 'open()' function are represented as file objects, which provide methods for reading, writing, and manipulating the file.
* [[Context Managers]]: The 'with' statement acts as a [[Context Managers]], ensuring that the file is automatically closed even in case of exceptions.
* [[Exception Handling]]: When working with files, it is important to handle exceptions such as FileNotFoundError, PermissionError, and IOError.
* [[File_I/O_Operations]]: [[File Handling]] operations in Python are non-blocking, which means that they do not block the main thread while performing tasks.**