from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import time
import os
import re

def keep_letters_regex(text):
  return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def get_transcript_without_timestamps(video_id):
  """Retrieves the transcript of a YouTube video without timestamps."""
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

# Read video IDs and titles from playlist.txt
playlist_file = "playlist.txt"
if not os.path.exists(playlist_file):
  print(f"{playlist_file} not found.")
  exit(1)

with open(playlist_file, "r") as f:
  lines = f.readlines()

for line in lines:
  if ":" not in line:
    print(f"Skipping invalid line: {line.strip()}")
    continue

  video_title, video_id = map(str.strip, line.split(":", 1))

  # Retrieve transcript without timestamps
  transcript = get_transcript_without_timestamps(video_id)

  if transcript:
    # Prepare the prompt for text generation
    prompt = transcript + """\nRewrite the transcript above into paragraphs."""
    extra_instruction = """\n\n
    Also, make sure that the first line of your response is an article name for what is being discussed in the transcript. It will be used as the file name. Do not put any additional text other than the title in the first line. Do not use special characters in the title.
    """
    # Generate text using your chosen library (replace `ai_text` if needed)
    article_text = ai_text(prompt)

    # Write the generated article to a file
    if article_text:
      lines = article_text.split("\n", 1)
      title = keep_letters_regex(lines[0].strip()) + ".md"
      content = lines[1] if len(lines) > 1 else ""
      with open(title, 'w') as f:
        f.write(f"{video_title}\n\nhttps://www.youtube.com/watch?v={video_id}\n\n" + content)
        print(f"{title} written")
    else:
      print(f"Text generation failed for video ID: {video_id}")
  else:
    print(f"Transcript could not be retrieved for video ID: {video_id}")
