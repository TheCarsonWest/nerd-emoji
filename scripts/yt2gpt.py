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
model = genai.GenerativeModel("gemini-1.5-flash")


def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        time.sleep(5)
        print('eror, waiting')
        return ai_text(p)


# Get user input for video ID
#video_id = input("Enter the YouTube video ID: ")
video_ids = []



# Retrieve transcript without timestamps
transcript = "\n\nNext video:\n\n".join([get_transcript_without_timestamps(video_id) for video_id in video_ids])

if transcript:
  # Prepare the prompt for text generation
  prompt = transcript + """\nUse these transcripts to do this assignemnt

  """

  # Generate text using your chosen library (replace `ai_text` if needed)
  article_text = ai_text(prompt)

  # Write the generated article to a file (modify filename if needed)
  if article_text:
      with open(f"{time.time()}.md", 'w') as f:
          f.write('\n'.join([f"https://www.youtube.com/watch?v={video_id}\n\n" for video_id in video_ids])+article_text)
          print("Article written")
  else:
      print("Text generation failed.")
else:
  print("Transcript could not be retrieved.")