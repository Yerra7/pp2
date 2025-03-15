import re

with open(r"C:\Users\Acer Nitro 5\Desktop\pp 2\lab5\row.txt") as file:
    data = file.read()

pattern = r"(?=[A-Z])"
split_data = re.split(pattern, data)
print(split_data)
