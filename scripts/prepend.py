def prepend_filename_to_markdown(file_path):
    """Prepends the name of the Markdown file to its text.

    Args:
        file_path: The path to the Markdown file.
    """

    with open(file_path, 'r') as f:
        text = f.read()

    file_name = os.path.basename(file_path)
    prepended_text = f"---\ntitle: {file_name}\n---\n\n{text}"

    with open(file_path, 'w') as f:
        f.write(prepended_text)




folder_path = './nerd-emoji/python1/'  # Specify your folder path here
prepend_filename_to_markdown(folder_path)