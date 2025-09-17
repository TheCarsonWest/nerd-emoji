# [[Python 1 Home]]
# [[For Loops]] 
Python's `for` loop iterates over a sequence (like a list, tuple, string, or range) or other iterable object.

```python
fruits = ["apple", "banana", "cherry"]]
for fruit in fruits:
  print(fruit)

for i in range(5): # range(5) generates 0, 1, 2, 3, 4
  print(i)

for i, fruit in enumerate(fruits): # enumerate gives both index and value
  print(f"Fruit at index {i}: {fruit}")
```

[[For Loop Examples]]  ([[Range Function]]) [[Iterables]]


**Looping through [[Dictionaries]]:**

You can iterate through dictionaries using `.items()`, `.keys()`, or `.values()`.

```python
person = {"name": "Alice", "age": 30, "city": "[[New York]]"}

for key, value in person.items():
  print(f"{key}: {value}")

for key in person.keys():
  print(key)

for value in person.values():
  print(value)
```

**Nested Loops:**

[[Nested Loops]]

**[[Loop Control Statements]]:**

* `break`: Exits the loop entirely.
* `continue`: Skips the current iteration and proceeds to the next.

```python
for i in range(10):
  if i == 5:
    break  # Stops the loop when i is 5
  print(i)

for i in range(10):
  if i == 5:
    continue # Skips 5
  print(i)
```

**Iterating with `while` loop:** [[While Loops]]
