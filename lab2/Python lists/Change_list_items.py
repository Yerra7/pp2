# Changing a single item in a list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)  # ['apple', 'blackcurrant', 'cherry']

# Changing a range of items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# Replacing one item with multiple new values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'cherry']

# Replacing multiple items with a single value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)  # ['apple', 'watermelon']

# Inserting an item without replacing anything
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)  # ['apple', 'banana', 'watermelon', 'cherry']
