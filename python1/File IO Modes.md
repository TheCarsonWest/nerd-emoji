## [[File IO Modes]]

### Overview
Python provides file handling modes to specify how the file is opened and how data is accessed. The mode specifies the usage of the file, such as reading, writing, or appending.

### File IO Mode Options
| Mode | Description |
|---|---|
| `'r'` | Opens a file for reading. The file must exist, or an `OSError` will be raised. |
| `'w'` | Opens a file for writing. If the file exists, it will be overwritten. If it doesn't, a new file will be created. |
| `'a'` | Opens a file for appending. Data is written to the end of the file without overwriting the existing content. If the file doesn't exist, a new file will be created. |
| `'r+'` | Opens a file for both reading and writing. The file must exist, or an `OSError` will be raised. |
| `'w+'` | Opens a file for both writing and reading. If the file exists, it will be overwritten. If it doesn't, a new file will be created. |
| `'a+'` | Opens a file for both appending and reading. Data is written to the end of the file without overwriting the existing content. If the file doesn't exist, a new file will be created. |
| `'x'` | Opens a file for exclusive creation and writing. If the file already exists, an `OSError` will be raised. |

### How to Use [[File IO Modes]]
When opening a file using the `open()` function, the mode is specified as the second parameter:

```python
with open('filename.txt', mode='r') as file:
 # reading operations
```

### Related Python Concepts
- [[File Handling]]: File IO modes are part of the Python file handling functionality.
- [[Context Managers]]: Context managers are used in Python to ensure proper resource management, including file handling.
- [[Exceptions]]: Errors while working with files, such as file not found or permission denied, raise exceptions that need to be handled appropriately.
# [[Python 1 Home]]