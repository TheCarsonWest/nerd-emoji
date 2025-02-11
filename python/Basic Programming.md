```python
print("Hello world")
```
it prints hello world to the console

# Full definition of print() function

###### `print(*, sep=" ", end="\n", file=sys.stdout, flush=False)`

- `*`: This means that anything and any amount of values can be passed as an argument to the print function
- `sep`: sep is what separates each argument passed to a singular print function
	- The Default value is " "(a space)
- `end`: end is what is written at the end of the print statement
	- The Default value is "\n", which makes a the console go to the next line
- `file`: not important to us, dictates what console the print gets sent to, keep it default
	- Default is your current terminal
- `flush`: not important to us. Forces the terminal to clear the writing buffer to write it
	- Default is False(I still am not entirely sure what this does)

# Comments

# its the # sign and the """Long string"""
```python
# Normal Comment
"""
Long strings can be used as comments
Yeah
"""

"You can also technically do this with normal strings but dont do that"

print("Hello word") # you can add a comment after all the code in a line
```

Thats it 

use comments to help people read your code and you are good


# String [[Operators]] and `input()`
```python
x = input("Name: ")
print("hello "+ x)
print(f"I hope you are doing ok today {x}")
print(x*[[5])
```
## input asks the user for their input in the console
- it always gets output as a string
- its not that complicated
## String Operations
### Add strings with plus
- you cannot add together a string and a nonstring
- fix this by putting it in str(<>)
```python
x = 12
y = "Hello"
try:
	print(y+" there all "+x+" of you") # this will error
except:
	print(y+" there all "+str(x)+" of you") # this wont
```
### f string
```python
x = 12
y = "Hello"
print(f"{y} there all {x} of you")
```
F strings automatically convert everything into strings