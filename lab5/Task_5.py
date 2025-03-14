import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()

pattern = r"a.*b$"
matches = re.findall(pattern, data, re.MULTILINE)  # Multi-line mode to check each line
print(matches)
