# [[For Loops]]
# [[For Loop Examples]] 
This note covers examples of using `for` loops in Python.

* **Basic Iteration:**

```python
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
```

* **Iterating through strings:**

```python
my_string = "hello"
for char in my_string:
    print(char.upper())
```

* **Iterating through dictionaries:**

```python
my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")

#Or using items():

for key, value in my_dict.items():
  print(f"Key: {key}, Value: {value}")
```

* **Iterating with `range()`:**

```python
for i in range(5):  #Prints 0 to 4
    print(i)

for i in range(2, 10, 2): #Starts at 2, goes up to (but not including) 10, incrementing by 2.
  print(i)
```


* **Nested Loops:**

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

* **Loop Control Statements:**

    * `break`: Terminates the loop prematurely.
    * `continue`: Skips the current iteration and proceeds to the next.

```python
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

for i in range(5):
    if i == 2:
        continue # Skip the iteration when i is 2
    print(i)

```

[[List Comprehensions]]  ([[Loop Control Statements]]) [[Range Function]]
