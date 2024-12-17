# [[Iterables]]
# [[Iterators]] 
An iterator is an object that allows you to traverse through a sequence of data one element at a time.  It doesn't load the entire sequence into memory at once, making it memory-efficient for large datasets.

Key characteristics:

*   **`__iter__` method:** Returns the iterator object itself.
*   **`__next__` method:** Returns the next item in the sequence. Raises `StopIteration` when there are no more items.


**Creating an Iterator:**

```python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_iterator = MyIterator([1, 2, 3, 4, 5])
for item in my_iterator:
    print(item)

#Manual Iteration
my_iterator = MyIterator([1,2,3])
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
#print(next(my_iterator)) #StopIteration

```

**Iterating over different data structures:**

Python's built-in functions and data structures already support iteration.  You don't always need to create custom iterators.


**Example with `for` loop (implicitly using iterators):**

```python
my_list = [10, 20, 30]
for item in my_list:  #The for loop implicitly calls iter() and next()
    print(item)
```

[[Iterables]]  ([[Generators]])
