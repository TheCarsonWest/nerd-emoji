# [[Python 1 Home]]
# [[Regular Expressions]] 
Regular expressions (regex or regexp) are powerful tools for pattern matching within strings.  They are incredibly useful for tasks like data validation, text manipulation, and searching.

Key Concepts:

* **Metacharacters:** Special characters that have specific meanings in regex (e.g., `.` for any character, `*` for zero or more repetitions, `+` for one or more repetitions, `?` for zero or one repetition, `[]` for character sets, `()` for grouping, `^` for beginning of string, `$` for end of string). [[Regex Metacharacters]]
* **Quantifiers:**  Specify how many times a character or group should appear (e.g., `*`, `+`, `?`, `{n}`, `{n,}`, `{n,m}`). [[Regex Quantifiers]]
* **Anchors:**  Match positions within a string, not characters (e.g., `^`, `$`).
* **Character Sets:** Define a set of characters to match (e.g., `[abc]`, `[a-z]`, `[^abc]`). [[Regex Character Sets]]
* **Grouping and Capturing:** Use parentheses `()` to group parts of a regex and capture matched substrings. [[Regex Grouping and Capturing]]
* **Alternation:** Use the pipe symbol `|` to specify alternative patterns.
* **Flags:** Modify the behavior of the regex engine (e.g., `re.IGNORECASE` for case-insensitive matching). [[Regex Flags]]

Python's `re` module provides functions for working with regular expressions:

```python
import re

text = "My phone number is 123-456-7890 and email is test@example.com"

# Find phone number
phone_number_match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if phone_number_match:
    print(f"Phone number: {phone_number_match.group(0)}")

# Find all email addresses (this assumes a simple email format)
email_matches = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(f"Email addresses: {email_matches}")

# Replace phone number with ***-***-****
new_text = re.sub(r"\d{3}-\d{3}-\d{4}", "***-***-****", text)
print(f"New text: {new_text}")

```

Related Notes:

- [[Regex Groups and Backreferences]]


Further Exploration:

*  Practice writing regexes for different scenarios.  Online regex testers can be helpful.
* Learn about more advanced techniques like lookahead and lookbehind assertions.


