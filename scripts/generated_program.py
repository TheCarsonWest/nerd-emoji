def transform_file(input_filename, output_filename, word_to_replace, replacement_word):
    """Replaces a word in a file and saves it to a new file."""
    try:
        with open(input_filename, 'r') as infile:
            file_content = infile.read()
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        return

    transformed_content = file_content.replace(word_to_replace, replacement_word)

    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(transformed_content)
    except Exception as e:
        print(f"Error writing to file: {e}")
        return

transform_file('kittens.md', 'kittens.md_transformed.md', 'kittens', 'dogs')