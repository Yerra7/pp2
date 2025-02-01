"""
Python - Remove Dictionary Items
"""
#-----------------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#-----------------------------------------------------
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.popitem()
print(thisdict1)
#-----------------------------------------------------
thisdict12 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict12["model"]
print(thisdict12)
#-----------------------------------------------------
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2.clear()
print(thisdict2)
#-----------------------------------------------------