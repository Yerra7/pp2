import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()

pattern = r"[ ,.]"
modified_data = re.sub(pattern, ":", data)
print(modified_data)
