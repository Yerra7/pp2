import os
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print(f"Deleted {path}")
    else:
        print(f"Cannot delete {path}: File doesn't exist or no permission")

delete_file("example.txt")
