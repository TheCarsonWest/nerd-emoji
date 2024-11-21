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
    
    
def generate_notes(strings: list, custom_prompt: str, recursion_level: int = 0, generated_files: set = None, backlink = "Python 1 Home"):
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

    if recursion_level >= 5:  # Stop recursion at level 3
        return

    for i, string in enumerate(strings):
        prompt = f"{custom_prompt} Full list: {strings}. Current string: {string}"
        notes = ai_text(prompt)

        # Find recursive note triggers ([[...]]).
        recursive_matches = re.findall(r"\[\[(.*?)\]\]", notes)

        for match in recursive_matches:
            filename = f"{match}.txt"
            if filename not in generated_files:
                generated_files.add(filename)
                generate_notes([match], custom_prompt, recursion_level + 1, generated_files,string)



        filename = f"{string}.md"
        with open(filename, "w") as f:
            f.write("# [["+backlink+"]]\n"+notes)



# Example usage
strings = ['Solutions']

custom_prompt = "You are writing notes for yourself about a python topic. Use markdown formatting(try to keep as much code as possible within triple backticks). For any topic that you believe needs its own independent explanation, enclose it in TWO brackets([[like this]], make sure they are just short titles for seperate notes), but, there will be a list of preiously written ntoes that can also be linked to in this way, so, either\n - Copy the name of the note EXACTLY\n - Make a link to another note that must be written(please note that those notes will be generated exclusivly off the name of the title). \nYou are to create notes about the python term:"


generate_notes(strings, custom_prompt)