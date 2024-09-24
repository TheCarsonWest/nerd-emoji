import os
import re

def list_md_files(directory):
    md_files = []
    
    # Traverse through all files in the folder and subfolders
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            # Check if the file has a .md extension
            if filename.endswith(".md"):
                # Get the full file path
                file_path = os.path.join(foldername, filename)
                md_files.append(file_path)
    
    # Return the list of markdown files
    return md_files

def wrap_file_references(files, stripped):
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Iterate over each stripped filename and add brackets around it in the content
        for name in stripped:
            # Use regex to find whole word matches only and replace with [[name]]
            content = re.sub(rf'\b{name}\b', f'[[{name}]]', content)

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Modified: {file_path}")

if __name__ == "__main__":
    directory_path = "./nerd-emoji/"
    
    # Get all .md files in the directory and subdirectories
    md_files = list_md_files(directory_path)
    
    # Create the stripped list containing only the filenames without extension
    stripped = [os.path.basename(f).split('.')[0] for f in md_files]
    
    # Modify the markdown files by wrapping references to stripped filenames
    wrap_file_references(md_files, stripped)