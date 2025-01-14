import subprocess
import sys
from time import sleep
import google.generativeai as genai

genai.configure(api_key=open('api.txt','r').readline())
model = genai.GenerativeModel("gemini-1.5-flash")



def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        print('eror, waiting')
        sleep(5)
        return ai_text(p)

def main():
  # Get arguments
  if len(sys.argv) != 3:
    print("Usage: transform.py <input_file> <transformation_description>")
    return

  input_file = sys.argv[1]
  transformation_description = sys.argv[2]

  # Generate Python program with Gemini
  prompt = f"Write a Python program that takes the file '{input_file}' as input and transforms it according to the description: '{transformation_description}'. The transformed file should be saved as <file name without extension>_transformed.<extension>. Return only the program and make sure it can do the transformations on the first run"
  program_code = ai_text(prompt).replace("```python", "").replace("```", "").strip()

  # Write generated program to a file
  with open("generated_program.py", "w") as f:
    f.write(program_code)

  # Run the generated program
  subprocess.run(["python", "generated_program.py"])

if __name__ == "__main__":
  main()