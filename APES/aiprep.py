import os


def append_to_markdown(folder_path, string_to_append):
  """Appends a string with filename to the bottom of every markdown file in a folder, clearing the file first.

  Args:
    folder_path: The path to the folder containing the markdown files.
    string_to_append: The string template to append to the bottom of each file.
  """
  for filename in os.listdir(folder_path):
    if filename.endswith(".md"):
      file_path = os.path.join(folder_path, filename)
      with open(file_path, "w") as file:  # Open in write mode to clear content
        # Add filename to the string
        complete_string = string_to_append.format(filename[:-3])  # Remove extension
        file.write(complete_string)

      print(f"Cleared content and appended string to {filename} in {folder_path}")


# Example usage
folder_paths = ['./LL']
for folder_path in folder_paths:
  string_to_append = f"\n\n# [[Locations and Legislation]]\n\n**Explanation for:** {{}}\n"
  append_to_markdown(folder_path, string_to_append)
