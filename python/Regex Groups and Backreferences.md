# [[Regular Expressions]]
# Regex Groups and Backreferences

These notes cover how to use groups and backreferences in [[Regular Expressions]] within Python.

The core idea is to create groups within a regex pattern to capture specific parts of the matched string.  These captured parts can then be reused (backreferenced) within the same pattern or accessed after the match is made.

**Creating Groups:**

Groups are created using parentheses `()` in your regular expression.  Each opening parenthesis starts a new group, and the corresponding closing parenthesis ends it.

```python
import re

text = "My phone number is 123-456-7890 and my zip code is 90210"
pattern = r"(\d{3})-(\d{3})-(\d{4})"  # Three groups: area code, prefix, line number

match = re.search(pattern, text)
if match:
    print(match.group(0))  # Entire match
    print(match.group(1))  # First group (area code)
    print(match.group(2))  # Second group (prefix)
    print(match.group(3))  # Third group (line number)
```

**Backreferences:**

Backreferences allow you to refer to previously captured groups within the same regular expression. This is done using backslash followed by the group number. `\1` refers to the first group, `\2` to the second, and so on.

```python
text = "abababa"
pattern = r"(a)(b)\1\2\1" # Matches "abababa"  \1 refers to (a), \2 refers to (b)

match = re.search(pattern, text)
if match:
    print(match.group(0))
```

**Named Capture Groups:**

Python also supports named capture groups, making your code more readable. These are defined using the `(?P<name>...)` syntax.

```python
text = "My email is test@example.com"
pattern = r"(?P<user>[^@]+)@(?P<domain>[^@]+)"

match = re.search(pattern, text)
if match:
    print(match.group("user"))  # Access using name
    print(match.group("domain"))
```


[[Regex Metacharacters]]  ([[Python's `re` Module]])


This is useful for extracting specific parts of a matched string in a structured way.  Refer to [[Regex Metacharacters]] for more information on the basic building blocks of [[Regular Expressions]] used in these examples.  The [[Python's `re` Module]] note will cover the different functions available within Python's `re` module for working with [[Regular Expressions]].
