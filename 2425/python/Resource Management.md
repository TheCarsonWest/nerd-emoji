# [[Custom Context Managers]]
# [[Resource Management]] in Python

This note covers resource management in Python, focusing on efficient and safe handling of system resources.

Key aspects include:

* **[[File Handling]]:**
    * Always close files explicitly using `with` statements or `file.close()`.  This ensures resources are released promptly, preventing resource leaks.
    ```python
    with open("my_file.txt", "r") as f:
        contents = f.read()
        # Process contents
    # File automatically closed here
    ```
    * [[File Handling Best Practices]]  (This will be a separate note).

* **Network Connections:**
    * Similar to files, network sockets should be closed after use.  Use `with` statements or explicit `socket.close()` calls.  [[Context Managers]] ensure cleanup even if exceptions occur.
    ```python
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('example.com', 80))
        # ... network operations ...
    # Socket automatically closed
    ```
    * [[Network Programming in Python]] (This will be a separate note).

* **Memory Management:**
    * Python's garbage collector automatically reclaims memory, but understanding how it works is important for avoiding memory leaks.  Be mindful of large data structures and circular references.
    * Techniques to aid the garbage collector include deleting large objects explicitly using `del` when done with them.  Using [[Generators]] to yield data instead of creating large [[Lists]] can also greatly reduce memory use.
    * [[Python Garbage Collection]] (This will be a separate note).

* **Database Connections:**
    * Database connections are expensive resources.  Always close connections when finished.  Use connection pooling where appropriate to reuse connections and minimize overhead.
    ```python
    import sqlite3

    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    # ... database operations ...
    cursor.close()
    conn.close()
    ```
    * [[Database Interaction in Python]] (This will be a separate note)


* **[[Context Managers]] (`with` statement):**
    * The `with` statement is crucial for resource management.  It ensures that resources (files, network connections, database connections, etc.) are properly released, even if errors occur.  It's the recommended way to handle resources that require explicit cleanup.  Learn about creating [[Custom Context Managers]] using the `contextlib` module.
    * [[Context Managers in Python]] (This will be a separate note)


* **Process and Thread Management:**
    * Properly manage processes and threads to avoid deadlocks and resource contention. Use libraries like `multiprocessing` and `threading` carefully, ensuring proper synchronization and cleanup.
    * [[Concurrency and Parallelism in Python]] (This will be a separate note)

* **[[Exception Handling]]:**
    * Robust [[Error Handling]] is essential to release resources safely in case of exceptions. Use `try...except...finally` blocks to ensure resources are cleaned up even if exceptions occur.  The `finally` block guarantees execution of cleanup code.
    ```python
    try:
        # Code that might raise exceptions
        file = open("my_file.txt", "r")
        # ... operations ...
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'file' in locals() and file:
            file.close()
    ```
    * [[Python Exception Handling]] (This will be a separate note)
