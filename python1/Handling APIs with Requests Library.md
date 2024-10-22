## [[Handling APIs with Requests Library]]

### What is the Requests Library?
The Requests library is a widely used Python package that simplifies the process of making HTTP requests and handling API responses. It provides a comprehensive set of features to interact with web services and retrieve data over the internet.

### How to Use the Requests Library
**1. Importing the Library:**
```python
import requests
```

**2. Sending GET Requests:**
```python
response = requests.get("https://example.com/api/endpoint")
```
**Parameters:**
* `url`: The URL of the API endpoint to send the request to.
* `params`: Optional dictionary of query parameters to send with the request.

**3. Sending POST Requests:**
```python
response = requests.post("https://example.com/api/endpoint", data={"name": "John"})
```
**Parameters:**
* `url`: The URL of the API endpoint to send the request to.
* `data`: Optional dictionary of data to send in the request body.

**4. Sending Other Request Types:**
The Requests library supports other request types such as `put`, `delete`, etc. The syntax is similar to `get` and `post`.

**5. Handling Responses:**
The `response` object contains information about the API response.
* `response.status_code`: HTTP status code (e.g., 200 for OK).
* `response.text`: Response body as a string.
* `response.json()`: Response body parsed as a JSON object.

### Code Examples
**1. GET Request:**
```python
response = requests.get("https://api.github.com/users/user_name")
if response.status_code == 200:
 user_data = response.json()
 print(f"User Name: {user_data['name']}")
```

**2. POST Request:**
```python
response = requests.post("https://api.example.com/create_task", json={"title": "New Task"})
if response.status_code == 201:
 print("Task created successfully.")
```

### Related Python Concepts
- [[Importing Modules]]: The Requests library must be imported to use its functionality.
- [[HTTP]]: The library is designed for working with HTTP protocols and API endpoints.
- [[JSON]]: The Requests library can parse and handle JSON responses.
- [[Exception Handling]]: Requests can raise exceptions in case of errors during the request or response handling.
- [[File Handling]]: The response body can be written to a file using file handling concepts.
# [[Python 1 Home]]