## [[Web Development with Django]]

### What is Django?
Django is a high-level Python web framework that simplifies the development of complex, database-driven websites. It provides a wide range of features, including:

- Model-View-Template (MTV) architecture
- Object-relational mapping (ORM)
- Built-in user authentication and authorization
- Support for RESTful APIs

### How to Use Django
To set up a Django project, create a new directory and run the following command:

```bash
django-admin startproject mysite
```

Navigate to the `mysite` directory and run the following command to create an app for handling users:

```bash
python manage.py startapp users
```

Edit the `models.py` file in the `users` app and define a `User` model:

```python
from django.db import models

class User(models.Model):
 username = models.CharField(max_length=150)
 email = models.EmailField()
 password = models.CharField(max_length=128)
```

Run the following command to create the database tables:

```bash
python manage.py migrate
```

Create a `views.py` file in the `users` app and define a view to display a list of users:

```python
from django.shortcuts import render

def user_list(request):
 users = User.objects.all()
 context = {
 'users': users,
 }
 return render(request, 'users/user_list.html', context)
```

Create a `user_list.html` template file in the `templates/users` directory:

```html
{% for user in users %}
 {{ user.username }}
{% endfor %}
```

Add a URL pattern to the `urls.py` file in the `mysite` directory:

```python
from django.urls import path

from users.views import user_list

urlpatterns = [
 path('users/', user_list, name='user_list'),
]
```

Run the Django server:

```bash
python manage.py runserver
```

### Other Python Concepts

- [[Models and Objects]]: Django's ORM uses models and objects to represent data in the database.
- [[Inheritance]]: Django models can inherit from other models to create a hierarchy of classes.
- [[Polymorphism]]: Django models support polymorphism through the use of the `ContentType` model.
- [[Databases and SQL]]: Django uses a database backend (such as SQLite or PostgreSQL) to store and retrieve data.
- [[Web Development]]: Django is a framework specifically designed for web development.
# [[Python 1 Home]]