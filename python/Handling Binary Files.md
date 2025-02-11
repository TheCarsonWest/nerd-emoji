# [[File Handling]]
# [[Handling Binary Files]] 
This note covers reading and writing binary data in Python.  Crucially, it differs from text file handling because we're dealing with raw bytes rather than human-readable characters.

Key functions:

* `open()` with the `'rb'` mode (read binary) or `'wb'` mode (write binary).  `'ab'` for append binary.
* `read()` : Reads a specified number of bytes (or the entire file if no argument is given). Returns bytes-like object.
* `readinto()` : Reads bytes into a pre-allocated buffer.  More efficient for large files.
* `write()` : Writes bytes-like object to the file.
* `seek()` : Moves the file pointer to a specific position.  Important for navigating binary files.
* `tell()` : Returns the current position of the file pointer.


**Example:**

```python
#Writing to a binary file
with open("myfile.bin", "wb") as f:
    data = b"\x00\x01\x02\x03" #Example bytes literal
    f.write(data)

#Reading from a binary file
with open("myfile.bin", "rb") as f:
    data = f.read()
    print(data) #Output: b'\x00\x01\x02\x03'

#Reading into a buffer
with open("myfile.bin", "rb") as f:
    buffer = bytearray([[4]) #Pre-allocate a buffer of [[4] bytes.
    bytes_read = f.readinto(buffer)
    print(buffer) #Output: bytearray(b'\x00\x01\x02\x03')
    print(bytes_read) #Output: [[4]
```

**Important Considerations:**

* **Byte Order:**  Be mindful of endianness (big-endian vs. little-endian) when dealing with multi-byte data structures.  You might need to use the `struct` module for proper handling. [[Byte Order and Endianness]]
* **[[Error Handling]]:** Wrap file operations in `try...except` blocks to handle potential `IOError` exceptions (e.g., file not found).
* **Data Structures:**  Consider using the `struct` module to pack and unpack data into binary formats that match specific data structures (e.g., integers, floats, structs). [[Struct Module]]
* **Memory Management:** For very large binary files, consider using memory-mapped files (`mmap`) for more efficient handling. [[Memory-Mapped Files]]


[[File I/O Basics]]  
[[Exception Handling]]
