import os

import google.generativeai as genai

genai.configure(api_key='AIzaSyA3l1_jbgsLdQ8dJ4HzRYKXUSlsGSmtqRk')
model = genai.GenerativeModel("gemini-pro")

def ai_text(p):
    return model.generate_content(p).text
def create_files(file_names, file_extension):
    for name in file_names:
        # Construct the file name with the given extension
        file_name = f"{name}.{file_extension}"

        # Generate the prompt with clear instructions and context
        prompt = f"""
        **Prompt:** Create a concise notecard summary on the topic of "{name}". Include the following information:

        * **When:** (exact date if possible, otherwise narrow it down to a specific time period)
        * **Who:** (key individuals involved or affected)
        * **What:** (main events, actions, or concepts)
        * **Impact:** (significance and long-term consequences)

        **Example:**

        **Topic:** French and Indian War

        **When:** 1754-1763

        **Who:** British, French, Native American tribes

        **What:** A series of battles between Britain and France over control of North America.

        **Impact:** Britain gained control of most of North America, leading to increased tensions with the American colonies and contributing to the American Revolution.
        """

        # Generate the text using the prompt
        response = ai_text(prompt)

        # Write the generated text to the file
        with open(file_name, 'w') as file:
            file.write(response)

# Example usage
file_names = [
    "Lee’s Resolution",
    "Battle of Bunker Hill",
    "Valley Forge",
    "The Wealth of Nations",
    "Battle of Yorktown",
    "Stono Rebellion",
    "Triangular Trade",
    "Albany Plan of Union",
    "Battle of Saratoga",
    "Treaty of Paris 1776"
]
file_extension = "md"  # Change to your desired file type

create_files(file_names, file_extension)
[[IDs unit 2]]
#ids