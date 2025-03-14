def count_lines(filename):
    with open(filename, "r") as file:
        print("Number of lines:", sum(1 for line in file))

count_lines("example.txt")
