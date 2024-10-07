## [[Automating Tasks with Selenium]]

### What is Selenium?
Selenium is an open-source framework used for web automation. It allows developers to control a web browser like a real user, enabling automated testing and interaction with web applications.

### How to Use Selenium
#### Importing the Selenium Module
```python
import selenium
from selenium import webdriver
```

#### Creating a WebDriver Instance
To control a browser, we create a WebDriver instance, which acts as a virtual "driver" that performs actions on the browser.
```python
driver = webdriver.Chrome() # for Chrome browser
# replace Chrome() with Firefox(), Edge(), or Safari() for other browsers
```

#### Common WebDriver Methods
- `get()`: Loads a URL in the browser.
- `find_element()`: Locates a web element on the page using various strategies (e.g., by ID, name, CSS selector).
- `find_elements()`: Locates all elements matching a given strategy.
- `click()`: Simulates a click on an element.
- `send_keys()`: Sends text input to a form field.

### Code Examples
#### Basic Usage
```python
driver.get("https://google.com")
search_field = driver.find_element("name", "q")
search_field.send_keys("Selenium")
search_field.submit()
```

#### More Advanced Example
```python
from selenium.webdriver.common.by import By

# wait for an element to be visible for up to 5 seconds
element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "example_id")))
```

### Related Python Concepts
- [[Variables and Data Types]]: Variables are used to store WebDriver instances and web elements.
- [[Operators]]: Comparison operators are used to check conditions in WebDriver methods.
- [[Control Flow If Statements]]: If statements can be used to conditionally execute WebDriver actions based on element visibility or other criteria.
- [[For Loops]]: For loops can be used to iterate over multiple web elements on a page.
- [[While Loops]]: While loops can be used to repeatedly perform actions on a page until a certain condition is met.
# [[Python 1 Home]]