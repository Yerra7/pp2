import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()

pattern = r"[A-Z][a-z]+"
matches = re.findall(pattern, data)
print(matches)
