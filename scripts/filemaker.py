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
Create a notecard on the APUSH topic {file_name}, using this following format:
WHEN: (exact date if possible, if not narrow it down to a specific time period...acts/laws, specific events, etc should have specific dates. AP exam questions are ALWAYS broken down into certain time frames; timelines will be very important)

WHO: (who is involved or who started the event or concept; if a person - who is the person, President, Doctor, lawyer, etc. that would be important to know) 

WHAT: (answer what the concept is or what the person did exactly or what happened specifically during an event 

IMPACT:Why is that significant? What did it lead to? What impact did the person or event or law have on the United States?

Here is an example:
# ID: Constitutional Convention
## When: May -September 1787
## Who: 
55 delegates, including James Madison, George W, and Alexander Hamilton (originally 70) from  12 states except for RI
## What:
Meeting held in Philadelphia Pennsylvania, to revise and fix the Articles of Confederation after weaknesses were exposed by Shays Rebellion
## Impact? Why Significant?: 
Decided to set aside the AOC due to its many weaknesses and create a new US Constitution
"""
        # Generate the text using the prompt
        response = ai_text(prompt)

        # Write the generated text to the file
        with open("./result/"+file_name, 'w') as file:
            file.write(response)
            print('created '+file_name)
        sleep(1)
        i += 1

file_names = ["Samuel Slater",
"Market Revolution",
"Industrial Revolution",
"Lowell Textile Mill",
"Cotton Gin",
"Free-soldiers",
"sectionalism",
"Wilmot Proviso",
"Compromise of 1850",
"Fugitive Slave Act",
"Popular Sovereignty(antebellum)",
"Uncle Toms Cabin",
"Kansas Nebraska Act",
"Bleeding Kansas",
"Dred Scott v Sandford",
"New Republican Party 1850",
"Freeport Doctrine",
"Lincoln Douglas Debates",
"Harpers Ferry Raid",
"Election of 1860",
"Fort Sumter",
"Anaconda Plan",
"Battle of Bull Run",
"Habaes Corpus(civil war)",
"Battle of Antietam",
"Emancipation Proclamation",
"Battle of Gettsyburg",
"Gettysburg Address",
"Shermans March to Sea",
"Surrender at Appomattox Courthouse",
"The Assassination of Abraham Lincoln",
"13th amendment",
"14th amendment",
"15th amendment",
"Radical Republicans(reconstruction era)",
"Black Codes(reconstruction era)",
"Civil Rights Act of 1866",
"Reconstruction Act of 1867",
"Scalawag(reconstruction era)",
"Carpetbagger",
"Tenure of Office Act",
"Freedmans Bureau",
"Tenant Farming",
"Sharecroppers(reconstruction)",
"Compromise of 1877",
"Jim Crow Laws(reconstruction)",
"Solid south(reconstruction)"]
file_extension = "md"  # Change to your desired file type

create_files(file_names, file_extension)

 