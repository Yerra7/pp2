import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()

pattern = r"(?=[A-Z])"
split_data = re.split(pattern, data)
print(split_data)
