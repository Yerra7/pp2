import re

with open(r"C:\Users\Acer Nitro 5\Desktop\pp 2\lab5\row.txt") as file:
    data = file.read()

pattern = r"([a-z])([A-Z])"
modified_data = re.sub(pattern, r"\1 \2", data)
print(modified_data)
