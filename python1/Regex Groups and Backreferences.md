## [[Regex Groups and Backreferences]]

### What are [[Regex Groups and Backreferences]]?
Groups in [[Regular Expressions]] are used to capture substrings within the matched pattern. Backreferences allow referencing these captured substrings within the regular expression itself or in subsequent processing.

### How to Use Regex Groups
To create a group in a regular expression, use parentheses:

```
# capture the word "python"
(python)
```

Backreferences are used by escaping the opening parenthesis of the group:

```
# replace "Python" with "Py"
Python -> (Py)thon
```

### Code Examples
```python
import re

# find all occurrences of phone numbers
phone_pattern = re.compile(r"(\d{3}-?\d{3}-?\d{4})")

# match a string
match = phone_pattern.search("My phone number is 123-456-7890")

# access the captured group
phone_number = match.group(1)
```

### Related Python Concepts

- [[Regular Expressions]]: Groups and backreferences are core components of [[Regular Expressions]].
- [[Python Functions]]: [[Regular Expressions]] often use matching [[Python Functions]] like `search` and `findall`.
- [[Lambda [[Python Functions]]: [[Regular Expressions]] can be used as arguments to [[Lambda Functions]].
- [[Python Sets]]: Groups can be used to construct [[Python Sets]] of matched substrings.
- [[Tuples]]: Backreferences return [[Tuples]] containing the captured substrings.
# [[Python 1 Home]]