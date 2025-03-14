import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()

pattern = r"([a-z])([A-Z])"
modified_data = re.sub(pattern, r"\1 \2", data)
print(modified_data)
