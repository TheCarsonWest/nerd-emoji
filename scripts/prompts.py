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



prompt = f"""
Create a notecard on the APUSH topic {file_name}, using this following format:
WHEN: (exact date if possible, if not narrow it down to a specific time period...acts/laws, specific events, etc should have specific dates. AP exam questions are ALWAYS broken down into certain time frames; timelines will be very important)

WHO: (who is involved or who started the event or concept; if a person - who is the person, President, Doctor, lawyer, etc. that would be important to know) 

WHAT: (answer what the concept is or what the person did exactly or what happened specifically during an event 

IMPACT:Why is that significant? What did it lead to? What impact did the person or event or law have on the United States?

Here is an example:
ID: Constitutional Convention
When: May -September 1787
Who: 55 delegates, including James Madison, George W, and Alexander Hamilton (originally 70) from  12 states except for RI
What: Meeting held in Philadelphia Pennsylvania, to revise and fix the Articles of Confederation after weaknesses were exposed by Shays Rebellion
Impact? Why Significant?: Decided to set aside the AOC due to its many weaknesses and create a new US Constitution
"""

prompt = f"""
Create an AP United States History rundown on {name}. Include events they were associated with, important legislation they signed, groups they were a part of, and their impact on the country
"""        

prompt = f"""
Create an AP United States History rundown on the state of {name}. Includ a timeline of events they were associated with, important legislation they signed, important court cases  they may have been a part of, their major industry, and their impact on the rest of the country
"""