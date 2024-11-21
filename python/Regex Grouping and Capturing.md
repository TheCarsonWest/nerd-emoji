# [[Regex Metacharacters]]
# Regex Grouping and Capturing

This note covers grouping and capturing in [[Regular Expressions]] using Python's `re` module.

**Core Concepts:**

* **Grouping:**  Parentheses `()` are used to group parts of a regular expression. This allows you to apply quantifiers or other operations to the entire group, rather than just a single character.

* **Capturing:**  By placing parentheses around parts of a regex, you can capture the matched text from those specific groups.  These captured groups can then be accessed using `re.match().groups()` or `re.findall()`.


**Syntax:**

```python
import re

text = "My phone number is 123-456-7890, and my zip code is 90210."

# Grouping and capturing phone number
match = re.search(r"(\d{3})-(\d{3})-(\d{4})", text) 

if match:
    area_code, exchange, line_number = match.groups()
    print(f"Area Code: {area_code}, Exchange: {exchange}, Line Number: {line_number}")

#Capturing multiple matches with findall
matches = re.findall(r"(\d{5})", text) #finds all 5 digit numbers
print(f"Zip codes found: {matches}")


#Named capturing groups (Python 3.6+)
match = re.search(r"(?P<area_code>\d{3})-(?P<exchange>\d{3})-(?P<line_number>\d{4})", text)
if match:
    print(f"Area Code: {match.group('area_code')}, Exchange: {match.group('exchange')}, Line Number: {match.group('line_number')}")

```

**Named Capture Groups:**  These are more readable and convenient for accessing captured groups by name instead of index.  See example in the code above.


**Applications:**

* Extracting specific parts of a string (like phone numbers, email addresses, dates).
* Replacing parts of a string based on captured groups (using `re.sub()`).
* Validating input data by checking if the input matches a certain pattern with specific groups.



[[Regex `re.sub()` function]]  ([[Regex `re.findall()` function]]) [[Python's `re` Module]]
