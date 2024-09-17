**Python Control Flow: [[If Statements]]**

**Explanation**

[[If Statements]] allow for conditional execution of code blocks in Python. They enable you to control the flow of your program based on whether a certain condition is true or false.

**Parameters**

- [[If]] clause: The condition that determines whether the code block will be executed.
- **colon**: Marks the end of the [[if]] clause and the beginning of the code block.
- **indentation**: Indent the code block to indicate that it belongs to the [[If Statements]] statement.

**Code Examples**

```python
# Check if a number is positive
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")

# Check if a string is empty
s = "Hello World"
if not s:
    print("The string is empty.")
```

**Variations**

- [[elif]] (else if): Used to check additional conditions.
- **else**: Used to execute code if none of the [[if]]/[[elif]] conditions are met.

**Code Examples**

```python
# Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

**Linked Concepts**

- [[Boolean operators]] : Used to create conditions in [[if]] statements (e.g., and, or, not).
- [[Comparison operators]] : Used to compare values in conditions (e.g., ==, !=, <, >).
- [[Loops]] : Can be used in conjunction with [[if]] statements for more complex conditional execution (e.g., for loops, while loops).
- [[Functions]] : Can return values that can be used as conditions in [[if]] statements.

**Task:** recreate the this markdown file exactly, but whenever one of these topics is mentioned, put two brackets around it, and make sure it matches one of the list of the other topics in the folder. Here are the list of topics in the folder:

Dictionaries.md
Variables_and_Data_Types.md
Generators.md
Context_Managers.md
Polymorphism.md
Libraries_like_Pandas.md
File_Handling.md
Inheritance.md
Decorators.md
Function_Parameters.md
Default_Parameters.md
List_Comprehension.md
Sets.md
Control_Flow_If_Statements.md
Recursion.md
Operators.md
Regular_Expressions.md
Libraries_like_Matplotlib.md
Return_Values.md
Tuples.md
Lists.md
Classes_and_Objects.md
Lambda_Functions.md
Encapsulation.md
Functions.md
Exception_Handling.md
For_Loops.md
While_Loops.md
Modules_and_Packages.md
Libraries_like_NumPy.md
Importing_Modules.md