import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()

def camel_to_snake(camel_str):
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", camel_str).lower()

camel_words = re.findall(r"\b[A-Z][a-z]+\w*\b", data)  # Find CamelCase words
converted = [camel_to_snake(word) for word in camel_words]
print(converted)
