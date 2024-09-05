import os
from time import sleep
import google.generativeai as genai

genai.configure(api_key=open('api.txt','r').readline())
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
        * **Who:** (key individuals BY NAME IF POSSIBLE involved or affected)
        * **What:** (main events, actions, or concepts)
        * **Impact:** (significance, short term and long-term consequences)

        **Example:**
ID: Headright System
When: 1618
Who: Sir Edwin Sandys of the Virginia Company (Virginia, Carolinas, Maryland, Georgia)
What: A legal practice in the Americas during European colonization that granted land to settlers in exchange for helping to populate the colonies
Impact: The system led to the expansion of population in the 13 Colonies but also increased indentured servitude as well as a wealthy planter society and continued conflicts with Native Americans over land
        """
        
        # Generate the text using the prompt
        response = ai_text(prompt)

        # Write the generated text to the file
        with open(file_name, 'w') as file:
            file.write(response)
            print('created '+file_name)
        sleep(1)

""" 
              "Headright System",
"House of Burgesses",
"Indentured Servitude",
"Puritans",
"Mayflower Compact",
"Pequot War",
"King Philip’s War",
"Bacon’s Rebellion",
"Enlightenment",
"Great Awakening",
"French and Indian War",
"Proclamation of 1763",
"Salutary Neglect",
"Sugar Act",
"Stamp Act",
"Sons of Liberty",
"Townshend Act",
"Letters from a Farmer in Pennsylvania",
"Committees of Correspondence",
"Boston Massacre",
"Tea Act",      
"Boston Tea Party",
"Coercive or Intolerable Acts",
"First Continental Congress",
"Olive Branch Petition",
"Second Continental Congress",
"Common Sense",
"Lee’s Resolution",
"Battle of Bunker Hill",
"Valley Forge",
"The Wealth of Nations",
"Battle of Yorktown",
"Stono Rebellion",

              """
file_names = [
"Triangular Trade",
"Albany Plan of Union",
"Battle of Saratoga",
"Treaty of Paris"]
file_extension = "md"  # Change to your desired file type

create_files(file_names, file_extension)

