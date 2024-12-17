# [[Data Type Conversions]]
# [[JSON Conversion]] 
This note covers JSON conversion in Python.

Key modules:  `json`

**Encoding (Python objects to JSON):**

```python
import json

data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

json_data = json.dumps(data, indent=4) # indent for pretty printing
print(json_data)

#writing to a file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
```

**Decoding (JSON to Python objects):**

```python
import json

with open('data.json', 'r') as f:
    loaded_data = json.load(f)

print(loaded_data)
print(type(loaded_data)) # confirms it's a dictionary


json_string = '{"name": "Jane Doe", "age": 25, "city": "London"}'
loaded_data_string = json.loads(json_string)
print(loaded_data_string)
```

**Handling Errors:**  Use `try...except` blocks to handle `json.JSONDecodeError` in case of invalid JSON.


```python
import json

try:
    invalid_json = '{"name": "Alice", "age": 28, "city": "Paris"}'  #missing quote
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

```

[[Error Handling in Python]]  ([[JSON Data Structures]])


**Special Considerations:**

*   **Data types:**  Python's dictionaries and lists map naturally to JSON objects and arrays.  However,  be mindful of unsupported data types (e.g., sets).  You might need custom encoding/decoding logic for these.
*   **Large files:** For extremely large JSON files, consider using iterative parsing to avoid loading the entire file into memory at once.  Libraries like `ijson` can be helpful here. [[Iterative JSON Parsing]]

