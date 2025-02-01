"""
Python Sets
"""
#-----------------------------------------------------
myset = {"apple", "banana", "cherry"}
#-----------------------------------------------------
thisset = {"apple", "banana", "cherry"}
print(thisset)
#-----------------------------------------------------
thisset1 = {"apple", "banana", "cherry", "apple"}

print(thisset1)
#-----------------------------------------------------
thisset2 = {"apple", "banana", "cherry", True, 1, 2}

print(thisset2)
#-----------------------------------------------------
thisset3 = {"apple", "banana", "cherry", False, True, 0}

print(thisset3)
#-----------------------------------------------------
thisset4 = {"apple", "banana", "cherry"}

print(len(thisset4))
#-----------------------------------------------------
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#-----------------------------------------------------
set4 = {"abc", 34, True, 40, "male"}
#-----------------------------------------------------
myset1 = {"apple", "banana", "cherry"}
print(type(myset))
#-----------------------------------------------------
thisset1 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset1)
#-----------------------------------------------------