import re

with open(r"C:\Users\Acer Nitro 5\Desktop\pp 2\lab5\row.txt") as file:
    data = file.read()

pattern = r"[ ,.]"
modified_data = re.sub(pattern, ":", data)
print(modified_data)
