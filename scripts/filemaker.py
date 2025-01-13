import os
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

def create_files(file_names, file_extension):
    i = 1
    for name in file_names:
        # Construct the file name with the given extension
        file_name = f"{name}.{file_extension}"

        # Generate the prompt with clear instructions and context
        prompt = f"""
Create a notecard on the APUSH gilded age topic {file_name}, using this following format:
WHEN: (exact date if possible, if not narrow it down to a specific time period...acts/laws, specific events, etc should have specific dates. AP exam questions are ALWAYS broken down into certain time frames; timelines will be very important)
Here is a good example
## ID: Battle of Gettysburg

## When: July 1-3, 1863

## Who: 
* **Union:**  General George Meade and the Army of the Potomac
* **Confederate:** General Robert E. Lee and the Army of Northern [[Virginia]]

## What: 
A pivotal battle of the American Civil War fought in Gettysburg, [[Pennsylvania]]. It involved three days of intense fighting between Union and Confederate forces. The battle culminated in a decisive Union victory, marking a turning point in the war.

## Impact: Why Significant?: 
* **Turning Point:**  The Battle of Gettysburg marked the beginning of the end for the Confederacy. It crippled Lee's army and forced him to retreat back to [[Virginia]].
* **Union Momentum:** The victory boosted Union morale and strengthened the resolve to continue the war.
* **Increased Casualties:** Both sides suffered significant casualties, highlighting the immense human cost of the war.
* **Lincoln's [[Gettysburg Address]]:** Delivered on November 19, 1863, Lincoln's famous speech redefined the purpose of the war as a fight for freedom and equality, solidifying the importance of the Union victory.
* **Strategic Significance:** Gettysburg stopped Lee's invasion of the North, preventing a major victory for the Confederates and ultimately leading to the Union's success.

"""
        # Generate the text using the prompt
        response = ai_text(prompt)+"\n# [[IDS Unit 5]]"

        # Write the generated text to the file
        with open("./result/"+file_name, 'w') as file:
            file.write(response)
            print('created '+file_name)
        sleep(1)
        i += 1

file_names = open("topics.txt", "r").read().splitlines()
file_extension = "md"  # Change to your desired file type

create_files(file_names, file_extension)

 