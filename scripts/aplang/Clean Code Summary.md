# [[Useful Websites and Articles]]
# [[Clean Code Summary]]

**Key Principles:**

* **Meaningful Names:**  Choose names that clearly reveal intent. Avoid abbreviations or acronyms unless widely understood within the context.  Example: `userName` instead of `un`.

* **Functions:**
    * **Small:** Keep functions short and focused on a single task.  A function should ideally fit on a single screen.
    * **One Level of Abstraction:** Functions should operate at the same level of abstraction.  Mixing levels leads to confusion.
    * **Do One Thing:** Functions should do exactly one thing. If a function does more than one thing, it's likely to need refactoring.

* **Comments:**
    * **Explain *why*, not *what*:** Comments should explain the *reasoning* behind the code, not simply restate what the code already says.
    * **Keep comments up-to-date:** Outdated comments are worse than no comments.

* **Formatting:**
    * **Consistency:**  Maintain consistent indentation, spacing, and line breaks throughout the codebase.  This improves readability.
    * **Vertical Formatting:** Separate logical sections of code with blank lines.

* **Error Handling:**
    * **Use exceptions appropriately:** Avoid excessive exception handling that clutters the code.  Use exceptions for genuine exceptional conditions.
    * **Handle errors gracefully:** Provide informative error messages to the user and log errors appropriately for debugging.


* **Classes:**
    * **Single Responsibility Principle (SRP):** A class should have only one reason to change.
    * **Open/Closed Principle (OCP):** Classes should be open for extension, but closed for modification.
    * **Liskov Substitution Principle (LSP):** Subtypes should be substitutable for their base types without altering the correctness of the program.
    * **Interface Segregation Principle (ISP):** Clients should not be forced to depend upon interfaces they don't use.
    * **Dependency Inversion Principle (DIP):** High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.


* **SOLID Principles:** [[SOLID Principles Explained]]


* **Testing:**
    * **Write tests first (Test-Driven Development - TDD):**  Define the expected behavior of your code *before* writing the code itself.
    * **Keep tests concise and readable:**  Tests should be easy to understand and maintain.
    * **High test coverage:** Aim for a high level of test coverage to ensure code quality.


* **Refactoring:**
    * **Iterative process:** Refactoring is an iterative process of improving code design without changing its functionality.
    * **Small steps:** Make small, incremental changes during refactoring to reduce the risk of introducing errors.
    * **Use automated tests:**  Automated tests help ensure that your refactoring doesn't break existing functionality.


* **Code Smells:** [[Code Smells Catalog]]


* **Design Patterns:** [[Common Design Patterns]]


* **Estimating Code Complexity:** $ cyclomatic \ complexity = E - N + 2P $ where $E$ is the number of edges, $N$ is the number of nodes, and $P$ is the number of connected components.  This equation helps assess complexity; higher values indicate more complex code.  A low cyclomatic complexity generally means a simpler, more maintainable function.

* **General Tips:**
     - Keep it simple.
     - Strive for readability.
     - Review your own and others' code regularly.
     - Use a linter.


This is a summary; each point warrants further investigation.  I will create detailed notes on each of the linked topics above.
