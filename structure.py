import os

def print_directory_structure(path, exclude_dirs=None, indent=0):
    if exclude_dirs is None:
        exclude_dirs = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if item in exclude_dirs:
                continue
            print("  " * indent + f"- {item}/")
            print_directory_structure(item_path, exclude_dirs, indent + 1)
        else:
            print("  " * indent + f"- {item}")

# Ganti '.' dengan path folder Anda
print_directory_structure(".", exclude_dirs=[".venv"])