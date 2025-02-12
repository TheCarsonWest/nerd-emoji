import os
import sys
import subprocess
from time import sleep
import google.generativeai as genai

# Load API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: GEMINI_API_KEY environment variable is not set.")
    sys.exit(1)

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")  # Or another suitable model

def ai_text(p):
    """Generate text from Gemini AI, with retry on failure."""
    try:
        response = model.generate_content(p)
        # Check if the response contains text before accessing it
        if hasattr(response, 'text'):
            return response.text
        else:
            print("Error: Gemini response does not contain text. Retrying in 5 seconds...")
            sleep(5)
            return ai_text(p)
    except Exception as e:
        print(f"Error: {e}. Retrying in 5 seconds...")
        sleep(5)
        return ai_text(p)


def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <output_file> <prompt_template> <replacement_string>")
        sys.exit(1)

    output_file = sys.argv[1]
    prompt_template = sys.argv[2]
    replacement_string = sys.argv[3]

    # Combine the prompt template and replacement string
    prompt = prompt_template.replace("%%", replacement_string)

    try:
        gemini_output = ai_text(prompt)

        if gemini_output:  # Check if the output is not None or empty
            with open(output_file, "w") as f:
                f.write(gemini_output)
            print(f"Gemini's output written to '{output_file}'")
        else:
            print("Gemini returned no output.")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()