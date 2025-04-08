from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import time
import sys
import os
import re
# Import for Generative AI (if still using `generativeai`)
# import google.generativeai as genai
# import requests  # This import might already be present

def keep_letters_regex(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)
  
def get_transcript_without_timestamps(video_id):
  """Retrieves the transcript of a YouTube video without timestamps.

  Args:
    video_id (str): The YouTube video ID.

  Returns:
    str: The transcript of the video without timestamps, or None if it could not be retrieved.
  """

  try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
  except YouTubeTranscriptApi.NoTranscriptFound:
    print("No transcript found for video ID:", video_id)
    return None

  text_transcript = ""
  for segment in transcript:
    text_transcript += segment["text"] + " "

  return text_transcript

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def ai_text(p):
    try:
        return model.generate_content(p).text
    except Exception as e:
        time.sleep(5)
        print(e)
        return ai_text(p)


# Get user input for video ID
#video_id = input("Enter the YouTube video ID: ")
video_id = sys.argv[1] if len(sys.argv) > 1 else input("Enter the YouTube video ID: ")



# Retrieve transcript without timestamps
transcript = get_transcript_without_timestamps(video_id)

if transcript:
  # Prepare the prompt for text generation
  prompt = transcript + """\nRewrite the transcript above into paragraphs
  """
  extra_instruction = """\n\n
  Also, make sure that the first line of your reponse is an article name for what is being discussed in the transcript. it will be used as file name. Do not put any additional text other than the title in the first line. Do not use special chracters in the title.
  """
  # Generate text using your chosen library (replace `ai_text` if needed)
  article_text = ai_text(prompt + extra_instruction)

  # Write the generated article to a file (modify filename if needed)
  if article_text:
      lines = article_text.split("\n", 1)
      title = keep_letters_regex(lines[0].strip()) + ".md"
      content = lines[1] if len(lines) > 1 else ""
      with open(title, 'w') as f:
          f.write(f"https://www.youtube.com/watch?v={video_id}\n\n" + content)
          print(f"{title} written")
  else:
      print("Text generation failed.")
else:
  print("Transcript could not be retrieved.")