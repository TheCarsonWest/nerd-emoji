import os
from time import sleep
import google.generativeai as genai

genai.configure(api_key=open('api.txt','r').readline())
model = genai.GenerativeModel("gemini-pro")

def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        sleep(5)
        print('eror, waiting')
        return ai_text(p)

def create_files(file_names, file_extension):
    for name in file_names:
        # Construct the file name with the given extension
        file_name = f"{name}.{file_extension}"

        # Generate the prompt with clear instructions and context
        prompt = f"""
        Create a detailed and structured notes page IN MARKDOWN, using headings and subheadings, on the topic of Python {name}. Include:
    - An explanation of what it is
    - How to use it(if it is a function an has parameters, how to use each one)
    - Code exmaples of how it is used
    - other python concepts are most closely relate to this one(5 max)
    - Mention other python concepts in the notes
    - Make sure to link to any other concepts mentioned by typing their file name in DOUBLED(like [[this]]) brackets whenever they come up. Here are the other topics:
    {str(file_names)}
    You can ONLY link to these other concepts, and only use the EXACT spelling shown above.\n DO NOT simply copy all of these concepts at the bottom of the text. 
    here is a good example:
    # Control Flow If Statements

## What are If Statements?
If statements are a foundational control flow construct that allows the execution of one or more code blocks based on a Boolean condition. They enable conditional execution and provide the means to make decisions and alter the flow of a program.

## How to Use If Statements
The syntax of an if statement in Python is:

```python
if condition:
    # code block to be executed if condition is True
```

The `condition` is typically a comparison expression that evaluates to either True or False. If the condition is True, the code block under the if statement will be executed. Otherwise, the execution will skip to the next statement after the if statement.

## Code Examples
```python
# check if the value of x is greater than 5
if x > 5:
    print("x is greater than 5")
```

```python
# check if the user is an administrator
if user_is_admin():
    # allow access to sensitive data
    pass
```

## Related Python Concepts

- [[Variables and Data Types]]: If statements rely on Boolean data types to evaluate conditions.
- [[Operators]]: Comparison operators like `>` and `==` are used to create conditions in if statements.
- [[Functions]]: If statements can be used to conditionally call functions.
- [[For Loops]]: If statements can be used to control the execution of for loops.
- [[While Loops]]: If statements can be used to terminate or continue the execution of while loops.
        """
        
        # Generate the text using the prompt
        response = ai_text(prompt)

        # Write the generated text to the file
        with open("./result/"+file_name, 'w') as file:
            file.write(response)
            print('created '+file_name)
        sleep(1)

file_names = [
    "Variables and Data Types",
    "Operators",
    "Control Flow If Statements",
    "For Loops",
    "While Loops",
    "Functions",
    "Function Parameters",
    "Return Values",
    "Default Parameters",
    "Recursion",
    "Lambda Functions",
    "Lists",
    "Tuples",
    "Dictionaries",
    "Sets",
    "List Comprehension",
    "File Handling",
    "Exception Handling",
    "Classes and Objects",
    "Inheritance",
    "Polymorphism",
    "Encapsulation",
    "Modules and Packages",
    "Importing Modules",
    "Generators",
    "Decorators",
    "Context Managers",
    "Regular Expressions",
    "Libraries like NumPy",
    "Libraries like Pandas",
    "Libraries like Matplotlib",
    "Type Hinting",
    "Mutable vs Immutable Types",
    "Bitwise Operators",
    "Nested If Statements",
    "Nested Loops",
    "Function Overloading",
    "Higher-Order Functions",
    "Closures",
    "Global and Nonlocal Variables",
    "Memoization in Recursion",
    "Map, Filter, and Reduce",
    "Multidimensional Lists",
    "Dictionary Comprehension",
    "Frozen Sets",
    "File IO Modes",
    "Handling Binary Files",
    "Custom Exceptions",
    "Abstract Classes",
    "Multiple Inheritance",
    "Method Resolution Order (MRO)",
    "Private and Protected Members",
    "Dynamic Importing",
    "Virtual Environments",
    "Async Generators",
    "Coroutines",
    "Chaining Decorators",
    "Custom Context Managers",
    "Regex Groups and Backreferences",
    "NumPy Broadcasting",
    "DataFrames in Pandas",
    "Plot Customization in Matplotlib",
    "Metaclasses",
    "Descriptors",
    "Duck Typing",
    "Concurrency and Multithreading",
    "Multiprocessing",
    "Asynchronous Programming",
    "Web Scraping with BeautifulSoup",
    "Building APIs with Flask or Django",
    "Working with Databases (SQLAlchemy, SQLite, MySQL)",
    "Unit Testing and Test-Driven Development",
    "Mocking in Unit Tests",
    "Profiling and Optimization",
    "Memory Management",
    "Garbage Collection",
    "Thread Safety",
    "Pathlib and OS Module",
    "Command Line Interface (CLI) Programs",
    "Creating GUI Applications with Tkinter or PyQt",
    "Web Development with Django",
    "Handling APIs with Requests Library",
    "Data Serialization (JSON, XML, Pickle)",
    "REST APIs with FastAPI",
    "Automating Tasks with Selenium",
    "Handling Large Datasets with Dask",
    "Building Machine Learning Models with Scikit-learn",
    "Deep Learning with TensorFlow or Keras",
    "Natural Language Processing with NLTK or Spacy",
    "Data Visualization with Seaborn",
    "Time Series Analysis",
    "Working with Big Data using PySpark",
    "Security and Cryptography (PyCryptodome)",
    "Network Programming (Sockets)",
    "Building and Distributing Python Packages",
    "Python Package Index (PyPI) Publishing",
    "Continuous Integration or Continuous Deployment (CI or CD) with Python"
]
file_extension = "md"  # Change to your desired file type

create_files(file_names, file_extension)

 