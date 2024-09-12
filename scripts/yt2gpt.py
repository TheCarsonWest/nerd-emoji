from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import time


# Import for Generative AI (if still using `generativeai`)
# import google.generativeai as genai
# import requests  # This import might already be present

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

genai.configure(api_key=open('api.txt','r').readline())
model = genai.GenerativeModel("gemini-pro")


def ai_text(p):
    return model.generate_content(p).text


# Get user input for video ID
video_id = input("Enter the YouTube video ID: ")

# Retrieve transcript without timestamps
transcript = get_transcript_without_timestamps(video_id)

if transcript:
  # Prepare the prompt for text generation
  prompt = transcript + "\n\n Turn this ENTIRE transcript into a readable article using markdown formatting."

  # Generate text using your chosen library (replace `ai_text` if needed)
  article_text = ai_text(prompt)

  # Write the generated article to a file (modify filename if needed)
  if article_text:
      with open(f"{time.time()}.md", 'w') as f:
          f.write(f"https://www.youtube.com/watch?v={video_id}\n\n"+article_text)
          print("Article written")
  else:
      print("Text generation failed.")
else:
  print("Transcript could not be retrieved.")