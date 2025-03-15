import re

with open(r"C:\Users\Acer Nitro 5\Desktop\pp 2\lab5\row.txt") as file:
    data = file.read()

pattern = r"\b[a-z]+_[a-z]+\b"
matches = re.findall(pattern, data)
print(matches)
