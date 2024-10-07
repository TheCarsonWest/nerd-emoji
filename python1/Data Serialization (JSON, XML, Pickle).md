## Data Serialization

### What is Data Serialization?
Data serialization is the process of converting an object into a format that can be stored and later reconstructed. It allows complex objects to be represented as streams of bytes, which can be easily stored in files, transmitted over networks, or processed by other programs.

### JSON (JavaScript Object Notation)

**How to Use JSON**
```python
import json

# Dictionary to JSON
data = {"name": "John Doe", "age": 30}
json_data = json.dumps(data)

# JSON to Dictionary
json_data = '{"name": "John Doe", "age": 30}'
data = json.loads(json_data)
```

**Parameters:**
- `json.dumps(obj, [indent, sort_keys, separators, default])`: Converts an object to a JSON string.
- `json.loads(json_string)`: Converts a JSON string to an object.

**Code Example:**
```python
data = {"name": "John Doe", "age": 30}
with open('data.json', 'w') as json_file:
 json.dump(data, json_file)

with open('data.json', 'r') as json_file:
 data = json.load(json_file)
```

### XML (Extensible Markup Language)

**How to Use XML**
```python
import xml.etree.ElementTree as ET

# Create XML element
root = ET.Element("root")
child = ET.SubElement(root, "child")
child.text = "data"

# Write XML to file
xml_string = ET.tostring(root)
with open('data.xml', 'w') as xml_file:
 xml_file.write(xml_string)

# Parse XML from file
with open('data.xml', 'r') as xml_file:
 root = ET.parse(xml_file).getroot()
```

**Parameters:**
- `ET.ElementTree.tostring(element, [encoding, method])`: Converts an XML element to a string.
- `ET.parse(source, [parser])`: Parses an XML document from a file or string.

**Code Example:**
```python
data = {"name": "John Doe", "age": 30}
root = ET.Element("root")
for key, value in data.items():
 ET.SubElement(root, "item", attrib={"key": key}).text = str(value)

xml_string = ET.tostring(root)
with open('data.xml', 'w') as xml_file:
 xml_file.write(xml_string)
```

### Pickle

**How to Use Pickle**
```python
import pickle

# Object to Pickle
data = {"name": "John Doe", "age": 30}

# Pickle to file
with open('data.pickle', 'wb') as pickle_file:
 pickle.dump(data, pickle_file)

# Unpickle from file
with open('data.pickle', 'rb') as pickle_file:
 data = pickle.load(pickle_file)
```

**Parameters:**
- `pickle.dump(obj, file, [protocol])`: Pickles an object and writes it to a file.
- `pickle.load(file, [fix_imports, encoding, errors])`: Unpickles an object from a file.

**Code Example:**
```python
data = {"name": "John Doe", "age": 30}
with open('data.pickle', 'wb') as pickle_file:
 pickle.dump(data, pickle_file)
```

### Related Python Concepts

- [[File Handling]]: Data serialization allows objects to be stored in files.
- [[Objects and Classes]]: Complex objects can be serialized using Pickle.
- [[Modules and Packages]]: JSON and XML use modules to provide serialization capabilities.
- [[Functions]]: Serialization is typically done using functions like `json.dumps` and `pickle.dump`.
- [[Decorators]]: [[Decorators]] can be used to enhance serialization functionality.
# [[Python 1 Home]]