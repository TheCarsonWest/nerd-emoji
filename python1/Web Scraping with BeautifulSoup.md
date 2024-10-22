## [[Web Scraping with BeautifulSoup]]

### What is [[Web Scraping with BeautifulSoup]]?
Web scraping with BeautifulSoup is a technique to extract and parse data from web pages. BeautifulSoup is a Python library that specifically focuses on parsing HTML and XML documents, making it an efficient tool for web scraping.

### How to Use BeautifulSoup
#### Creating a BeautifulSoup Object
To use BeautifulSoup for scraping, first create a BeautifulSoup object by parsing the HTML or XML document. The syntax is:

```python
from bs4 import BeautifulSoup

html_doc = "<html><body><p>This is a paragraph</p></body></html>"
soup = BeautifulSoup(html_doc, "html.parser")
```

#### Navigating the Document
Once the BeautifulSoup object is created, you can navigate and extract data from the HTML or XML document using various methods:

- `soup.find('tag_name')`: Finds the first occurrence of the specified HTML tag.
- `soup.find_all('tag_name')`: Finds all occurrences of the specified HTML tag.
- `soup.select('css_selector')`: Selects elements using CSS selectors.

#### Extracting Data
To extract data from the HTML elements, use methods like:

- `element.text`: Returns the text content of the element.
- `element.attrs`: Returns a dictionary of the element's attributes.
- `element.get('attribute_name')`: Gets the value of a specific attribute.

### Code Examples
```python
# parse HTML from a website
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# find the title of the page
title_element = soup.find('title')
title = title_element.text
```

### Related Python Concepts

- [[Libraries like Requests Library]]: BeautifulSoup is often used in conjunction with libraries like Requests for fetching web pages.
- [[Regular Expressions]]: BeautifulSoup uses regular expressions for extracting specific patterns from web pages.
- [[HTML and XML]]: BeautifulSoup specifically parses HTML and XML documents.
- [[Web Development with Django]]: Web scraping can be used to gather data for web development projects.
- [[Handling APIs with Requests Library]]: Web scraping can be used to access data from APIs.
# [[Python 1 Home]]