# [[Regular Expressions]]
# Regex Metacharacters

These characters have special meaning within [[Regular Expressions]] and are not treated literally.  They modify the behavior of other characters or patterns.  It's crucial to understand them for effective regex use.

**List of Common Metacharacters:**

* `.` (dot): Matches any single character except a newline.
* `^`: Matches the beginning of a string.
* `$`: Matches the end of a string.
* `*`: Matches zero or more occurrences of the preceding character or group.
* `+`: Matches one or more occurrences of the preceding character or group.
* `?`: Matches zero or one occurrence of the preceding character or group.
* `[]`: Defines a character set.  Matches any single character within the brackets.  `[a-z]` matches any lowercase letter. `[0-9]` matches any digit.
* `[^]`:  Negates a character set. Matches any character *not* within the brackets.
* `()`: Creates a capturing group. Allows you to extract specific parts of a matched string.  Also used for grouping in quantifiers (e.g., `(ab)+`).
* `|`: Acts as an "or" operator. Matches either the expression before or after the pipe.  `cat|dog` matches either "cat" or "dog".
* `\`: Escapes a metacharacter, treating it as a literal character.  `\.` matches a literal dot.  `\*` matches a literal asterisk.


**Examples:**

```python
import re

text = "The quick brown fox jumps over the lazy dog."

# Matches any character followed by a 'o'
print(re.findall(r".o", text))  # Output: ['Th', 'o', 'o']

# Matches the string only if it starts with 'The'
print(re.findall(r"^The", text)) # Output: ['The']

# Matches the string only if it ends with '.'
print(re.findall(r"\.$", text)) # Output: ['.']

# Matches 'o' followed by zero or more 'x' characters
print(re.findall(r"ox*", text)) # Output: ['o', 'ox']

# Matches one or more occurrences of 'l' followed by 'o'
print(re.findall(r"l+o", text)) # Output: ['lo']

# Matches either 'fox' or 'dog'
print(re.findall(r"fox|dog", text)) # Output: ['fox', 'dog']

#Using capturing group
print(re.findall(r"(quick) (brown)", text)) #Output:[('quick', 'brown')]

```

[[Regex Character Sets]]  
[[Regex Quantifiers]]
[[Regex Grouping and Capturing]]
[[Regex Special Sequences]]


