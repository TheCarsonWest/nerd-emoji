# [[Variable Naming Conventions]]
# Python: [[Code Style Guides]] 
These notes cover Python code style guides, focusing on best practices and tools for ensuring consistent and readable code.


Key aspects:

* **Consistency:**  The most important aspect.  Choose a style and stick to it throughout your project.

* **Readability:**  Code should be easy to understand and maintain.  This includes using meaningful names, adding comments where necessary, and following consistent formatting.


**Main Style Guides:**

* **PEP 8:**  The official Python Enhancement Proposal for style.  It's the de facto standard and widely adopted.  Consider this your starting point.  See the detailed explanation in [[PEP 8 Deep Dive]].

    *   **Indentation:**  Use [[4]] spaces, *never* tabs.
    *   **Line Length:** Aim for 79 characters per line.
    *   **Naming Conventions:**  `snake_case` for variables and functions, `CamelCase` for classes.
    *   **Blank Lines:** Use blank lines to separate logical sections of code.

* **Google Python Style Guide:**  A stricter, more comprehensive guide often used in larger projects. It builds on PEP 8, adding further details and rules. [[Google Style Guide Details]]

* **Other Guides:**  Various organizations and companies have their own style guides (e.g., internal standards).  These often extend or modify PEP 8.



**Tools for Enforcing Style:**

* **`pylint`:** A popular tool for static code analysis that checks for style violations, as well as other potential problems.  [[Pylint Usage]]

* **`flake8`:** Combines `pycodestyle` (PEP 8 checker), `pyflakes` (finds errors), and `mccabe` (complexity checker). Often preferred for its speed and comprehensive coverage. [[Flake8 Usage]]

* **IDE Integration:**  Most IDEs (e.g., VS Code, PyCharm) have built-in support for PEP 8 and other linters, providing real-time feedback and automatic code formatting.


**Example (Illustrative):**

```python
# Good Example (PEP 8 Compliant):

def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    total = a + b
    return total

```

```python
# Bad Example (Violates PEP 8):
def CalculateSum(a,b):#no spaces, poor naming
    total=a+b  #no spaces
    return total #missing blank line before return
```


**Further Considerations:**

* **Docstrings:**  Write clear and concise docstrings to explain the purpose of functions, classes, and modules.  See [[Docstring Best Practices]].

* **Comments:**  Use comments to explain complex logic or non-obvious code sections.  Avoid over-commenting.


This is a summary.  Refer to the linked notes for more detailed explanations.
