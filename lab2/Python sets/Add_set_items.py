"""
Python - Add Set Items
"""
#-----------------------------------------------------
thisset1 = {"apple", "banana", "cherry"}

thisset1.add("orange")

print(thisset1)
#-----------------------------------------------------
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#-----------------------------------------------------
thisset2 = {"apple", "banana", "cherry"}
mylist2 = ["kiwi", "orange"]

thisset2.update(mylist2)

print(thisset2)
#-----------------------------------------------------