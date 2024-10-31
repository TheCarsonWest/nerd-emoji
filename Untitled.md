```python
import os
import time
import google.generativeai as genai

genai.configure(api_key=open('/Users/carson/Desktop/nerd-emoji/api.txt','r').readline())
model = genai.GenerativeModel("gemini-1.5-flash")

def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        time.sleep(5)
        print('eror, waiting')
        return ai_text(p)

def file_file_prompt(body_file, prompt_file):
  """
  Reads the content of two files, combines them, and writes the result to a new file.

  Args:
    body_file: The path to the file containing the body text.
    prompt_file: The path to the file containing the prompt text.
  """

  # Check if files exist
  if not os.path.exists(body_file):
    raise FileNotFoundError(f"File not found: {body_file}")
  if not os.path.exists(prompt_file):
    raise FileNotFoundError(f"File not found: {prompt_file}")

  # Read the content of both files
  with open(body_file, 'r') as body_f, open(prompt_file, 'r') as prompt_f:
    body_text = body_f.read()
    prompt_text = prompt_f.read()

  # Combine the content
  combined_text = body_text + "\n\n" + prompt_text

  # Generate a unique filename using the current timestamp
  timestamp = str(time.time()).replace('.', '_')
  output_filename = f"/Users/carson/Desktop/nerd-emoji/nerd-emoji/voice-ai-test/combined_{timestamp}.md"

  # Write the combined text to the new file
  with open(output_filename, 'w') as output_f:
    output_f.write(ai_text(combined_text))

  print(f"Combined text written to: {output_filename}")

body = '/Users/carson/Desktop/nerd-emoji/notes.txt'
prompt = '/Users/carson/Desktop/nerd-emoji/p.txt'
file_file_prompt(body,prompt)
```
how do i get this program to analyze pdfs with gemeni

You're right! The current code is designed to work with text files. To analyze PDFs with Gemini, you need to extract the text from the PDF first. Here's how you can modify your code to handle PDFs:

```python
import os
import time
import google.generativeai as genai
import PyPDF2  # Install PyPDF2: pip install PyPDF2

genai.configure(api_key=open('/Users/carson/Desktop/nerd-emoji/api.txt','r').readline())
model = genai.GenerativeModel("gemini-1.5-flash")

def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        time.sleep(5)
        print('eror, waiting')
        return ai_text(p)

def pdf_file_prompt(pdf_file, prompt_file):
  """
  Reads text from a PDF, combines it with the prompt, and sends it to Gemini.

  Args:
    pdf_file: The path to the PDF file.
    prompt_file: The path to the file containing the prompt text.
  """

  # Check if files exist
  if not os.path.exists(pdf_file):
    raise FileNotFoundError(f"File not found: {pdf_file}")
  if not os.path.exists(prompt_file):
    raise FileNotFoundError(f"File not found: {prompt_file}")

  # Extract text from the PDF
  with open(pdf_file, 'rb') as pdf_f:
    pdf_reader = PyPDF2.PdfReader(pdf_f)
    pdf_text = ''
    for page in range(len(pdf_reader.pages)):
      pdf_text += pdf_reader.pages[page].extract_text()

  # Read the prompt
  with open(prompt_file, 'r') as prompt_f:
    prompt_text = prompt_f.read()

  # Combine the content
  combined_text = pdf_text + "\n\n" + prompt_text

  # Generate a unique filename using the current timestamp
  timestamp = str(time.time()).replace('.', '_')
  output_filename = f"/Users/carson/Desktop/nerd-emoji/nerd-emoji/voice-ai-test/combined_{timestamp}.md"

  # Write the combined text to the new file
  with open(output_filename, 'w') as output_f:
    output_f.write(ai_text(combined_text))

  print(f"Combined text written to: {output_filename}")

# Example usage
pdf_file = '/path/to/your/pdf.pdf'  # Replace with your PDF path
prompt_file = '/Users/carson/Desktop/nerd-emoji/p.txt'
pdf_file_prompt(pdf_file, prompt_file)
```

**Explanation:**

1. **Install PyPDF2:**  Use `pip install PyPDF2` to install the library for reading PDFs.
2. **Import PyPDF2:** Add `import PyPDF2` at the top of your script.
3. **`pdf_file_prompt` function:**
   - This function takes the PDF file path and prompt file path as arguments.
   - It reads the PDF using `PyPDF2.PdfReader` and extracts text from all pages.
   - It then combines the extracted PDF text with the prompt text.
   - Finally, it writes the combined text to a new file after processing by Gemini.

**To use the code:**

1. **Replace `'/path/to/your/pdf.pdf'`** with the actual path to your PDF file.
2. **Make sure your prompt file (`/Users/carson/Desktop/nerd-emoji/p.txt`) is correctly set.**
3. **Run the script.**

This code will now extract text from your PDF, combine it with the prompt, and use Gemini to generate content based on the combined text. 
