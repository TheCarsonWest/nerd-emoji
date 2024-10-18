import os

def append_to_files_in_folder(folder_path, string_to_append):
    # Get a list of all files in the specified folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        
        # Open each file in append mode and add the string
        with open(file_path, 'a') as file:
            file.write(string_to_append)

# Example usage
folder_path = "./result/"  # Replace with your folder path
string_to_append = "\n# [[IDS Unit 3]]"  # Replace with your desired string

append_to_files_in_folder(folder_path, string_to_append)

