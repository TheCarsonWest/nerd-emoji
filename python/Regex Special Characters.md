# [[Regex Flags]]
# Regex Special Characters

These notes cover special characters used in [[Regular Expressions]] within Python.  Remember to import the `re` module before using any regex functions.  `import re`

[[Regex Metacharacters]]  These are symbols with special meanings in regex.

* **`.` (Dot):** Matches any single character except a newline.

* **`^` (Caret):** Matches the beginning of a string.

* **`$` (Dollar):** Matches the end of a string.

* **`*` (Asterisk):** Matches zero or more occurrences of the preceding character or group.

* **`+` (Plus):** Matches one or more occurrences of the preceding character or group.

* **`?` (Question Mark):** Matches zero or one occurrence of the preceding character or group.

* **`[]` (Square Brackets):** Defines a character set.  e.g., `[abc]` matches 'a', 'b', or 'c'.  Ranges are possible: `[a-z]` matches any lowercase letter.  `[^abc]` negates the set (matches anything *except* a, b, or c).

* **`()` (Parentheses):** Creates a capturing group.  Used for extracting specific parts of a matched string.  Also useful for grouping parts of the regex for applying quantifiers.

* **`\|` (Vertical Bar):** Acts as an "or" operator.  e.g., `cat|dog` matches either "cat" or "dog".

* **`\` (Backslash):** Escapes special characters.  e.g., `\.` matches a literal dot, `\(` matches a literal opening parenthesis.  It's also used for special escape [[Sequences]] like `\d` (digit), `\w` (alphanumeric), `\s` (whitespace).


[[Regex Quantifiers]]  These characters control how many times a preceding element should appear.  (Already mentioned some above, but details here are crucial)

* **`*` (Asterisk):** Zero or more occurrences.

* **`+` (Plus):** One or more occurrences.

* **`?` (Question Mark):** Zero or one occurrence.

* **`{n}`:** Exactly *n* occurrences.

* **`{n,}`:** *n* or more occurrences.

* **`{n,m}`:** Between *n* and *m* occurrences (inclusive).


**Example:**

```python
import re

text = "The quick brown fox jumps over the lazy fox."
pattern = r"fox"  # Matches the literal string "fox"

matches = re.findall(pattern, text)
print(matches)  # Output: ['fox', 'fox']

pattern = r".ox" # Matches any character followed by "ox"
matches = re.findall(pattern, text)
print(matches) # Output: ['fox', 'fox']

pattern = r"f.x" # Matches 'f' followed by any character followed by 'x'
matches = re.findall(pattern, text)
print(matches) # Output: ['fox', 'fox']

pattern = r"The.*fox" # Matches 'The' followed by any characters (except newline) followed by 'fox'
matches = re.findall(pattern, text)
print(matches) # Output: ['The quick brown fox']

pattern = r"\bf\w+\b" #Matches whole words starting with 'f'
matches = re.findall(pattern,text)
print(matches) # Output: ['fox', 'fox']
```


[[Regex Escape Sequences]]  Details on `\d`, `\w`, `\s`, etc.

[[Python re Module]]  Functions like `re.findall`, `re.search`, `re.match`, `re.sub`, etc.
