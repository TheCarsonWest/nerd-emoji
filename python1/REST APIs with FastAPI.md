## [[REST APIs with FastAPI]]

### What are FastAPI REST APIs?
FastAPI is a modern, high-performance web framework for building RESTful APIs in Python. It offers features such as automatic [[Type Hinting]], dependency injection, and support for [[Asynchronous Programming]]. REST APIs are web services that follow the Representational State Transfer (REST) architectural style, using a set of request methods (e.g., GET, POST, PUT) to interact with data.

### How to Use FastAPI
To create a REST API with FastAPI, you can follow these steps:

1. Install FastAPI using pip: `pip install fastapi`
2. Create a Python file to define your API routes and data models.
3. Use `@app.get`, `@app.post`, `@app.put`, or `@app.delete` [[Decorators]] to define the API routes and HTTP methods.
4. Use FastAPI data models to define the data structures that your API will handle.
5. Run the API using `uvicorn main:app`, replacing `main` with the name of your Python file.

### Code Examples
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def get_item(item_id: int):
 return {"item_id": item_id}
```

### Related Python Concepts

- [[Modules and Packages]]: FastAPI is a Python module, and you need to import it to use its features.
- [[Functions]]: FastAPI routes are defined using function [[Decorators]].
- [[Type Hinting]]: FastAPI supports [[Type Hinting]] for data models and [[Function Parameters]].
- [[Asynchronous Programming]]: FastAPI supports [[Asynchronous Programming]], allowing for more efficient and scalable APIs.
- [[Importing Modules]]: You need to import the FastAPI module to use it in your Python code.
# [[Python 1 Home]]