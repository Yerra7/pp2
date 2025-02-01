# Python - Loop Lists
'''
You can loop through list items in various ways in Python. 
The most common methods include using a for loop, indexing, a while loop, and list comprehension.
'''

# Loop Through a List
''' 
You can loop through the list items using a for loop. 
This method is the most straightforward.
'''

# Example: Print all items in the list one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)  # Output: apple, banana, cherry

# Loop Through the Index Numbers
''' 
You can also loop through the list items by referring to their index number. 
This requires using the range() and len() functions to create an iterable for the indices.
'''

# Example: Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])  # Output: apple, banana, cherry

# Using a While Loop
''' 
In a while loop, you loop through the list items by using their index numbers.
You start at index 0 and loop through the list by increasing the index after each iteration.
'''

# Example: Print all items using a while loop:
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])  # Output: apple, banana, cherry
    i = i + 1

# Looping Using List Comprehension
''' 
List comprehension offers a concise way to loop through the list items.
This method combines a loop and conditional expression in a single line.
'''

# Example: A shorthand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]  # Output: apple, banana, cherry
