# Python - Add List Items

# Using append() to add an item at the end
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print("After append:", thislist)  
# Output: ['apple', 'banana', 'cherry', 'orange']

# Using insert() to add an item at a specific index
thislist.insert(1, "orange")
print("After insert:", thislist)  
# Output: ['apple', 'orange', 'banana', 'cherry', 'orange']

# Using extend() to add multiple elements from another list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("After extend with list:", thislist)  
# Output: ['apple', 'orange', 'banana', 'cherry', 'orange', 'mango', 'pineapple', 'papaya']

# Using extend() to add elements from a tuple
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print("After extend with tuple:", thislist)  
# Output: ['apple', 'orange', 'banana', 'cherry', 'orange', 'mango', 'pineapple', 'papaya', 'kiwi', 'orange']
