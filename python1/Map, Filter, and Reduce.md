## [[Map, Filter, and Reduce]]

### Explanation
 [[Map, Filter, and Reduce]] are higher-order functions that operate on sequences and return a new sequence. They are widely used for functional programming in Python.

### How to Use

**Map:**
* Takes a function and a sequence as arguments.
* Applies the function to each element in the sequence.
* Returns a new sequence with the results.

```python
map(function, sequence)
```

**Filter:**
* Takes a function and a sequence as arguments.
* Applies the function to each element in the sequence.
* Returns a new sequence containing only the elements for which the function returns True.

```python
filter(function, sequence)
```

**Reduce:**
* Takes a function, a sequence, and an initial value as arguments.
* Applies the function to the initial value and the first element in the sequence.
* Continues applying the function to the result and the next element in the sequence.
* Returns the final result.

```python
reduce(function, sequence, initial_value)
```

### Code Examples

**Map:**
```python
# Square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25]
```

**Filter:**
```python
# Find all even numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # Output: [2, 4, 6, 8, 10]
```

**Reduce:**
```python
# Find the product of all numbers in a list
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product) # Output: 120
```

### Related Python Concepts

- [[Higher-Order [[Functions]]: [[Map, Filter, and Reduce]] are higher-order functions.
- [[Lambda [[Functions]]: Lambda functions are commonly used as arguments to Map and Filter.
- [[List Comprehension]]: [[Map, Filter, and Reduce]] are alternatives to using list comprehensions for functional programming.
- [[Generators]]: Map and Filter can be used to create generators.
- [[Functional Programming]]: [[Map, Filter, and Reduce]] are core concepts in functional programming.
# [[Python 1 Home]]