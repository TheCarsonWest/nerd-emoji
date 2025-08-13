import os
from time import sleep
import google.generativeai as genai

genai.configure(api_key=open('api.txt','r').readline())
model = genai.GenerativeModel("gemini-2.0-flash")

def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        print('eror, waiting')
        sleep(5)
        return ai_text(p)

def create_files(file_names, file_extension):
    i = 1
    for name in file_names:
        # Construct the file name with the given extension
        file_name = f"{name}.{file_extension}"

        # Generate the prompt with clear instructions and context

        # Generate the text using the prompt
        
        prompt = f"""
Make a AP Physics I note page on topic {name} in markdown format:
- make use of headings
- use the LaTeX equation library format when writing equations.($$Two dollar signs for a block equation$$, $One dollar sign for an inline equation$
- For any topic that you believe needs its own independent explanation, enclose it in TWO brackets([[like this]]). The notes page for that will be generated solely off of its title, so make sure its specific enough.
        """
        response =ai_text(prompt) 

        # Write the generated text to the file
        with open("./result/"+file_name.split(" - ")[0], 'w') as file:
            file.write(response)
            print('created '+file_name.split(" - ")[0])
        sleep(1)
        i += 1

file_names = open("topics.txt", "r").read().splitlines()
file_extension = "md"  # Change to your desired file type

create_files(file_names, file_extension)

 