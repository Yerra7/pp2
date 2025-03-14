import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()

def snake_to_camel(snake_str):
    return ''.join(word.capitalize() for word in snake_str.split('_'))

snake_words = re.findall(r"\b[a-z]+_[a-z]+\b", data)
converted = [snake_to_camel(word) for word in snake_words]
print(converted)
