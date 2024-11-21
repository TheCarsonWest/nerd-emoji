# [[Python 1 Home]]
# File Handling

Key aspects to remember about file handling in Python:

*   **Opening Files:**  Use the `open()` function.  Specify the filename and the mode ('r' for reading, 'w' for writing, 'a' for appending, 'x' for exclusive creation, 'b' for binary, 't' for text -  'r+' for reading and writing, etc.).

```python
file = open("my_file.txt", "r") #Opens file for reading
```

*   **Reading Files:**

    *   `file.read()` : Reads the entire file content as a single string.
    *   `file.readline()` : Reads a single line at a time.
    *   `file.readlines()` : Reads all lines into a list of strings.
    *   Iteration: You can directly iterate over a file object to read line by line.

```python
file = open("my_file.txt", "r")
contents = file.read() #reads entire file
lines = file.readlines() #reads entire file into list of lines
for line in file: #iterates over lines
  print(line)
file.close() #IMPORTANT: Always close the file!

```

*   **Writing to Files:**

    *   `file.write()` : Writes a string to the file.
    *   Remember to close the file after writing to ensure data is saved.

```python
file = open("my_file.txt", "w")
file.write("This is some text.\n")
file.write("This is another line.\n")
file.close()
```

*   **Appending to Files:** Use `"a"` mode to add content to the end of an existing file.

*   **Error Handling:** Use `try...except` blocks to handle potential `FileNotFoundError` exceptions.

```python
try:
    file = open("my_file.txt", "r")
    # ... file operations ...
except FileNotFoundError:
    print("File not found!")
finally:
    file.close() #This will still execute even if exception occurs.  Best way to ensure file is closed
```

*   **Context Managers (`with` statement):** The preferred way to handle files, automatically closing them even if errors occur.

```python
with open("my_file.txt", "r") as file:
    contents = file.read()
    # ... process contents ...

# File is automatically closed here.
```

[[File IO Modes]], [[Handling Binary Files]]


