## [[Building APIs with Flask or Django]]

**What are Flask and Django?**
Flask and Django are popular Python frameworks for building web applications and APIs. Flask is a lightweight framework that provides a flexible base for creating web applications, while Django is a more comprehensive framework that follows the Model-View-Template (MVT) architecture.

## Using Flask

### Route Decoration
- `@app.route('/path')`: Decorator used to define a route that responds to HTTP requests at the specified path.

### Request Handling
- `request`: Represents the incoming HTTP request and provides access to its headers, body, and other attributes.
- `render_template('template.html')`: Renders an HTML template with the provided data.

### Response Handling
- `return 'Hello, world!'`: Sends a response to the client.
- `jsonify({'message': 'Success'})`: Sends a JSON response.

## Using Django

### URL Configuration
- `urlpatterns`: A list of `path()` objects that map URL patterns to views.
- `path('path/', view, name='view-name')`: Creates a URL pattern that calls the specified view.

### Views
- `HttpRequest` and `HttpResponse`: Objects representing the HTTP request and response respectively.
- `render(request, 'template.html')`: Renders an HTML template with the provided data.

### Models
- `models.Model`: Base class for Django models that define database fields and methods.
- `CharField`: A field that stores character data.
- `IntegerField`: A field that stores integer data.

## Related Python Concepts

- [[Variables and Data Types]]: Flask and Django use variables to store data in routes, views, and models.
- [[Functions]]: Routes and views are essentially functions that handle HTTP requests and responses.
- [[Classes and Objects]]: Django models are classes that represent database entities as objects.
- [[Modules and Packages]]: Flask and Django are modules that can be imported into Python scripts.
- [[Web Development with Django]]: Django is a comprehensive framework specifically designed for web development.
# [[Python 1 Home]]