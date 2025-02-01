# Python Lists
"""
Lists are used to store multiple items in a single variable.
They are ordered, changeable, and allow duplicate values.
"""

# Creating a List
mylist = ["apple", "banana", "cherry"]
print(mylist)  # Output: ['apple', 'banana', 'cherry']

# Lists allow duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'apple', 'cherry']

# Checking List Length
print(len(mylist))  # Output: 3

# Lists can contain different data types
list1 = ["apple", "banana", "cherry"]  # Strings
list2 = [1, 5, 7, 9, 3]               # Integers
list3 = [True, False, False]          # Booleans
list4 = ["abc", 34, True, 40, "male"]  # Mixed data types
print(list4)  # Output: ['abc', 34, True, 40, 'male']

# Checking the type of a list
print(type(mylist))  # Output: <class 'list'>

# Creating a list using the list() constructor
thislist = list(("apple", "banana", "cherry"))  # Note the double round brackets
print(thislist)  # Output: ['apple', 'banana', 'cherry']

# Lists are ordered: The order of elements does not change unless modified
ordered_list = ["first", "second", "third"]
print(ordered_list[0])  # Output: first

# Lists are changeable: Modifying an element
ordered_list[1] = "modified"
print(ordered_list)  # Output: ['first', 'modified', 'third']

# Adding items to a list
ordered_list.append("new item")
print(ordered_list)  # Output: ['first', 'modified', 'third', 'new item']

# Removing items from a list
ordered_list.remove("modified")
print(ordered_list)  # Output: ['first', 'third', 'new item']

# Using a loop to iterate through a list
for item in mylist:
    print(item)

# Checking if an item exists in a list
if "banana" in mylist:
    print("Banana is in the list!")  # Output: Banana is in the list!

# Python Collections Overview:
"""
List: Ordered, changeable, allows duplicates.
Tuple: Ordered, unchangeable, allows duplicates.
Set: Unordered, unchangeable (but items can be removed/added), no duplicates.
Dictionary: Ordered (since Python 3.7), changeable, no duplicates.
"""
