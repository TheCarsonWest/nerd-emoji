# [[ndarray Explained]]
# [[Indexing and Slicing Deep Dive]] 
This note covers advanced techniques and nuances of indexing and slicing in Python sequences (lists, tuples, strings).

**Basic Indexing:**

*   Python uses zero-based indexing.  The first element is at index 0, the second at index [[1, and so on.
*   Negative indexing allows access from the end of the sequence: -[[1 refers to the last element, -2 to the second to last, etc.

```python
my_list = [10, 20, 30, 40, 50]]
print(my_list[0]])  # Output: 10
print(my_list[-1) # Output: 50
```

**Slicing:**

*   Slicing extracts a portion of a sequence using `[start:stop:step]]`.
*   `start` is the index of the first element to include (inclusive). Defaults to 0.
*   `stop` is the index of the element to stop *before* (exclusive). Defaults to the length of the sequence.
*   `step` is the increment between indices. Defaults to 1.

```python
my_string = "abcdefg"
print(my_string[[1:4)  # Output: "bcd" (indices [[1, 2, 3)
print(my_string[::2)  # Output: "aceg" (every other element)
print(my_string[::-1) # Output: "gfedcba" (reversed string)

my_list = list(range(10))
print(my_list2:7:2) #Output: 2, 4, 6
```

**Advanced Slicing Techniques:**

*   **Omitting `start`, `stop`, or `step`:**  Provides flexibility.  For example, `[:]]` creates a copy of the entire sequence.
*   **Slicing with negative indices:** Allows for flexible selection from the end.
*   **Slicing and mutability:** Slices create *views* of the original sequence; modifying a slice modifies the original.  This is different from creating a copy with `[:]]`.  This is particularly relevant for mutable sequences like lists.  ([[Mutability and Immutability]])

```python
my_list = [[1,2,3,4,5
sliced_list = my_list[[1:4
sliced_list[0]] = 10
print(my_list) #Output: [[1, 10, 3, 4, 5 - original list modified

copied_list = my_list[:]]
copied_list[0]] = 20
print(my_list) #Output: [[1, 10, 3, 4, 5 - original list unchanged
```

**Slicing and Strings:**

* String slicing works similarly, but produces new strings (strings are immutable).

```python
my_string = "hello"
new_string = my_string[[1:4
print(new_string) #Output: "ell"
```


**[[Error Handling]]:**

*   IndexError: Occurs when accessing an index outside the valid range.
*   This can be avoided by using bounds checking or exception handling.


**Further Exploration:**

* [[List Comprehensions]]  (Could use slicing within list comprehensions for powerful data manipulation)
* [[Sequence Unpacking]] (Closely related to accessing elements)

