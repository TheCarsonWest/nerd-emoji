import os
from collections import Counter
import re
import csv

def is_name(word):
    """
    Simple heuristic to check if a word is likely a name.
    Names are assumed to be capitalized words.
    """
    return word[0].isupper() and word[1:].islower()

def process_file(file_path):
    """
    Reads a file and returns a list of words that may be names.
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        words = re.findall(r'\b\w+\b', text)  # Extract words using regex
        names = [word for word in words if is_name(word)]
    return names

def process_folder(folder_path):
    """
    Walks through a folder and its subfolders, processing each file.
    Returns a Counter object with name frequencies.
    """
    name_counter = Counter()
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                names = process_file(file_path)
                name_counter.update(names)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
    
    return name_counter

def write_csv(counter, output_file):
    """
    Writes the counter of names and their frequencies to a CSV file.
    """
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Count'])  # Header
        for name, count in counter.most_common():
            writer.writerow([name, count])

if __name__ == "__main__":
    folder_path = './nerd-emoji/'
    output_file = "name_frequencies.csv"
    
    # Process the folder
    name_frequencies = process_folder(folder_path)
    
    # Write to CSV
    write_csv(name_frequencies, output_file)
    
    print(f"CSV file with name frequencies saved as {output_file}")