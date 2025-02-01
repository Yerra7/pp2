
"""
Python - Access Tuple Items
"""
#-----------------------------------------------------
thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[1])
#-----------------------------------------------------
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#-----------------------------------------------------
thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple2[2:5])
#-----------------------------------------------------
thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple3[:4])
#-----------------------------------------------------
thistuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple4[2:])
#-----------------------------------------------------
thistuple5 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple5[-4:-1])
#-----------------------------------------------------
thistuple6 = ("apple", "banana", "cherry")
if "apple" in thistuple6:
  print("Yes, 'apple' is in the fruits tuple")
#-----------------------------------------------------
