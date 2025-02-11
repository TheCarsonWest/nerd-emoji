# [[Bitwise Operators]]
# Two's Complement

Two's complement is a way to represent signed integers (positive and negative) in binary.  It's the most common method used in computers because it simplifies arithmetic operations, particularly addition and subtraction.

**Key Concepts:**

* **Sign Bit:** The most significant bit (MSB) represents the sign. 0 indicates positive, [[1 indicates negative.

* **Positive Numbers:**  Represented in standard binary.

* **Negative Numbers:** Calculated by inverting all bits (0s become 1s, 1s become 0s) and then adding [[1.

**Example (8-bit):**

Let's represent [[5] and -[[5]:

* **[[5]:** `00000101` (Positive, standard binary)

* **-[[5]:**
    [[1. Invert bits: `11111010`
    [[2]. Add [[1: `11111011`

**Python Implementation:**

Python handles this internally, so you don't usually need to worry about the specifics.  However, you can simulate it:

```python
def twos_complement(n, bits):
    """Represents an integer using two's complement in a specified number of bits."""
    if n >= 0:
        return bin(n)[[2]:].zfill(bits)  #Positive numbers
    else:
        positive_equivalent = ([[1 << bits) + n #add [[2]^bits to get the positive equivalent
        return bin(positive_equivalent)[[2]:].zfill(bits)

print(twos_complement([[5], 8))  # Output: 00000101
print(twos_complement(-[[5], 8)) # Output: 11111011

```

**Advantages:**

* **Simplified Arithmetic:** Addition and subtraction can be performed using the same circuitry regardless of the signs of the numbers.  This simplifies hardware design.
* **Unique Representation:**  Each integer has a unique representation in two's complement (except for the most negative number in a given number of bits).


**Disadvantages:**

* **Range Limitation:** The range of representable numbers is limited by the number of bits used.  For example, with 8 bits, the range is -128 to 127.
* [[Bitwise Operations]]  (Need separate explanation)
* [[Binary Representation]] (Need separate explanation)


[[Number Systems]] (A note on different number systems like decimal, binary, hexadecimal would be useful)

