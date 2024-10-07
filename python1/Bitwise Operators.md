## [[Bitwise [[Operators]]

### What are [[Bitwise [[Operators]]?
Bitwise operators perform operations on the binary representations of integers. They allow manipulation of individual bits, providing precise control over the binary-level details of data.

### How to Use [[Bitwise [[Operators]]
Bitwise operators are represented by symbols that indicate the specific operation to be performed on the bits of the operands. The operands must be integers or bitwise expressions. The result is a new integer that represents the modified binary value.

### Common [[Bitwise [[Operators]]

| Operator | Name | Description | Example |
|---|---|---|---|
| `&` | AND | Performs a bitwise AND operation, returning 1 if both bits are 1, and 0 otherwise | `5 & 3 = 1` (0101 & 0011 = 0001) |
| `|` | OR | Performs a bitwise OR operation, returning 1 if either bit is 1 | `5 | 3 = 7` (0101 | 0011 = 0111) |
| `^` | XOR | Performs a bitwise XOR operation, returning 1 if the bits are different, and 0 if they are the same | `5 ^ 3 = 6` (0101 ^ 0011 = 0110) |
| `~` | NOT | Performs a bitwise NOT operation, flipping 0s to 1s and vice versa | `~5 = -6` (0101 -> 1010) |
| `<<` | Left Shift | Shifts the bits to the left, multiplying by 2<sup>n</sup>, where n is the number of positions shifted | `5 << 2 = 20` (0101 << 2 = 10100) |
| `>>` | Right Shift | Shifts the bits to the right, dividing by 2<sup>n</sup>, where n is the number of positions shifted | `20 >> 2 = 5` (10100 >> 2 = 0101) |

### Related Python Concepts

- [[Variables and Data Types]]: Bitwise operators operate on integers and bitwise expressions.
- [[Operators]]: Bitwise operators are a type of operator, distinct from arithmetic and logical operators.
- [[Lists]]: Bitwise operators can be applied to elements of lists containing integers.
- [[Tuples]]: Bitwise operators can be applied to elements of tuples containing integers.
- [[Sets]]: Bitwise operators can be applied to elements of sets containing integers.
# [[Python 1 Home]]