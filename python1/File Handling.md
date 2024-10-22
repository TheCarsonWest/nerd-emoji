## [[File Handling]]

### Explanation
File handling in Python refers to the process of reading, writing, updating, and managing files on the computer system. It enables programs to perform operations like creating, deleting, opening, closing, and manipulating files.

### How to Use [[File Handling]]
To perform file operations, you need to open a file using the `open()` function. The `open()` function takes two parameters:

- `filename`: The name of the file to be opened.
- `mode`: The mode in which the file should be opened. Common modes include:

 - 'r' - Read only
 - 'w' - Write only (overwrites existing file)
 - 'a' - Append only (adds to the end of existing file)

Once the file is opened, you can use methods like `read()`, `write()`, and `close()` to perform various operations on the file.

### Code Examples
```python
# Open a file for reading
file = open("myfile.txt", "r")
# Read the contents of the file
contents = file.read()
# Close the file
file.close()
```

```python
# Open a file for writing
file = open("myfile.txt", "w")
# Write some data to the file
file.write("This is a test.")
# Close the file
file.close()
```

### Related Python Concepts

- [[Variables and Data Types]]: File handling operations involve working with strings and file objects.
- [[Operators]]: File I/O operations use operators like `+` for string concatenation.
- [[Control Flow If Statements]]: File handling operations often involve conditional execution.
- [[Functions]]: File I/O operations can be encapsulated in functions for reuse.
- [[File IO Modes]]: There are several different modes available for opening files, each with specific behavior.
# [[Python 1 Home]]