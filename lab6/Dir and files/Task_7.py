import shutil

def copy_file(source, destination):
    shutil.copy(source, destination)
    print(f"Copied {source} to {destination}")

copy_file("example.txt", "copy.txt")
