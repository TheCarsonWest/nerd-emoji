## [[Regular Expressions]]

### What are [[Regular Expressions]]?
Regular expressions (regex) are a powerful tool for matching and manipulating strings in Python. They provide a concise and expressive way to search for patterns, validate input, and perform complex string transformations.

### How to Use Regex
To use regex in Python, you can import the `re` module and create a regular expression object:

```python
import re
pattern = re.compile(r'pattern')
```

The `pattern` is a string that specifies the matching rules. Regular expressions use a special syntax to represent different types of patterns, such as:

- **Character classes**: `[abc]` matches any of the characters within the brackets.
- **Metacharacters**: `.` matches any single character, `*` matches zero or more occurrences of the preceding expression.
- **Quantifiers**: `{n}` matches exactly `n` occurrences, `{m,n}` matches between `m` and `n` occurrences.

### Code Examples
```python
# search for the word "Python" in a string
match = re.search(r'Python', 'This is a Python program')
```

```python
# find all occurrences of the digit 5 in a string
matches = re.findall(r'[5]', 'The number is 123456789')
```

```python
# replace all spaces with underscores in a string
new_string = re.sub(r' ', '_', 'Hello World')
```

### Related Python Concepts

- [[Variables and Data Types]]: Regular expressions can be stored in string variables.
- [[Operators]]: Comparison operators (`==`) can be used to test the result of a regex match.
- [[Functions]]: Regular expression functions like `re.search()` and `re.findall()` are used to perform string matching and manipulation.
- [[For Loops]]: Regex patterns can be iterated over using the `re.finditer()` function.
- [[While Loops]]: Regular expressions can be used to control the execution of while loops based on matching conditions.
# [[Python 1 Home]]