import os
from time import sleep
import google.generativeai as genai

genai.configure(api_key=open('api.txt','r').readline())
model = genai.GenerativeModel("gemini-pro")

def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        sleep(5)
        print('eror, waiting')
        return ai_text(p)

def create_files(file_names, file_extension):
    for name in file_names:
        # Construct the file name with the given extension
        file_name = f"{name}.{file_extension}"

        # Generate the prompt with clear instructions and context
        prompt = f"""
        Create a detailed and structured notes page on the topic of Python {name}. Include:
    - An explanation of what it is
    - Various parameters is may have
    - Code exmaples of how to use it
    - other python concepts that link back to this one
        
        """
        
        # Generate the text using the prompt
        response = ai_text(prompt)

        # Write the generated text to the file
        with open(file_name, 'w') as file:
            file.write(response)
            print('created '+file_name)
        sleep(1)

file_names = [
    "Variables_and_Data_Types",
    "Operators",
    "Control_Flow_If_Statements",
    "For_Loops",
    "While_Loops",
    "Functions",
    "Function_Parameters",
    "Return_Values",
    "Default_Parameters",
    "Recursion",
    "Lambda_Functions",
    "Lists",
    "Tuples",
    "Dictionaries",
    "Sets",
    "List_Comprehension",
    "File_Handling",
    "Exception_Handling",
    "Classes_and_Objects",
    "Inheritance",
    "Polymorphism",
    "Encapsulation",
    "Modules_and_Packages",
    "Importing_Modules",
    "Generators",
    "Decorators",
    "Context_Managers",
    "Regular_Expressions",
    "Libraries_like_NumPy",
    "Libraries_like_Pandas",
    "Libraries_like_Matplotlib"
]
file_extension = "md"  # Change to your desired file type

create_files(file_names, file_extension)

 