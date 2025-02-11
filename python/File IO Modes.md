# [[File Handling]]
# [[File IO Modes]] 
Python's built-in `open()` function allows for various file access modes, influencing how the file is handled during operations.  These modes are specified as a second argument to `open()`.

Common Modes:

*   `'r'` (read): Opens the file for reading.  This is the default mode.  An error occurs if the file does not exist.
*   `'w'` (write): Opens the file for writing.  If the file exists, its contents are overwritten. If the file does not exist, a new file is created.
*   `'x'` (exclusive creation): Opens the file for writing, but only if the file does not already exist.  If the file exists, an error is raised.
*   `'a'` (append): Opens the file for writing.  If the file exists, new data is appended to the end of the file. If the file does not exist, a new file is created.
*   `'b'` (binary):  Used in conjunction with other modes (`'rb'`, `'wb'`, `'ab'`, `'xb'`). Opens the file in binary mode.  Crucial for working with non-text files (images, executables, etc.).  Data is read and written as bytes.
*   `'t'` (text): Used in conjunction with other modes (`'rt'`, `'wt'`, `'at'`). Opens the file in text mode (this is the default). Data is read and written as strings.  Handles newline characters according to the system's convention.
*   `'+'` (update): Used with other modes (`'r+'`, `'w+'`, `'a+'`, `'x+'`). Opens the file for both reading and writing.


Example Usage:

```python
# Reading a file
f = open("my_file.txt", "r")
contents = f.read()
f.close()

# Writing to a file
f = open("my_file.txt", "w")
f.write("Hello, world!")
f.close()

# Appending to a file
f = open("my_file.txt", "a")
f.write("\nThis is appended text.")
f.close()

#Binary read
f = open("image.jpg","rb")
image_data = f.read()
f.close()

# safer way to handle files: using 'with' statement. Auto closes file for you.
with open("my_file.txt", "r") as file:
    contents = file.read()
    print(contents)

```

[[File Handling]] Best Practices]]  [[Error Handling]] with Files]] [[Context Managers]]
