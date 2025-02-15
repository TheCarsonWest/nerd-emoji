# [[Handling Binary Files]]
# [[Struct Module]] Notes

The `struct` module in Python is used for packing and unpacking data in binary format.  It's particularly useful when dealing with binary files, network communication, or interacting with C code or libraries.

**Key Concepts:**

* **Formats:**  Format strings define how data is represented in bytes.  They use a specific syntax (see below). [[Format String Syntax]]
* **Packing:** Converting Python data (integers, floats, etc.) into a byte string using `struct.pack()`.
* **Unpacking:**  Converting a byte string back into Python data using `struct.unpack()`.
* **Byte Order:**  Specifies the order of bytes (big-endian or little-endian).  This is crucial for interoperability. [[Byte Order and Endianness]]
* **Alignment:**  Controls how data is aligned in memory (can impact performance and compatibility with other systems).


**Example:**

```python
import struct

# Pack a single integer and a float
data = struct.pack('if', 10, 3.14)  # 'i' for integer, 'f' for float
print(data) # Output: b'\n\x00\x00\x00\x9a\x99\x99\x99'


# Unpack the data
unpacked_data = struct.unpack('if', data)
print(unpacked_data) # Output: (10, 3.140000104367573)

#Example with byte order specification
packed_data_big_endian = struct.pack(">i", 10) # > indicates big-endian
packed_data_little_endian = struct.pack("<i",10) # < indicates little-endian
print(packed_data_big_endian)
print(packed_data_little_endian)

```

**Common Format Characters:**

| Character | C Type             | Python Type(s)     | Size (bytes) |
|-----------|----------------------|----------------------|---------------|
| `x`       | pad byte            |                     | [[1             |
| `c`       | char                | bytes (length [[1)    | [[1             |
| `b`       | signed char         | int                 | [[1             |
| `B`       | unsigned char       | int                 | [[1             |
| `h`       | short               | int                 | 2             |
| `H`       | unsigned short      | int                 | 2             |
| `i`       | int                 | int                 | 4             |
| `I`       | unsigned int        | int                 | 4             |
| `l`       | long                | int                 | 4             |
| `L`       | unsigned long       | int                 | 4             |
| `q`       | long long           | int                 | 8             |
| `Q`       | unsigned long long  | int                 | 8             |
| `f`       | float               | float               | 4             |
| `d`       | double              | float               | 8             |


**[[Error Handling]]:**

`struct.error` is raised if there's an issue with the format string or data.


**Related Notes:**

* [[Format String Syntax]]
* [[Byte Order and Endianness]]
* [[Python Data Types]]

