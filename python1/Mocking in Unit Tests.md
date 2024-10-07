## [[Mocking in Unit Tests]]

### What is Mocking?
Mocking is a technique in unit testing where a specific class or function is replaced with a substitute (or mock) object that simulates its behavior. The substitute object can be controlled and programmed to provide predictable responses, allowing you to test the code that relies on it without the actual implementation.

### How to Use Mocking
To use mocking in Python, you can use a mocking framework such as Mock from the `unittest.mock` module.

- `Mock` Function:
 - `Mock(**attrs)`: Creates a mock object.
 - `mock.configure_mock(**attrs)`: Configures the attributes of the mock object.
 - `mock.assert_called_with(*args, **kwargs)`: Asserts that the mock object was called with the specified arguments.
 - `mock.assert_not_called()`/`assert_called_once()`/`assert_called_n_times(n)`: Asserts the number of times the mock object was called.

### Code Examples
```python
# Mock a function using Mock from unittest.mock
from unittest.mock import Mock

mock_function = Mock()

# Configure the mocked function to return a specific value
mock_function.configure_mock(return_value="Mocked Response")

# Call the mocked function
result = mock_function("Hello")

# Assert that the mocked function was called with the correct argument
mock_function.assert_called_with("Hello")

# Assert that the mocked function returned the expected value
assert result == "Mocked Response"
```

### Related Python Concepts

- [[Unit Testing and Test-Driven Development]]: Mocking is a technique used in unit testing to isolate and test individual functions or classes.
- [[Functions]]: Mocks are used to substitute for other functions or objects.
- [[Classes and Objects]]: Mocks can be used to create substitute objects for testing purposes.
- [[Inheritance]]: Mocks can be used to create subclasses of existing classes with overridden methods for testing.
- [[Polymorphism]]: Mocks provide a way to create objects that behave like other objects, enabling polymorphism in testing.
# [[Python 1 Home]]