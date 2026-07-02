import os

def list_directory_contents(path="Python clases"):
    try:
        contents = os.listdir(path)
        print(f"\nContents of directory: {os.path.abspath(path)}")
        print("-" * 40)

        for item in sorted(contents):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f"  [DIR]  {item}")
            else:
                print(f"  [FILE] {item}")

        print("-" * 40)
        print(f"Total items: {len(contents)}")

    except FileNotFoundError:
        print(f"Error: Directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")

# --- Run it ---
list_directory_contents(".")          # current directory
# list_directory_contents("/your/path") # or specify a path