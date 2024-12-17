import os
import re

def process_markdown_files(folder_path):
    """
    Scans a folder and its subfolders for .md files, adding double brackets around filenames
    found within other filenames.

    Args:
        folder_path: The path to the folder to scan.
    """

    md_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))

    filenames = [os.path.splitext(os.path.basename(file))[0] for file in md_files]

    # Prioritize files containing other filenames
    filenames_to_move = []
    for i in range(len(filenames)):
        for j in range(len(filenames)):
            if i != j and filenames[i] in filenames[j]:
                if filenames[i] not in filenames_to_move :  # Avoid duplicates
                    filenames_to_move.append(filenames[i])
    
    for name in filenames_to_move:
        filenames.remove(name)
        filenames.append(name)  # Move to the back
                

    for i, file in enumerate(md_files):
        with open(file, 'r', encoding='utf-8') as f:  # Handle potential encoding issues
            content = f.read()

        new_content = content
        for j, name in enumerate(filenames):
            # Check for exact match with spaces on both sides
            pattern = r"(?<!\[)\[\[?\s*" + re.escape(name) + r"\s*\]?\]?(?!\])"
            if name in new_content and not re.search(pattern, new_content):
                new_content = re.sub(r"\s" + re.escape(name) + r"\s", " [[{}]] ".format(name), new_content)
                #new_content = new_content.replace(" " + name + " ", " [[{}]] ".format(name))

        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)


# Example usage:
folder_path = "./../"  # Replace with the actual path to your folder
process_markdown_files(folder_path) 