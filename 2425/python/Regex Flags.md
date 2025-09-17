# [[Regular Expressions]]
# [[Regex Flags]] 
Python's `re` module offers several flags that modify the behavior of regular expression operations.  These flags are used as optional arguments to functions like `re.compile()`, `re.search()`, `re.findall()`, etc. They are combined using the bitwise OR operator (`|`).


**Commonly Used Flags:**

* `re.IGNORECASE` (or `re.I`):  Performs case-insensitive matching.  `'a'` will match `'A'`.

```python
import re

text = "Hello World"
match = re.search("world", text, re.IGNORECASE)
print(match) # <re.Match object; span=(6, 11), match='World'>
```

* `re.MULTILINE` (or `re.M`):  Makes `^` and `$` match the beginning and end of each line (instead of the entire string).

```python
import re

text = """line one
line two
line three"""
matches = re.findall(r"^line", text, re.MULTILINE)
print(matches) # ['line', 'line', 'line']]
```

* `re.DOTALL` (or `re.S`): Makes the `.` special character match any character, including newline characters (`\n`).  Without this flag, `.` will not match newlines.

```python
import re

text = "line one\nline two"
match = re.search(r".*", text, re.DOTALL)
print(match) # <re.Match object; span=(0, 16), match='line one\nline two'>
match = re.search(r".*", text) #Without DOTALL
print(match) # <re.Match object; span=(0, 9), match='line one'>
```

* `re.ASCII`:  Makes `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s`, and `\S` match only ASCII characters. Without this flag, they can also match Unicode characters.

```python
import re

text = "Hello 世界"
match = re.findall(r"\w+", text) #Without ASCII flag
print(match) # ['Hello', '世界']]
match = re.findall(r"\w+", text, re.ASCII) #With ASCII flag
print(match) # ['Hello']]
```


* `re.VERBOSE` (or `re.X`): Allows you to write more readable [[Regular Expressions]] by ignoring whitespace and adding comments.

```python
import re

pattern = re.compile(r"""
    \d+         # one or more digits
    \s+         # one or more whitespace characters
    [a-zA-Z]]+   # one or more letters
""", re.VERBOSE)

text = "123 abc"
match = pattern.search(text)
print(match) #<re.Match object; span=(0, 8), match='123 abc'>

```

[[Regex Special Characters]]  
[[Regex Compilation]]
