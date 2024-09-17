**Python For_Loops**

**Explanation:**

A [[For_Loops]] is a [[Control_Flow_If_Statements]] statement used in Python to iterate over a [[Sequence]] ([[Lists]], [[Tuples]], [[Strings]], etc.) and execute a set of statements for each element in the [[Sequence]].

**Parameters:**

* [[Iterable]] (required):** The [[Sequence]] ([[Lists]], [[Tuples]], [[Strings]], etc.) to iterate over.
* [[Variable]] (required):** A variable to hold the current element of the [[Iterable]].
* [[Range of Numbers]] (optional):** Specifies a range of numbers to iterate over using the syntax `range(start, stop, step)`.
* [[else]]:** An optional clause that executes after the loop has completed.

**Code Examples:**

**Iterating over a [[List]]:**

```python
my_list = 1, 2, 3, 4, 5

for item in my_list:
    print(item)
```

**Iterating over a [[Tuple]]:**

```python
my_tuple = (1, 2, 3, 4, 5)

for item in my_tuple:
    print(item)
```

**Iterating over a [[String]]:**

```python
my_string = "Hello World"

for char in my_string:
    print(char)
```

**Iterating over a [[Range of Numbers]]:**

```python
for i in range(1, 6):
    print(i)
```

**Using the [[else]] Clause:**

```python
my_list = 1, 2, 3, 4, 5

for item in my_list:
    print(item)
else:
    print("Loop completed successfully.")
```

**Other Python Concepts Linked to For_Loops:**

* **[[Iterables]]:** Objects that can be iterated over, such as [[Lists]], [[Tuples]], [[Strings]], and [[Ranges]].
* **[[Control_Flow_If_Statements]]:** Statements that control the flow of execution, such as [[If-Else Statements]] and [[While_Loops]].
* **[[Ranges]]:** Objects that generate consecutive numbers, used to iterate over a specific range.
* **[[List_Comprehension]]:** A compact way to create new [[Lists]] by iterating over an [[Iterable]].