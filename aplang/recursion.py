import os
from time import sleep
import google.generativeai as genai
import re

genai.configure(api_key=open('api.txt','r').readline())
model = genai.GenerativeModel("gemini-1.5-flash-002")

def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        print('eror, waiting')
        sleep(5)
        return ai_text(p)
    
    
def generate_notes(strings: list, custom_prompt: str, recursion_level: int = 0, generated_files: set = None, backlink = "nexus"):
    """
    Generates notes from a list of strings using an AI, handling recursive note generation.

    Args:
        strings: The list of strings to generate notes for.
        custom_prompt: A custom prompt to include in the AI text generation.
        recursion_level: The current recursion level (default is 0).
        generated_files: A set to keep track of generated filenames to prevent infinite recursion.
    """

    if generated_files is None:
        generated_files = set()

    if recursion_level >= 3:  # Stop recursion at level 3
        return

    for i, string in enumerate(strings):
        prompt = f"{custom_prompt} Full list: {strings}. Current string: {string}"
        notes = ai_text(prompt)

        filename = f"{string}.md"
        with open(filename, "w",encoding='utf-8') as f:
            f.write("# [["+backlink+"]]\n"+notes)

        # Find recursive note triggers ([[...]]).
        recursive_matches = re.findall(r"\[\[(.*?)\]\]", notes)

        for match in recursive_matches:
            filename = f"{match}.txt"
            if filename not in generated_files:
                generated_files.add(filename)
                generate_notes([match], custom_prompt, recursion_level + 1, generated_files,string)
        if recursion_level == 4:
            notes.replace("[[","")
            notes.replace("]]","")





# Example usage
strings = ['AP English Language and Composition', 'Rhetorical Analysis', 'Argumentative Essay', 'Synthesis Essay']

custom_prompt = "You are writing notes for yourself about a topic . Use markdown formatting. Write equations using the LaTeX Equation Library(use $equation$ for an inline equation, and ## $$equation$$ for a block equation). For any topic that you believe needs its own independent explanation, enclose it in TWO brackets([[like this]], make sure they are just short titles for seperate notes), but, there will be a list of preiously written ntoes that can also be linked to in this way, so, either\n - Copy the name of the note EXACTLY\n - Make a link to another note that must be written(please note that those notes will be generated exclusivly off the name of the title). Some notes can follow a template that exclusivly branches off into other topics if it makes sense to. \nYou are to create notes about the Topic: "


generate_notes(strings, custom_prompt)



def list_md_files(directory):
    md_files = []
    
    # Traverse through all files in the folder and subfolders
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            # Check if the file has a .md extension
            if filename.endswith(".md"):
                # Get the full file path
                file_path = os.path.join(foldername, filename)
                md_files.append(file_path)
    
    # Return the list of markdown files
    return md_files

def wrap_file_references(files, stripped):
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Iterate over each stripped filename and add brackets around it in the content
        for name in stripped:
            # Use regex to find whole word matches only and replace with [[name]]
            content = re.sub(rf'\b{name}\b', f'[[{name}]]', content)

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Modified: {file_path}")

if __name__ == "__main__":
    directory_path = "./"
    
    # Get all .md files in the directory and subdirectories
    md_files = list_md_files(directory_path)
    
    # Create the stripped list containing only the filenames without extension
    stripped = [os.path.basename(f).split('.')[0] for f in md_files]
    
    # Modify the markdown files by wrapping references to stripped filenames
    wrap_file_references(md_files, stripped)