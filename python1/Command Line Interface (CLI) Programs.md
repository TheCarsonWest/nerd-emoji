## Python Command Line Interface (CLI) Programs

### Explanation

A Python Command Line Interface (CLI) program is a script or application that is designed to be executed from the command line interface (also known as the terminal). It allows users to interact with the program by entering text commands and receiving output. CLI programs are commonly used for tasks such as system administration, software development, and data processing.

### How to Use CLI Programs

The general syntax for executing a Python CLI program is:

```
python script.py [arguments]
```

where:

- `script.py` is the name of the Python script file.
- `[arguments]` are optional arguments that can be passed to the program.

### Code Examples

```python
# hello.py
print("Hello, world!")
```

To run this program, open a terminal window and execute the following command:

```
python hello.py
```

Output:

```
Hello, world!
```

```python
# calculator.py
import sys

def add(a, b):
 return a + b

def subtract(a, b):
 return a - b

operation = sys.argv[1]
a = int(sys.argv[2])
b = int(sys.argv[3])

if operation == "add":
 result = add(a, b)
elif operation == "subtract":
 result = subtract(a, b)
else:
 print("Invalid operation")

print(result)
```

To run this program and perform addition, execute the following command:

```
python calculator.py add 10 5
```

Output:

```
15
```

### Python Concepts Most Closely Related

- [[Variables and Data Types]]: CLI programs use variables to store data and data types to define the type of data stored in variables.
- [[Operators]]: CLI programs use operators to perform mathematical and logical operations on data.
- [[Control Flow If Statements]]: CLI programs use if statements to conditionally execute code based on a given condition.
- [[For Loops]]: CLI programs use for loops to iterate over sequences and perform actions for each element.
- [[Functions]]: CLI programs often use functions to organize code and perform specific tasks.
# [[Python 1 Home]]