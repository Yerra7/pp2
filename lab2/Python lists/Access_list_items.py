# Python - Access List Items

# Accessing Items by Index
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # Output: banana (index starts at 0)

# Negative Indexing
print(thislist[-1])  # Output: cherry (last item)

# Range of Indexes (returns a sublist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # Output: ['cherry', 'orange', 'kiwi']

# Leaving out the start index (starts from the beginning)
print(thislist[:4])  # Output: ['apple', 'banana', 'cherry', 'orange']

# Leaving out the end index (goes till the end)
print(thislist[2:])  # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# Range of Negative Indexes (starts from the end)
print(thislist[-4:-1])  # Output: ['orange', 'kiwi', 'melon']

# Checking if an item exists in the list
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")  # Output: Yes, 'apple' is in the fruits list
