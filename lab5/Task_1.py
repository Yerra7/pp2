import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()

pattern = r"ab*"
matches = re.findall(pattern, data)
print(matches)
