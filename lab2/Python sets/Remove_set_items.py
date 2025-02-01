"""
Python - Remove Set Items
"""
#-----------------------------------------------------
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#-----------------------------------------------------
thissetq = {"apple", "banana", "cherry"}

thissetq.discard("banana")

print(thissetq)
#-----------------------------------------------------
thisset1 = {"apple", "banana", "cherry"}

x = thisset1.pop()

print(x)

print(thisset1)
#-----------------------------------------------------
thisset2 = {"apple", "banana", "cherry"}

thisset2.clear()

print(thisset2)
#-----------------------------------------------------
thisset3 = {"apple", "banana", "cherry"}

del thisset3

print(thisset3)
#-----------------------------------------------------