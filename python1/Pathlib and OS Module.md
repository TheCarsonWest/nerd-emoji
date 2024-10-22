## [[Pathlib and OS Module]]

### Overview
Pathlib and OS are two important modules in Python that provide extensive capabilities for interacting with the file system and operating system. Pathlib offers a modern, object-oriented approach to working with files and directories, while the OS module offers a comprehensive set of functions for performing system-level tasks.

### Pathlib

#### What is Pathlib?
Pathlib is a Python module that provides a convenient and consistent way to work with files and directories. It offers a class-based approach to representing and interacting with paths, making it easier to handle file operations and navigate the file system.

#### How to Use Pathlib
The basic usage of Pathlib involves creating a Path object, which represents a path to a file or directory. The Path object provides various methods for manipulating and accessing the file system.

```python
from pathlib import Path

# create a Path object for the current working directory
cwd = Path.cwd()

# get the home directory
home_dir = Path.home()

# create a path to a specific file
file_path = Path('my_file.txt')
```

#### Code Example
```python
# create a Path object for the current working directory
cwd = Path.cwd()

# get the absolute path to the cwd
abs_path = cwd.absolute()

# get the parent directory of the cwd
parent_dir = cwd.parent

# list all files and directories in the cwd
for item in cwd.iterdir():
 print(item)
```

### OS Module

#### What is the OS Module?
The OS module in Python provides a wide range of functions for interacting with the operating system. It offers system-level functionality, such as process management, file manipulation, and directory operations.

#### How to Use the OS Module
The OS module can be imported into Python programs using the following statement:

```python
import os
```

Once imported, the OS module provides various functions for performing different system-level tasks.

#### Code Example
```python
import os

# check if a file exists
if os.path.isfile('my_file.txt'):
 print("File exists")

# create a directory
os.mkdir('new_dir')

# rename a file
os.rename('old_file.txt', 'new_file.txt')

# delete a file
os.remove('temp_file.txt')
```

### Related Python Concepts

- [[File Handling]]: Pathlib and OS are essential for working with files and directories.
- [[Variables and Data Types]]: Variables are used to store paths and other information related to files and directories.
- [[Operators]]: [[Operators]] are used in Pathlib and OS functions for comparisons and other operations.
- [[Control Flow If Statements]]: If statements are used to check conditions related to files and directories.
- [[For Loops]]: For loops are used to iterate over files and directories.
# [[Python 1 Home]]