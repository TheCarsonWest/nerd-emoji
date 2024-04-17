
import os

def rename_sequentially(folder_path):
  """Renames all files in a folder sequentially based on alphabetical order.

  Args:
    folder_path: The path to the folder containing the files to rename.
  """
  counter = 1
  for filename in sorted(os.listdir(folder_path)):
    # Get the file extension (if any)
    extension = os.path.splitext(filename)[1]
    # Construct the new filename with sequential number and extension
    new_filename = f"{counter}{extension}"
    # Build the full paths for old and new files
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_filename)
    # Rename the file
    os.rename(old_path, new_path)
    counter += 1

# Example usage
folder_paths = ["./u3/","./u4/","./u5/","./u6/","./u7/","./u8/","./u9/"]  # Replace with the desired folder path
folder_paths = ['./u9/']
for folder_path in folder_paths:
  rename_sequentially(folder_path)

  print("Files renamed sequentially in", folder_path)
