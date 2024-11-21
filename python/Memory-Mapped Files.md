# [[Handling Binary Files]]
# Memory-Mapped Files

Python's `mmap` module allows for memory-mapping files. This means treating a file on disk as if it were directly accessible in your program's memory.  This can offer significant performance advantages for large files, especially when dealing with random access.


**Key Concepts:**

* **Efficiency:**  Avoids the overhead of repeatedly reading and writing to the file from disk. Changes made in memory are reflected on disk (and vice-versa, depending on the mode).
* **Shared Memory:** Multiple processes can access and modify the same memory-mapped file simultaneously, enabling inter-process communication (IPC). [[Inter-Process Communication (IPC)]]
* **Synchronization:** Because multiple processes can access the same memory, proper synchronization mechanisms (like locks) are crucial to prevent race conditions and data corruption. [[Synchronization Primitives]]
* **File Modes:**  Different modes affect how the mapped file behaves (read-only, read-write, copy-on-write, etc.).
* **Error Handling:**  Properly handle exceptions like `mmap.error` for scenarios where the mapping fails.


**Example:**

```python
import mmap
import os

filename = "my_large_file.dat"

# Create a large file for demonstration (optional)
with open(filename, "wb") as f:
    f.write(b"A" * (1024 * 1024 * 10)) # 10MB file

try:
    with open(filename, "r+b") as f:  # Open in read-write binary mode
        mm = mmap.mmap(f.fileno(), 0) # Map the entire file

        # Access and modify the file's contents directly through mm
        print(mm[:10]) # Read the first 10 bytes

        mm[0:10] = b"Hello, world!" # Write to the first 10 bytes

        mm.close()  # Close the mapped file
except OSError as e:
    print(f"Error mapping file: {e}")
finally:
    # Ensure the file is closed and resources are released.
    # If the file was newly created, you might need to delete it here
    # if os.path.exists(filename):
    #   os.remove(filename)

```


**Further Exploration:**

*  [[Memory Management in Python]]
*  [[File I/O in Python]]


**Important Notes:**

* Memory-mapped files consume memory. For extremely large files that exceed available RAM, this approach can lead to performance issues (swapping).
*  Always close the `mmap` object (`mm.close()`) to release resources.  Using `with` statement is recommended for automatic cleanup.

