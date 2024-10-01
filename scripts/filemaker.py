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
Create an AP United States History rundown on {name}. Include events they were associated with, important legislation they signed, groups they were a part of, and their impact on the country
"""        
        # Generate the text using the prompt
        response = ai_text(prompt)

        # Write the generated text to the file
        with open("./result/"+file_name, 'w') as file:
            file.write(response)
            print('created '+file_name)
        sleep(1)
file_names = ['George Washington',
'John Adams',
'Thomas Jefferson',
'James Madison',
'James Monroe',
'John Quincy Adams',
'Andrew Jackson',
'Martin Van Buren',
'William Henry Harrison',
'John Tyler',
'James K. Polk',
'Zachary Taylor',
'Millard Fillmore',
'Franklin Pierce',
'James Buchanan',
'Abraham Lincoln',
'Andrew Johnson',
'Ulysses S. Grant',
'Rutherford B. Hayes',
'James A. Garfield',
'Chester A. Arthur',
'Grover Cleveland',
'Benjamin Harrison',
'Grover Cleveland',
'William McKinley',
'Theodore Roosevelt',
'William Howard Taft',
'Woodrow Wilson',
'Warren G. Harding',
'Calvin Coolidge',
'Herbert Hoover',
'Franklin D. Roosevelt',
'Harry S. Truman',
'Dwight D. Eisenhower',
'John F. Kennedy',
'Lyndon B. Johnson',
'Richard Nixon',
'Gerald Ford',
'Jimmy Carter',
'Ronald Reagan',
'George H. W. Bush',
'Bill Clinton',
'George W. Bush',
'Barack Obama',
'Donald Trump',
'Joe Biden']

file_extension = "md"  # Change to your desired file type

create_files(file_names, file_extension)

 