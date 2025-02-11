import os
import sys

def replace_string_in_file(file_path, search_string, replace_string):
    """Replaces all occurrences of search_string with replace_string in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        new_content = content.replace(search_string, replace_string)

        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def replace_string_in_folder(folder_path, search_string, replace_string):
    """Processes all .md files in a folder and replaces occurrences of search_string."""
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                replace_string_in_file(file_path, search_string, replace_string)

def main():
    if len(sys.argv) != 4:
        print("Usage: replace <file_or_folder> <find_string> <replace_string>")
        sys.exit(1)

    path = sys.argv[1]
    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    if os.path.isfile(path):
        replace_string_in_file(path, search_string, replace_string)
    elif os.path.isdir(path):
        replace_string_in_folder(path, search_string, replace_string)
    else:
        print(f"Error: {path} is neither a file nor a directory.")
        sys.exit(1)

if __name__ == "__main__":
    main()
