import os
import time
from google import genai
from google.genai import types

client = genai.Client(api_key=open('api.txt', 'r').read())

def ai_text(p, think=-1):
    """Generate text using Gemini API with retry logic."""
    try:
        if think > 1:
            result = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=p,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(thinking_budget=think)
                    # Turn off thinking:
                    # thinking_config=types.ThinkingConfig(thinking_budget=0)
                    # Turn on dynamic thinking:
                    # thinking_config=types.ThinkingConfig(thinking_budget=-1)
                ),
            )
        else:
            result = client.models.generate_content(contents=p,model="gemini-2.5-flash")
        # Check for NoneType result
        if result is None or getattr(result, "text", None) is None:
            print('Received None from Gemini API, retrying...')
            time.sleep(5)
            return ai_text(p, think)
        return result.text
    except Exception as e:
        print(f'Error in ai_text: {e}')
        time.sleep(5)
        return ai_text(p, think)

def create_files(file_names, file_extension):
    i = 1
    for name in file_names:
        # Construct the file name with the given extension
        print(name)
        fixed_name = name.split(":")[1]
        file_name = f"{fixed_name}.{file_extension}"

        # Generate the prompt with clear instructions and context

        # Generate the text using the prompt
        
        prompt = f"""
Make a AP Physics note page on topic {name} in markdown format:
- make use of headings
- You can use the markdown table format when writing tables.
- Keep it around 300-600 words.
- use the LaTeX equation library format when writing equations.($$Two dollar signs for a block equation$$, $One dollar sign for an inline equation$
- For any topic that you believe needs its own independent explanation, enclose it in TWO brackets([[like this]]). The notes page for that will be generated solely off of its title, so make sure its specific enough.
- There are already several notes pages on AP Statistics that you can link to. If you want to link to one of those pages, enclose the title in TWO brackets([[like this]]).
- Here is a list of all the existing notes pages you can link to:
 {", ".join([x.split(":")[1] for x in open("topics.txt", "r").readlines()])}
        """
        response =f"# [[AP Physics Home]]"+ai_text(prompt,300) 


        # Write the generated text to the file
        with open("./result/"+file_name.split(" - ")[0], 'w') as file:
            file.write(response)
            print('created '+file_name.split(" - ")[0])
        time.sleep(1)
        i += 1

file_names = open("topics.txt", "r").read().splitlines()
file_extension = "md"  # Change to your desired file type

create_files(file_names, file_extension)

