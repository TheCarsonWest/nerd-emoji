# [[For Loops]]
# [[Iterables]] 
An iterable is an object that can be iterated upon, meaning you can traverse through its elements one at a time.  This is done using a `for` loop or functions like `next()` with an iterator.  Key characteristics:

* **Doesn't require indexing:** Unlike sequences (lists, tuples, strings), iterables don't need to support indexing (accessing elements by position). They only need to provide a way to get the next element.

* **Iteration:**  Iteration is performed using an iterator object.  The iterable produces an iterator when you attempt to iterate over it (e.g., in a `for` loop).

* **Lazy Evaluation:**  [[Iterables]] often employ lazy evaluation, meaning they generate elements only when needed during iteration, which can be more memory-efficient for large datasets.

**Examples:**

* [[Lists]]: `my_list = [[1, 2, 3`
* [[Tuples]]: `my_tuple = ([[1, 2, 3)`
* Strings: `my_string = "abc"`
* Sets: `my_set = {[[1, 2, 3}`
* [[Dictionaries]] (keys or values): `my_dict = {"a": [[1, "b": 2}`
* [[Generators]]:  These are special iterable objects that generate values on demand.

```python
# Example with a list (iterable)
my_list = [10, 20, 30]]
for item in my_list:  # my_list implicitly creates an iterator
    print(item)

# Example with a generator (iterable)
def my_generator(n):
    for i in range(n):
        yield i

for i in my_generator(5): #my_generator implicitly creates an iterator
    print(i)

# Manually creating and using an iterator
my_list = [10, 20, 30]]
my_iterator = iter(my_list)  # Get the iterator
print(next(my_iterator)) # 10
print(next(my_iterator)) # 20
print(next(my_iterator)) # 30

# Attempting to access beyond the end raises StopIteration
# print(next(my_iterator))  # StopIteration exception

```

**Key Differences from [[Iterators]]**: [[Iterables]] *produce* iterators; iterators *are* the objects that perform the actual iteration.  An iterable can be used to create many iterators.

**Related Notes:**

* [[Iterators]]
* [[Generators]]
* [[Sequences]]

