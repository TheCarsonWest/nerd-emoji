import os

def append_to_markdown(folder_path, string_to_append):
  """Appends a string to the bottom of every markdown file in a folder.

  Args:
    folder_path: The path to the folder containing the markdown files.
    string_to_append: The string to append to the bottom of each file.
  """
  for filename in os.listdir(folder_path):
    if filename.endswith(".md"):
      file_path = os.path.join(folder_path, filename)
      with open(file_path, "r+") as file:
        content = file.read()
        file.seek(0)  # Rewind back to the beginning of the file
        file.write(content + string_to_append)

# Example usage:
folder_paths = ["./u3/","./u4/","./u5/","./u6/","./u7/","./u8/","./u9/"]  # Replace with the desired folder path
folder_paths = ["./u7/"]
for folder_path in folder_paths:
  string_to_append = f"\n\n[[Unit {folder_path[3]}]]\nWrite a shortish, clear, and concise summarization as notes"
  append_to_markdown(folder_path, string_to_append)

  print("Appended string to all markdown files in", folder_path)
