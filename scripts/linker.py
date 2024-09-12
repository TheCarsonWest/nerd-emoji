import os
from time import sleep
import google.generativeai as genai

files = os.listdir(folder_path)
genai.configure(api_key=open('api.txt','r').readline())
model = genai.GenerativeModel("gemini-pro")

def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        sleep(5)
        print('eror, waiting')
        return ai_text(p)

