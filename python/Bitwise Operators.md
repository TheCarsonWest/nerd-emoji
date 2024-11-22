# [[Operators]]
# Bitwise Operators

Bitwise operators work directly on the individual bits of integers.  They are rarely used in typical Python programming but are essential for low-level programming, working with hardware, or specific optimization scenarios.


**Types of Bitwise Operators:**

*   `&` (AND):  Returns 1 if both bits are 1, otherwise 0.
*   `|` (OR): Returns 1 if at least one bit is 1, otherwise 0.
*   `^` (XOR): Returns 1 if the bits are different, otherwise 0.
*   `~` (NOT): Inverts all bits (0 becomes 1, 1 becomes 0).
*   `<<` (Left Shift): Shifts bits to the left by a specified number of positions, filling with 0s on the right.
*   `>>` (Right Shift): Shifts bits to the right by a specified number of positions.  The behavior of the leftmost bit depends on the signedness of the integer (generally filled with the sign bit in two's complement).


**Examples:**

```python
a = 10  # Binary: 1010
b = 4   # Binary: 0100

print(a & b)  # Output: 0 (Binary: 0000)
print(a | b)  # Output: 14 (Binary: 1110)
print(a ^ b)  # Output: 14 (Binary: 1110)
print(~a)   # Output: -11 (depends on system's representation of negative numbers)
print(a << 2) # Output: 40 (Binary: 101000)
print(a >> 1) # Output: 5  (Binary: 0101)

```

**[[Twos Complement]]**  (This needs a separate explanation)

**[[Binary Representation of Numbers]]** (This also needs a separate explanation)


**Use Cases:**

*   **Flags and bit fields:**  Representing multiple boolean states within a single integer.
*   **Low-level programming:** Interfacing with hardware or embedded systems.
*   **Cryptography:** Certain cryptographic algorithms utilize bitwise operations.
*   **Data compression/manipulation:**  Efficiently packing and unpacking data.


**Important Note:**  Bitwise operators only work on integers. Applying them to other data types will result in a `TypeError`.
