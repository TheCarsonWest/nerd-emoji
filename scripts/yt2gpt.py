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
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en-US"])
  except YouTubeTranscriptApi.NoTranscriptFound:
    print("No transcript found for video ID:", video_id)
    return None

  text_transcript = ""
  for segment in transcript:
    text_transcript += segment["text"] + " "

  return text_transcript

genai.configure(api_key=open('api.txt','r').readline())
model = genai.GenerativeModel("gemini-2.0-flash")


def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        time.sleep(5)
        print('eror, waiting')
        return ai_text(p)


# Get user input for video ID
#video_id = input("Enter the YouTube video ID: ")
video_id = input("Enter the YouTube video ID: ")



# Retrieve transcript without timestamps
transcript = get_transcript_without_timestamps(video_id)

if transcript:
  # Prepare the prompt for text generation
  prompt = transcript + """\nUse this transcript to create a study guide of 40 questions, with answers under them, similar to the ohne on ancient china below:
  1.	What is the unique significance of China’s statehood?
a.	It is the longest continuous state on earth
2.	What major events disrupted Chinese culture during the modern era?
a.	Foreign invasions and civil wars have always disrupted culture throughout Chinese History, but nothing compares to the cultures and traditions lost during Mao Zedong’s Cultural Revolution
3.	What is the Qingming Festival? What do Chinese families do during the Qingming Festival? 
a.	The Qingming Festival is a festival where Chinese families come together to clean the tombs of their ancestors, as well as performing various rituals and giving offerings 
4.	What makes Chinese family structures different from western family structures?
a.	Chinese families often stay much more connected to each other and can often trace back their lineages dozens of generations, whereas western families may not even know their great grandparents many times, leading to almost all families splintering into much smaller ones.
5.	Who is Nuwa? How does the myth of Nuwa explain the creation of humanity?
a.	Nuwa was the mother goddess who created humanity with mud from the Yellow River and her own blood.
6.	What is the Yellow River? Why is it so significant in Chinese culture and storytelling? Why is the Yellow River called the “destroyer” in Chinese history?
a.	The Yellow River is the river that runs down the center of modern China, and it is often considered one of the cradles of civilizations.
b.	 It is sometimes called the destroyer as is has frequent and unpredictable floods that cause widespread destruction
7.	What was the Xia dynasty and what was its significance? Who was its king and what stories were told about him?
a.	The Xia dynasty was considered the first dynasty in China
b.	Their king was King Yu, and myths about him say that he controlled the flooding of the Yellow River
8.	Why is there a debate over the existence of the Xia Dynasty?
a.	There is very little written evidence in ancient records, but there is plenty of archeological evidence of their existence 
9.	What significant advances in technology did the Shang dynasty achieve? What rituals were common during the Shang Dynasty?
a.	The Shang dynasty were the first people to have written things down in Chinese
b.	Human sacrifice and divination were common practice in the Shang Dynasty
10.	What was significant about the rule of the Zhou dynasty? What influence did the Zhou dynasty’s values have on modern China?
a.	The Zhou dynasty were the first rulers of China to use the ‘Mandate of Heaven’ to justify their rule
b.	The Zhou dynasty saw the start of Daoism, which is still practiced today in China
11.	Who was Confucious? When and where did he live?
a.	Confucious was a philosopher from a small town named Qufu during a ‘warring states period’ of China’s history 
12.	What were the main ideas of Confucious’ philosophy? Where were they written?
a.	Confucious’ teachings, or just his sayings, were written in a book called the Analects 
b.	His teachings were more political in nature than theological, and he sought to have political harmony by having virtuous rulers and morality.
13.	How was Confucious’ teachings treated by the Communist Revolution in China? How have his teachings been interpreted in modern times?
a.	The communist revolution condemned Confucian teachings/
b.	The modern Chinese state and people have began listening to his teachings again and social harmony is returning once again
14.	How did the Qin Dynasty come to power? 
a.	By conquering all of China, and unifying everyone under their rule
15.	What were the innovations of the Qin Dynasty?
a.	The standardized Chinese language and writing, coins, weights, and measurements, as well as roads.
16.	How did the Qin dynasty treat dissidents? What led to the emperor’s downfall?
a.	The emperor imposed tyrannical power over captured lands and made entire regions into labor forces
b.	He often killed dissenting scholars and burned history books
c.	This made him very unpopular and would eventually lead to the people revolting
17.	What historical Chinese monuments were constructed during the Qin Dynasty?
a.	The Terracotta Army and the Great Wall both come from the Qin Dynasty
18.	How did the Han come to power? Who was their leader? What was the legend told around his birth?
a.	The Han came to power 3 years after the death of emperor Qin after a rebellion
b.	Their leader was Liu Bang, and he was said to have been a virgin birth after his mother dreamed of mating with a dragon
19.	How did the Han dynasty last so long? What influence did the systems they create have on the modern Chinese government?
a.	The Han dynasty lasted so long because they were much less harsh than the Qin and had a functional government
b.	The Bureaucracy created by the Han laid the groundwork for modern China
20.	What did the Han dynasty do to expand China’s influence westward?
a.	They created the Silk road and began communicating with the western Civilizations
  """
  prompt = transcript + "Summarize the video in an article of 500 words or more."
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