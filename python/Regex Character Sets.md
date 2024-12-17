# [[Regex Metacharacters]]
# [[Regex Character Sets]] 
These notes cover Python's regular expression character sets.  Character sets allow you to match one character from a specified group.

* **Basic Syntax:**  Character sets are defined using square brackets `[]`.  For example, `[abc]` matches 'a', 'b', or 'c'.

* **Ranges:** You can specify ranges of characters using a hyphen.  `[a-z]` matches any lowercase letter, `[0-9]` matches any digit, and `[A-Z]` matches any uppercase letter.  You can combine ranges: `[a-zA-Z0-9]` matches any alphanumeric character.

* **Negation:** A caret `^` at the beginning of a character set negates it. `[^abc]` matches any character *except* 'a', 'b', or 'c'.  `[^0-9]` matches any non-digit character.

* **Special Characters:** Inside character sets, most [[Regex Metacharacters]] lose their special meaning *except* for `\` (backslash), `^` (caret - when at the beginning), and `-` (hyphen).  To match a literal `]` (closing square bracket), place it first or escape it with a backslash `\]`. To match a literal `-`, place it at the beginning or end, or escape it with `\-`. To match a literal `^`, place it anywhere other than the beginning, or escape it.


* **Examples:**

```python
import re

string = "Hello, World! 123"

# Match any lowercase vowel
match = re.findall(r"[aeiou]", string)  # Output: ['e', 'o', 'o']

# Match any digit
match = re.findall(r"[0-9]", string)  # Output: ['1', '2', '3']

# Match any character except a space
match = re.findall(r"[^ ]", string) #Output: ['H', 'e', 'l', 'l', 'o', ',', 'W', 'o', 'r', 'l', 'd', '!', '1', '2', '3']

# Match any uppercase or lowercase letter
match = re.findall(r"[a-zA-Z]", string) # Output: ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']

# Matching a literal ]
match = re.findall(r"[]]abc]", "abc[]]") #Output: ['abc]']

#Matching a literal -
match = re.findall(r"[-abc]", "abc-def") #Output: ['-']

#Matching a literal ^
match = re.findall(r"[^abc]", "abc^def") #Output: ['^']

```

[[Character Classes]]  ([[Escape Sequences]]) [[Regex Quantifiers]]
