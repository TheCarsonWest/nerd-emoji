# [[List Comprehension]]
# [[For Loops]] in Python]] 
Basic Syntax:

```python
for i in iterable:
    # code to be executed in each iteration
```

`iterable` can be a sequence (list, tuple, string) or any other object that supports iteration (e.g., a range object, a file, a dictionary).


**Example with a list:**

```python
my_list = ["apple", "banana", "cherry"]
for fruit in my_list:
    print(fruit)
```

**Example with a range:**

```python
for i in range([[5]]):  # iterates from 0 to [[4]]
    print(i)

for i in range([[1]],[[6]]): #iterates from [[1]] to [[5]]
    print(i)

for i in range([[1]],10,[[2]]): #iterates from [[1]] to 9 stepping by [[2]]
    print(i)

```

**Example with a string:**

```python
my_string = "hello"
for char in my_string:
    print(char)
```

**Iterating through dictionaries:**

```python
my_dict = {"a": [[1]], "b": [[2]], "c": [[3]]}
for key in my_dict:  # iterates through keys
    print(key, my_dict[key])

for key, value in my_dict.items(): #iterates through key-value pairs
    print(key, value)
```

**Nested Loops:**

```python
for i in range([[3]]):
    for j in range([[2]]):
        print(f"i = {i}, j = {j}")
```

**[[Loop Control Statements]]:**

* `break`:  Terminates the loop prematurely.
* `continue`: Skips the rest of the current iteration and proceeds to the next.


**Example with `break`:**

```python
for i in range([[5]]):
    if i == [[3]]:
        break
    print(i)
```

**Example with `continue`:**

```python
for i in range([[5]]):
    if i == [[3]]:
        continue
    print(i)
```

[[List Comprehensions]]  ([[Range Function]]) [[Break and Continue Statements]]
