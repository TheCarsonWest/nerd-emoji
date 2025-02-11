# [[File IO Modes]]
# [[Error Handling]] with Files]] 
This note covers error handling specifically when working with files in Python.  Crucially, it focuses on anticipating and gracefully managing potential issues that might arise during file operations.

Key potential errors:

* **`FileNotFoundError`**:  The file specified doesn't exist.
* **`IOError`**: A general I/O error, encompassing various problems like permission issues or disk errors.
* **`PermissionError`**:  Lack of sufficient permissions to read from or write to a file.


Best practices for handling these:

Always use `try...except` blocks to wrap file operations.  This allows for catching specific exceptions and implementing appropriate recovery strategies.

```python
try:
    with open("my_file.txt", "r") as f:
        contents = f.read()
        # Process the file contents
except FileNotFoundError:
    print("File not found. Please check the filename.")
except PermissionError:
    print("Insufficient permissions to access the file.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
except Exception as e: #Catch any other possible errors
    print(f"An unexpected error occurred: {e}")

```

[[File I/O Basics]]  (This note will detail fundamental file operations like opening, reading, writing, and closing files.)

[[Exception Handling]] in Python]] (This note will provide a broader overview of Python's exception handling mechanisms beyond file I/O.)


Example demonstrating context manager (`with` statement):  The `with` statement ensures that the file is automatically closed even if exceptions occur. This prevents resource leaks and improves code robustness.


Advanced techniques:

*   Using the `os` module to check file existence (`os.path.exists()`), size (`os.path.getsize()`), etc. before attempting operations. This is a proactive approach to error prevention.
*   Implementing custom exception classes for more specific error handling within your application.


Further reading:

*   Python's official documentation on exception handling and file I/O.

Remember to handle all expected exceptions for robust code!
