import os

# Function to replace a string in a file
def replace_string_in_file(file_path, search_string, replace_string):
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace all occurrences of the search string
    new_content = content.replace(search_string, replace_string)

    # If there was a change, write the new content back to the file
    if content != new_content:
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"Updated: {file_path}")

# Function to iterate through all files in a folder, only process .md files
def replace_string_in_folder(folder_path, search_string, replace_string):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Only process .md files
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                replace_string_in_file(file_path, search_string, replace_string)

if __name__ == '__main__':
    folder_paths = ['./nerd-emoji/apush/']
    search_string = "president of the [[United States]]"
    replace_string = '[[President of the United States]]'

    for folder_path in folder_paths:
        replace_string_in_folder(folder_path, search_string, replace_string)
