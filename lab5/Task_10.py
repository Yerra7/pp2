import re

with open(r"C:\Users\Acer Nitro 5\Desktop\pp 2\lab5\row.txt") as file:
    data = file.read()

def camel_to_snake(camel_str):
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", camel_str).lower()

camel_words = re.findall(r"\b[A-Z][a-z]+\w*\b", data)
converted = [camel_to_snake(word) for word in camel_words]
print(converted)
