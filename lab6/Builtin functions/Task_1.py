from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

print(multiply_list([1, 2, 3, 4, 5]))  # Output: 120
