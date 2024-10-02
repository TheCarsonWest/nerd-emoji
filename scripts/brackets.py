
import os
import re

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Find all occurrences of words enclosed in double brackets
    bracketed_words = re.findall(r'\[\[.*?\[\]', content)

    # For each bracketed word, ask the user if they want to remove the brackets
    for word in bracketed_words:
        if word not in os.listdir(folder_path).split('.md')[0]:
            print(f"Do you want to remove the brackets around '{word}'? (y/n): ", end='')
            choice = input().strip().lower()
        
        choice = 'y'
        if choice == 'y':
            content = content.replace(f'[[{word}]]', word)

    # Write the changes back to the file
    with open(file_path, 'w') as file:
        file.write(content)

# Function to iterate through all files in a folder
def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.md'):  # Process only text files or modify as needed
                print(f"Processing file: {file_path}")
                process_file(file_path)


folder_path = './nerd-emoji/apush/'
process_folder(folder_path)