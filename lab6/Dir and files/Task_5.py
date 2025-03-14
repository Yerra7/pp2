def write_list_to_file(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(str(item) + "\n")

write_list_to_file("output.txt", [1, 2, 3, "Hello"])
