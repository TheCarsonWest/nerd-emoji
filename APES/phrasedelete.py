def replace_in_file(folder_path, phrase, replacement):
  """Replaces a phrase in all files within a folder.

  Args:
    folder_path: Path to the folder containing the files.
    phrase: The phrase to replace.
    replacement: The replacement string.
  """
  import os

  for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
      # Read file content
      with open(file_path, 'r') as f:
        content = f.read()
      # Replace phrase with new content
      new_content = content.replace(phrase, replacement)
      # Write modified content back to file
      with open(file_path, 'w') as f:
        f.write(new_content)
        print(f"Modified file: {filename}")

folders = ["./u1/","./u2/","./u3/","./u4/","./u5/","./u6/","./u7/","./u8/","./u9/"]
# Example usage
for folder_path in folders:  # Replace with your actual folder path
    phrase_to_replace = "Write a shortish, clear, and concise summarization as notes"
    replacement_text = ""  # Replace with empty string to delete

    replace_in_file(folder_path, phrase_to_replace, replacement_text)
