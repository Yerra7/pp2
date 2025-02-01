"""
Python - Join Sets
"""
#-----------------------------------------------------
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#-----------------------------------------------------
set11 = {"a", "b", "c"}
set21 = {1, 2, 3}

set31 = set11 | set21
print(set31)
#-----------------------------------------------------
set12 = {"a", "b", "c"}
set22 = {1, 2, 3}
set32 = {"John", "Elena"}
set42 = {"apple", "bananas", "cherry"}

myset = set1.union(set22, set32, set42)
print(myset)
#-----------------------------------------------------
set1q = {"a", "b", "c"}
set2q = {1, 2, 3}
set3q = {"John", "Elena"}
set4q = {"apple", "bananas", "cherry"}

mysetq = set1q | set2q | set3q |set4q
print(mysetq)
#-----------------------------------------------------
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
#-----------------------------------------------------
set1w = {"a", "b" , "c"}
set2w = {1, 2, 3}

set1w.update(set2w)
print(set1w)
#-----------------------------------------------------
set1a = {"apple", "banana", "cherry"}
set2a = {"google", "microsoft", "apple"}

set3a = set1a.intersection(set2a)
print(set3a)
#-----------------------------------------------------
set1s = {"apple", "banana", "cherry"}
set2s = {"google", "microsoft", "apple"}

set3s = set1s & set2s
print(set3s)
#-----------------------------------------------------
set1e = {"apple", "banana", "cherry"}
set2e = {"google", "microsoft", "apple"}

set1e.intersection_update(set2e)

print(set1e)
#-----------------------------------------------------
set1z = {"apple", 1,  "banana", 0, "cherry"}
set2z = {False, "google", 1, "apple", 2, True}

set3z = set1z.intersection(set2z)

print(set3z)
#-----------------------------------------------------
set1x = {"apple", "banana", "cherry"}
set2x = {"google", "microsoft", "apple"}

set3x = set1x.difference(set2x)

print(set3x)
#-----------------------------------------------------
set13 = {"apple", "banana", "cherry"}
set23 = {"google", "microsoft", "apple"}

set33 = set13 - set23
print(set33)
#-----------------------------------------------------
set1h = {"apple", "banana", "cherry"}
set2h = {"google", "microsoft", "apple"}

set1h.difference_update(set2h)

print(set1h)
#-----------------------------------------------------
set1v = {"apple", "banana", "cherry"}
set2v = {"google", "microsoft", "apple"}

set3v = set1v.symmetric_difference(set2v)

print(set3v)
#-----------------------------------------------------
set1l = {"apple", "banana", "cherry"}
set2l = {"google", "microsoft", "apple"}

set3l = set1l ^ set2l
print(set3l)
#-----------------------------------------------------
set1k = {"apple", "banana", "cherry"}
set2k = {"google", "microsoft", "apple"}

set1k.symmetric_difference_update(set2k)

print(set1k)
#-----------------------------------------------------