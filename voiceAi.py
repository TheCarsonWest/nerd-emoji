import speech_recognition as sr
import os
import time
import google.generativeai as genai
import keyboard

genai.configure(api_key=open('api.txt','r').readline())
model = genai.GenerativeModel("gemini-2.0-flash")

def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        time.sleep(5)
        print('eror, waiting')
        return ai_text(p)


# Function to capture speech continuously until a stop phrase is spoken
def continuous_speech_to_text(stop_phrase="end recording"):
    recognizer = sr.Recognizer()
    stop_listening = False
    full_transcription = []
    notes = open("./notes.txt","r")
    with sr.Microphone() as source:
        print("Listening... (say 'end recording' to stop)")

        while not stop_listening:
            try:
                audio = recognizer.listen(source)
                speech_text = recognizer.recognize_google(audio)
                print(f"You said: {speech_text}")
                
                if stop_phrase.lower() in speech_text.lower() or stop_phrase in notes.read():
                    full_transcription.append(speech_text)
                    stop_listening = True
                    print("Stopping recording...")
                else:
                    full_transcription.append(speech_text)                    
            except sr.UnknownValueError:
                print("Sorry, could not understand the audio.")
            except sr.RequestError:
                print("Request error from Google Speech Recognition.")
    
    return " ".join(full_transcription)

# Main workflow
def convert_continuous_speech_to_notes():
    # Step 1: Continuously capture speech until stop phrase is detected
    speech_text = continuous_speech_to_text()

    if speech_text:
        # Step 2: Pass the full transcription to AI to generate notes
        speech_text += '\ncreate highly in depth notes in markdown on this transcript, ignore any "end recording"s or "and recording"s toward the end. The transcript may be talking to you, referring to you as ChatGPT or AI or Gemini, asking you to do something a certain way. If it does this, then follow its instructions. Do not mention the fact that this is from a transcript'
        ai_generated_notes = ai_text(speech_text)

        # Step 3: Display or save notes
        print(ai_generated_notes)
        with open(f'./{time.time()}', 'w') as file:
            file.write(ai_generated_notes)



convert_continuous_speech_to_notes()