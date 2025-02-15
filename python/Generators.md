# [[Python 1 Home]]
# [[Generators]]  [[Generators]] are a powerful feature in Python that allows you to create iterators in a concise and efficient way.  Instead of creating a whole list in memory at once, generators produce values one at a time, only when requested. This makes them memory-efficient, especially when dealing with large datasets or infinite sequences.

Key characteristics:

*   **Memory Efficiency:** Generates values on demand, avoiding storage of the entire sequence.
*   **Lazy Evaluation:**  Values are computed only when needed.
*   **Iterable:** Can be used in `for` loops and other iteration contexts.


**Creating [[Generators]]:**
 [[Generators]] are defined using functions, but instead of a `return` statement, they use the `yield` keyword.  `yield` pauses execution and returns a value, preserving the generator's state.  The next time the generator is called, it resumes from where it left off.

```python
def my_generator(n):
    for i in range(n):
        yield i

gen = my_generator(5)
print(next(gen))  # Output: 0
print(next(gen))  # Output: [[1
print(list(gen))  # Output: 2, 3, 4 #consuming the rest

#using for loop
for i in my_generator(3):
    print(i) #output 0,[[1,2

```

**Generator Expressions:**

Similar to list comprehensions, generator expressions offer a concise way to create generators. They use parentheses `()` instead of square brackets `1`.

```python
gen_expr = (i**2 for i in range(5))
print(list(gen_expr)) #Output: [0, [[1, 4, 9, 16
```

**Advantages over [[Lists]]:**

*   Memory Efficiency:  Especially beneficial for large datasets or infinite sequences.
*   Readability:  Can make code cleaner and more concise than explicit iterator classes.
*   Lazy Evaluation: Avoids unnecessary computations.


**Related Notes:**

* [[Iterators]]
* [[List Comprehensions]]
* [[Async Generators]] (for asynchronous operations)

