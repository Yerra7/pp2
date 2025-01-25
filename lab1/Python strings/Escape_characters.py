# Escape Characters
''' 
An escape character is used to insert characters that are illegal in a string.
It is represented by a backslash (\) followed by the character you want to insert.
'''

# Example of using an escape character
''' 
If you try to use double quotes inside a string surrounded by double quotes, 
it will result in an error.
'''

# This will cause an error:
# txt = "We are the so-called "Vikings" from the north."

# To fix this, use the escape character to allow the double quotes inside the string:
txt = "We are the so-called \"Vikings\" from the north."

print(txt)  # Output: We are the so-called "Vikings" from the north.

# Escape Characters in Python
''' 
Here are some other escape characters that you can use in Python:
'''

# Example of different escape characters:
txt = 'It\'s a great day'  # Single quote
print(txt)  # Output: It's a great day

txt = "This is a backslash: \\"  # Backslash
print(txt)  # Output: This is a backslash: \

txt = "This is a new line:\nThis is the next line"  # New line
print(txt)  
# Output:
# This is a new line:
# This is the next line

txt = "This is a carriage return:\rOverwritten"  # Carriage return
print(txt)  # Output: Overwritten

txt = "This is a tab:\tTab space"  # Tab
print(txt)  # Output: This is a tab:    Tab space

txt = "This is a backspace:\bBackspace"  # Backspace
print(txt)  # Output: This is a backspacBackspace

txt = "This is a form feed:\fForm feed"  # Form feed
print(txt)  # Output: This is a form feed:Form feed

# Octal and Hexadecimal values
txt = "\101"  # Octal value (equivalent to 'A')
print(txt)  # Output: A

txt = "\x41"  # Hexadecimal value (equivalent to 'A')
print(txt)  # Output: A
