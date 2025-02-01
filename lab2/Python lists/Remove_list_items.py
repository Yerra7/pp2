# Removing List Items in Python

# 1. Using remove() - Removes the first occurrence of a specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # Output: ['apple', 'cherry']

# If the item appears multiple times, only the first occurrence is removed
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)  # Output: ['apple', 'cherry', 'banana', 'kiwi']


# 2. Using pop() - Removes an item at a specific index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # Removes "banana" at index 1
print(thislist)  # Output: ['apple', 'cherry']

# If no index is specified, pop() removes the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  # Output: ['apple', 'banana']


# 3. Using del - Removes an item at a specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]  # Removes "apple" at index 0
print(thislist)  # Output: ['banana', 'cherry']

# Using del to delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist)  # This would cause an error because the list no longer exists


# 4. Using clear() - Empties the list without deleting it
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # Output: []
