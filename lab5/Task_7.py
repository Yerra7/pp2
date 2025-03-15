import re

with open(r"C:\Users\Acer Nitro 5\Desktop\pp 2\lab5\row.txt") as file:
    data = file.read()

def snake_to_camel(snake_str):
    return ''.join(word.capitalize() for word in snake_str.split('_'))

snake_words = re.findall(r"\b[a-z]+_[a-z]+\b", data)
converted = [snake_to_camel(word) for word in snake_words]
print(converted)
