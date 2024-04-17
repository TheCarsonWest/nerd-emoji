import os
import re

def split_and_save(filepath):
  """
  Splits the text in a file based on a section number and saves each section in a folder named after the section number.

  Args:
    filepath: Path to the text file.
  """
  filename = os.path.basename(filepath)
  section_number = filename[5]  # Extract section number from 5th character
  print(section_number)
  section_count = 0

  with open(filepath, "r") as f:
    text = f.read()

  # Split text by "<section_number>." (non-greedy)
  sections = re.split(rf"{section_number}.\d", text, flags=re.DOTALL)

  for section in sections:
    section_count += 1
    section_folder = f"u{section_number}"  # Create folder name with "u" prefix
    section_filename = f"{section_number}.{section_count}raw.md"

    # Create folder if it doesn't exist
    if not os.path.exists(section_folder):
      os.makedirs(section_folder)

    filepath = os.path.join(section_folder, section_filename)  # Update filepath with folder
    with open(filepath, "w") as f:
      f.write(section.strip())  # Remove leading/trailing whitespace

if __name__ == "__main__":
  folder_path = "./raw/"  # Replace with your folder path
  for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
      filepath = os.path.join(folder_path, filename)
      split_and_save(filepath)
  print("Finished splitting and saving sections.")
