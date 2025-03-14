def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Uppercase Letters:", upper)
    print("Lowercase Letters:", lower)

count_case("Hello World!")
