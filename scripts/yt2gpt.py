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
    try:
        return model.generate_content(p).text
    except:
        time.sleep(5)
        print('eror, waiting')
        return ai_text(p)


# Get user input for video ID
#video_id = input("Enter the YouTube video ID: ")
 #['VvayG1X6xqo', 'IVGznwKGJ7A', 'Y72s6IYifOk', '2pG9Ub5vSeE', 'BpjQbQ4sfAw', 'msV7rGsbgC0', 'D-8JuJd2JfA', '7BHnNug4hlo', 'nXTBbyJnftc', '5XEu2y4_OOI', 'BBLjMCPK94s', 'SNuThz0N5MA', 'dTVlFTbZDkU', 'X77l9AW_Wyw', 'DpgSjQpAyIs', 'fKYMO6x4A-E', 'yHUaoCDmUU4', '9e_pGy0YfG8', 'UlKquFdGaKM', '5VNpcY8L1HA', 'u6VTcolm1hA', 'TNrS5v5w-HQ', 'P0BGykCEeMA', 'E6OF_1spYrE',
f =  ['ymZ5VS-HMX4', 'puVxuSNvNME', '2vPTKo1ThRA', 'S72kHxogO_g', 'AbGnOhEi7Zk', 'OrNq9I9e3_8', '26ljPCbyCRk', '0RaXTYklx9E', 'uPIcrxfmzY4', 'Ddid842NqZE', 'oZECmTx8pvU', '6hcraCILoBE', 'C8v-Y2fFY8I', 'UGMModRYCkc', 'XJwV5pdPyBE', 'oZSBt1T9Rn8', 'dTVY2TKJjaU', 'b44OM9HtxZc', '_fq9hXSSh3w', 'fpKCE8D3wpk', 'XU6RmcFD2oI', 'kmkIk0E9kzY', 'ggNV7qtaIP8', 'cQdFHYvf8aI', 'HnVUumloTsM', 'WOAkAOgRIqQ']
for video_id in f:

  # Retrieve transcript without timestamps
  transcript = get_transcript_without_timestamps(video_id)
  if transcript:
    # Prepare the prompt for text generation
    prompt = transcript + "\n\n Extract ONLY the major concepts from this transcript."

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