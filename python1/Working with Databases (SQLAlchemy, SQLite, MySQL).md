## Working with Databases (SQLAlchemy, SQLite, MySQL)

### What is Working with Databases?
Working with databases in Python involves using libraries and tools to establish connections with database management systems (DBMS) like SQLite, MySQL, or PostgreSQL. It allows Python programs to manipulate, retrieve, and manage data stored in these databases. SQLAlchemy is a popular Python object-relational mapping (ORM) library that simplifies the interaction with databases and makes it easier to perform common database operations.

### How to Use SQLAlchemy with SQLite
1. **Install SQLAlchemy:** Use pip to install SQLAlchemy package:
```
pip install sqlalchemy
```
2. **Import SQLAlchemy:** Import the necessary modules from SQLAlchemy.
```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
```
3. **Create an Engine:** Establish a connection to the SQLite database.
```python
engine = create_engine('sqlite:///database.sqlite')
```
4. **Define a Model:** Define a class that represents the database table.
```python
Base = declarative_base()

class User(Base):
 __tablename__ = 'users'
 id = Column(Integer, primary_key=True)
 name = Column(String)
```
5. **Create Tables:** Create the database tables using the engine.
```python
Base.metadata.create_all(engine)
```

### How to Use MySQL with SQLAlchemy
1. **Install SQLAlchemy and MySQL Connector:** Install both SQLAlchemy and MySQL Connector packages.
```
pip install sqlalchemy
pip install mysql-connector-python
```
2. **Import Necessary Modules:** Import from SQLAlchemy and MySQL Connector.
```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import mysql.connector
```
3. **Create an Engine:** Establish a connection to the MySQL database.
```python
engine = create_engine('mysql+mysqlconnector://[username]:[password]@[host]:[port]/[database_name]')
```
4. **Define a Model:** Similarly to SQLite, define a class representing the database table.
5. **Create Tables:** Create the tables using the engine.

### Related Python Concepts
- [[Variables and Data Types]]: Database connections and data are stored in variables.
- [[Object-Oriented Programming]]: SQLAlchemy uses classes and objects to model database schemas.
- [[List Comprehension]]: Database queries often utilize list comprehensions for data filtering and manipulation.
- [[Generators]]: SQLAlchemy uses generators to lazily load data from databases.
- [[File Handling]]: Database operations often involve reading and writing to files.
# [[Python 1 Home]]