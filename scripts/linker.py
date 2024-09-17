import os
from time import sleep
import google.generativeai as genai


folder_path = "./nerd-emoji/python1/"
files = os.listdir(folder_path)
genai.configure(api_key=open('./nerd-emoji/scripts/api.txt','r').readline())
model = genai.GenerativeModel("gemini-pro")
file_text = ''
for file in files:
    # Append the file name to the result string, followed by a newline character
    file_text += file + "\n"
def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        sleep(5)
        print('eror, waiting')
        return ai_text(p)

for x in files: 
    file = open(folder_path+x, 'r')
    txt = file.read()
    prompt = "you are reading "+x+", here is the text inside of it\n"+txt+"**Task:** recreate the this markdown file exactly, but whenever one of these topics is mentioned, put two brackets around it, and make sure it matches one of the list of the other topics in the folder. Here are the list of topics in the folder:\n"+file_text+" \n example: if there is a file named cheeseburgers.md, and in the text there is the word cheeseburger, turn it into [[cheeseburgers]].\n DO NOT SIMPLY PUT ALL OF THE TOPICS AT THE BOTTOM\nDO NOT COPY THE .md WHEN BRACKETING\nDO NOT FORGOT THE UNDERSCORES IN THE BRACKETS\nIF SOMETHING IS NOT EXACTLY IN THE FILE TREE, DO NOT BRACKET IT. IF SOMETHING THAT IS NOT IN THE FILE TREE IS BRACKETTED, UNBRACKET IT.\n DO NOT MAKE NESTED BRACKETS\nPUT TWO(2) BRACKETS AROUND THE TOPICS"
    f = ai_text(prompt)
    file.close()
    file = open(folder_path+x, 'w')
    file.write(f)
    print('wrote to '+x)