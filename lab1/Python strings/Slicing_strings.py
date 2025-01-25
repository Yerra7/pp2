# Slicing Strings
''' 
Slicing allows you to extract a specific range of characters from a string.
You specify the start and end indices, separated by a colon.
'''

# Example of slicing:
b = "Hello, World!"

# Get the characters from position 2 to position 5 (not included)
print(b[2:5])  # Output: "llo"

# Slice From the Start
''' 
If you omit the start index, the slice will begin from the first character (index 0).
'''

# Get the characters from the start to position 5 (not included)
print(b[:5])  # Output: "Hello"

# Slice To the End
''' 
If you omit the end index, the slice will go until the end of the string.
'''

# Get the characters from position 2, and all the way to the end
print(b[2:])  # Output: "llo, World!"

# Negative Indexing
''' 
Negative indexes allow you to start counting from the end of the string.
'''

# Get the characters from "o" (position -5) to "d" (position -2)
print(b[-5:-2])  # Output: "orl"
