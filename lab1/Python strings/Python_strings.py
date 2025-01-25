# Python Strings
''' 
Strings in Python are surrounded by either single quotation marks (' ') or double quotation marks (" ").
'hello' is the same as "hello".
'''

# Example of printing strings
print("Hello")  # Output: Hello
print('Hello')  # Output: Hello

# Quotes Inside Quotes
''' 
You can use quotes inside a string, as long as they don't match the quotes surrounding the string.
'''

# Examples of using quotes inside strings:
print("It's alright")  # Output: It's alright
print("He is called 'Johnny'")  # Output: He is called 'Johnny'
print('He is called "Johnny"')  # Output: He is called "Johnny"

# Assign String to a Variable
''' 
Assigning a string to a variable is done with the variable name followed by an equal sign and the string.
'''

# Example of assigning a string to a variable:
a = "Hello"
print(a)  # Output: Hello

# Multiline Strings
''' 
You can assign a multiline string to a variable by using triple quotes.
'''

# Example using triple double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Example using triple single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

''' 
Note: in the result, the line breaks are inserted at the same position as in the code.
'''

# Strings are Arrays
''' 
Strings in Python are arrays of bytes representing unicode characters.
A single character is simply a string with a length of 1.
'''

# Example of accessing a character at position 1 (remember that the first character has position 0):
a = "Hello, World!"
print(a[1])  # Output: e

# Looping Through a String
''' 
You can loop through the characters in a string, just like you would with an array.
'''

# Example of looping through the letters in the word "banana":
for x in "banana":
  print(x)  # Output: b, a, n, a, n, a

# String Length
''' 
To get the length of a string, use the len() function.
'''

# Example of using len() to find the length of a string:
a = "Hello, World!"
print(len(a))  # Output: 13

# Check String
''' 
To check if a certain phrase or character is present in a string, use the "in" keyword.
'''

# Example of checking if "free" is present in the text:
txt = "The best things in life are free!"
print("free" in txt)  # Output: True

# Use it in an if statement:
if "free" in txt:
  print("Yes, 'free' is present.")  # Output: Yes, 'free' is present.

# Check if NOT
''' 
To check if a certain phrase or character is NOT present in a string, use the "not in" keyword.
'''

# Example of checking if "expensive" is NOT present in the text:
txt = "The best things in life are free!"
print("expensive" not in txt)  # Output: True

# Use it in an if statement:
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")  # Output: No, 'expensive' is NOT present.
