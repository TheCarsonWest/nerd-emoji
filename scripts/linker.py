import os
import re

def process_markdown_files(source_folder, target_folder):
    """
    Creates links to all files in the source folder but only adds brackets around them
    within files in the target folder.

    Args:
        source_folder: The folder containing files to link.
        target_folder: The folder where links should be added.
    """

    # Get all .md files in the source folder
    source_md_files = []
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".md"):
                source_md_files.append(os.path.join(root, file))

    # Get all .md files in the target folder
    target_md_files = []
    for root, _, files in os.walk(target_folder):
        for file in files:
            if file.endswith(".md"):
                target_md_files.append(os.path.join(root, file))

    # Extract filenames (without extensions) from the source folder
    filenames = [os.path.splitext(os.path.basename(file))[0] for file in source_md_files]

    # Prioritize files containing other filenames
    filenames_to_move = []
    for i in range(len(filenames)):
        for j in range(len(filenames)):
            if i != j and filenames[i] in filenames[j]:
                if filenames[i] not in filenames_to_move:  # Avoid duplicates
                    filenames_to_move.append(filenames[i])

    for name in filenames_to_move:
        filenames.remove(name)
        filenames.append(name)  # Move to the back

    # Process files in the target folder
    for file in target_md_files:
        with open(file, 'r', encoding='utf-8') as f:  # Handle potential encoding issues
            content = f.read()

        new_content = content
        for name in filenames:
            # Check for exact match with spaces on both sides
            pattern = r"(?<!\[)\[\[?\s*" + re.escape(name) + r"\s*\]?\]?(?!\])"
            if name in new_content and not re.search(pattern, new_content):
                new_content = re.sub(r"\s" + re.escape(name) + r"\s", " [[{}]] ".format(name), new_content)

        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)


# Example usage:
source_folder = "./../"  # Replace with the actual path to the source folder
target_folder = "./result/" # Replace with the actual path to the target folder
source_folder,target_folder = target_folder,source_folder
process_markdown_files(source_folder, target_folder)