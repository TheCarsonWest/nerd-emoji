# [[Regex Metacharacters]]
# [[Regex Special Sequences]] 
This note covers Python's regular expression special [[Sequences]].  These [[Sequences]] provide shortcuts for commonly used patterns.

**Important Note:** Remember to import the `re` module before using any of these.  `import re`

```python
import re
```

Here's a breakdown of common special [[Sequences]]:

* `\d`: Matches any decimal digit (0-9).  Equivalent to `[0-9]`.
* `\D`: Matches any non-digit character. Equivalent to `[^0-9]`.
* `\w`: Matches any alphanumeric character (a-z, A-Z, 0-9, and underscore _). Equivalent to `[a-zA-Z0-9_]`.
* `\W`: Matches any non-alphanumeric character. Equivalent to `[^a-zA-Z0-9_]`.
* `\s`: Matches any whitespace character (space, tab, newline).
* `\S`: Matches any non-whitespace character.
* `\b`: Matches a word boundary (the position between a word character and a non-word character).  Useful for finding whole words.
* `\B`: Matches a non-word boundary.
* `.`: Matches any character (except newline).

**Examples:**

```python
text = "My phone number is 123-456-7890."

# Find all digits
digits = re.findall(r"\d", text)
print(f"Digits: {digits}")

# Find all words
words = re.findall(r"\b\w+\b", text) # \b ensures whole words are matched
print(f"Words: {words}")


# Find phone number (more complex example - requires more than just special sequences)
phone_number = re.search(r"\d{3}-\d{3}-\d{4}", text)
if phone_number:
    print(f"Phone number: {phone_number.group(0)}")
```

[[Character Sets]]  These provide an alternative way of defining patterns, often in conjunction with special [[Sequences]].

[[Quantifiers]]  These are used to specify how many times a character or group should appear.  (e.g., `+`, `*`, `?`, `{n}`, `{n,}`, `{n,m}`)

[[Anchors]]  These match positions within a string, not characters. (e.g., `^`, `$`, `\b`, `\B`)

[[Groups and Capturing]]  This covers capturing groups using parentheses `()` and accessing captured substrings.

[[Regex Metacharacters]] A comprehensive overview of metacharacters used in regex beyond special sequences.

[[Regex Methods in Python's `re` module]] A complete reference to all methods within Python's `re` module for working with [[Regular Expressions]].
